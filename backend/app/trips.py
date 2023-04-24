import polars as pl
from pathlib import Path
from datetime import datetime, timezone, timedelta
import math

root_path = Path(__file__).resolve().parents[2]  # It works, Trust Me(tm).

df = pl.read_csv(
    root_path / "data/2021-05.csv", infer_schema_length=100000, try_parse_dates=True
)
df = df.sort("Departure")
df = df.head(500000)

# Convert to UTC to make comparison work, Polars can't compare dates with different timezones
df = df.with_column(
    pl.col("Departure")
    .dt.replace_time_zone("Europe/Helsinki")
    .dt.convert_time_zone("UTC")
)
df = df.with_column(
    pl.col("Return")
    .dt.replace_time_zone("Europe/Helsinki")
    .dt.convert_time_zone("UTC")
)
print(df.head(5))


def get_trips(start_time: datetime, end_time: datetime, page, page_size):
    assert start_time < end_time
    some_trips: pl.DataFrame = (
        df.lazy()
        .filter(pl.col("Departure") > start_time)
        .filter(pl.col("Departure") < end_time)
        .collect()
    )
    some_trips_len = len(some_trips)
    some_trips = some_trips.with_column(
        pl.col("Departure").apply(lambda x: x.isoformat(), return_dtype=pl.Utf8)
    ).with_column(pl.col("Return").apply(lambda x: x.isoformat(), return_dtype=pl.Utf8))

    trip_list = list(
        some_trips.slice(page * page_size, page_size).iter_rows(named=True)
    )
    return {
        "trips": trip_list,
        "pages": math.ceil(some_trips_len / page_size),
        "start_time": start_time.isoformat(),
        "end_time": end_time.isoformat(),
    }
