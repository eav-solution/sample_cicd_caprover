from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware


class NoCacheMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        return response


app = FastAPI()

# Add the NoCacheMiddleware to your application
# app.add_middleware(NoCacheMiddleware)


@app.get("/")
async def root():
    return "Hello, this is version 15"
