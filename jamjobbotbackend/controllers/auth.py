from pyrogram import Client
from quart import Quart, make_response, request
from jamjobbotbackend.services import auth
from jamjobbotbackend.utils.is_user_auth import is_user_auth


# Controllers to log in to Telegram account
def register_auth_controller(client: Client, httpserver: Quart):
    # Send verification code by Telegram
    @httpserver.post('/auth/send_code')
    async def send_code():
        if await is_user_auth(client):
            return await make_response("You already authorized", 400)
        phone = request.args.get('phone', type=str)
        await auth.send_code(client, phone)
        return await make_response("Authentication code was send succeed", 200)

    # Sign In to Telegram account
    @httpserver.post('/auth/sign_in')
    async def sign_in():
        if await is_user_auth(client):
            return await make_response("You already authorized", 400)
        code = request.args.get('code', type=str)
        phone = request.args.get('phone', type=str).strip()
        password = request.args.get('password', type=str)
        # TODO: Add redis storage for stroing phone number and code hash to authorize

        result = await auth.sign_in(
            client,
            phone=phone,
            code=code,
            password=password
        )
        if result is None:
            return await make_response('You must send code before sign in.', 400)
        return await make_response("You've successfully logged in", 200)

    # Sign Out from Telegram account
    @httpserver.post('/auth/sign_out')
    async def sign_out():
        await auth.sign_out(client)
        return await make_response('You are logged out.', 200)
