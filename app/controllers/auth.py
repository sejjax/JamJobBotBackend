from telethon import TelegramClient
from flask import Flask, request, make_response
from app.services import auth


def register_auth_controller(client: TelegramClient, httpserver: Flask):
    @httpserver.post('/auth/send_code')
    async def send_code():
        if await client.is_user_authorized():
            return make_response("You already authorized", 400)
        phone = request.args.get('phone', type=str)
        await auth.send_code(client, phone)
        return make_response("Authentication code was send succeed", 200)

    @httpserver.post('/auth/sign_in')
    async def sign_in():
        if await client.is_user_authorized():
            return make_response("You already authorized", 400)
        code = request.args.get('code', type=str)
        password = request.args.get('password', type=str)
        await auth.sign_in(client, code, password)
        return make_response("You've successfully logged in", 200)

    @httpserver.post('/auth/sign_out')
    async def sign_out():
        await auth.sign_out(client)
