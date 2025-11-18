from fastapi import FastAPI, UploadFile, File, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uuid, os
import convert
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
UPLOAD_DIR = "./backend/converted"
os.makedirs(UPLOAD_DIR, exist_ok=True)
tasks = {}
@app.post("/upload")
async def upload(file: UploadFile = File(...), background: BackgroundTasks = None):
    tid = str(uuid.uuid4())
    path = os.path.join(UPLOAD_DIR, f"{tid}_" + file.filename)
    with open(path, "wb") as f: f.write(await file.read())
    tasks[tid] = {"status": "queued", "result": None}
    background.add_task(convert.convert_file, tid, path, file.filename, tasks)
    return {"task_id": tid}
@app.get("/status/{task_id}")
def status(task_id: str):
    return tasks.get(task_id, {"status": "not_found"})
@app.get("/download/{filename}")
def download(filename: str):
    fp = os.path.join(UPLOAD_DIR, filename)
    if os.path.exists(fp):
        return FileResponse(fp, filename=filename)
    raise HTTPException(404)
