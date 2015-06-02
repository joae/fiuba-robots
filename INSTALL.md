# Instalar postgreSQL
sudo apt-get install postgresql-9.3
sudo apt-get install postgresql-contrib
sudo /etc/init.d/postgresql restart

# Crear usuarios de postgres

1-Primero entrar a la consola de postgres
$ sudo -u postgres psql database

/** Si no les deja ingresar y le tira un FATAL ERROR. Tienen que modificar el archivo pg_hba.conf (http://stackoverflow.com/questions/7695962/postgresql-password-authentication-failed-for-user-postgres) **/

2-Setear el pass del usuario ‘postgres’ y salir de la consola de psql (Ctrl-D o \q):
# ALTER USER postgres with encrypted password 'xxxxxxx';		//robots1234 le puse yo
Fundamental poner el ‘;’ al final de la sentencia del ALTER

3-Editar el archivo pg_hba.conf cambiando los ‘peer’ por ‘md5’ de las lineas que no estén comentadas:
$ sudo vim /etc/postgresql/9.1/main/pg_hba.conf

4-Reiniciar postgres:
$ sudo /etc/init.d/postgresql restart

5-Chequear que haya quedado bien configurado ingresando con:
$ psql -U postgres
Luego ingresar el pass y si está todo ok, salir (\q)

6-Ahora falta crear un nuevo usuario, de mismos permisos que ‘postgres’, pero de igual nombre que el user de UNIX con el que estamos loggeados (ante la duda, ejecutar whoami):
$ createuser -U postgres -d -e -E -l -P -r -s <my_name>

7-Chequear que esté todo correcto ingresando con:
$ psql template1


# Python y Django

Install PIP (Python package installer)
$ sudo apt-get install python-pip
Instalar Django 
$ sudo pip install django

Conectar python y postgresql
$ sudo apt-get build-dep python-psycopg2
$ sudo pip install psycopg2

/** GUI para postgres **/
$ sudo apt-get install pgadmin3
