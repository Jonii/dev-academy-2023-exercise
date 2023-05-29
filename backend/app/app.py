import asyncio
from typing import BinaryIO, Dict
from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
import time
from datetime import datetime, timedelta

from uuid import uuid4

from .trips import TripCollection

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

trip_collection: TripCollection = TripCollection()

@app.get("/api/bike-trips")
async def trip_search(start_time: datetime, end_time: datetime):
    print(start_time, end_time)

    trip_list = trip_collection.get_trips(start_time, end_time)
    response = JSONResponse(trip_list)
    response.headers["Cache-Control"] = "public, max-age=30"
    time.sleep(0.2)
    print(trip_list["trips"][0:5])
    return response

@app.get("api/default-time")
async def default_time():
    return { "default_time": datetime(2021, 5, 1, 0, 0, 0, 0).isoformat() }

@app.post("/api/upload")
async def upload(file: UploadFile):
    print(file.filename)
    unique_id = str(uuid4())
    file_bytes = await file.read()
    upload_processing_items[unique_id] = CsvProcessing()
    asyncio.create_task(process_csv(unique_id, file_bytes))
    return {
            "filename": file.filename,
            "id": unique_id,
        }

async def process_csv(id, file: BinaryIO):
    print("processing csv", id)
    await asyncio.sleep(0.9)
    try:
        trip_collection.load_csv(file)
        upload_processing_items[id].set_done("done")
    except Exception as e:
        upload_processing_items[id].set_done("error: {}".format(e))
class CsvProcessing:
    def __init__(self):
        self.status = "processing"
        self.result: None | str = None
    
    def set_done(self, result):
        self.status = "done"
        self.result = result

upload_processing_items: Dict[str, CsvProcessing] = {}

async def event_stream(id):
    while upload_processing_items[id].status == "processing":
        yield "data: {}\n\n".format(upload_processing_items[id].status)
        await asyncio.sleep(1)
    yield "data: {}\n\n".format(upload_processing_items[id].result)

@app.get("/api/status/{id}")
async def status(id):
    if id not in upload_processing_items:
        raise HTTPException(status_code=404, detail="Item not found")
    return StreamingResponse(event_stream(id), media_type="text/event-stream")