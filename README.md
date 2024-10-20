# Ucamp_proyect_3 Galton Machine
Repositorio destinado para el almacenamiento de proyectos del Módulo 3 de Ucamp "bootcamp fundamentos de Python".

OJO: Este repositorio hace uso de libreias para la generación de gráficas, por esa razón se deja el archivo requerimients.txt que contitne 
las librerias necesarias para la ejecución del proyecto, esto con la finalidad paraq ue puedea configurar su entorno de desarrollo y se evito la subida del archivo .env para eviotar problemas de compatibilidad. Esto es especificamente para la funcionalidada del archivo Galton_Machine.py.

Nota: en este caso por motivos de mostrar la gráfica no se recomienda la eliminación del código con relacion con la gráfica.
Pero si puede personalizar las gráficas para mayor comodidad o gusto. Pero si solo necesita revisar que librerias se utilizaron solo necesita abrir el archivo requerimients.txt.

Contenido Repositorio:
Programa que simula un máquina de Galthon: 2.56 KB ---> En disco = 4.00 KB

Tamaño Completo (Todos los archivos y librerias) = 118 MB (En disco 125 MB)

Descripción:

Programa inspirado en la máquina de creada por Francis Galthon en 1894, la cual consiste en una serie de agujeros en una placa de madera, a través de los cuales caen bolas, y estas se distribuyen en un conjunto de contenedores en la parte inferior de la placa. La distribución de las bolas en los contenedores se asemeja a la distribución de probabilidades en una distribución binomial.

Asi que en este asao en vez de madera y clavos usaremos código python, para simular la caida de las bolas y su distribucion usaremos celdas y concatenaremos con cada resultado un +1 o un -1 dependiendo si irá a derecha, está se hará con random para lograr que sea de forma aleatoria posible.

OJO: Se trato de no usar demasiadas estructuras de control, por esa razón no se crearón 12 estructuras de control para cada nivel, sino que se creó una sola estructura de control que se repite 12 veces, esto con la finalidad de que sea más fácil de modificar y personalizar el número de niveles.

Tendrá una barra de carga modificable como un extra y una marca personalizada de mi persona.

Se adaptó para que la gráfica se más fácil de personalizar ya que puede modicarse por separado.(Se recomiendo no quitar las gráficas ya que no se agrego una función para quitarlas además de ser necesariar para mostrar los resultados de las ejecuciones).

Galton_Machine.py: Archivo principal del proyecto, contiene dos funciones principales balls_simulator() que se encarga del calculo de los resultados y contien tambien la barra de carga y galton_grafic() genera la gráfica respectivamente.

----------------------------------------------------------------------------------------------------------------------------------------------

Comentarios: este programa si me difuculto ya que usé por primera vez las funciones y aunque se que hay cosas que tengo que aclarar algunas formas de como aplicar las funciones, pero lo más escencial lo logré entender, aunque gracias al proyecto anteior el proble de las librerias me fue más fácil solucionarlo que en la anterior ocasión. Lo que igual me llevo algo de tiempo támbien fue la personalizacionde la gráfica.



