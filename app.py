
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from routers.api_router import router as api_router

app = FastAPI(
    title="autotube",
    description="This is an application as a service",
    version="0.0.2",
    contact=[{
        "name": "Akkil M G",
        "url": "http://github.com/AkkilMG",
    }, {
        "name": "Akkil M G",
        "url": "http://github.com/AkkilMG",
    }],
    license_info={
        "name": "GNU GENERAL PUBLIC License v3.0",
        "url": "https://www.gnu.org/licenses/gpl-3.0.en.html",
    },
    docs_url="/method",
    redoc_url="/",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return JSONResponse({"success": True})

app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    try:
        print('------------------- Initializing Web Server -------------------')
        print('----------------------- Service Started -----------------------')
        uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
    except KeyboardInterrupt:
        print('----------------------- Service Stopped -----------------------')
