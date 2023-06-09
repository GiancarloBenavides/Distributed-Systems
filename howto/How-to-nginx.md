# Crear un servicio web con Nginx.   
<p><code>Servicios informáticos en Ubuntu Server</code></p>
<p>Creado por <code>Giancarlo Ortiz</code>

<br>

---
## [1. Nginx](#)  ✔
### <code>Servidor web Ligero</code>
Para construir un servicio de [alojamiento web][alw].

1. Antes de instalar un nuevo paquete en [Ubuntu Server][1] siempre es recomendable actualizar la lista de paquetes disponibles y actualizar los paquetes instalados a su version mas reciente; para ello es necesario usar la herramienta de empaquetado disponible en la distribución Linux, en el caso de las distribuciones derivadas de Debian esta herramienta de linea de comandos es _Advanced Packaging Tool_. 
2. Usando la herramienta [apt][2] instalar el paquete del servidor web Nginx; para ello no es necesario agregar fuentes a la lista ya que el paquete esta disponible en los repositorios oficiales de de la distribución.
3. Instalar [nano][3] o el editor de texto de preferencia para editar los archivos de configuración de Nginx.
4. Crear una estructura de directorios usando el comando [mkdir][4] para al los archivos del sitio que se desea servir con Nginx y para el historial de eventos de uso y errores del servidor web.
5. Crear una copia del [server block][5] por defecto habilitado en Nginx, editar la copia del nuevo server block para enrutar una solicitud de dominio al recurso correspondiente y habilitarlo para que se incluya en la configuración de Nginx que se procesa al cargar el servidor.
6. __Opcional:__ Si se requiere [alojamiento compartido][6] se pueden repetir los pasos 4-5 para crear varios server blocks y atender solicitudes de multiples dominios y subdominios en un único servidor físico.
7. __Opcional:__ [eliminar][7] el enlace de la carpeta de habilitados para deshabilitar el server block por defecto de Nginx.
8. Revisar y aplicar la [configuración][8] del servidor reiniciando o recargando el servicio.

---

>__Nota:__ No hay limite de server blocks en una instancia de Nginx siempre que el servidor sea capaz de procesar el trafico demandado para todos los dominios. 

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

[1]:https://ubuntu.com/server
[2]:https://manpages.ubuntu.com/manpages/kinetic/man8/apt.8.html
[3]:https://manpages.ubuntu.com/manpages/kinetic/en/man1/nano.1.html
[4]:https://manpages.ubuntu.com/manpages/kinetic/en/man1/mkdir.1.html
[5]:https://www.nginx.com/resources/wiki/start/topics/examples/server_blocks/
[6]:https://es.wikipedia.org/wiki/Alojamiento_compartido
[7]:https://manpages.ubuntu.com/manpages/kinetic/en/man1/rm.1.html
[8]:https://nginx.org/en/docs/switches.html

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
