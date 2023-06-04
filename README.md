# Practica_BDD_TestFuncionales
## Introducción


La carpeta features contiene los siguienes ficheros

- test.feature
- Environment.py
- Carpeta steps
  - test.py

 ### test.feature:
 
 Este fichero sirve para describir el comportamiento de cada funcionalidad del test.py en la página web, LIDL.

 When, se utiliza para indicar que se realiza la acción de visitar el sitio web especificado, como en el primer escenario.

 Then, se verifica si el título web coincide con el que se ha escrito en los ejemplos.

 Examples, se pone el nombre de la etiqueta y debajo con lo que debería corresponder en la página web.
 
 En resumen, este fichero describe las funcionalidades y prueba cada una de ellas, verificando una etiqueta que creamos con las del fichero.py y las de la página LDL.

### Environment.py

Este fichero sirve para configurar el entorno de prueba antes de ejecutar los escenarios, cargar el sitio web, aceptar las cookies y cerrar el navegador.

### Carpeta steps

Esta carpeta sirve para almacenar los archivos de definición de pasos, con todo el código python, sus respectivas funcionalidades, trabajando con behave y selenium.
