import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL


# ==================================================
# 1. KONFIGURASI PROJECT
# ==================================================

PROJECT_DIR = Path(__file__).resolve().parents[1]

load_dotenv(PROJECT_DIR / ".env")

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST", "localhost") 
DB_PORT = os.getenv("DB_PORT", "5432")      

if not all([DB_USER, DB_PASSWORD, DB_NAME]):
    raise ValueError(
        "Konfigurasi DB_USER, DB_PASSWORD, atau DB_NAME "
        "belum lengkap di file .env"
    )


# ==================================================
# 2. KONEKSI DATABASE
# ==================================================

db_url = URL.create(
    drivername="postgresql+psycopg2",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,        
    port=int(DB_PORT),  
    database=DB_NAME,
)

engine = create_engine(db_url)


# ==================================================
# 3. FILE EXCEL DAN MAPPING SHEET
# ==================================================

FILE = (
    PROJECT_DIR
    / "data"
    / "raw"
    / "Data_Bengkel_Firsty_Jaya_Motor_Diperbaiki.xlsx"
)

SHEETS = {
    "Data Inventaris": "inventaris",
    "Data Penjualan": "penjualan",
    "Riwayat Transaksi": "riwayat",
}


# ==================================================
# 4. FUNGSI NORMALISASI NAMA KOLOM
# ==================================================

def snake(column):
    return (
        str(column)
        .strip()
        .lower()
        .replace("/", "_")
        .replace(" ", "_")
    )


# ==================================================
# 5. PROSES DATA INGESTION
# ==================================================

def main():

    print("=" * 55)
    print("FIRSTY JAYA MOTOR - RAW DATA INGESTION")
    print("=" * 55)

    # Periksa file Excel
    if not FILE.exists():
        raise FileNotFoundError(
            f"File Excel tidak ditemukan: {FILE}"
        )

    print(f"File ditemukan: {FILE.name}")

    # Periksa nama sheet
    excel_file = pd.ExcelFile(FILE)

    missing_sheets = [
        sheet
        for sheet in SHEETS
        if sheet not in excel_file.sheet_names
    ]

    if missing_sheets:
        raise ValueError(
            f"Sheet tidak ditemukan: {missing_sheets}. "
            f"Sheet tersedia: {excel_file.sheet_names}"
        )

    print("Seluruh sheet berhasil ditemukan.")

    # Pastikan schema raw tersedia
    with engine.begin() as conn:
        conn.execute(
            text("CREATE SCHEMA IF NOT EXISTS raw")
        )

    # Memuat masing-masing sheet
    for sheet_name, table_name in SHEETS.items():

        print(f"\nMemproses sheet: {sheet_name}")

        df = pd.read_excel(
            FILE,
            sheet_name=sheet_name
        )

        # Normalisasi nama kolom
        df.columns = [snake(col) for col in df.columns]

        # Pastikan nama kolom tidak duplikat
        if df.columns.duplicated().any():
            duplicates = df.columns[
                df.columns.duplicated()
            ].tolist()

            raise ValueError(
                f"Kolom duplikat pada {sheet_name}: {duplicates}"
            )

        # Tambahkan waktu pemuatan data
        df["loaded_at"] = pd.Timestamp.now()

        # Masukkan data ke PostgreSQL
        df.to_sql(
            name=table_name,
            con=engine,
            schema="raw",
            if_exists="replace",
            index=False
        )

        print(
            f"Berhasil: raw.{table_name} "
            f"| Total baris: {len(df):,}"
        )

    print("\n" + "=" * 55)
    print("RAW DATA INGESTION SELESAI")
    print("=" * 55)


if __name__ == "__main__":
    main()