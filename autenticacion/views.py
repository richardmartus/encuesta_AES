from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'autenticacion/index.html')


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("board:index")
        else:
            mensaje = "Credenciales inválidas. Serás redirigido al inicio en 5 segundos."
            return render(request, 'autenticacion/error.html', {'mensaje': mensaje})
    return render(request, 'autenticacion/inicio_sesion.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('/')


def error(request):
    mensaje = "Credenciales inválidas. Serás redirigido al inicio en 5 segundos."
    return render(request, 'autenticacion/error.html', {'mensaje': mensaje})
