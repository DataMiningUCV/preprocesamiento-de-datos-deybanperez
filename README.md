# Ambiente de Desarrollo

Se utilizó el lenguaje de programación [Python](https://www.python.org/) en su versión 2.7, debido a su simplicidad y a las herramientas que ofrece para el preprocesamiento de datos, tales como [Numpy](http://www.numpy.org/) o [Pandas](http://pandas.pydata.org/).

Como IDE, se utilizó [Spyder](https://pythonhosted.org/spyder/) que es un ambiente de desarrollo para el lenguaje de programación python que posee herramientas como visor de variables, cónsola incorporada, autocompletación de texto, etc.

Se creó un [Ambiente Virtual](https://virtualenv.readthedocs.org/en/latest/) para la instalación de paquetes en python, de tal manera que ese ambiente sea separado y no interfieran versiones con otros programas.

El sistema operativo utilizado fue [Ubuntu](http://www.ubuntu.com/) en su versión 14.04 LTS que ofrece un soporte prolongado, y sobre el cual se instalaron las diferentes herramientas mencionadas previamente.

## Configuración del Ambiente

* Crear el directorio de trabajo: sudo mkdir deyban_perez
* Instalar los diferentes paquetes necesarios (Fuera de Python): sudo apt-get install python-pip python-dev libblas-dev liblapack-dev libatlas-base-dev gfortran python-qt4 python-sphinx gfortran libopenblas-dev liblapack-dev build-essential python-dev python-setuptools python-numpy python-scipy libatlas-dev libatlas3gf-base
* Instalar el ambiente virtual: sudo pip install virtualenv
* Crear el ambiente virtual: sudo virtualenv -p /usr/bin/python2.7  deyban_perez
* Levantar el ambiente virtual: sudo source deyban_perez/bin/activate
* Moverse al directorio creado: cd deyban_perez
* Crear un directorio para colocar los diferentes archivo: sudo mkdir tarea_1
* Instalar los paquetes iniciales necesarios: sudo pip install numpy scipy scikit-learn pytz pandas spyder
* Instalar matplot: sudo apt-get install python-matplotlib
* Respaldo de paquetes: pip freeze > paquetes.txt
* Cierre del entorno: deactivate
* Proximo acceso al entorno: sudo source deyban_perez/bin/activate
* Revisión de los paquetes necesarios previamente instalados: pip install -r paquetes.txt


