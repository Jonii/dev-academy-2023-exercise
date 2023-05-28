import polars as pl
from pathlib import Path
from datetime import datetime

#root_path = Path(__file__).resolve().parents[2]  # It works, Trust Me(tm).

df = pl.DataFrame({
    "Departure": [],
    "Return": [],
    "Departure station id": [],
    "Departure station name": [],
    "Return station id": [],
    "Return station name": [],
    "Covered distance (m)": [],
    "Duration (sec.)": [],
})

def load_csv(csv_file):
    global df
    df = pl.read_csv(
        csv_file, infer_schema_length=100000, try_parse_dates=True
    )
    print(df.head(5))
    return df

def get_trips(start_time_after: datetime, start_time_before: datetime):
    print("serving trips", start_time_after, start_time_before)
    assert start_time_after < start_time_before
    some_trips: pl.DataFrame = (
        df.lazy()
        .filter(pl.col("Departure") > start_time_after)
        .filter(pl.col("Departure") < start_time_before)
    )
    some_trips = some_trips.with_column(
        pl.col("Departure").apply(lambda x: x.isoformat(), return_dtype=pl.Utf8)
    ).with_column(pl.col("Return").apply(lambda x: x.isoformat(), return_dtype=pl.Utf8)).collect()

    trip_list = list(
        some_trips.iter_rows(named=True)
    )
    return {
        "trips": trip_list,
        "start_time": start_time_after.isoformat()
    }
