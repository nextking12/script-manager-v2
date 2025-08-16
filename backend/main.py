from fastapi import FastAPI, HTTPException
from typing import List
from models import Script
from uuid import UUID
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db: List[Script] = [
    Script(
        id=UUID("55a058bc-0606-4089-9a87-d6711a5a1775"),
        name="test",
        language="Python",
        message="my script",
    ),
    Script(
        id=UUID("6b01e942-d924-4588-8456-e362d90a5888"),
        name="Bash",
        language="Bash",
        message="my Bash script",
    ),
]


@app.get("/")
async def root():
    return {"Hello": "World"}


# expose endpoint to GET list of scripts
@app.get("/api/v1/scripts")
# function to return db list defined on line 9
async def fetch_scripts():
    return db


@app.post("/api/v1/scripts")
async def create_script(script: Script):
    db.append(script)
    return {"id": script.id}


@app.delete("/api/v1/scripts/{script_id}")
async def delete_script(script_id: UUID):
    for script in db:
        if script.id == script_id:
            db.remove(script)
            return
    raise HTTPException(
        status_code=404, detail=f"script with id: {script_id} does not exist"
    )

