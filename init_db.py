"""Create the tables (and demo data) from database/schema.sql and database/seed.sql.

    python init_db.py             # schema + demo data
    python init_db.py --no-seed   # schema only

WARNING: schema.sql drops and recreates the tables, so existing data is lost.
"""
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")

from arena.db import connect  # noqa: E402


def run_script(conn, path):
    with conn.cursor() as cur:
        cur.execute(path.read_text(encoding="utf8"))
        while cur.nextset():   # drain the result of every statement in the script
            pass


if __name__ == "__main__":
    conn = connect(database=False, multi=True)
    run_script(conn, ROOT / "database" / "schema.sql")
    print("Schema created")
    if "--no-seed" not in sys.argv:
        run_script(conn, ROOT / "database" / "seed.sql")
        print("Demo data loaded")
    conn.close()
