from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate", response_class=HTMLResponse)
async def calculate(request: Request):
    form = await request.form()
    weight = float(form["weight"])
    height = float(form["height"]) / 100

    bmi = weight / (height ** 2)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "bmi": round(bmi, 2)
        }
    )
