from fastapi import FastAPI, Path, Body, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from student import Student

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


@app.get("/")
async def index():
    return {"message": "Hi world!"}


@app.get("/hello/{name}")
async def hello(name: str = Path(..., min_length=1, max_length=20), page: int = Path(..., ge=1)):
    return {"message": f"Hello {name}!, page={page}"}


@app.post("/students")
async def student_data(s1: Student):
    # data = {
    #     "id": 1,
    #     "name": "test",
    #     "subjects": ["test1", "test2"],
    # }
    # s1 = Student(**data)
    # print(s1)
    # o1 = s1.model_dump()
    # print(o1)
    return s1


@app.post("/students2")
async def student_data2(name: str = Body(...), marks: int = Body(...)):
    return {"name": name, "marks": marks}


@app.post("/students/{college}")
async def student_data3(college: str, age: int, student: Student):
    return {"college": college, "age": age, **student.model_dump()}


# HTMLResponse
@app.get("/html")
async def html():
    ret = '''
    <html>
    <body>
    <h1>Hello, World!</h1>
    </body>
    </html>
    '''
    return HTMLResponse(content=ret)


@app.get("/html2/{name}", response_class=HTMLResponse)
async def html2(request: Request, name: str):
    return templates.TemplateResponse(
        "hello.html", {"request": request, "name": name}
    )
