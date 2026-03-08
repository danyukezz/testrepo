from django_bolt import BoltAPI
from django_bolt.auth import JWTAuthentication, IsAuthenticated

api = BoltAPI()

# Mount Django's URL system
api.mount_django("/django")


@api.get("/health")
async def health_check():
    return {"status": "healthy"}


@api.get(
    "/me",
    auth=[JWTAuthentication()],
    guards=[IsAuthenticated()]
)
async def current_user(request):
    return {
        "id": request.user.id,
        "email": request.user.email,
    }
