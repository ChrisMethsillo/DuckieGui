# Duckiegym User Interface (DUI)
## Introducción :
El Duckiegym User Interface (DUI) consiste en una interfaz que permite de una manera más sencilla el cambio de mapa, velocidad y cámara del simulador gym-duckietown.
## Requisitos previos:
-Python 3.6+\
-PyQt5 
## Instalación:
Clonar el repositorio DUI. Luego en la carpeta recién creada clonaremos la versión modificada del simulador
(esta se encuentra en https://github.com/ChrisMethsillo/gym-duckietown)
## Uso:
Correr el archivo DuckieGUI en algún compilador, debería aparecer una ventana con el icono del DuckieDUI 
y las opciones para el cambio de mapa, velocidad y cámara\
\
Para elegir el mapa se abrirá una nueva ventana donde se debe adjuntar el mapa que se quiere abrir, si no se agrega la velocidad ni cámara se 
ejecutará el mapa con la velocidad y cámara que vienen por defecto. El mapa escogido se muestra en la parte inferior de la interfaz.\
\
Para el cambio de la velocidad del Duckiebot, se abre una ventana donde ingresar los parámetros de la velocidad (solo acepta números). El procedimiento para cambiar la cámara es parecido al anterior,
solo que en vez de ingresar los parámetros se escoge entre las opciones disponible (la cámara selecciona se muestra en la parte inferior de la ventana).\
\
Finalmente para ejecutar el simulador se presiona el botón "Star simulation".
