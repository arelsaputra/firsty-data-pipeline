# Firsty Jaya Motor - Data Engineering Pipeline

## Project Overview

End-to-end Data Engineering Pipeline
for Firsty Jaya Motor.

Proyek ini bertujuan membangun sistem
pengolahan data bengkel menggunakan
Python, PostgreSQL, Docker, Apache Airflow,
dan Metabase.

## Business Problem

Data inventaris, penjualan, dan riwayat
transaksi masih dikelola menggunakan Excel.

Hal tersebut dapat menyebabkan perbedaan
data stok dan kesulitan membuat laporan.

## Technology Stack

- Python
- Pandas
- PostgreSQL
- SQL
- Docker
- Apache Airflow
- Metabase
- GitHub

## Data Source

Data yang digunakan merupakan data simulasi
untuk kebutuhan portofolio.

## Project Status

Development - Stage 1

## Raw Data Ingestion

Data sumber berasal dari file Excel simulasi bengkel
Firsty Jaya Motor dengan tiga sheet:

- Data Inventaris
- Data Penjualan
- Riwayat Transaksi

Data dimuat menggunakan Python, Pandas, dan SQLAlchemy
ke PostgreSQL schema `raw`.

### Menjalankan ingestion

```bash
python src/load_raw.py
```

### Raw tables

- raw.inventaris
- raw.penjualan
- raw.riwayat
