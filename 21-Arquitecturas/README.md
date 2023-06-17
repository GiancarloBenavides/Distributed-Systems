# Sistemas Descentralizados
<p><code>Fundamentos de sistemas Distribuidos</code></p>
<p>Creado por <code>Giancarlo Ortiz</code> y <code>Diego Villareal</code> para explicar los fundamentos de los <code>Sistemas distribuidos</code></p>

## Arquitectura de software
La arquitectura de software de un sistema es el conjunto de estructuras necesarias para dar sentido a un sistema, lo cual abarca los elementos del software, las relaciones entre ellos y las propiedades de ambos

## Agenda
1. [Cliente-Servidor](#1-cliente-servidor).
1. [Multi-capas](#2-multi-capa).
1. [Red entre iguales](#3-red-entre-iguales).
1. [Cadena de bloques](#4-cadena-de-bloques).

<br>

---
# 1. Cliente-Servidor
Una arquitectura [Client–server][1] se refiere a un sistema donde los clientes inteligentes se ponen en contacto con el servidor para hacer peticiones de datos, formatearlos y mostrarlos en una vista a los usuarios. Si los datos fueron modificados por el cliente se envían para persistir los datos en el servidor.

* ><i>"La ciencia es una ecuación diferencial;<br>
la religión es una condición de frontera."</i><br>
<cite style="display:block; text-align: right">[Alan Turing](https://es.wikipedia.org/wiki/Alan_Turing)</cite>

[1]:https://es.wikipedia.org/wiki/Cliente-servidor

## 1.1. Servicios en internet ✔

![Imagen de sistemas mainframe](../img/client-server.svg "Sistemas mainframe")

## 1.2. Características ✔
* Los clientes hacen solicitudes de servicio.
* Los servidores dan respuesta a solicitudes de servicio.
* Los clientes inician la comunicación con el servidor.
* Los Los servidores proveen el servicio.

## 1.3. Multiples clientes ✔

![Imagen de servidores con multiples clientes](../img/a-cliente-servidor.svg "Sistemas centralizados")

<br>

# 2. Multi-capas
Una arquitectura [n-Tier][2] se refiere a sistemas donde el servidor reenvía peticiones del cliente a otros servicios conectados.

* ><i>"Es indigno que hombres notables pierdan su tiempo como esclavos del cálculo cuando podrían dejar ese trabajo en manos de cualquiera si se usaran las máquinas."</i><br><cite style="display:block; text-align: right">[Gottfried Leibniz](https://es.wikipedia.org/wiki/Gottfried_Leibniz)</cite>

[2]:https://es.wikipedia.org/wiki/Programaci%C3%B3n_por_capas

## 2.1. Multiples servidores ✔

![Imagen de sistemas centralizados](../img/a-mulilayer-server.svg "Sistemas centralizados")


## 2.2. Características ✔
* Los terminales locales realizan procesos propios.
* Los procesos locales y remotos no comparten memoria.
* Los terminales locales y remotos comparten recursos en una red.
* Los procesos remotos pueden ejecutarse sincronizados o pueden ser asíncronos.
* Capacidad de escalar verticalmente y horizontalmente.
* Clientes débilmente acoplados al servidor, si alguna capa falla puede fallar la aplicación.

<br>

# 3. Red entre iguales
Una arquitectura [P2P][3] se refiere a sistemas donde no hay máquinas especiales que presten un servicio o gestionen los recursos de la red. En su lugar, todas las responsabilidades se reparten uniformemente entre todas las máquinas, conocidas como peers.

* ><i>"La gente con conocimientos técnicos está dispuesta a perdonar a un ordenador que se cuelga un par de veces al año, pero los usuarios normales no."</i><br><cite style="display:block; text-align: right"> [Andrew S. Tanenbaum](https://es.wikipedia.org/wiki/Andrew_S._Tanenbaum)</cite>

[3]:https://es.wikipedia.org/wiki/Peer-to-peer

## 3.1. Multiples servidores ✔

![Imagen de sistemas distribuidos](../img/os-distributed.svg "Sistemas Distribuidos")


## 3.2. Características ✔
* Procesamiento Cooperativo.
* Los procesos locales y remotos no comparten memoria.
* Los procesos remotos son asíncronos.
* Operaciones similares o idénticas para acceder a objetos locales o remotos.
* Capacidad de escalar verticalmente y horizontalmente.
* Clientes desacoplados a un servidor, la falla de un terminal no afecta al sistema.

<br>

# 4. Cadena de bloques
Un sistema [descentralizado][3] es un grupo de entidades que permiten el procesamiento de información intercambiando información entre pares, sin que exista un nodo único que toma las decisiones. 

* ><i>"Si nadie se ríe de alguna de tus ideas, entonces significa que no estás siendo demasiado creativo."</i><br><cite style="display:block; text-align: right"> [Bill Gates](https://es.wikipedia.org/wiki/Bill_Gates)</cite>

[3]:https://en.wikipedia.org/wiki/Distributed_operating_system

## 4.1. Multiples servidores ✔

![Imagen de sistemas distribuidos](../img/os-distributed.svg "Sistemas Distribuidos")


## 4.2. Características ✔
* Un solo nodo no conoce el estado de todo el sistema.
* Cada nodo toma la decision mas conveniente.
* La respuesta colectiva se logra en función del consenso entre pares.
* Multiples controladores.
* Distribución de los costes (recursos) entre los usuarios.
* Capacidad de escalar horizontalmente con rapidez.
* Clientes desacoplados.


<br>

---
## Mas Recursos
- [Computación distribuida](https://es.wikipedia.org/wiki/Computaci%C3%B3n_distribuida) (Wikipedia)
- [Problema de los dos generales](https://es.wikipedia.org/wiki/Problema_de_los_dos_generales) (Wikipedia)
- [Cadena de bloques](https://es.wikipedia.org/wiki/Cadena_de_bloques) (Wikipedia)
- [Red entre iguales](https://es.wikipedia.org/wiki/Peer-to-peer) (Wikipedia)