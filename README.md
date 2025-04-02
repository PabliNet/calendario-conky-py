# Calendario para Conky en Python

## Instalación

### Descargar el proyecto:

`$ git clone https://github.com/PabliNet/calendario-conky-py`

### Ingresar al directorio:

`cd calendario-conky-py`

### Crear el directorio ~/.local/share/conky:

`mkdir -P ~/.local/share/conky`

### Copiar los archivos «cal.py» y «conky-cal.py»:

`cp {cal.py,conky-cal.py} ~/.local/share/conky`

### El código en ~/.conkyrc
~~~
conky.text = [[
${execp ~/.local/share/conky/conky-cal.py '«color de los días»' '«color día actual»'}
]]
~~~

#### Ejemplo:
~~~
conky.text = [[
${execp ~/.local/share/conky/conky-cal.py '${color yellow} ${color orange}'}
]]
~~~

[Sitio con el nombre de los colores](https://htmlcolorcodes.com/es/nombres-de-los-colores)

## Capturas de pantalla

![Captura de pantalla completa](https://postimg.cc/FdFhMtvg)

![Conky](https://postimg.cc/7bfk0nZ6)

![Calendario](https://postimg.cc/GBqWs40G)
