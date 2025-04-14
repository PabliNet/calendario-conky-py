# Calendario para Conky en Python

## Instalación

### Descargar el proyecto:

`$ git clone https://github.com/PabliNet/calendario-conky-py`

### Ingresar al directorio:

`$ cd calendario-conky-py`

### Crear el directorio ~/.local/share/conky:

`$ mkdir -P ~/.local/share/conky`

### Copiar los archivos cal.py y concal:

`$ cp {cal.py,concal} ~/.local/share/conky`

### El código en ~/.conkyrc:
~~~
conky.text = [[
${execp env PYTHONDONTWRITEBYTECODE=1 ~/.local/share/conky/concal '«color año, mes y $hr»' '«color de los días»' '«color día actual» «color de los días» «tipografía»'}
]]
~~~

#### Ejemplo:
~~~
conky.text = [[
${execp env PYTHONDONTWRITEBYTECODE=1 ~/.local/share/conky/concal '${color gold}' '${color yellow} ${color orange} ${font Monospace:size=10:weight=bold}'}
]]
~~~

[Sitio con el nombre de los colores](https://htmlcolorcodes.com/es/nombres-de-los-colores)

## Capturas de pantalla

[Captura de pantalla completa](https://i.postimg.cc/81nv9zd1/Screenshot-20250401-194418.png)

![Conky](https://i.postimg.cc/vyJgVj3S/conky.png)

![Calendario](https://i.postimg.cc/3RTYVGnS/calendario.png)
