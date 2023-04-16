from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
async def trips():
    trip_list = get_trips()
    print(trip_list)
    return trip_list