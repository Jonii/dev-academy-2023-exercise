from fastapi import FastAPI

app = FastAPI()


@app.get("/api/bike-trips")
async def trips():
    return {"message": "Hello World"}