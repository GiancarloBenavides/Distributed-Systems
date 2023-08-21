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
# 1. Patrones para implementación


## 1.1 Patrones de descomposición ✔
* Patron [DDD][11_1] (Domain Driven Design) - Para basar el diseño en el modelo.

[11_1]:https://es.wikipedia.org/wiki/Dise%C3%B1o_guiado_por_el_dominio


## 1.2 Patrones de infraestructura ✔
* Patron de [Balanceo de carga][12_1]
* Patron [Circuit breaker design pattern][12_2]

[12_1]:https://es.wikipedia.org/wiki/Equilibrio_de_carga
[12_2]:https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern


## 1.3 Patrones de integración ✔
* Patron [API Gateway][13_1] - Para un único punto de entrada a varios micro-servicios.
* Patron productor consumidor.
* Patron [Saga][13_3] - Para transacciones distribuidas

[13_1]:https://es.wikipedia.org/wiki/Gesti%C3%B3n_de_API
[13_3]:https://docs.aws.amazon.com/es_es/prescriptive-guidance/latest/modernization-data-persistence/saga-pattern.html


## 1.4 Patrones de acceso a datos ✔
* Patron [CQRS][14_1] (Command Query Responsibility Segregation) - Para separar Lectura/Escritura.
* Patron [Sharding][14_2] - Para fragmentar bases de datos.

[14_1]:https://docs.aws.amazon.com/es_es/prescriptive-guidance/latest/modernization-data-persistence/cqrs-pattern.html
[14_2]:https://en.wikipedia.org/wiki/Shard_(database_architecture)

<br>

# 2. Recursos para implementación
## 2.1. Sistemas Distribuidos con ASP.NET de Microsoft  ✔
* [__TUTORIALES:__][21_1] patrones para implementar [micro-servicios con .NET][21_2]
* [__LIBRO:__][21_3] De la Torre, C. 2021. [Microservicios .NET: arquitectura para aplicaciones .NET en contenedores][21_3]. 7Ed. Microsoft Corp.

[21_1]:#41-sistemas-distribuidos-con-aspnet-de-microsoft-✔
[21_2]:https://www.netmentor.es/entrada/patron-api-gateway
[21_3]:https://learn.microsoft.com/en-us/dotnet/architecture/microservices/


## 2.1. Sistemas Distribuidos con Python  ✔
* [__BIBLIOTECA:__][21_1] Pyro5 - Python Remote Objects.


```shell
# Para agregar Pyro5 a una instalación de Python
# https://pypi.org/project/Pyro5/
pip install Pyro5
```

[21_1]:https://pyro5.readthedocs.io/en/latest/

<br>

---
## Mas Recursos
- [Arquitectura de software](https://es.wikipedia.org/wiki/Arquitectura_de_software) (Wikipedia)
- [Patrón de diseño](https://es.wikipedia.org/wiki/Patr%C3%B3n_de_dise%C3%B1o) (Wikipedia)
- [Video curso introductorio de patrones para sistemas distribuidos](https://www.youtube.com/watch?v=a-2T09eV6uw&list=PLesmOrW3mp4jpSbdFMtVWINJZ7OLdSASS) (YuTube)


---

Redis 
Shardear

- ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png) `#f03c15`
- ![#c5f015](https://placehold.co/15x15/c5f015/c5f015.png) `#c5f015`
- ![#1589F0](https://placehold.co/15x15/1589F0/1589F0.png) `#1589F0`