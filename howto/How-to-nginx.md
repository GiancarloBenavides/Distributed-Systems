# Crear un servicio web con Nginx.   
<p><code>Servicios informáticos en Ubuntu</code></p>
<p>Creado por <code>Giancarlo Ortiz</code>

<br>

---
## [1. Nginx](#)  ✔
### <code>Servidor web Ligero</code>

1. Conectarse a la instancia y ejecutar [update][1] para actualizar la lista de paquetes disponibles en los repositorios de ubuntu y [upgrade][1] para actualizar los paquetes que se necesite a su version mas reciente.
1. Instalar el paquete del servidor web usando el comando [apt][1]. No hay necesidad de agregar fuentes ya que esta disponible en los repositorios oficiales de Ubuntu.
1. Instalar [nano][3] o el editor de texto de preferencia.
1. Crear un directorio usando el comando [mkdir][4] para alojar el historial de errores  los archivos del sitio que se desea servir con Nginx.
1. Crear un directorio usando el comando [mkdir][4] para el historial de eventos de uso y errores del servidor web.
1. Crear un copia del [server block][6] por defecto de Nginx.
1. Editar la copia del nuevo [server block][6] para enrutar una solicitud de dominio al recurso correspondiente.
1. Habilitar el nuevo [server block][6] para que se incluya en la configuración de Nginx que se procesa al cargar el servidor.

---

>__Nota:__ una sola instancia nunca superara las 750 horas disponibles mensualmente, pero puedes crear varias instancias con un propósito especifico y alternar su uso sin superar los limites de la capa gratuita. 

<br>

## [2. Comandos necesarios](#)  ✔
### <code>Interfaz de linea de comandos</code>
En los comandos reemplazar la cadena _"com.domain-name"_ con el nombre de dominio registrado en [notación de dominio inverso][cmd].

```sh
# Para actualizar los paquetes a su version mas reciente 
sudo apt update
sudo apt upgrade
# Para instalar el servidor web
sudo apt install nginx nano
# Para crear la carpeta para alojar el sitio web
sudo mkdir -p /var/www/domain-name.com/html
# Para crear una carpeta para los archivos de registro, log; de errores de apache
sudo mkdir -p /var/log/apache2/domain-name.com/html
# Para crear un nuevo Server Block, copiar el archivo por defecto en otro archivo
sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/domain-name.com
# Para editar el nuevo Server Block
sudo nano /etc/nginx/sites-available/domain-name.com
# Para habilitar el sitio creado
sudo ln -s /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled/
```
<br>

## [3. Comandos necesarios](#)  ✔
### <code>Interfaz de linea de comandos</code>


[1]:https://manpages.ubuntu.com/manpages/kinetic/man8/apt.8.html
[3]:https://manpages.ubuntu.com/manpages/kinetic/en/man1/nano.1.html
[4]:https://manpages.ubuntu.com/manpages/kinetic/en/man1/mkdir.1.html
[6]:https://www.nginx.com/resources/wiki/start/topics/examples/server_blocks/

[cmd]:https://es.wikipedia.org/wiki/Notaci%C3%B3n_de_nombre_de_dominio_inverso

[7]:1

<br>

---
## Mas Recursos
- [Nginx](https://es.wikipedia.org/wiki/Nginx) (Wikipedia)
- [Tutorial de introducción](https://nginx.org/en/docs/beginners_guide.html) (Nginx - Docs)
- [Ejemplos de SERVER BLOCKS](https://www.nginx.com/resources/wiki/start/topics/examples/server_blocks/) (Nginx - Docs)
