from fastapi import FastAPI

app = FastAPI()


# Define a GET operation at the root ("/") of your API
@app.get("/")
async def root():
    # Return a simple string directly to the user
    return "Hello, this is sample website version 2"
