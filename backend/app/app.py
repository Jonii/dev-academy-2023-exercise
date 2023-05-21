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
async def trips(start_time: datetime, end_time: datetime):
    print(start_time, end_time)

    trip_list = get_trips(start_time, end_time)
    response = JSONResponse(trip_list)
    response.headers["Cache-Control"] = "public, max-age=600"
    time.sleep(1)
    print(trip_list["trips"][0:5])
    return response

@app.get("api/default-time")
async def default_time():
    return { "default_time": datetime(2021, 5, 1, 0, 0, 0, 0).isoformat() }