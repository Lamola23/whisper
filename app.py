from fastapi import FastAPI, UploadFile, File
import whisper
import shutil
import os
print("🚀 FastAPI is starting up...")

app = FastAPI()


@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    model = whisper.load_model("tiny")
    temp_path = f"temp_{file.filename}"
    
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = model.transcribe(temp_path)
    os.remove(temp_path)

    return {"text": result["text"]}
