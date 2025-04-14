from fastapi import FastAPI, UploadFile, File
import whisper
import shutil
import os

app = FastAPI()
model = whisper.load_model("base")

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = model.transcribe(temp_path)
    os.remove(temp_path)

    return {"text": result["text"]}
