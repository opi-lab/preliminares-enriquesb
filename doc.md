# Basic Image Handling and Processing

## Ejemplo 1 (ch0_ejemplo1.py)

En este ejemplo se ponen a prueba los comandos que permiten graficar puntos y líneas sobre una imagen.

El código del ejemplo inicia leyendo la imagen space.jpg que se encuentra en la carpeta data, y se almacena en la variable `im`. A continuación, se muestra la imagen con el comando `imshow`.

Luego se definen las coordenadas de cinco puntos que se quieren graficar en sobre la imagen im en dos vectores, `x` y `y`, que guardan las coordenadas horizontales y verticales respectivamente. Al utilizar el comando `plot`, se observa que estos puntos no se grafican en otra ventana. En el comando plot se puede ingresar, además de las coordenadas, parámetros para personalizar la apariencia de los marcadores. En este caso los marcadores tienen forma circular y son de color amarillo y se consigue con el tercer parámetro de entrada de la línea `plot(x,y,'yo')`.

La línea de código `plot(x[1:3],y[1:3],'g--')` dibuja una línea discontinua que conecta el segundo y tercer punto definido anteriormente. Por último, se coloca un título a la gráfica.

El resultado de este código es la imagen ``space_points.png`` en la carpeta ``resultados``.




## Capítulo 1 - Ejercicio 1

Para resolver este ejercicio se importó el paquete de procesamiento de imágenes multidimensionales ``ndimage`` de la biblioteca ``scipy`` para aplicar el filtro gaussiano.

Primero que todo se leyó la imagen ``hotel.jpg``  con la cual se trabajó, y se convirtió a escala de grises. La imagen resultante se filtró tres veces con el filtro gaussiano, cada vez con una desviación estándar de distinto valor.

Con el comando ``contour`` se visualizan los iso contornos de las imágenes, tanto de la original como de las imágenes resultantes de los filtrados. Para una mejor visualización se quitaron los ejes.

![alt text](https://imgur.com/z6v4XTK)


Esta primera tarea tiene que ver con familiarizarse con Python para el manejo básico de imágenes y su 
procesamiento.

Deberán subir un archivo ``README.md`` (pueden usar este para iniciar) en dónde escriban la documentación del código que están adjuntando. En particular deben cumplir con lo siguiente:

1. Por lo menos dos programas en dónde utilicen código de ejemplo del capítulo 1 y modifiquen parámetros, cambien imágenes, etc. Las imágenes o archivos binarios que utilicen deben subirlas al repositorio también en una carpeta llamada ``data``.
2. Deben resolver por lo menos los primeros dos ejercicios de final del capítulo. Deben llevar los nombres ``ch01-ex1.py`` y ``ch01-ex2.py``. 
3. Bonificación por cualquier ejercicio o programa adicional.

Ejemplo de la estructura del repositorio a subir

	preliminares-JuanPerez/
	.
	├── README.md
	├── ch01-ex1.py
	├── ch01-ex2.py
	├── data
	│   ├── image.jpg
