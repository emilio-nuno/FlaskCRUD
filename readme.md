Para que este programa funcione se necesitan los siguientes paquetes:
- flask
- flask_sqlalchemy

En la línea de comando, use los siguientes comandos para instalar las dependencias necesarias:
- pip install flask
- pip install flask_sqlalchemy

Los archivos son los siguientes:
- index.php -> La ruta / de app.py y el template es index.html
- formulario.php -> La ruta /agregar de app.py (método GET) y el template es form.html
- store.php -> La ruta /agregar de app.py (método POST)
- conexion.php -> El archivo app.py la inicializa cuando se corre el servidor
