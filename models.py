from pydantic import BaseModel


# Модель для входа в аккаунт
class LoginModel(BaseModel):
    username: str
    password: str


# Модель для регистрации
class RegisterModel(BaseModel):
    username: str
    password: str
    email: str


class Token(BaseModel):
    access_token: str
    token_type: str
