from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import Base 
from app.database import engine
from app.routes import clinicalprofile, doctors, isaaquestions, login, user  


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with the domain(s) you want to allow
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (e.g., GET, POST, OPTIONS)
    allow_headers=["*"],  # Allow all headers
)


Base.metadata.create_all(bind=engine) #ORM=>SQLAlchemy


app.include_router(user.router)
app.include_router(login.router)
app.include_router(clinicalprofile.router)
app.include_router(isaaquestions.router)
app.include_router(doctors.router)




@app.get("/")
async def test() :
    return {"Working" : "Fine"} 
