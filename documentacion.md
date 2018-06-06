# Basic Image Handling and Processing

## Ejemplo 1 (ch0_ejemplo1.py)

En este ejemplo se ponen a prueba los comandos que permiten graficar puntos y líneas sobre una imagen.

El código del ejemplo inicia leyendo la imagen space.jpg que se encuentra en la carpeta data, y se almacena en la variable `im`. A continuación, se muestra la imagen con el comando `imshow`.

Luego se definen las coordenadas de cinco puntos que se quieren graficar en sobre la imagen im en dos vectores, `x` y `y`, que guardan las coordenadas horizontales y verticales respectivamente. Al utilizar el comando `plot`, se observa que estos puntos no se grafican en otra ventana. En el comando plot se puede ingresar, además de las coordenadas, parámetros para personalizar la apariencia de los marcadores. En este caso los marcadores tienen forma circular y son de color amarillo y se consigue con el tercer parámetro de entrada de la línea `plot(x,y,'yo')`.

La línea de código `plot(x[1:3],y[1:3],'g--')` dibuja una línea discontinua que conecta el segundo y tercer punto definido anteriormente. Por último, se coloca un título a la gráfica.

El resultado de este código es la imagen ``space_points.png`` en la carpeta ``resultados``.

## Ejemplo 2 (ch0_ejemplo2.py)

El primer paso fue cargar la imagen space.jpg con el comando ``im = array(Image.open('data\space.jpg').convert('L'))``. En la misma línea se transforma la imagen a escala de grises y se guarda en la variable `im`. Se crea una nueva figura con el comando figure() y con el comando contour se visualizan los iso contornos, es decir, los bordes de las regiones que tienen un mismo nivel de intensidad.

El resultado de este código es la imagen ``space_contours.npg`` que se encuentra en la carpeta ``resultados``.

## Capítulo 1 - Ejercicio 1 (ch01-ex1.py)

Para resolver este ejercicio se importó el paquete de procesamiento de imágenes multidimensionales ``ndimage`` de la biblioteca ``scipy`` para aplicar el filtro gaussiano.

Primero que todo se leyó la imagen ``hotel.jpg``  con la cual se trabajó, y se convirtió a escala de grises. La imagen resultante se filtró tres veces con el filtro gaussiano, cada vez con una desviación estándar de distinto valor.

Con el comando ``contour`` se visualizan los iso contornos de las imágenes, tanto de la original como de las imágenes resultantes de los filtrados. Para una mejor visualización se quitaron los ejes.

Las imágenes resultantes están en la carpeta ``resultados``. La imagen ``ex1_1.png`` muestra los contornos de la imagen original. Las imágenes ``ex1_2.png``,``ex1_3.png`` y ``ex1_4.png``  muestran los contornos de los resultados de filtrado con desviación estándar 5, 10 y 15 respectivamente.


Se observa que a medida que aumenta el valor de la desviación estándar hay menos regiones.  Esto se debe a que cuando el suavizado es más fuerte se pierden los detalles y contornos de la imagen, lo que provoca que hayan grandes regiones uniformes.

## Capítulo 1 - Ejercicio 2 (ch01-ex2.py)

En este ejercicio se realiza una opereación con 'unsharp masking' a una imagen en esacala de grises y también a color. Para esto se utilizó la librería numpy para trabajar con matrices y la librería scipy para aplicar un filtro gaussiano.




