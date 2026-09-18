from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
    }
