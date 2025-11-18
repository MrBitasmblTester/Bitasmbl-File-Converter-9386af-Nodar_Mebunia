from PyPDF2 import PdfReader
from PIL import Image
import os, time
UPLOAD_DIR = "./backend/converted"
img_exts = (".png",".jpg",".jpeg",".gif",".tif",".tiff")
def convert_file(task_id, path, filename, tasks):
    try:
        tasks[task_id]["status"] = "processing"
        name, ext = os.path.splitext(filename.lower())
        if ext == ".pdf":
            reader = PdfReader(path)
            text = "\n".join(p.extract_text() or "" for p in reader.pages)
            out = f"{task_id}_converted.txt"
            with open(os.path.join(UPLOAD_DIR, out), "w", encoding="utf-8") as f: f.write(text)
        elif ext in img_exts:
            img = Image.open(path)
            out = f"{task_id}_converted.png"
            img.convert("RGBA").save(os.path.join(UPLOAD_DIR, out), "PNG")
        else:
            tasks[task_id]["status"] = "error"
            tasks[task_id]["result"] = "unsupported file type"
            return
        tasks[task_id]["status"] = "done"
        tasks[task_id]["result"] = out
    except Exception as e:
        tasks[task_id]["status"] = "error"
        tasks[task_id]["result"] = str(e)
