from telethon import TelegramClient
from flask import Flask, request, make_response
from jamjobbotbackend.services import auth


# Controllers to log in to Telegram account
def register_auth_controller(client: TelegramClient, httpserver: Flask):
    # Send verification code by Telegram
    @httpserver.post('/auth/send_code')
    async def send_code():
        # Check for authorizing
        if await client.is_user_authorized():
            return make_response("You already authorized", 400)
        phone = request.args.get('phone', type=str)
        await auth.send_code(client, phone)
        return make_response("Authentication code was send succeed", 200)

    # Sign In to Telegram account
    @httpserver.post('/auth/sign_in')
    async def sign_in():
        # Check for authorizing
        if await client.is_user_authorized():
            return make_response("You already authorized", 400)
        code = request.args.get('code', type=str)
        password = request.args.get('password', type=str)
        await auth.sign_in(client, code, password)
        return make_response("You've successfully logged in", 200)

    # Sign Out from Telegram account
    @httpserver.post('/auth/sign_out')
    async def sign_out():
        await auth.sign_out(client)
