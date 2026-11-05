import sys
from pathlib import Path

from sqlalchemy import create_engine

from load_raw import engine


def run_sql(file_path):

    sql_file = Path(file_path)

    if not sql_file.is_absolute():
        sql_file = Path(__file__).resolve().parents[1] / sql_file

    if not sql_file.exists():
        raise FileNotFoundError(
            f"File SQL tidak ditemukan: {sql_file}"
        )

    sql_script = sql_file.read_text(encoding="utf-8")

    if not sql_script.strip():
        raise ValueError("File SQL kosong.")

    with engine.begin() as conn:
        conn.exec_driver_sql(sql_script)

    print(f"Berhasil menjalankan SQL: {sql_file.name}")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print(
            "Cara penggunaan: "
            "python src/run_sql.py sql/nama_file.sql"
        )
        sys.exit(1)

    run_sql(sys.argv[1])