from django.shortcuts import render
from django.views import View
from .utils.qr import generate_qr_code




# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'generate.html')

    def post(self, request):
        data = request.POST.get('data')
        if data:
            print(f"Data received for QR code generation: {data}")
            qr_image_url = generate_qr_code(data)
        return render(request, 'generate.html', {'qr_image_url': qr_image_url})
