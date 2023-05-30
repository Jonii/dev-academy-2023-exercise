from pathlib import Path
import polars as pl

class StationCollection:
    def __init__(self) -> None:
        root_path = Path(__file__).resolve().parents[2]
        path = root_path / "data" / "Helsingin_ja_Espoon_kaupunkipyöräasemat_avoin.csv"
        self.stations = pl.read_csv(path)
    def get_stations_by_id(self, station_id: int):
        station = self.stations.filter(pl.col("ID") == station_id)
        return list(station.iter_rows(named=True))
    
    def get_stations_by_fid(self, station_fid: int):
        station = self.stations.filter(pl.col("FID") == station_fid)
        return list(station.iter_rows(named=True))