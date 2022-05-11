from pyrogram import Client
from quart import Quart, make_response, request

from jamjobbotbackend.services import auth
from jamjobbotbackend.utils import is_user_auth
from jamjobbotbackend.misc.http_messages import HttpMessages


# Controllers to log in to Telegram account
def register_auth_controller(client: Client, httpserver: Quart):
    # Send verification code by Telegram
    @httpserver.post('/auth/send_code')
    async def send_code():
        # If user already authorized
        if await is_user_auth(client):
            return await make_response(HttpMessages.YOU_ARE_ALREADY_LOGGED_IN, 400)
        # If user not authorized
        phone = request.args.get('phone', type=str)
        await auth.send_code(client, phone)
        return await make_response(HttpMessages.AUTHORIZATION_CODE_WAS_SUCCESSFULLY_SENT, 200)

    # Sign In to Telegram account
    @httpserver.post('/auth/sign_in')
    async def sign_in():
        # If user already authorized
        if await is_user_auth(client):
            return await make_response(HttpMessages.YOU_ARE_ALREADY_LOGGED_IN, 400)
        # If user not authorized
        code = request.args.get('code', type=str)
        phone = request.args.get('phone', type=str).strip()
        password = request.args.get('password', type=str)
        # TODO: Add redis storage for strong phone number and code hash to authorize

        result = await auth.sign_in(
            client,
            phone=phone,
            code=code,
            password=password
        )
        if result is None:
            return await make_response(HttpMessages.YOU_MUST_SEND_A_CODE_BEFORE_ENTERING, 400)
        return await make_response(HttpMessages.YOU_HAVE_SUCCESSFULLY_LOGGED_IN, 200)

    # Sign Out from Telegram account
    @httpserver.post('/auth/sign_out')
    async def sign_out():
        await auth.sign_out(client)
        return await make_response(HttpMessages.YOU_HAVE_SUCCESSFULLY_LOGGED_IN, 200)
