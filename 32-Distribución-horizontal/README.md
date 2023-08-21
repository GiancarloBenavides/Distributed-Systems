# Sistemas Descentralizados
<p><code>Fundamentos de sistemas Distribuidos</code></p>
<p>Creado por <code>GncDev</code> para explicar los fundamentos de los <code>Sistemas distribuidos</code>.</p>

## Distribución Horizontal
es un enfoque para el desarrollo de software que consiste en construir una aplicación como un conjunto de pequeños servicios, los cuales se ejecutan en su propio proceso y se comunican con mecanismos ligeros como una API de recursos HTTP.

## Agenda
1. [Procesamiento local](#1-procesamiento-local).
1. [Procesamiento remoto](#2-procesamiento-remoto).

<br>

---
# 1. [Procesamiento local](#agenda)
Una modelo de [Procesamiento local][1] es un enfoque para el que las capas de software se procesan unicamente en servidores controlados por el desarrollador.

* ><i>"Las grandes oportunidades, solo nacen;<br>
de haber sabido aprovechar las pequeñas."</i><br>
<cite style="display:block; text-align: right">[Bill Gates](https://es.wikipedia.org/wiki/Bill_Gates)</cite>

[1]:https://svelte.dev/docs/client-side-component-api

## 1.1. Características ✔
* Puede ser distribuida en el servidor.
* Todos los datos se procesan en los servidores.
* La visualización en pantalla es un reflejo de la estación remota.
* Un cambio en el cliente requiere nuevos datos de la capa.
* Los datos se entregan al cliente en estado final.


### 1.1.1. Ventajas.
* Control de la seguridad.
* Control del rendimiento.
* Control del costo.
* Pocas dependencias.


### 1.1.2. Desventajas.
* Mas difíciles de mantener.
* Mas difíciles de escalar.
* Menos flexibles.
* Mas complejas.

### 1.1.2. Arquitectura

![Imagen de sistemas centralizados](../img/a-mulilayer-server.svg "Sistemas centralizados")

## 1.2. Ejemplos ✔
* [SSG][12_1] - static site generation
* [SSR][12_2] - server side rendering

[12_1]:https://es.wikipedia.org/wiki/P%C3%A1gina_web_est%C3%A1tica
[12_2]:https://es.wikipedia.org/wiki/P%C3%A1gina_web_din%C3%A1mica

<br>

# 2. [Procesamiento remoto](#agenda)
Una modelo de [Procesamiento remoto][2] es un enfoque para el que algunas capas de software se procesan en servidores remotos no controlados por el desarrollador o en los dispositivos cliente.

* ><i>"Debes tener el control de tu tiempo, y no podrás tenerlo a menos que digas “no” a menudo."</i><br>
<cite style="display:block; text-align: right">[Warren Buffett](https://es.wikipedia.org/wiki/Warren_Buffett)</cite>

[2]:https://vuejs.org/guide/scaling-up/ssr.html


## 2.1. Características ✔
* Distribuidas.
* Progresivas.
* Socket.
* Ajax 

### 2.1.1. Ventajas ✔
* Livianas - Menos demanda de servicios de red.
* Ágiles - Entrega temprana.
* Menor infraestructura.
* Reactivas.


### 2.1.2. Desventajas ✔
* Multiples puntos de fallo.
* Multiples dependencias.
* Menor libertad.
* Menor Privacidad.

### 2.1.3. Arquitectura

![Imagen de sistemas descentralizados](../img/a-mulilayer-remote.svg "Sistemas descentralizados")

## 2.2. Ejemplos ✔
* [CSR][22_1] - client side rendering
* [CC][22_2] - cloud computing
* [SC][22_3] - serverless computing

[22_1]:https://es.wikipedia.org/wiki/Single-page_application
[22_2]:https://es.wikipedia.org/wiki/Computaci%C3%B3n_en_la_nube
[22_3]:https://es.wikipedia.org/wiki/Serverless_computing

<br>

---
## Mas Recursos
- [Alojamiento en Internet](https://es.wikipedia.org/wiki/Servicio_de_alojamiento_de_Internet) (Wikipedia)
- [Servicio WEB](https://es.wikipedia.org/wiki/Servicio_web) (Wikipedia)