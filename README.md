# QR Code Generator

Generador de códigos QR usando Django.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/QR-Code-Generator.git
   cd QR-Code-Generator
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Realiza las migraciones:
   ```bash
   python manage.py migrate
   ```
4. Ejecuta el servidor:
   ```bash
   python manage.py runserver
   ```

## Uso

- Ingresa el texto o URL en el formulario y haz clic en "Generar" para obtener el código QR.

## Dependencias
- Django
- qrcode

## Estructura
- `core/views.py`: Lógica de generación de QR.
- `core/utils/qr.py`: Función utilitaria para crear el QR.
- `core/templates/`: Plantillas HTML.

