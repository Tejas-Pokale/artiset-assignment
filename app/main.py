from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from app.encoder import encode_message, decode_message

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {}
    )


@app.post("/encrypt")
async def encrypt(message: str = Form(...)):
    encoded = encode_message(message)
    return JSONResponse({"result": encoded})


@app.post("/decrypt")
async def decrypt(message: str = Form(...)):
    try:
        decoded = decode_message(message)
        return JSONResponse({"result": decoded})
    except Exception:
        return JSONResponse(
            {"error": "Invalid Base64 input"},
            status_code=400
        )


@app.get("/health")
async def health():
    return {"status": "healthy"}