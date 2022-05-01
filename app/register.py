from .app import App
from .controllers import register_auth_controller


# Register all http controllers and telegram bot handlers
def register_all(app: App):
    # register all http controllers
    register_auth_controller(app.tgclient, app.httpserver)
