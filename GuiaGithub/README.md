![banner](../imgs/cropped-logo-fcfm-die-1.png)

# Guia básica Github

Curso EL4203 Programación Avanzada por *Joaquin Zepeda Valero*, primavera 2022.  
Profesor Alberto Castro


## Motivación


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

## Manejo básico de un repositorio: Comandos GIT

### GIT PUSH

### GIT PULL



#










