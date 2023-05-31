# Sistemas Descentralizados
<p><code>Fundamentos de sistemas Distribuidos</code></p>
<p>Creado por <code>Giancarlo Ortiz</code> y <code>Diego Villareal</code> para explicar los fundamentos de los <code>Sistemas distribuidos</code></p>

## Patrones arquitectónicos para sistemas distribuidos
Los patrones arquitectónicos son aquellas soluciones recurrentes a un problema de diseño entre componentes y su relación entre ellos y puede estar conformada de uno o más patrones de diseño.


## Agenda
1. [Sistemas mainframe](#1-sistemas-mainframes).
1. [Sistemas centralizados](#2-sistemas-centralizados).

1. [Patrones para implementación](#3-sistemas-distribuidos).
1. [Recursos para implementación](#4-sistemas-descentralizados).

<br>

---
# 3. Patrones para implementación

## 3.1 Patrones de descomposición ✔
* Patron Domain Driven Design (DDD) - Para basar el diseño en el modelo.

## 3.2 Patrones de infraestructura ✔
* Balanceo de carga

## 3.3 Patrones de integración ✔
* Patron API Gateway - Para un único punto de entrada a varios micro-servicios.
* Patron productor consumidor.
* Patron Saga - Para transacciones distribuidas

## 3.4 Patrones de acceso a datos ✔
* Patron CQR - Para separar lectura/Escritura.



# 4. Recursos para implementación
## 4.1. Sistemas Distribuidos con ASP.NET de Microsoft  ✔
* [__TUTORIALES:__][41_1] patrones para implementar [micro-servicios con .NET][41_2]
* [__LIBRO:__][41_1] De la Torre, C. 2023. [Microservicios .NET: arquitectura para aplicaciones .NET en contenedores][41_3]. 7Ed. Microsoft Corp.

[41_1]:#41-sistemas-distribuidos-con-aspnet-de-microsoft-✔
[41_2]:https://www.netmentor.es/entrada/patron-api-gateway
[41_3]:https://learn.microsoft.com/en-us/dotnet/architecture/microservices/

## 4.1. Sistemas Distribuidos con Python  ✔
* [__BIBLIOTECA:__][42_1] Pyro5 - Python Remote Objects.
* [__BIBLIOTECA:__][42_1] Pyro5 - Python Remote Objects.

```shell
# Para agregar Pyro5 a una instalación de Python
# https://pypi.org/project/Pyro5/
pip install Pyro5
```

[42_1]:https://pyro5.readthedocs.io/en/latest/

<br>

---
## Mas Recursos
- [Video curso introductorio de patrones para sistemas distribuidos](https://www.youtube.com/watch?v=a-2T09eV6uw&list=PLesmOrW3mp4jpSbdFMtVWINJZ7OLdSASS) (YuTube)


- [Llamada a procedimiento remoto](https://es.wikipedia.org/wiki/Llamada_a_procedimiento_remotos) (Wikipedia)


- [Distributed Component Object Model](https://es.wikipedia.org/wiki/Modelo_de_Objetos_de_Componentes_Distribuidos) (Wikipedia)
- [Common Object Request Broker Architecture](https://es.wikipedia.org/wiki/CORBA) (Wikipedia)
- [Remote Method Invocation](https://es.wikipedia.org/wiki/Java_Remote_Method_Invocation) (Wikipedia)
- [Simple Object Access Protocol](https://es.wikipedia.org/wiki/Simple_Object_Access_Protocol) (Wikipedia)