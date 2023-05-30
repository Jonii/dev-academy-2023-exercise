from pathlib import Path
import polars as pl

class StationCollection:
    def __init__(self) -> None:
        root_path = Path(__file__).resolve().parents[2]
        path = root_path / "data" / "Helsingin_ja_Espoon_kaupunkipyöräasemat_avoin.csv"
        self.stations = pl.read_csv(path)

    def find_stations(self, fid: int = None, id: int = None):
        if fid is not None:
            station = self.stations.filter(pl.col("FID") == fid)
        elif id is not None:
            station = self.stations.filter(pl.col("ID") == id)
        return list(station.iter_rows(named=True))
    def all_stations(self):
        return {row["ID"]: row for row in self.stations.iter_rows(named=True)}
    
    def all_stations_by_fid(self):
        return {row["FID"]: row for row in self.stations.iter_rows(named=True)}