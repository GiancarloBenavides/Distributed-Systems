# Crear un servicio PostgreSQL.      
<p><code>Servicios informáticos en AWS</code></p>
<p>Creado por <code>Giancarlo Ortiz</code>

<br>

---
## [1. PosgreSQL](#)  ✔
### <code>Servidor web Ligero</code>
Para construir un servicio de [Bases de datos][alw].

1. En la plataforma en el menu de servicios/Bases_de_datos encontramos el panel de Relational Data Service , RDS;  para administrar varios [tipos de instancias][1] de bases de datos.
1. Damos click en Crear base de datos para crear una instancia Single-AZ db.t2.micro, db.t3.micro o db.t4g.micro con PosgreSQL y hasta 20 GB de almacenamiento en SSD apta para [capa gratuita][2] (750 horas al mes y 20GB de copias de seguridad por 12 meses)
    1. Escoja el tipo y version del [motor de base de datos][21] de la instancia de RDS.
    1. Escoja la plantilla de [Capa gratuita][22].
    1. Escoja nombre de las DB, [usuario maestro][23] y su contraseña.
1. Configure la instancia db.t3.micro con almacenamiento SSD hasta 20 GB y habilite/deshabilite el [escalado automático][3] para que no supere los limites de capa gratuita.
1. Configure los parámetros de la red de AWS para su instancia:
    1. Configure la [Nube Virtual AWS][41] para conectar la instancia con otros servicios de amazon en una LAN.
    1. Configure el [acceso publico][42] si quiere tener acceso al DB desde fuera de la LAN de la Nube AWS configurada.
    1. Configure 5432 como [puerto TCP][43] para el servicio.
1. Finalize la configuración adicional de la base de datos:
    1. Configure la [autentificación PosgreSQL][28] con las contraseñas de la DB.
    1. Configure el nombre de la [base de datos inicial][29].
    1. Habilitar/Deshabilitar las [copias de seguridad][210] teniendo en cuenta 20Gb para la capa gratuita.
    1. Habilitar la [actualización automática][211] de versiones secundarias.
1. Iniciar la instancia, esperar por el estado "[Running][5]" o en ejecución y esperar a que asigne una ip publica dinámica (cambiara con cada inicio de la instancia).
2. Usando la herramienta [apt][2] instalar el paquete del servidor web Nginx; para ello no es necesario agregar fuentes a la lista ya que el paquete esta disponible en los repositorios oficiales de de la distribución.
3. Instalar [nano][3] o el editor de texto de preferencia para editar los archivos de configuración de Nginx.
4. Crear una estructura de directorios usando el comando [mkdir][4] para al los archivos del sitio que se desea servir con Nginx y para el historial de eventos de uso y errores del servidor web.
5. Crear una copia del [server block][5] por defecto habilitado en Nginx, editar la copia del nuevo server block para enrutar una solicitud de dominio al recurso correspondiente y habilitarlo para que se incluya en la configuración de Nginx que se procesa al cargar el servidor.
6. __Opcional:__ Si se requiere [alojamiento compartido][6] se pueden repetir los pasos 4-5 para crear varios server blocks y atender solicitudes de multiples dominios y subdominios en un único servidor físico.
7. __Opcional:__ [eliminar][7] el enlace de la carpeta de habilitados para deshabilitar el server block por defecto de Nginx.
8. Revisar y aplicar la [configuración][8] del servidor reiniciando o recargando el servicio.

---

>__Nota:__ una sola instancia nunca superara las 750 horas disponibles mensualmente, pero puedes crear varias instancias con un propósito especifico y alternar su uso sin superar los limites de la capa gratuita. 

<br>

## [2. Comandos necesarios](#)  ✔
### <code>Interfaz de linea de comandos</code>
En los comandos reemplazar la cadena _"com.domain-name"_ con el nombre de dominio registrado en [notación de dominio inverso][cmd].

```shell
# Para actualizar los paquetes a su version mas reciente 
sudo apt update
sudo apt upgrade
# Para instalar el servidor web
sudo apt install nginx nano
# Para crear la carpeta para alojar el sitio web
sudo mkdir -p /var/www/domain-name.com/html
# Para crear una carpeta para los archivos de registro, log; de errores de Nginx
sudo mkdir -p /var/log/nginx/domain-name.com
# Para cambiar el propietario de el mismo directorio
$ sudo chown -R www-data:www-data /var/www
# Para verificar y/o modificar permisos del directorio publico de Nginx
sudo chmod –R 755 /var/www
# Para crear un nuevo Server Block, copiar el archivo por defecto en otro archivo
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/domain-name.com.conf
# Para editar el nuevo Server Block
sudo nano /etc/nginx/sites-available/domain-name.com.conf
# Para habilitar el sitio creado con un enlace simbólico en la carpeta de habilitados
sudo ln -s /etc/nginx/sites-available/domain-name.com.conf /etc/nginx/sites-enabled
# Para deshabilitar el sitio por defecto eliminar el enlace simbólico
rm /etc/nginx/sites-enabled/domain-name.com.conf
# Para revisar la configuración del servicio
sudo nginx -t
# Para aplicar la configuración del servicio
sudo nginx -s reload

```

<br>

## [3. Comandos para administrar el servicio](#)  ✔
### <code>Manipulación de servicios usando SystemD</code>
Alternativamente a los modificadores de Nginx para administrar el servicio es posible usar las herramientas para servicios de [SystemD][smd].

```shell
# Para manejar el servicio usando SystemD
sudo systemctl status nginx
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
sudo systemctl reload nginx
sudo systemctl disable nginx
sudo systemctl enable nginx

```


[1]:https://aws.amazon.com/es/rds/postgresql/pricing/?pg=pr&loc=3
[2]:https://aws.amazon.com/es/rds/free/
[3]:https://aws.amazon.com/es/ec2/pricing/on-demand/
[4]:https://aws.amazon.com/es/free/free-tier/?p=ft&z=subnav&loc=1&refid=ft_card
[41]:https://es.wikipedia.org/wiki/OpenSSH
[42]:https://es.wikipedia.org/wiki/Redirecci%C3%B3n_de_puertos
[43]:https://es.wikipedia.org/wiki/Criptograf%C3%ADa_asim%C3%A9trica
[5]:https://docs.aws.amazon.com/es_es/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html
[6]:https://es.wikipedia.org/wiki/WebSocket
[7]:https://manpages.ubuntu.com/manpages/xenial/man8/apt.8.html
[8]:https://docs.aws.amazon.com/es_es/AWSEC2/latest/UserGuide/Stop_Start.html

[alw]:https://es.wikipedia.org/wiki/Alojamiento_web
[cmd]:https://es.wikipedia.org/wiki/Notaci%C3%B3n_de_nombre_de_dominio_inverso
[smd]:https://es.wikipedia.org/wiki/Systemd

<br>

---
## Mas Recursos
- [Nginx](https://es.wikipedia.org/wiki/Nginx) (Wikipedia)
- [Ubuntu](https://es.wikipedia.org/wiki/Ubuntu) (Wikipedia)
- [Advanced Packaging Tool](https://es.wikipedia.org/wiki/Advanced_Packaging_Tool) (Wikipedia)
- [Tutorial de introducción](https://nginx.org/en/docs/beginners_guide.html) (Nginx - Docs)
- [Ubuntu Server documentation](https://ubuntu.com/server/docs) (Ubuntu - Docs)
- [Ejemplos de SERVER BLOCKS](https://www.nginx.com/resources/wiki/start/topics/examples/server_blocks/) (Nginx - Docs)
