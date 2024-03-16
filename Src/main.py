from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


# Define a GET operation at the root ("/") of your API
@app.get("/")
async def root():
    # Return a simple string directly to the user
    return "Hello, this is sample website version 1"
