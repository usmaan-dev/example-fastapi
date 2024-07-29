from fastapi import FastAPI
from .routers import posts, users, authentication, vote
from . import models
from .database import engine
from .config import Settings
from fastapi.middleware.cors import CORSMiddleware
from pydantic_settings import BaseSettings # type: ignore

class Settings(BaseSettings):
    database_password: str = "postgres"
    access_key: str = "hdwje83jwdw8ewhdhdjwe83jw8d"
    
settings = Settings()
print(settings.database_password)

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# origins = ["https://google.com", "https://fastapi.tiangolo.com", "https://www.youtube.com"]
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(authentication.router)
app.include_router(vote.router)
    
# while True:
#     try:
#         connection = psycopg2.connect(host = 'localhost', database = 'postgres', user = 'postgres',
#                                   password = 'postgres', cursor_factory= RealDictCursor)
#         cursor = connection.cursor()
#         print("Connection established")
#         break
#     except Exception as error:
#         print("Connection: failed")
#         print("error", error)
#     # time.sleep(2)


# my_posts = [{"title": "Here on the moon", "body": "gravity is very less", "id": 1},
#             {"title": "My favorite food", "body": "I love Biryani and karahi", "id": 2}]

# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p
        

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i
        
@app.get("/")
def read_root():
    return {"Hello": "World"}




