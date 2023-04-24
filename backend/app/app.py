from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import time
from datetime import datetime, timedelta

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
    if end_time is None and start_time is None:
        end_time = datetime(2021, 5, 3, 13, 0, 0)
        start_time = datetime(2021, 5, 3, 12, 0, 0)
    if start_time is None:
        raise HTTPException(status_code=400, detail="start_time is required with end_time")
    if end_time is None:
        end_time = start_time + timedelta(minutes=15)
    print(start_time, end_time)

    trip_list = get_trips(start_time, end_time, page, page_size)
    response = JSONResponse(trip_list)
    response.headers["Cache-Control"] = "public, max-age=600"
    time.sleep(1)
    print(trip_list)
    return response