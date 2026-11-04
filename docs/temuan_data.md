# Temuan Data - Firsty Jaya Motor

## 1. Sumber Data

Nama file:
Data_Bengkel_Firsty_Jaya_Motor_Diperbaiki.xlsx

Jenis data:
Data simulasi bengkel.

## 2. Ringkasan Dataset

| Sheet             |        Jumlah Baris | Jumlah Kolom |
| ----------------- | ------------------: | -----------: |
| Data Inventaris   | Isi hasil profiling |          Isi |
| Data Penjualan    | Isi hasil profiling |          Isi |
| Riwayat Transaksi | Isi hasil profiling |          Isi |

## 3. Temuan Data Quality

| No  | Pemeriksaan      | Hasil     | Status      |
| --- | ---------------- | --------- | ----------- |
| 1   | Missing Values   | Isi hasil | Perlu dicek |
| 2   | Duplicate ID     | Isi hasil | Perlu dicek |
| 3   | Konsistensi Stok | Isi hasil | Perlu dicek |
| 4   | Relasi Produk    | Isi hasil | Perlu dicek |
| 5   | Relasi Penjualan | Isi hasil | Perlu dicek |
| 6   | Validasi Tanggal | Isi hasil | Perlu dicek |
| 7   | Validasi Margin  | Isi hasil | Perlu dicek |

## 4. Kesimpulan

Data telah melalui proses profiling
menggunakan Python dan Pandas.

Hasil profiling digunakan sebagai dasar
untuk proses ETL dan transformasi data
ke PostgreSQL.
