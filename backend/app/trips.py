import polars as pl
from datetime import datetime

#root_path = Path(__file__).resolve().parents[2]  # It works, Trust Me(tm).
class TripCollection:
    def __init__(self) -> None:
        self.df = pl.DataFrame({
            "Departure": [],
            "Return": [],
            "Departure station id": [],
            "Departure station name": [],
            "Return station id": [],
            "Return station name": [],
            "Covered distance (m)": [],
            "Duration (sec.)": [],
        },
        schema={
            "Departure": pl.Datetime,
            "Return": pl.Datetime,
            "Departure station id": pl.Int64,
            "Departure station name": pl.Utf8,
            "Return station id": pl.Int64,
            "Return station name": pl.Utf8,
            "Covered distance (m)": pl.Float64,
            "Duration (sec.)": pl.Int64
        })
        self.default_time = datetime(2021, 5, 1, 0, 0, 0, 0).isoformat()
    
    def load_csv(self, csv_file):
        self.df = pl.read_csv(
            csv_file, infer_schema_length=100000, try_parse_dates=True
        )
        # Filter invalid trips
        min_trip_duration_seconds = 10
        min_trip_distance_meters = 10
        self.df = self.df.filter(pl.col("Duration (sec.)") >= min_trip_duration_seconds
                       ).filter(pl.col("Covered distance (m)") >= min_trip_distance_meters)
        print(self.df.head(5))
        return self.df
    
    def get_trips(self, start_time_after: datetime, start_time_before: datetime):
        assert start_time_after < start_time_before
        print(f"serving trips {start_time_after} - {start_time_before}")
        some_trips: pl.DataFrame = (
            self.df.lazy()
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
    
    def get_hourly_stats(self, date = None, departure_station_id = None):
        hourly_stats = self.df.with_columns(
            pl.col('Departure').dt.hour().alias('hour')).with_columns(
            pl.col("Departure").dt.date().alias("date"))
        if date:
            hourly_stats = hourly_stats.filter(pl.col("date").dt.date() == date)
        if departure_station_id:
            hourly_stats = hourly_stats.filter(pl.col("Departure station id") == departure_station_id)
        hourly_stats = hourly_stats.groupby('hour', "date", "Departure station name", "Return station name").agg(pl.count('Duration (sec.)').alias("Count")).sort("Count", descending=True)
        return hourly_stats
