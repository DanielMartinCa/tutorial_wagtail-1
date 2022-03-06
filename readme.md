# tutorial_wagtail
## Descripción
Web para blog desarrollada con Wagtail

En ella podemos ver una lista de películas y empleados, acceder a un blog, sección de noticias y una página de contactos, cuyos datos podremos ver almacenados en el admin y podremos descargar en formato excel.

Al ser un fork de lmorillas, he estado utilizando Usuario: lm, contraseña: lm.


## Ejecución en Linux
- Clonamos el repositorio con git clone https://github.com/DanielMartinCa/tutorial_wagtail.git
- Dentro del directorio del proyecto, creamos el entorno virtual con python3 -m venv env
- Activamos el entorno con source env/bin/activate e instalamos los requisitos que tenemos en requirements.txt
- Para arrancarlo, ejecutamos python manage.py runserver y en el buscador buscaremos la dirección donde se      aloja, que en éste caso es localhost:8000
- Para la creación de la sección de personal, nos meteremos en el shell con python manage.py shell. Importaremos la base de datos, imports qlite3, y ejecutaremos el script de creación con %run datos/crear_personal.py
