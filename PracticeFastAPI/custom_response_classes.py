from fastapi import FastAPI
from fastapi.responses import HTMLResponse	

app = FastAPI()
# # 
# Response class	    Used for
# JSONResponse	       JSON data
# HTMLResponse	       HTML pages
# PlainTextResponse	   Plain text
# FileResponse	       Sending a file
# StreamingResponse	   Sending data gradually
@app.get("/hello", response_class=HTMLResponse)
def hello():
    return "Hello Manan"