# Data Profiling - Firsty Jaya Motor

Sumber: Data_Bengkel_Firsty_Jaya_Motor_Diperbaiki.xlsx

Catatan: Data merupakan data simulasi.

## Data Inventaris

- Jumlah baris: 1,000
- Jumlah kolom: 12
- Duplikasi seluruh baris: 0

### Struktur kolom

| Kolom | Tipe Data | Missing Values |
|---|---|---:|
| ID Produk | str | 0 |
| Nama Produk | str | 0 |
| Kategori | str | 0 |
| Merk | str | 0 |
| Tipe/Ukuran | str | 0 |
| Harga Beli | int64 | 0 |
| Harga Jual | int64 | 0 |
| Stok | int64 | 0 |
| Satuan | str | 0 |
| Supplier | str | 0 |
| Tanggal Masuk | datetime64[us] | 0 |
| Keterangan | str | 0 |

### Preview data

| ID Produk   | Nama Produk   | Kategori   | Merk   | Tipe/Ukuran   |   Harga Beli |   Harga Jual |   Stok | Satuan   | Supplier                    | Tanggal Masuk       | Keterangan   |
|:------------|:--------------|:-----------|:-------|:--------------|-------------:|-------------:|-------:|:---------|:----------------------------|:--------------------|:-------------|
| PRD0001     | Mpx 2         | Oli        | AHM    | 800 Ml        |        50000 |        55000 |     72 | Botol    | PT. Multidaya Prima Lestari | 2026-01-23 00:00:00 | Slow Moving  |
| PRD0002     | Mpx 1         | Oli        | AHM    | 800 Ml        |        50000 |        55000 |      8 | Botol    | PT. Multidaya Prima Lestari | 2026-03-05 00:00:00 | Slow Moving  |
| PRD0003     | Spx 2         | Oli        | AHM    | 800 Ml        |        55000 |        60000 |     35 | Botol    | PT. Multidaya Prima Lestari | 2026-01-21 00:00:00 | Normal       |
| PRD0004     | Spx 1         | Oli        | AHM    | 800 Ml        |        55000 |        60000 |     20 | Botol    | PT. Multidaya Prima Lestari | 2026-05-01 00:00:00 | Slow Moving  |
| PRD0005     | Mpx 1         | Oli        | AHM    | 1000 Ml       |        60000 |        65000 |     49 | Botol    | PT. Multidaya Prima Lestari | 2026-01-06 00:00:00 | Fast Moving  |

## Data Penjualan

- Jumlah baris: 1,000
- Jumlah kolom: 12
- Duplikasi seluruh baris: 0

### Struktur kolom

| Kolom | Tipe Data | Missing Values |
|---|---|---:|
| ID Penjualan | str | 0 |
| Tanggal Penjualan | datetime64[us] | 0 |
| ID Produk | str | 0 |
| Nama Produk | str | 0 |
| Kategori | str | 0 |
| Merk | str | 0 |
| Kuantitas | int64 | 0 |
| Harga Satuan | int64 | 0 |
| Total Penjualan | int64 | 0 |
| Metode Pembayaran | str | 0 |
| Nama Pelanggan | str | 0 |
| Kasir | str | 0 |

### Preview data

| ID Penjualan   | Tanggal Penjualan   | ID Produk   | Nama Produk                                | Kategori      | Merk   |   Kuantitas |   Harga Satuan |   Total Penjualan | Metode Pembayaran   | Nama Pelanggan   | Kasir   |
|:---------------|:--------------------|:------------|:-------------------------------------------|:--------------|:-------|------------:|---------------:|------------------:|:--------------------|:-----------------|:--------|
| SALE00001      | 2026-01-01 00:00:00 | PRD0535     | Roller Racing YSP Vario 7 Gram             | Roller Racing | YSP    |           2 |          52000 |            104000 | Debit               | Pelanggan Umum   | Arel    |
| SALE00002      | 2026-01-01 00:00:00 | PRD0737     | Fuel Pump NPP Vario Techno 125 PGM FI 2011 | Fuel Pump     | NPP    |           3 |         530000 |           1590000 | QRIS                | Dedi Hakim       | Didi    |
| SALE00003      | 2026-01-01 00:00:00 | PRD0896     | Karburator NPP Thunder 125 (Old)           | Karburator    | NPP    |           1 |         565000 |            565000 | QRIS                | Siti Yulianto    | Ade     |
| SALE00004      | 2026-01-01 00:00:00 | PRD0457     | Comstir Ball Set [Pelor Terpisah] YSP MIO  | Comstir       | YSP    |           2 |          80000 |            160000 | Debit               | Pelanggan Umum   | Arel    |
| SALE00005      | 2026-01-01 00:00:00 | PRD0532     | Roller Racing YSP N-Max 10 Gram            | Roller Racing | YSP    |           3 |          52000 |            156000 | QRIS                | Pelanggan Umum   | Didi    |

