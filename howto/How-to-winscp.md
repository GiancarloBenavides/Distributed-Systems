# Conectar con una maquina virtual remota.   
<p><code>Servicios informáticos en VPS</code></p>
<p>Creado por <code>Giancarlo Ortiz</code>

<br>

---
## [1. WinSCP](#)  ✔
### <code>Cliente Seguro FTP</code>
El equipo debe remoto debe tener instalado OpenSSH y habilitado el subsistema sftp-server para permitir conectarse al sistema de archivos remoto.

1. Verificar que OpenSSH este instalado en el equipo remoto.
1. Descargar WinSCP de [sitio web oficial][1].
1. Ejecutar el [cliente WinSCP][2] para conectarse al sistema de archivos remoto.
1. En el panel izquierdo seleccionar nuevo sitio para almacenar una nueva conexión [SFTP][3] a la configuración.
1. Configurar las opciones de la session y guardar:
    1. __Protocolo:__ SFTP
    1. __Port:__ 22
    1. __Hostname:__ DNS o IPv4 del servidor remoto 
    1. __Username:__ Ubuntu
    1. __Password:__ en blanco si se conecta mediante llave criptográfica.
1. Configurar opciones avanzadas.
    1. __SSH/Authentication/PrivateKeyFile:__  si se conecta mediante llave criptográfica, seleccionar el archivo que contiene la llave privada generada o descargada del servidor al que se desea conectar.
    1. __Environment/SFTP/SFTPServer:__ seleccionar [sudo su -c /usr/lib/openssh/sftp-server][sudo] para ejecutar el servicio como root.

>__Nota:__ FTP no es un protocolo seguro, SFTP es un protocolo distinto y puede usar [criptografía asimétrica][4] para encriptar todo el contenido que se transfiere por la conexión con la clave publica y que solo puede ser descifrado con la clave privada. 

<br>

## [2. Comandos necesarios](#)  ✔
### <code>Interfaz de linea de comandos</code>

```bash
# Comandos para actualizar los paquetes del computador remoto a su version mas reciente 
sudo apt update
sudo apt upgrade
sudo apt install openssh-server
sudo systemctl status ssh
$ sudo systemctl enable ssh
$ sudo systemctl start ssh

```

[1]:https://winscp.net/eng/downloads.php
[2]:https://es.wikipedia.org/wiki/WinSCP
[3]:https://es.wikipedia.org/wiki/SSH_File_Transfer_Protocol
[4]:https://es.wikipedia.org/wiki/Criptograf%C3%ADa_asim%C3%A9trica


<br>
---
## Mas Recursos
- [WinSCP](https://es.wikipedia.org/wiki/WinSCP) (Wikipedia)
- [Tutorial de introducción](https://winscp.net/eng/docs/guide_amazon_ec2) (WinSCP - Docs)
- [Instalar LAMP](https://docs.aws.amazon.com/es_es/AWSEC2/latest/UserGuide/tuts-lamp.html) (AWS - Docs)

