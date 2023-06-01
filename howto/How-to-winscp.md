# Conectar con una maquina virtual.   
<p><code>Servicios informáticos en VPS</code></p>
<p>Creado por <code>Giancarlo Ortiz</code>

<br>

---
## [1. WinSCP](#)  ✔
### <code>Cliente Seguro FTP</code>

1. Crear un alias de correo para administrar AWS y con el crear una cuenta de en la [plataforma de amazon][1] (necesario tarjeta de crédito, se descontaran 3,000 pesos que luego se regresaran).
1. Después de diligenciar los datos personales espera confirmación via SMS de la cuenta creada e [iniciamos sesión][2] en AWS, con el correo y la contraseña registrados.
1. En la plataforma en el menu de servicios encontramos el panel de Elastic Compute, EC2;  para administrar varios [tipos de instancias][3] de servidores virtuales.
1. Damos click en Lanzar instancia para crear una instancia t2.micro con Ubuntu Linux y hasta 30 GB de almacenamiento en SSD apta para [capa gratuita][4] (750 horas al mes y 100GB de ancho de banda por 12 meses)
    1. Habilitar trafico SSH para poder conectarse via [OpenSSH][41] a la instancia virtual.
    1. Habilitar HTTP, HTTPS para [mapear los puertos][42] 80 y 443 según se requiera.
    1. Generar un par de [claves publicas][43] y guardar el archivo.

1. Iniciar la instancia, esperar por el estado "[Running][5_1]" o en ejecución y esperar a que asigne una ip publica dinámica (cambiara con cada inicio de la instancia).
1. Dar click en el ID de la instancia donde tenemos acceso a todos los detalles de la instancia en ejecución y de donde podemos conectar con la instancia desde el navegador web usando SSH sobre [webSocket][6].
1. Luego de conectarse a la instancia ejecutar [update][7] para actualizar la lista de paquetes disponibles en los repositorios de ubuntu y [upgrade][7] para actualizar los paquetes que se necesite a su version mas reciente.
1. Al finalizar las pruebas puede detener la instancia, las [instancias detenidas][8] no generan cargos.

>__Nota:__ una sola instancia nunca superara las 750 horas disponibles mensualmente, pero puedes crear varias instancias con un propósito especifico y alternar su uso sin superar los limites de la capa gratuita. 

<br>

## [2. Comandos necesarios](#)  ✔
### <code>Interfaz de linea de comandos</code>

```bash
# Comandos para actualizar los paquetes a su version mas reciente 
sudo apt update
sudo apt upgrade
```

[1]:https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?pg=ec2price&cta=herobtn
[2]:https://console.aws.amazon.com/console/home?nc2=h_ct&src=header-signin
[3]:https://aws.amazon.com/es/ec2/pricing/on-demand/
[4]:https://aws.amazon.com/es/free/free-tier/?p=ft&z=subnav&loc=1&refid=ft_card
[41]:https://es.wikipedia.org/wiki/OpenSSH
[42]:https://es.wikipedia.org/wiki/Redirecci%C3%B3n_de_puertos
[43]:https://es.wikipedia.org/wiki/Criptograf%C3%ADa_asim%C3%A9trica
[5]:https://docs.aws.amazon.com/es_es/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html
[6]:https://es.wikipedia.org/wiki/WebSocket
[7]:https://manpages.ubuntu.com/manpages/xenial/man8/apt.8.html
[8]:https://docs.aws.amazon.com/es_es/AWSEC2/latest/UserGuide/Stop_Start.html


<br>

---
## Mas Recursos
- [WinSCP](https://es.wikipedia.org/wiki/WinSCP) (Wikipedia)
- [Tutorial de introducción](https://docs.aws.amazon.com/es_es/AWSEC2/latest/UserGuide/EC2_GetStarted.html) (AWS - Docs)
- [Instalar LAMP](https://docs.aws.amazon.com/es_es/AWSEC2/latest/UserGuide/tuts-lamp.html) (AWS - Docs)



Redis 
Shardear