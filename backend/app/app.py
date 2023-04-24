from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import time
from datetime import datetime

from .trips import get_trips

app = FastAPI()

origins = [
    "http://localhost:5173"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/bike-trips")
async def trips(start_time: datetime = None, end_time: datetime = None, page: int = 0, page_size: int = 25):
    if start_time is None:
        start_time = datetime(2021, 5, 3, 12, 0, 0)
    if end_time is None:
        end_time = datetime(2021, 5, 3, 13, 0, 0)
    trip_list = get_trips(start_time, end_time, page, page_size)
    time.sleep(1)
    print(trip_list)
    return trip_list