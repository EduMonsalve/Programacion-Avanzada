![banner](../imgs/cropped-logo-fcfm-die-1.png)

# Guia básica Github

Curso EL4203 Programación Avanzada por *Joaquin Zepeda Valero*, primavera 2022.  
Profesor Alberto Castro


## Motivación


Git es un estándar al momento de crear un proyecto en equipo. Es una herramienta ampliamente utilizada en la industria. En algunos trabajos piden conocimientos sobre el uso de Github, además puede servir como “CV” de las habilidades de programación. A continuación se presentan ejemplos de: 

**Repositorio grande FreeCodeCamp:** https://github.com/freeCodeCamp/freeCodeCamp   
**Perfil personal Github:** https://github.com/SauravMukherjee44  
**Página Web:** https://sauravmukherjee44.github.io/Portfolio-Saurav-Mukherjee/  


## Crear una cuenta en Github

Se recomienda registrarse en [Github](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home) con su correo @ing.uchile.cl o @ug.uchile.cl . De todas maneras pueden agregar otros correos personales a la cuenta. 

Soliciten el pack educativo de Github [aquí](https://education.github.com/pack). Con esto podrán acceder a varias herramientas de forma gratuita para sus proyectos, al postular deben hacerlo usando sus correos institucionales, pueden responder en ‘Cómo planeas usar Github?’ diciendo ‘I need it for university projects’.


## Instalar Git

Recomiendo utilizar los valores por defecto en la instalación (en caso de usar un instalador).

### Windows

Descargar Git desde https://gitforwindows.org/  
Recomiendo utilizar los valores por defecto en la instalación.

### Linux

Pueden revisar un tutorial de instalación en el siguiente enlace:  
https://git-scm.com/book/es/v2#Instalando-en-Linux

Por otro lado, en caso de querer instalar en una distribución basada en Debian como Ubuntu, se puede usar apt-get:
```
$ apt-get install git
```


### OSX

Pueden revisar un tutorial de instalación en el siguiente enlace:  
https://git-scm.com/download/mac

### Comprobar que se instalo bien

Para comprobar que todo está funcionando bien pueden abrir la CMD y escribir ```git```, esto deberia desplegar información sobre el comando. Por otro lado podrán utilizar la git bash, la git cmd y el git GUI.  
En lo personal lo que más utilizo es la git bash.
![image](https://user-images.githubusercontent.com/51517852/193935173-0e19ea3c-2661-4908-8837-b1716c8e5844.png)


## Crear un repositorio

Una de las opciones es crear un nuevo repositorio desde la página de Github, se puede seleccionar distintas opciones tales como agregar un README (recomendado) y agregar gitignore (Este archivo sirve para que Git no suba algunos archivos al repositorio central. Por ejemplo se podría poner
los nombres de las bases de datos, o archivos de compilación de python como los con terminación *.pyc.). 

1. [IMPORTANTE] En una terminal, asociar su cuenta de GitHub a su computador.
```
git config --global user.name "Mi Nombre"
git config --global user.email "mi@correo.cl"
```
2.  Ir a https://www.github.com e iniciar sesión.
3. Hacer click en ‘New Repository’ (ubicado en barra lateral, sobre, ‘Your Repositories’).
4. En repository name escribir EjemploGit-EL4203 y marcar repositorio como privado. Presionar ‘Create Repository’.

![image](https://user-images.githubusercontent.com/51517852/194338253-c948dc00-67a1-4522-a6e4-54c383be2f5c.png)

Una vez creado se pueden subir archivos, modificar el README, manejar colaboradores, crear ramas, etc. 


5. Crear una carpeta donde se ubicará el proyecto, abrir una terminar en la carpeta y escribir 
```
git clone  https://github.com/username/Nombre-Repositorio.git
```
de esta manera se podrá tener una copia del repositorio de forma local. Este enlace lo pueden obtener desde el mismo repositorio como se muestra en la siguiente imagen:

![image](https://user-images.githubusercontent.com/51517852/194342207-d4aa712d-ee04-4161-8830-838dace1f240.png)




### Agregra colaboradores

Dentro del repositorio nos vamos a settings>Collaborators>Add people y seleccionamos un colaborador buscandolo por username, nombre completo o por correo.

![image](https://user-images.githubusercontent.com/51517852/194343365-6714a4c1-6825-4774-bbfa-30a1d443bd8e.png)

## README file

Archivo que utiliza el lenguaje Markdown, útil como presentación y/o resumen del repositorio, es bastante util para explicar sobre el repositorio, como utilizar los archivos, etc.

![image](https://user-images.githubusercontent.com/51517852/194356583-97538019-9b7d-4629-92bb-8605441b2a1a.png)


## Manejo básico de un repositorio: Comandos GIT

### GIT PUSH

Permite agregar/subir todos los archivos que se han modificado hasta el momento, para esto seguimos los siguientes pasos:

Apretamos click derecho dentro de la carpeta del repositorio que fue clonado. Seleccionamos abrir una git bash y luego se deben escribir las siguientes 3 líneas:

```
git add <filename> o git add .
```
```git add .``` agrega toda la carpeta en la que se encuentra. 

Agregar nombre o etiqueta de los archivos:
```
git commit -m "Mensaje explicativo"
```
Realizar el push en la rama correspondiente (git push):
 ```
 git push o git push origin main
 ```

### GIT PULL

Como es probable que su colaborador realice modificaciones al código, actualizando el repositorio en GitHub sin que usted lo sepa, ES IMPORTANTE que siempre antes de trabajar, usted realice una actualización de su repositorio local al hacer un pull del repositorio de GitHub, al ejecutar:
```
git pull
```

En caso de que usted no realice un pull y modifique el repositorio, existirán conflictos entre su repositorio local y
el de GitHub, lo que le impedirá realizar push de sus modificaciones, hasta que resuelva sus conflictos o realice una
nueva copia del repositorio con git clone del repositorio e introduzca sus modificaciones ahí.


# Manejo de Ramas
En Git existe una herramienta muy útil al momento de tener muchas personas trabajando sobre un mismo proyecto,
o simplemente si se desea mantener la integridad de un proyecto. Estas son las ramas o branches, que permiten
crear ‘copias’ o ‘versiones’ de un proyecto, que normalmente tiene como rama principal la rama main. La idea es
que siempre que se quiera probar ideas o realizar modificaciones a un proyecto principal, se cree una rama con una
copia de este, se realicen los cambios, y una vez que se esta segur@ de que los cambios han sido realizados tal y como
se quiere y de forma correcta, esta rama se junte o haga merge con la rama main. De este modo no se compromete
la integridad del proyecto, y un@ se asegura de modificar la rama main de forma consciente.
A continuación se ejemplifica el proceso de crear una rama, modificar su contenido y luego hacerle push a la rama
main.

## Crear y acceder a Rama

Para crear una nueva rama:
```
git checkout -b nombre_de_rama
```

Para cambiarse de rama, es decir, las modificaciones que se realicen en
la carpeta del repositorio sólo quedarán registradas en la rama nombre_de_rama.
```
git checkout -b nombre_de_rama
```

Si se desea saber en que rama se está trabajando, ejecutar:
```
git branch
```

## Modificar y hacer push en Rama

Al igual que en la parte anterior:
```
git add -A
git commit -m "Mensaje explicativo de cambios realizados"
git push origin nombre_de_rama
```

## Hacer merge con main

Una vez se esta segur@ de que las modificaciones en la rama funcionan apropiadamente y desean ser juntadas con
la rama main, ejecutar:

```
git checkout main
git merge nombre_de_rama
git push origin main
```
Si es que existen conflictos entre main y la rama que se esta haciendo merge, estos han de resolverse manualmente.

![image](https://user-images.githubusercontent.com/51517852/194357976-91eaf9a7-05f7-4720-94e6-91a7459774c8.png)

Imagen de: https://rogerdudler.github.io/git-guide/index.es.html

# Extra: Personalizar tu cuenta: Repositorio especial

Crear un repositorio que tenga como nombre el username, el readme de este se mostrará como tu perfil. Viendo el readme de la otra persona se puede ver la plantilla.
Ejemplos: 
https://github.com/joaquinzepeda  
https://github.com/SauravMukherjee44
![image](https://user-images.githubusercontent.com/51517852/194355526-dccbeb4e-ad7b-4155-98aa-1391df67f605.png)



# Agradecimientos

Agradecimientos al Cuerpo docente de EL4106 Inteligencia Computacional 2020, pues esta guia es una adpatación de su Auxiliar 3. Por otro lado, tambien agradecimientos al Cuerpo Docente del curso CC3002-1 Metodologías de Diseño y Programación 2017, Primavera, ya que esta guía la guia de curso de inteligencia es una adaptación de sus Auxiliares 1 y 2.







