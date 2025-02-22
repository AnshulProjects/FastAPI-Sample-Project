from models.models import *
from fastapi import APIRouter,FastAPI
from api.endpoints.main_router import *
import uvicorn



app = FastAPI()

main_endpoint = main_router()

app.include_router(main_endpoint.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)








