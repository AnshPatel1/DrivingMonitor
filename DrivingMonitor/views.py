from django.shortcuts import render


class AuthenticationViews:
    @staticmethod
    def login(request):
        return render(request, "login.html")

    @staticmethod
    def register(request):
        return render(request, "register.html")