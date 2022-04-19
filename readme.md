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
- Tanto en el menú de Series como en el de Películas, se encuentra un formulario para cargar una recomendación, en el que hay que 
completar el nombre, la categoría (drama / suspenso / terror / etc), una descripción, tildar si se encuentra o no 
en netflix. Esto va a generar también información de la fecha y hora en que se hizo la recomendación y el usuario. 
También podemos acceder a realizar una búsqueda de una serie o película, por nombre.
Por último, tenemos un listado de las series y películas recomendadas, donde podemos ver el nombre y la categoría, las mismas se pueden borrar o editar y si hacemos click en Leer más se puede ver si se encuentra o no en netflix, la descripción, fecha de creación y autor.  
- El blog cuenta con Sign up, login y logut.
- Los usuarios logueados podran acceder a consultar sus datos, donde también se pueden realizar modificaciones.

## Panel de Administración

Se puede crear un super usuario para acceder al panel de administración, el cual nos da acceso a nuestra base de datos. 
Para crear el superusuario para acceder al panel debemos ingresar el siguiente código:

```sh
py manage.py createsuperuser
```
Definir el usuario y la contraseña, y luego acceder desde http://127.0.0.1:8000/admin/

En este panel podemos consultar la base de datos, eliminar, modificar o crear elementos. 
