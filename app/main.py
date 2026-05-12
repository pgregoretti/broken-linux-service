from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

LOG_FILE = "/var/log/debug-app/app.log"

@app.get("/")
def read_root():
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - root endpoint hit\n")

    return {"status": "ok"}

@app.get("/health")
def health():
    return {"health": "healthy"}