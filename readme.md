# Proyecto Florencia Villalba

## Configuración

Lo primero que se debe hacer es clonar el repositorio:

```sh
git clone https://github.com/VillalbaFlorencia/EntregaFinalVillalba.git
cd EntregaFinalVillalba
```

Luego crear un entorno virtual y activarlo:

```sh
py -m venv venv
. venv/Scripts/activate
```
Instalar los paquetes necesarios:

```sh
pip install -r requirements.txt
```

Levantar el servidor y acceder a la pagina:

```sh
py manage.py runserver
```

## Funcionalidades

- Lo primero que podemos ver es la pagina de inicio, la cual tiene una imagen y un texto de bienvenida. 
- Luego en el menú de recomendadas podemos ver una lista de las principales series recomendadas.
- En el menú Recomendar Serie, se encuentra un formulario para cargar una recomendación de serie, en el que hay que 
completar el nombre de la serie, la categoría (drama / suspenso / terror / etc) y tildar si la misma se encuentra o no 
en netflix. 
- En el menú Recomendar Pelicula, se encuentra un formulario para cargar una recomendación de peliculas, en el que hay 
que completar el nombre, la categoría (drama / suspenso / terror / etc) y tildar si se encuentra o no en netflix. 
- En el menú Recomendar Documental, se encuentra un formulario para cargar una recomendación de documentales, en el que
 hay que completar el nombre, la categoría (drama / suspenso / terror / etc) y tildar si se encuentra o no en netflix. 
- Luego en lista de recomendaciones de series, hay un formulario para buscar los nombres de las series que se 
recomendaron en la base de datos, la busqueda arroja un listado de los nombres de las series con su categoria. 

## Panel de Administración

Se puede crear un super usuario para acceder al panel de administración, el cual nos da acceso a nuestra base de datos. 
Para crear el superusuario para acceder al panel debemos ingresar el siguiente código:

```sh
py manage.py createsuperuser
```
Definir el usuario y la contraseña, y luego acceder desde http://127.0.0.1:8000/admin/

En este panel podemos consultar la base de datos, eliminar, modificar o crear elementos. 
