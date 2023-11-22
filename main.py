# get = получаем данных из базы данных
# post = отпровляет данные в базу данных
# HS256 для работы с JWT
from fastapi import FastAPI
from passlib.context import CryptContext

SECRET_KEY = 'Biba4and3Boba2best1friend'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
app = FastAPI(docs_url='/')

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


@app.get('/home')
async def home():
    return 'Home page'


@app.post("/register")
async def register():
    return 'Register page'


@app.post('/login')
async def login():
    return 'Login Page'

