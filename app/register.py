from .app import App
from .controllers import register_auth_controller


def register_all(app: App):
    # register all http controllers
    register_auth_controller(app.tgclient, app.httpserver)
