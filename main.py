from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.api_route("/", methods=["GET", "POST"], response_class=HTMLResponse)
async def bmi(request: Request):
    bmi_value = None

    if request.method == "POST":
        form = await request.form()
        weight = float(form["weight"])
        height = float(form["height"]) / 100
        bmi_value = round(weight / (height ** 2), 2)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "bmi": bmi_value
        }
    )
