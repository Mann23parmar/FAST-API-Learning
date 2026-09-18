from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body>
            <h1>Hello Manan</h1>
            <p>Welcome to my FastAPI application.</p>
        </body>
    </html>
    """