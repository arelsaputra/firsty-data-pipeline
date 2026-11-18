# firsty-data-pipeline

Proyek ini adalah *end-to-end data pipeline* untuk **Firsty Jaya Motor**. Pipeline ini mengotomatiskan proses ekstraksi data dari file Excel, memuatnya ke database PostgreSQL, melakukan transformasi (staging dan data mart), menjalankan pengecekan kualitas data, dan mengatur seluruh orkestrasi menggunakan Apache Airflow, yang pada akhirnya disajikan dalam bentuk *dashboard* menggunakan Metabase.

## 🏗️ Arsitektur Pipeline

Alur data pada proyek ini berjalan sebagai berikut:

`File Excel` ➡️ `PostgreSQL (Raw)` ➡️ `PostgreSQL (Staging)` ➡️ `PostgreSQL (Marts)` ➡️ `Data Quality Checks` ➡️ `Metabase Dashboard`

Seluruh proses diorkestrasi oleh **Apache Airflow 3.x** yang berjalan di dalam container Docker.

## 🛠️ Teknologi yang Digunakan

- **Orkestrasi:** Apache Airflow 3.x (CeleryExecutor)
- **Database:** PostgreSQL 16
- **Visualisasi:** Metabase
- **Kontainerisasi:** Docker & Docker Compose
- **Bahasa Pemrograman:** Python 3
- **Library Utama:** Pandas, SQLAlchemy, psycopg2

## 🚀 Fitur Utama

1. **Incremental Loading**: Memproses transaksi harian tanpa memasukkan data yang sama berulang kali (idempoten).
2. **Simulasi Harian**: Menghasilkan data transaksi acak setiap hari untuk mensimulasikan aktivitas bisnis.
3. **Data Quality Checks**: Memvalidasi integritas data secara otomatis setelah transformasi.
4. **Containerized**: Seluruh *environment* terisolasi dengan baik menggunakan Docker Compose.

---

## 📂 Struktur Direktori

```text
firsty-data-pipeline/
├── dags/                    # File DAG Airflow (pipeline_dag.py)
├── data/                    # Folder data (raw, incoming, dll)
├── docs/                    # Dokumentasi tambahan
├── sql/                     # File query SQL (staging, marts)
├── src/                     # Script Python (load_raw, simulate_daily, dll)
├── config/                  # Konfigurasi Airflow
├── docker-compose.airflow.yml # File orkestrasi Docker
├── Dockerfile.airflow       # Custom image untuk Airflow
└── requirements-airflow.txt # Dependensi Python untuk Airflow
