# Calendario para Conky en Python

## Instalación

### Descargar el proyecto:

`$ git clone https://github.com/PabliNet/calendario-conky-py`

### Ingresar al directorio:

`cd calendario-conky-py`

### Crear el directorio ~/.local/share/conky:

`mkdir -P ~/.local/share/conky`

### Copiar los archivos cal.py y concal:

`cp {cal.py,concal} ~/.local/share/conky`

### El código en ~/.conkyrc
~~~
conky.text = [[
${execp ~/.local/share/conky/concal '«color de los días»' '«color día actual»'}
]]
~~~

#### Ejemplo:
~~~
conky.text = [[
${execp ~/.local/share/conky/concal '${color yellow} ${color orange}'}
]]
~~~

[Sitio con el nombre de los colores](https://htmlcolorcodes.com/es/nombres-de-los-colores)

## Capturas de pantalla

[Captura de pantalla completa](https://i.postimg.cc/81nv9zd1/Screenshot-20250401-194418.png)

![Conky](https://i.postimg.cc/vyJgVj3S/conky.png)

![Calendario](https://i.postimg.cc/3RTYVGnS/calendario.png)
