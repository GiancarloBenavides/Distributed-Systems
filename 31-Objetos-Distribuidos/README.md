# Sistemas Descentralizados
<p><code>Fundamentos de sistemas Distribuidos</code></p>
<p>Creado por <code>Giancarlo Ortiz</code> y <code>Diego Villareal</code> para explicar los fundamentos de los <code>Sistemas distribuidos</code></p>

## Objetos Distribuidos
En los sistemas Cliente/Servidor, un objeto distribuido es aquel que está gestionado por un servidor y sus clientes invocan sus métodos utilizando un «método de invocación remota». El cliente invoca el método mediante un mensaje al servidor que gestiona el objeto, se ejecuta el método del objeto en el servidor y el resultado se devuelve al cliente en otro mensaje.


## Agenda
1. [Distributed Component Object Model](#1-distributed-component-object-model).
1. [Remote Invocation Method](#2-remote-invocation-method).
1. [Common Object Request Broker Architecture](#2-common-object-request-broker-architecture).

<br>

---
# 1. Distributed Component Object Model
El Modelo de Objeto Componente Distribuido, [DCOM][1]; esta incluido en los sistemas operativos de Microsoft. Es un juego de conceptos e interfaces de programa, en el cual los objetos de programa del cliente, pueden solicitar servicios de objetos de programa servidores en otras computadoras dentro de una red. Esta tecnología está asociada a la plataforma de productos Microsoft.

[1]:https://es.wikipedia.org/wiki/Modelo_de_Objetos_de_Componentes_Distribuidos

<br>

# 2. Remote Invocation Method
El sistema de Invocación Remota de Métodos, [RMI][2]; de Java permite, a un objeto que se está ejecutando en una Máquina Virtual Java (VM), llamar a métodos de otro objeto que está en otra VM diferente. Esta tecnología está asociada al lenguaje de programación Java, es decir, que permite la comunicación entre objetos creados en este lenguaje.

[2]:https://es.wikipedia.org/wiki/Java_Remote_Method_Invocation

<br>

# 3. Remote Invocation Method
La Arquitectura de agente de solicitud de objetos comunes, [CORBA][3]; de Java permite, a un objeto que se está ejecutando en una Máquina Virtual Java (VM), llamar a métodos de otro objeto que está en otra VM diferente. Esta tecnología está asociada al lenguaje de programación Java, es decir, que permite la comunicación entre objetos creados en este lenguaje.

[3]:https://es.wikipedia.org/wiki/CORBA

<br>

---
## Mas Recursos
- [Llamada a procedimiento remoto](https://es.wikipedia.org/wiki/Llamada_a_procedimiento_remotos) (Wikipedia)
- [Simple Object Access Protocol](https://es.wikipedia.org/wiki/Simple_Object_Access_Protocol) (Wikipedia)