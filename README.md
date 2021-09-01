Instrucciones para correr aplicacion

1. Levantar un Docker una base de datos MySQL:
   $docker run -p 3308:3306 -d --name mysql -e MYSQL_ROOT_PASSWORD=password mysql/mysql-server

2. Usar una consola para accesar a contenedor para correr los siguientes comandos:
   $docker exec -it mysql bash
   bash-4.2# mysql -uroot -ppassword

   mysql> CREATE USER 'roberto'@'%' IDENTIFIED BY 'password';
   Query OK, 0 rows affected (0.00 sec)

   mysql> GRANT ALL PRIVILEGES ON * . * TO 'roberto'@'%';
   Query OK, 0 rows affected (0.00 sec)

3. Correr la aplicacion "models.py" $>python models.py
   (esto ultimo crea las tablas)

4. Correr la aplicacion "app.py"

5. Ir a la direccion http://127.0.0.1:5000/ y apretar el boton "fetch" para poblar la BD

6. Para hacer la consulta ir a la direccion y apretar el boton "show"

Se ha considerado no duplicar las noticias del misma sitio web, y en cuanto a las consultas
para no provocar un enorme listado, se han limitado a las consultadas durante la ultima semana
