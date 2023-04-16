import polars as pl
from pathlib import Path

root_path = Path(__file__).resolve().parents[2] # It works, Trust Me(tm).

df = pl.read_csv(root_path / "data/2021-05.csv", infer_schema_length=100000, try_parse_dates=True)

def get_trips():
    some_trips = df.head().iter_rows(named=True)
    return list(some_trips)