import polars as pl
from pathlib import Path
from datetime import datetime
import math

root_path = Path(__file__).resolve().parents[2] # It works, Trust Me(tm).

df = pl.read_csv(root_path / "data/2021-05.csv", infer_schema_length=100000, try_parse_dates=True)
df = df.sort("Departure")

def get_trips(start_time: datetime, end_time: datetime, page, page_size):
    assert start_time < end_time
    some_trips = df.lazy().filter(pl.col("Departure") > start_time).filter(pl.col("Departure") < end_time).collect()
    some_trips_len = len(some_trips)
    trip_list = list(some_trips.slice(page * page_size, page_size).iter_rows(named=True))
    return {"trips": trip_list,
            "pages": math.ceil(some_trips_len / page_size),
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat()}