## Riwayat Transaksi

- Jumlah baris: 3,101
- Jumlah kolom: 12
- Duplikasi seluruh baris: 0

### Struktur kolom

| Kolom | Tipe Data | Missing Values |
|---|---|---:|
| ID Riwayat | str | 0 |
| Tanggal Transaksi | datetime64[us] | 0 |
| ID Referensi | str | 0 |
| ID Produk | str | 0 |
| Nama Produk | str | 0 |
| Jenis Transaksi | str | 0 |
| Stok Masuk | int64 | 0 |
| Stok Keluar | int64 | 0 |
| Stok Sebelum | int64 | 0 |
| Stok Sesudah | int64 | 0 |
| Supplier | str | 0 |
| Keterangan | str | 0 |

### Preview data

| ID Riwayat   | Tanggal Transaksi   | ID Referensi   | ID Produk   | Nama Produk                                                                                                                                                                                                                                          | Jenis Transaksi   |   Stok Masuk |   Stok Keluar |   Stok Sebelum |   Stok Sesudah | Supplier                | Keterangan              |
|:-------------|:--------------------|:---------------|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|-------------:|--------------:|---------------:|---------------:|:------------------------|:------------------------|
| HIST00001    | 2025-12-02 00:00:00 | PO00001        | PRD0737     | Fuel Pump NPP Vario Techno 125 PGM FI 2011                                                                                                                                                                                                           | Barang Masuk      |            7 |             0 |              0 |              7 | PT Jayamas Motorindo    | Stok awal dari supplier |
| HIST00002    | 2025-12-05 00:00:00 | PO00002        | PRD0440     | Piece Slider YSP SCOOPY ESP                                                                                                                                                                                                                          | Barang Masuk      |           32 |             0 |              0 |             32 | PT. YSP Motorindo Parts | Stok awal dari supplier |
| HIST00003    | 2025-12-07 00:00:00 | PO00003        | PRD0353     | Diskpad [Kemasan Press]Kemasan Press YSP MIO M3 (FR), NMAX (FR), RX KING (FR), MIO Z (FR), FINO (FR), MIO SOUL GT (FR), AEROX (FR)                                                                                                                   | Barang Masuk      |           89 |             0 |              0 |             89 | PT. YSP Motorindo Parts | Stok awal dari supplier |
| HIST00004    | 2025-12-07 00:00:00 | PO00004        | PRD0535     | Roller Racing YSP Vario 7 Gram                                                                                                                                                                                                                       | Barang Masuk      |           68 |             0 |              0 |             68 | PT. YSP Motorindo Parts | Stok awal dari supplier |
| HIST00005    | 2025-12-08 00:00:00 | PO00005        | PRD0625     | Seal Roda Belakang YSP VARIO 110 (2006–2019), BEAT FI (2012–2014), BEAT KARBU (2008–2012), SCOOPY (2013–2024), SPACY (2011–2018), BEAT & BEAT STREET (2020–2025), BEAT POP (2014–2019), BEAT SPORTY ESP (2014–2020), GENIO (2019–2025) Size: 29X44X7 | Barang Masuk      |          134 |             0 |              0 |            134 | PT. YSP Motorindo Parts | Stok awal dari supplier |

## Pemeriksaan Kandidat Primary Key

- **Data Inventaris / ID Produk:** duplikat 0, kosong 0
- **Data Penjualan / ID Penjualan:** duplikat 0, kosong 0
- **Riwayat Transaksi / ID Riwayat:** duplikat 0, kosong 0

## Pemeriksaan Relasi

- Produk penjualan tanpa inventaris: 0
- Produk riwayat tanpa inventaris: 0
- Referensi riwayat tanpa penjualan: 2101
- Referensi barang keluar tanpa penjualan: 0
- Contoh referensi bermasalah: []

## Ringkasan

- Total baris seluruh sheet: 5,101
- Pemeriksaan lanjutan diperlukan untuk validasi stok, tanggal, dan nilai transaksi.