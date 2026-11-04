from pathlib import Path
import pandas as pd

# ==========================================
# 1. KONFIGURASI
# ==========================================

BASE_DIR = Path(__file__).resolve().parents[1]

FILE_PATH = (
    BASE_DIR
    / "data"
    / "raw"
    / "Data_Bengkel_Firsty_Jaya_Motor_Diperbaiki.xlsx"
)

OUTPUT_PATH = BASE_DIR / "docs" / "profil_data.md"

EXPECTED_SHEETS = [
    "Data Inventaris",
    "Data Penjualan",
    "Riwayat Transaksi",
]


# ==========================================
# 2. FUNGSI FORMAT LAPORAN
# ==========================================

def section(title):
    return f"\n## {title}\n"


def normalize_column(name):
    return str(name).strip().lower()


# ==========================================
# 3. MEMBACA FILE EXCEL
# ==========================================

def main():

    print("=" * 60)
    print("FIRSTY JAYA MOTOR - DATA PROFILING")
    print("=" * 60)

    if not FILE_PATH.exists():
        raise FileNotFoundError(
            f"File Excel tidak ditemukan: {FILE_PATH}"
        )

    excel = pd.ExcelFile(FILE_PATH)

    print("\nSheet ditemukan:")
    for sheet in excel.sheet_names:
        print("-", sheet)

    missing_sheets = set(EXPECTED_SHEETS) - set(
        excel.sheet_names
    )

    if missing_sheets:
        raise ValueError(
            f"Sheet tidak ditemukan: {missing_sheets}"
        )

    data = {
        sheet: pd.read_excel(FILE_PATH, sheet_name=sheet)
        for sheet in EXPECTED_SHEETS
    }

    report = [
        "# Data Profiling - Firsty Jaya Motor",
        "",
        "Sumber: Data_Bengkel_Firsty_Jaya_Motor_Diperbaiki.xlsx",
        "",
        "Catatan: Data merupakan data simulasi.",
    ]

    # ======================================
    # 4. PROFILING SETIAP SHEET
    # ======================================

    print("\n" + "=" * 60)
    print("PROFILING SETIAP SHEET")
    print("=" * 60)

    for sheet_name, df in data.items():

        print(f"\nSHEET: {sheet_name}")
        print("-" * 50)

        print("Jumlah baris:", len(df))
        print("Jumlah kolom:", len(df.columns))

        print("\nNama kolom:")
        print(df.columns.tolist())

        print("\nTipe data:")
        print(df.dtypes)

        print("\nMissing values:")
        print(df.isnull().sum())

        print("\nDuplikasi seluruh baris:")
        print(df.duplicated().sum())

        print("\nPreview:")
        print(df.head(5).to_string(index=False))

        report.append(section(sheet_name))

        report.append(
            f"- Jumlah baris: {len(df):,}"
        )
        report.append(
            f"- Jumlah kolom: {len(df.columns)}"
        )
        report.append(
            f"- Duplikasi seluruh baris: {df.duplicated().sum()}"
        )

        report.append("\n### Struktur kolom\n")
        report.append("| Kolom | Tipe Data | Missing Values |")
        report.append("|---|---|---:|")

        for col in df.columns:
            report.append(
                f"| {col} | {df[col].dtype} | "
                f"{df[col].isna().sum()} |"
            )

        report.append("\n### Preview data\n")
        report.append(
            df.head(5).to_markdown(index=False)
        )

    # ======================================
    # 5. PEMERIKSAAN DUPLIKASI PRIMARY KEY
    # ======================================

    print("\n" + "=" * 60)
    print("PEMERIKSAAN KANDIDAT PRIMARY KEY")
    print("=" * 60)

    key_candidates = {
        "Data Inventaris": ["ID Produk"],
        "Data Penjualan": ["ID Penjualan"],
        "Riwayat Transaksi": ["ID Riwayat"],
    }

    report.append(section("Pemeriksaan Kandidat Primary Key"))

    for sheet, candidates in key_candidates.items():

        df = data[sheet]

        for key in candidates:

            if key in df.columns:

                duplicated = df[key].duplicated().sum()
                missing = df[key].isna().sum()

                print(
                    f"{sheet} - {key}: "
                    f"duplikat={duplicated}, "
                    f"kosong={missing}"
                )

                report.append(
                    f"- **{sheet} / {key}:** "
                    f"duplikat {duplicated}, "
                    f"kosong {missing}"
                )

            else:
                print(
                    f"PERHATIAN: Kolom {key} tidak ditemukan "
                    f"di {sheet}"
                )

                report.append(
                    f"- PERLU DIPERIKSA: Kolom `{key}` "
                    f"tidak ditemukan di `{sheet}`."
                )

    # ======================================
    # 6. PEMERIKSAAN RELASI ANTAR SHEET
    # ======================================

    print("\n" + "=" * 60)
    print("PEMERIKSAAN RELASI ANTAR SHEET")
    print("=" * 60)

    inventory = data["Data Inventaris"]
    sales = data["Data Penjualan"]
    history = data["Riwayat Transaksi"]

    report.append(section("Pemeriksaan Relasi"))

    if all(
        col in inventory.columns
        for col in ["ID Produk"]
    ) and all(
        col in sales.columns
        for col in ["ID Produk"]
    ):

        inventory_ids = set(
            inventory["ID Produk"].dropna()
        )

        sales_ids = set(
            sales["ID Produk"].dropna()
        )

        orphan_sales = sales_ids - inventory_ids

        print(
            "Produk penjualan tanpa inventaris:",
            len(orphan_sales)
        )

        report.append(
            f"- Produk penjualan tanpa inventaris: "
            f"{len(orphan_sales)}"
        )

    if all(
        col in inventory.columns
        for col in ["ID Produk"]
    ) and all(
        col in history.columns
        for col in ["ID Produk"]
    ):

        inventory_ids = set(
            inventory["ID Produk"].dropna()
        )

        history_ids = set(
            history["ID Produk"].dropna()
        )

        orphan_history = history_ids - inventory_ids

        print(
            "Produk riwayat tanpa inventaris:",
            len(orphan_history)
        )

        report.append(
            f"- Produk riwayat tanpa inventaris: "
            f"{len(orphan_history)}"
        )

    if all(
        col in sales.columns
        for col in ["ID Penjualan"]
    ) and all(
        col in history.columns
        for col in ["ID Referensi"]
    ):

        sales_ids = set(
            sales["ID Penjualan"].dropna()
        )

        history_ids = set(
            history["ID Referensi"].dropna()
        )

        orphan_references = history_ids - sales_ids

        print(
            "Referensi riwayat tanpa penjualan:",
            len(orphan_references)
        )

        report.append(
            f"- Referensi riwayat tanpa penjualan: "
            f"{len(orphan_references)}"
        )

    if all(
        col in sales.columns
        for col in ["ID Penjualan"]
    ) and all(
        col in history.columns
        for col in ["ID Referensi", "Jenis Transaksi"]
    ):

        barang_keluar = history[
            history["Jenis Transaksi"].astype(str).str.strip().str.lower()
            == "barang keluar"
        ]

        sales_ids = set(
            sales["ID Penjualan"].dropna().astype(str).str.strip()
        )

        outgoing_refs = set(
            barang_keluar["ID Referensi"].dropna().astype(str).str.strip()
        )

        orphan_outgoing = outgoing_refs - sales_ids

        print(
            "Referensi barang keluar tanpa penjualan:",
            len(orphan_outgoing)
        )

        print(
            "Contoh referensi bermasalah:",
            sorted(orphan_outgoing)[:10]
        )

        report.append(
            f"- Referensi barang keluar tanpa penjualan: "
            f"{len(orphan_outgoing)}"
        )

        report.append(
            "- Contoh referensi bermasalah: "
            f"{sorted(orphan_outgoing)[:10]}"
        )

    # ======================================
    # 7. RINGKASAN
    # ======================================

    report.append(section("Ringkasan"))

    total_rows = sum(
        len(df) for df in data.values()
    )

    report.append(
        f"- Total baris seluruh sheet: {total_rows:,}"
    )

    report.append(
        "- Pemeriksaan lanjutan diperlukan untuk "
        "validasi stok, tanggal, dan nilai transaksi."
    )

    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    OUTPUT_PATH.write_text(
        "\n".join(report),
        encoding="utf-8"
    )

    print("\n" + "=" * 60)
    print("DATA PROFILING SELESAI")
    print("=" * 60)

    print("Total baris:", total_rows)
    print("Laporan:", OUTPUT_PATH)


if __name__ == "__main__":
    main()