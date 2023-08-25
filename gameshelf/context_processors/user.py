from django.http import HttpRequest

def username(request: HttpRequest):
    return {
        "username": request.user.username
    }
