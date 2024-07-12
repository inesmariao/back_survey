from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login, logout
from .forms import RegistroForm


@csrf_exempt
def registrar_usuario(request):
    if request.method == 'POST':
        data = request.POST
        form = RegistroForm(data)
        if form.is_valid():
            user = form.save()
            messages.success(request, '¡Registro exitoso! El usuario ha sido registrado correctamente.')
            return JsonResponse({'message': 'Usuario registrado exitosamente', 'user_id': user.id})
        else:
            return JsonResponse({'error': form.errors}, status=400)

    return JsonResponse({'error': 'Método no permitido'}, status=405)


@csrf_exempt  # Para manejar solicitudes POST sin CSRF token en desarrollo
def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, '¡Inicio de sesión exitoso!')
            return JsonResponse({'message': 'Inicio de sesión exitoso', 'user_id': user.id})
        else:
            messages.error(request, 'Credenciales inválidas. Verifique e intente nuevamente.')
            return JsonResponse({'error': 'Credenciales inválidas'}, status=400)

    return JsonResponse({'error': 'Método no permitido'}, status=405)