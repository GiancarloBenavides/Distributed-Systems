# Sistemas Descentralizados
<p><code>Fundamentos de sistemas Distribuidos</code></p>
<p>Creado por <code>GncDev</code> para explicar los fundamentos de los <code>Sistemas distribuidos</code>.</p>

## Aplicaciones Distribuidas
Es un enfoque para el desarrollo de software que consiste en construir una aplicación como un conjunto de componentes que se ejecutan en su propio proceso y se comunican entre si con mecanismos ligeros.

## Agenda
1. [Bases de datos](#1-bases-de-datos).
1. [Cluster](#2-Cluster).
1. [Grid](#3-Grid).

<br>

---
# 1. [Bases de datos](#agenda)
Una base de datos distribuida o [BDD][1] es un conjunto de múltiples bases de datos lógicamente relacionadas las cuales se encuentran distribuidas en diferentes espacios lógicos y geográficos.

[1]:https://es.wikipedia.org/wiki/Base_de_datos_distribuida

## 1.1 Características ✔
* Una única base de datos lógica en DDBMS.
* Dividida en fragmentos controlados por un DBMS.
* Múltiples servidores, llamados nodos.
* Red de Computadores necesaria.

### 1.1.1 Ventajas.
* Refleja una estructura organizacional.
* Autonomía local.
* Disponibilidad.
* Rendimiento.
* Economía.
* Modularidad.

### 1.1.2 Desventajas.
* Complejidad.
* Seguridad.
* Desconocimiento.
* Carencia de estándares.
* QoS de la red.

## 1.2 Componentes ✔
* [SBDD][12_1] - Motor de Base de datos distribuido.
* [DDBMS][12_1] - Gestor de base de datos distribuido.
* [DTM][12_1] - Nodo de transacción.
* [DBM][12_1] - Nodo de base de datos.

[12_1]:https://es.wikipedia.org/wiki/Base_de_datos_distribuida


## 1.3. Productos existentes ✔
* [Oracle Database][13_1]
* [PostgreSQL][13_2]
* [SQL Server][13_3]
* [MySQL][13_4]
* [MongoDB][13_5]

[13_1]:https://es.wikipedia.org/wiki/Oracle_Database
[13_2]:https://es.wikipedia.org/wiki/PostgreSQL
[13_3]:https://es.wikipedia.org/wiki/Microsoft_SQL_Server
[13_4]:https://es.wikipedia.org/wiki/MySQL
[13_5]:https://es.wikipedia.org/wiki/MongoDB

## 1.4. Arquitectura ✔

![Imagen de bases de datos distribuidas ](../img/app-db-distributed-.svg "Sistemas distribuidos")

<br>

# 2. [Cluster](#agenda)
Un [clúster][2] se refiere a una colección de recursos de hardware y software que se comportan como si fuesen un único servidor, distribuidos en granjas de servidores unidos entre sí por una red de alta velocidad y disponibilidad.

[2]:https://es.wikipedia.org/wiki/Cl%C3%BAster_de_computadoras


## 2.1. Características ✔
* [Alto rendimiento][21_1].
* [Alta disponibilidad][21_2].
* [Alta Eficiencia][21_3].
* [Equilibrio][21_4].
* [Escalable][21_5].

[21_1]:https://es.wikipedia.org/wiki/Cl%C3%BAster_de_alto_rendimiento
[21_2]:https://es.wikipedia.org/wiki/Cl%C3%BAster_de_alta_disponibilidad
[21_3]:https://en.wikipedia.org/wiki/High-throughput_computing
[21_4]:https://es.wikipedia.org/wiki/Equilibrio_de_carga
[21_5]:https://es.wikipedia.org/wiki/Escalabilidad

## 2.2. Componentes ✔
* Infraestructura de red y protocolos de comunicación.
* Nodos de infraestructura (procesamiento y almacenamiento).
* Sistemas operativos.
* Servicios, middleware y aplicaciones.

## 2.3. Productos existentes ✔
* [Proxmox][23_1].
* [VMware ESXi][23_2].
* [HTCondor][23_3].
* [Xen][23_4].

[23_1]:https://es.wikipedia.org/wiki/Proxmox_Virtual_Environment
[23_2]:https://es.wikipedia.org/wiki/VMware_ESXi
[23_3]:https://en.wikipedia.org/wiki/HTCondor
[23_4]:https://es.wikipedia.org/wiki/Xen

<br>

# 3. [Grid](#agenda)
La computación en malla o [grid computing][3] es una tecnología que permite utilizar de forma coordinada recursos heterogéneos (entre ellos procesadores, almacenamiento y aplicaciones específicas) que no están sujetos a un control centralizado.

[3]:https://es.wikipedia.org/wiki/Computaci%C3%B3n_en_malla


## 3.1. Características ✔
* Conjunto Heterogéneo. 
* Descentralizado.
* Altamente escalable.
* Altamente flexible.

## 3.2. Componentes ✔
* [Conectividad][32_] - Red : tcp/ip.
* [Infraestructura][32_] - Hardware.
* [Recursos][32_] - Servicios.
* [Aplicaciones][32_] - Nodo de transacción.

[32_]:https://es.wikipedia.org/wiki/Computaci%C3%B3n_en_malla

## 2.3. Proyectos existentes ✔
* [SETI@home][33_1].
* [gLite][33_2].
* [UNICORE][33_3].

[33_1]:https://es.wikipedia.org/wiki/SETI@home
[33_2]:https://en.wikipedia.org/wiki/GLite
[33_3]:https://en.wikipedia.org/wiki/UNICORE


<br>

---
## Mas Recursos
- [Almacenamiento conectado en red](https://es.wikipedia.org/wiki/Almacenamiento_conectado_en_red) (Wikipedia)
- [Computación en la nube](https://es.wikipedia.org/wiki/Computaci%C3%B3n_en_la_nube) (Wikipedia)
- [Logical Volume Manager](https://es.wikipedia.org/wiki/Logical_Volume_Manager_(Linux)) (Wikipedia)
- [Shard](https://es.wikipedia.org/wiki/Shard_(arquitectura_de_base_de_datos)) (Wikipedia)
- [RAID](https://es.wikipedia.org/wiki/RAID) (Wikipedia)

