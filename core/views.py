from django.shortcuts import render
from django.views import View
from .utils.qr import generate_qr_code




# Vistas principales de la aplicación QR
class HomeView(View):
    """
    Vista principal para generar códigos QR.
    - GET: Muestra el formulario.
    - POST: Procesa el formulario y genera el QR.
    """
    def get(self, request):
        """Muestra el formulario para ingresar datos."""
        return render(request, 'generate.html')

    def post(self, request):
        """Genera el código QR a partir de los datos enviados."""
        data = request.POST.get('data')
        qr_image_url = None
        if data:
            print(f"Data received for QR code generation: {data}")
            qr_image_url = generate_qr_code(data)
        return render(request, 'generate.html', {'qr_image_url': qr_image_url})
