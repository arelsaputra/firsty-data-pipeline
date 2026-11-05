-- ==========================================
-- FIRSTY JAYA MOTOR
-- 02 - DATA MART / STAR SCHEMA
-- ==========================================

CREATE SCHEMA IF NOT EXISTS mart;


-- ==========================================
-- 1. HAPUS TABEL LAMA
-- ==========================================

DROP TABLE IF EXISTS
    mart.fact_penjualan,
    mart.fact_stok,
    mart.dim_produk,
    mart.dim_pelanggan,
    mart.dim_tanggal
CASCADE;


-- ==========================================
-- 2. DIMENSI PRODUK
-- ==========================================

CREATE TABLE mart.dim_produk AS

SELECT
    id_produk,
    nama_produk,
    kategori,
    merk,
    satuan,
    supplier,
    kelas_perputaran,
    harga_beli,
    harga_jual,

    harga_jual - harga_beli AS margin_rp,

    ROUND(
        (
            (harga_jual - harga_beli)::numeric
            / NULLIF(harga_beli, 0)
        ) * 100,
        1
    ) AS margin_persen,

    tanggal_masuk,
    stok AS stok_saat_ini

FROM stg.inventaris;

ALTER TABLE mart.dim_produk
ADD PRIMARY KEY (id_produk);


-- ==========================================
-- 3. DIMENSI PELANGGAN
-- ==========================================

CREATE TABLE mart.dim_pelanggan AS

SELECT
    ROW_NUMBER() OVER (
        ORDER BY nama_pelanggan
    ) AS id_pelanggan,

    nama_pelanggan

FROM (
    SELECT DISTINCT nama_pelanggan
    FROM stg.penjualan
    WHERE nama_pelanggan IS NOT NULL
) AS pelanggan;

ALTER TABLE mart.dim_pelanggan
ADD PRIMARY KEY (id_pelanggan);


-- ==========================================
-- 4. DIMENSI TANGGAL
-- ==========================================

CREATE TABLE mart.dim_tanggal AS

WITH rentang AS (

    SELECT
        LEAST(
            (SELECT MIN(tanggal) FROM stg.penjualan),
            (SELECT MIN(tanggal) FROM stg.riwayat)
        ) AS tanggal_awal,

        GREATEST(
            (SELECT MAX(tanggal) FROM stg.penjualan),
            (SELECT MAX(tanggal) FROM stg.riwayat)
        ) AS tanggal_akhir

)

SELECT
    d::date AS tanggal,

    EXTRACT(YEAR FROM d)::int AS tahun,

    EXTRACT(MONTH FROM d)::int AS bulan,

    TO_CHAR(d, 'YYYY-MM') AS tahun_bulan,

    EXTRACT(ISODOW FROM d)::int AS hari_dalam_minggu

FROM rentang r

CROSS JOIN LATERAL
    generate_series(
        r.tanggal_awal,
        r.tanggal_akhir,
        INTERVAL '1 day'
    ) AS d

WHERE r.tanggal_awal IS NOT NULL
  AND r.tanggal_akhir IS NOT NULL;

ALTER TABLE mart.dim_tanggal
ADD PRIMARY KEY (tanggal);


-- ==========================================
-- 5. FACT PENJUALAN
-- ==========================================

CREATE TABLE mart.fact_penjualan AS

SELECT
    s.id_penjualan,
    s.tanggal,
    s.id_produk,
    c.id_pelanggan,

    s.kuantitas,
    s.harga_satuan,
    s.total_penjualan,

    s.kuantitas *
        (s.harga_satuan - p.harga_beli)
        AS laba_kotor,

    s.metode_pembayaran,
    s.kasir

FROM stg.penjualan s

JOIN mart.dim_produk p
    ON p.id_produk = s.id_produk

JOIN mart.dim_pelanggan c
    ON c.nama_pelanggan = s.nama_pelanggan;

ALTER TABLE mart.fact_penjualan
ADD PRIMARY KEY (id_penjualan);


-- ==========================================
-- 6. FACT STOK
-- ==========================================

CREATE TABLE mart.fact_stok AS

SELECT
    id_riwayat,
    tanggal,
    id_referensi,
    id_produk,
    jenis_transaksi,
    stok_masuk,
    stok_keluar,
    stok_sebelum,
    stok_sesudah

FROM stg.riwayat;

ALTER TABLE mart.fact_stok
ADD PRIMARY KEY (id_riwayat);


-- ==========================================
-- 7. SELESAI
-- ==========================================

SELECT 'Data mart berhasil dibuat' AS status;