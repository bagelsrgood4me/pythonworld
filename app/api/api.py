from ninja import NinjaAPI

api = NinjaAPI()
api.add_router("/", "app.api.router.router")