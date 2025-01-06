from fastapi import FastAPI, Path, Body
from fastapi.middleware.cors import CORSMiddleware
from student import Student

app = FastAPI()

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
