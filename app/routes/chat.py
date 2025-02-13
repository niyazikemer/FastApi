from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/send")
async def send_message(message: str = Form(...)):
    return HTMLResponse(f"<p class='bg-gray-100 rounded-lg p-3'>{message}</p>")