from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    """
    Middleware that requires a user to be authenticated to view any page
    except the login or register pages.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            # Allow access to login, register, or static/media files
            if not (request.path.startswith(reverse('login')) or 
                    request.path.startswith(reverse('register')) or 
                    request.path.startswith('/static/')):
                return redirect(reverse('login'))  # Redirect to login page
        return self.get_response(request)
