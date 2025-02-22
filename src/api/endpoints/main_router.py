from fastapi import  APIRouter
from fastapi.responses import JSONResponse
from models.models import User



user_list = []


class main_router():

   
    router = APIRouter(prefix="/main")

    @router.get("/")
    
    def main_page():
        return JSONResponse(content={"message": "Hello World"})
    
    @router.get("/create_user" , response_model= User)
    def create_user(new_user: User):

        for user in user_list:
            if user.email == new_user.email: 
                return JSONResponse(content={"message": "User already exists"})
            
        user_list.append(new_user)
       
        return JSONResponse(content={"message": "User Created"})
    
