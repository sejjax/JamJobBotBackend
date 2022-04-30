from flask import Flask, request
from app.services.auth import AuthService


def register_auth_controller(httpserver: Flask, auth_service: AuthService):
    @httpserver.post('/auth/send_code')
    async def send_code():
        phone = request.args.get('phone', type=str)
        await auth_service.send_code(phone)

    @httpserver.post('/auth/sign_in')
    async def sign_in():
        code = request.args.get('code', type=str)
        password = request.args.get('password', type=str)
        await auth_service.sign_in(code, password)
