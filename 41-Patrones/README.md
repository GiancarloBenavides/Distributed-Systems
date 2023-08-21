# Sistemas Descentralizados
<p><code>Fundamentos de sistemas Distribuidos</code></p>
<p>Creado por <code>GncDev</code> para explicar los fundamentos de los <code>Sistemas distribuidos</code>.</p>

## Patrones arquitectónicos para sistemas distribuidos
Los patrones arquitectónicos son aquellas soluciones recurrentes a un problema de diseño entre componentes y su relación entre ellos y puede estar conformada de uno o más patrones de diseño.

## Agenda
1. [Patrones para implementación](#1-sistemas-distribuidos).
1. [Recursos para implementación](#2-sistemas-descentralizados).

<br>

---
# 1. [Patrones para implementación](#agenda)
Los patrones de diseño que regularmente se implementan en un sistema distribuido se pueden dividir por escenarios de uso, según el componente que se desea escalar o desacoplar de el resto del sistema.

## 1.1 Patrones de descomposición ✔
* [Domain driven design][11_1] - Para basar el diseño en el modelo.
* [Bulkhead][11_2] - Para mejorar la tolerancia a fallas.
* [Strangler][11_2] - Para migrar un sistema heredado.

[11_1]:https://es.wikipedia.org/wiki/Dise%C3%B1o_guiado_por_el_dominio
[11_2]:https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead
[11_3]:https://learn.microsoft.com/es-es/azure/architecture/patterns/strangler-fig

## 1.2 Patrones de infraestructura ✔
* [Service discovery][12_1] - Para registro y detección automática de servicios.
* [Circuit breaker design pattern][12_2] - Para comprobar disponibilidad.
* [Patron de Balanceo de carga][12_3] - Para escalar.

[12_1]:https://en.wikipedia.org/wiki/Service_discovery
[12_2]:https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern
[12_3]:https://es.wikipedia.org/wiki/Equilibrio_de_carga

## 1.3 Patrones de integración ✔
* [API gateway][13_1] - Para un único punto de entrada a varios micro-servicios.
* [Patron productor/consumidor][13_2] - Para actualizar por eventos.
* [Patron saga][13_3] - Para transacciones distribuidas.

[13_1]:https://es.wikipedia.org/wiki/Gesti%C3%B3n_de_API
[13_2]:https://es.wikipedia.org/wiki/Arquitectura_dirigida_por_eventos
[13_3]:https://docs.aws.amazon.com/es_es/prescriptive-guidance/latest/modernization-data-persistence/saga-pattern.html


## 1.4 Patrones de acceso a datos ✔
* [Command Query Responsibility Segregation][14_1] - Para separar Lectura/Escritura.
* [Bases de datos por dominio][14_1] - Para fragmentar la persistencia.
* [Sharding][14_2] - Para fragmentar bases de datos.

[14_1]:https://docs.aws.amazon.com/es_es/prescriptive-guidance/latest/modernization-data-persistence/cqrs-pattern.html
[14_2]:https://es.wikipedia.org/wiki/Modelo_de_dominio
[14_3]:https://en.wikipedia.org/wiki/Shard_(database_architecture)#

<br>

# 2. [Recursos para implementación](#agenda)
Algunos recursos útiles para implementar una arquitectura de Microservicios.

## 2.1. Conceptos Útiles ✔
* [__BLOG:__][21_1] -> [Chris Richardson][21_1] .
* [__BLOG:__][21_2] -> [Martin Fowler][21_2] .
* [__BLOG:__][21_3] -> [Robert Cecil Martin][21_3] 

[21_1]:https://microservices.io/
[21_2]:https://www.martinfowler.com/microservices/
[21_3]:http://blog.cleancoder.com/uncle-bob/2014/10/01/CleanMicroserviceArchitecture.html


## 2.2. Tecnologías multiplataforma ✔
* [__BIBLIOTECA:__][22_1] gRPC - sistema RPC multiplataforma.
* [__SOFTWARE:__][22_2] Redis - Base de datos en memoria.
* [__SOFTWARE:__][22_2] RabbitMQ - Base de datos en memoria.

[22_1]:https://grpc.io/docs/languages/python/
[22_2]:https://redis.io/docs/clients/om-clients/stack-python/
[22_3]:https://www.rabbitmq.com/tutorials/tutorial-one-python.html


## 2.3. ASP.NET de Microsoft  ✔
* [__TUTORIALES:__][23_1] distribuidos con Microsoft .NET
* [__TUTORIALES:__][23_2] patrones para implementar [micro-servicios con .NET][23_2]
* [__LIBRO:__][23_3] De la Torre, C. 2021. [Microservicios .NET: arquitectura para aplicaciones .NET en contenedores][23_3]. 7Ed. Microsoft Corp.

[23_1]:#41-sistemas-distribuidos-con-aspnet-de-microsoft-✔
[23_2]:https://www.netmentor.es/entrada/patron-api-gateway
[23_3]:https://learn.microsoft.com/en-us/dotnet/architecture/microservices/


## 2.3. Python  ✔
* [__BIBLIOTECA:__][23_1] Pyro5 - Python Remote Objects.
* [__BIBLIOTECA:__][23_2] FastAPI - Micro-framework 
* [__TEMPLATE:__][23_2] Estructura de carpetas.

```shell
# Para agregar Pyro5 a una instalación de Python
# https://pypi.org/project/Pyro5/
pip install Pyro5
```

[23_1]:https://pyro5.readthedocs.io/en/latest/
[23_2]:https://fastapi.tiangolo.com/tutorial/
[23_3]:https://alvaromonsalve.com/2021/03/11/microservicios-en-python-plantilla-basica/

<br>

---
## Mas Recursos
- [Arquitectura de software](https://es.wikipedia.org/wiki/Arquitectura_de_software) (Wikipedia)
- [Patrón de diseño](https://es.wikipedia.org/wiki/Patr%C3%B3n_de_dise%C3%B1o) (Wikipedia)
- [Video curso introductorio de patrones para sistemas distribuidos](https://www.youtube.com/watch?v=a-2T09eV6uw&list=PLesmOrW3mp4jpSbdFMtVWINJZ7OLdSASS) (YuTube)