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
# 1. [Distributed Component Object Model](#agenda)
El Modelo de Objeto Componente Distribuido, [DCOM][1]; esta incluido en los sistemas operativos de Microsoft. Es un juego de conceptos e interfaces de programa, en el cual los objetos de programa del cliente, pueden solicitar servicios de objetos de programa servidores en otras computadoras dentro de una red. Esta tecnología está asociada a la plataforma de productos Microsoft.

[1]:https://es.wikipedia.org/wiki/Modelo_de_Objetos_de_Componentes_Distribuidos


1.1. Historia ✔
* 1990: [OLE][11_1] permite compartir objetos entre procesos.
* 1993: [COM][11_2] es incluido en Win 95 y windows NT 4.0
* 1996: [DCOM][11_3] extiende COM resolviendo problemas de serialization.
* 1996: [ActiveX][11_4] extiende DCOM en IE.
* 2002: [.NET Remoting][11_5] es incluido en Win XP.
* 2006: [WCF][11_6] es incluido en Windows vista.

[11_1]:https://es.wikipedia.org/wiki/Object_Linking_and_Embedding
[11_2]:https://es.wikipedia.org/wiki/Component_Object_Model
[11_3]:https://es.wikipedia.org/wiki/Modelo_de_Objetos_de_Componentes_Distribuidos
[11_4]:https://es.wikipedia.org/wiki/ActiveX
[11_5]:https://en.m.wikipedia.org/wiki/.NET_Remoting
[11_6]:https://es.wikipedia.org/wiki/Windows_Communication_Foundation

<br>

# 2. [Remote Invocation Method](#agenda)
El sistema de Invocación Remota de Métodos, [RMI][2]; de Java permite, a un objeto que se está ejecutando en una Máquina Virtual Java (VM), llamar a métodos de otro objeto que está en otra VM diferente. Esta tecnología está asociada al lenguaje de programación Java, es decir, que permite la comunicación entre objetos creados en este lenguaje.

[2]:https://es.wikipedia.org/wiki/Java_Remote_Method_Invocation

2.1. Historia ✔
* 1996: [JDK 1.0][21_1] lanzamiento de Java.
* 1997: [RMI][21_2] primera version en JDK 1.1.
* 1998: [Java IDL][21_3] lanzamiento en J2SE 1.2 con compatibilidad CORBA.
* 2000: [RMI+][21_4] nueva versión en J2SE 1.3 basada en CORBA.
* 2002: [FOSS][21_5] serialization, criptografía en J2SE 1.4.
* 2004: [STUB][21_6] automático para RMI en J2SE 1.4.

[21_1]:https://en.wikipedia.org/wiki/Java_version_history
[21_2]:https://es.wikipedia.org/wiki/Java_Remote_Method_Invocation
[21_3]:https://es.wikipedia.org/wiki/Java_IDL
[21_4]:https://es.wikipedia.org/wiki/Java_SE
[21_5]:https://es.wikipedia.org/wiki/Software_libre_y_de_c%C3%B3digo_abierto
[21_6]:https://es.wikipedia.org/wiki/Stub

<br>

# 3. [Remote Invocation Method](#agenda)
La Arquitectura de agente de solicitud de objetos comunes, [CORBA][3]; de Java permite, a un objeto que se está ejecutando en una Máquina Virtual Java (VM), llamar a métodos de otro objeto que está en otra VM diferente. Esta tecnología está asociada al lenguaje de programación Java, es decir, que permite la comunicación entre objetos creados en este lenguaje.

[3]:https://es.wikipedia.org/wiki/CORBA

<br>

---
## Mas Recursos
- [Java: programación)](https://es.wikipedia.org/wiki/Java_(lenguaje_de_programaci%C3%B3n)) (Wikipedia)
- [Distributed object](https://en.m.wikipedia.org/wiki/Distributed_object) (Wikipedia)
- [Llamada a procedimiento remoto](https://es.wikipedia.org/wiki/Llamada_a_procedimiento_remotos) (Wikipedia)
- [Simple Object Access Protocol](https://es.wikipedia.org/wiki/Simple_Object_Access_Protocol) (Wikipedia)