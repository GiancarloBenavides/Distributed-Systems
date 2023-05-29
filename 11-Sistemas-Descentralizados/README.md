# Sistemas Descentralizados
<p><code>Fundamentos de sistemas Distribuidos</code></p>
<p>Creado por <code>Giancarlo Ortiz</code> y <code>Diego Villareal</code> para explicar los fundamentos de los <code>Sistemas distribuidos</code></p>

## Fundamentos
La administración y los servicios que ofrece un sistema de procesamiento digital, pueden estar distribuidos en diferentes componentes de hardware y según como organicen pueden ser clasificados.

## Agenda

1. [Sistemas mainframe](#1-sistemas-mainframes).
1. [Sistemas Centralizados](#2-sistemas-centralizados).
1. [Sistemas Descentralizados](#3-sistemas-distribuidos).

<br>


---
# 1. Sistemas Mainframes
Un sistemas operativo [mainframe][1] es una entidad que permite el procesamiento de información y soporta multiples usuarios en multiples terminales falsas, que no tienen capacidad de procesamiento.

* ><i>"La ciencia es una ecuación diferencial;<br>
la religión es una condición de frontera."</i><br>
<cite style="display:block; text-align: right">[Alan Turing](https://es.wikipedia.org/wiki/Alan_Turing)</cite>

[1]:https://es.wikipedia.org/wiki/Unidad_central

## 1.1. Multiples terminales ✔

![Imagen de sistemas distribuidos](../img/os-multi-station.svg "Sistemas mainframe")

## 1.2. Características ✔
* Las terminales locales no realizan procesos.
* Todos los procesos se ejecutan en el mainframe y comparten memoria.
* Los procesos pueden ejecutarse paralelos o en concurrencia.
* Existe un reloj común y global entre las terminales y usuarios.
* No es necesaria la sincronización.
* Capacidad de escalar unicamente verticalmente.
* Terminales fuertemente acoplados al mainframe, si falla falla el sistema.

<br>

# 2. Sistemas Centralizados
Un sistemas operativo [centralizado][2] es una entidad que permite el procesamiento de información y soporta multiples usuarios en multiples terminales inteligentes, que intercambian información de cliente a servidor.

* ><i>"Es indigno que hombres notables pierdan su tiempo como esclavos del cálculo cuando podrían dejar ese trabajo en manos de cualquiera si se usaran las máquinas."</i><br>
<cite style="display:block; text-align: right">[Gottfried Leibniz](https://es.wikipedia.org/wiki/Gottfried_Leibniz)</cite>

[2]:https://es.wikipedia.org/wiki/Computaci%C3%B3n_centralizada

## 2.1. Multiples clientes ✔

![Imagen de sistemas centralizados](../img/os-centralized%20.svg "Sistemas centralizados")

## 2.2. Características ✔
* Los terminales locales realizan procesos propios.
* Los procesos locales y remotos no comparten memoria.
* Los terminales locales y remotos comparten recursos en una red.
* Los procesos remotos pueden ejecutarse sincronizados o pueden ser asíncronos.
* Capacidad de escalar verticalmente y horizontalmente.
* Posibilita la distribución de una aplicación por capas.
* Clientes débilmente acoplados al servidor, si alguna capa falla puede fallar la aplicación.

<br>

# 3. Sistemas distribuidos
Un sistemas operativo [distribuido][3] es una entidad que permite el procesamiento de información y soporta multiples usuarios en multiples terminales inteligentes, que intercambian información entre pares.

* ><i>"La gente con conocimientos técnicos está dispuesta a perdonar a un ordenador que se cuelga un par de veces al año, pero los usuarios normales no."</i><br><cite style="display:block; text-align: right">
[Andrew S. Tanenbaum](https://es.wikipedia.org/wiki/Andrew_S._Tanenbaum)</cite>

[3]:https://en.wikipedia.org/wiki/Distributed_operating_system

## 3.1. Multiples servidores ✔

![Imagen de sistemas distribuidos](../img/os-distributed.svg "Sistemas Distribuidos")

## 3.2. Características ✔
* Los procesos locales y remotos no comparten memoria.
* Los procesos remotos son asíncronos.
* Capacidad de escalar verticalmente y horizontalmente.
* Clientes desacoplados a un servidor, la falla de un terminal no afecta al sistema.

## 3.3 Ventajas y desventajas ✔

| Ventajas | Desventajas |
|--|--|
| Mas barato escalar | Mas complejo escalar |
| Tolerancia a fallos | Confiabilidad |
| Mas flexible | Menos seguro |
| Colaborativo | Inconsistencias |
| Mas transparente | Análisis complejo  | 

<br>

---
## Mas Recursos
- [Computación distribuida](https://es.wikipedia.org/wiki/Computaci%C3%B3n_distribuida) (Wikipedia)
- [Problema de los dos generales](https://es.wikipedia.org/wiki/Problema_de_los_dos_generales) (Wikipedia)


- [Cadena de bloques](https://es.wikipedia.org/wiki/Cadena_de_bloques) (Wikipedia)
- [Red entre iguales](https://es.wikipedia.org/wiki/Peer-to-peer) (Wikipedia)


- [Llamada a procedimiento remoto](https://es.wikipedia.org/wiki/Llamada_a_procedimiento_remotos) (Wikipedia)


- [Distributed Component Object Model](https://es.wikipedia.org/wiki/Modelo_de_Objetos_de_Componentes_Distribuidos) (Wikipedia)
- [Common Object Request Broker Architecture](https://es.wikipedia.org/wiki/CORBA) (Wikipedia)
- [Remote Method Invocation](https://es.wikipedia.org/wiki/Java_Remote_Method_Invocation) (Wikipedia)
- [Simple Object Access Protocol](https://es.wikipedia.org/wiki/Simple_Object_Access_Protocol) (Wikipedia)