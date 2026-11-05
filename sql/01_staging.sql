-- ==========================================
-- FIRSTY JAYA MOTOR
-- 01 - STAGING LAYER
-- ==========================================

CREATE SCHEMA IF NOT EXISTS stg;


-- ==========================================
-- 1. STAGING INVENTARIS
-- ==========================================

CREATE OR REPLACE VIEW stg.inventaris AS

SELECT
    id_produk,
    TRIM(nama_produk) AS nama_produk,
    TRIM(kategori) AS kategori,
    TRIM(merk) AS merk,
    TRIM(satuan) AS satuan,
    TRIM(supplier) AS supplier,
    keterangan AS kelas_perputaran,
    harga_beli,
    harga_jual,
    stok,
    tanggal_masuk::date AS tanggal_masuk

FROM raw.inventaris;


-- ==========================================
-- 2. STAGING PENJUALAN
-- ==========================================

CREATE OR REPLACE VIEW stg.penjualan AS

SELECT
    id_penjualan,
    tanggal_penjualan::date AS tanggal,
    id_produk,
    kuantitas,
    harga_satuan,
    total_penjualan,
    metode_pembayaran,
    TRIM(nama_pelanggan) AS nama_pelanggan,
    TRIM(kasir) AS kasir

FROM raw.penjualan;


-- ==========================================
-- 3. STAGING RIWAYAT TRANSAKSI
-- ==========================================

CREATE OR REPLACE VIEW stg.riwayat AS

SELECT
    id_riwayat,
    tanggal_transaksi::date AS tanggal,
    id_referensi,
    id_produk,
    jenis_transaksi,
    stok_masuk,
    stok_keluar,
    stok_sebelum,
    stok_sesudah

FROM raw.riwayat;


-- ==========================================
-- SELESAI
-- ==========================================

SELECT 'Staging layer berhasil dibuat' AS status;