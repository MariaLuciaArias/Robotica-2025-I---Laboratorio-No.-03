# Robótica 2025-I Laboratorio-No.03
***Robótica Industrial - Análisis y Operación del Manipulador Motoman MH6***  
  
Maria Lucia Arias Ortiz - `mariasor@unal.edu.co`  
Andrés Felipe Quenan Pozo - `aquenan@unal.edu.co`
***
# Desarrollo

1. Cuadro comparativo detallado de las características técnicas del Motoman MH6 y el IRB140, incluyendo carga maxima, alcance, número de grados de libertad, velocidad, aplicaciones típicas, etc.
   | Característica | IRB140 | Motoman MH6 |
   | :---         |     :---:      |          :---: |
   | Fabricante  | ABB Robotics   | Yaskawa Motoman   |
   | Carga máxima  | 6 kg     | 6 kg    |
   | Alcance     | 810 mm   | 1422 mm    |
   | Número grados de libertad | 6 | 6 expandible a 8 |
   | Velocidad Eje 1  |  200 ° / s | 220 °/s |
   | Velocidad Eje 2  |  200 ° / s | 200 °/s |
   | Velocidad Eje 3  |  260 ° / s | 220 °/s |
   | Velocidad Eje 4  |  360 ° / s | 410 °/s |
   | Velocidad Eje 5  |  360 ° / s | 410 °/s |
   | Velocidad Eje 6  |  450 ° / s | 610 °/s |
   | Repetibilidad  | 0.03 mm| 0.08 mm |
   | Peso del robot	 | 98 kg| 	130 kg|
   | Interfaz de programación  | RAPID | 	INFORM II | 	
   | Controlador  | IRC5 Compact | DX100 / DX200|
   | Aplicaciones típicas| Soldadura por arco, Mecanizado, manipulación de piezas, montaje de piezas  | Soldadura por arco, ensamblaje, dosificación, moldeo por inyección, alimentación de máquinas, manipulación de materiales, embalaje |
   
2. Descripción de las configuraciones home1 y home2 del Motoman MH6, indicando la posición de cada articulación, ¿Cual posición es mejor?, justifique su respuesta.
  ### Home 1
  La posición Home 1 es cuando el robot está con el brazo recogido y ocupa menos espacio, como se puede apreciar en la siguiente imagen
  ![image](https://github.com/user-attachments/assets/3b2a775c-56c8-4bf8-8702-ed39f4814645)
  A continuación se muestra la posición de cada articulación en la posición Home 1
  ![image](https://github.com/user-attachments/assets/16d9e717-3729-4cb7-9a2a-789202762118)

  ### Home 2
  La posición Home 2 es cuando el robot está con el brazo extendido verticalmente y se puede apreciar con mayor claridad el efector final
  ![image](https://github.com/user-attachments/assets/24638a88-d767-4977-afdb-4f538258bf43)
  A continuación se muestra la posición de cada articulación en la posición Home 2
  ![image](https://github.com/user-attachments/assets/b40fc08d-6595-4c44-8ecd-08b1dba2fc5b)

  Al comparar las dos posiciones de Home del robot Motoman MH6, la mejor opción dependerá del propósito específico de dicha posición. La posición Home 2, con el brazo extendido hacia arriba, es ideal cuando se requiere iniciar trayectorias con un área de trabajo despejada, ya que ofrece mayor visibilidad del efector final y reduce el riesgo de colisión al comienzo de la operación. Por otro lado, la posición Home 1, con el brazo recogido y más compacto, es más adecuada como posición de reposo o espera, ya que ocupa menos espacio, protege mejor los cables y componentes, y es más segura durante tareas de mantenimiento o al encender/apagar el robot. Por lo tanto, si el objetivo es seguridad y compacidad, se recomienda la segunda posición; si se busca una postura inicial eficiente para iniciar movimientos, la primera resulta más conveniente.

3. Procedimiento detallado para realizar movimientos manuales, especificando cómo cambiar entre modos de operación (articulaciones, cartesiano) y realizar traslaciones y rotaciones en los ejes X, Y, Z.
   
   En un principio se debe asegurar que el robot se encuentra en modo manual (Teach Mode) girando la llave de modo a la posición “TEACH” confirmando que el robot no está en modo remoto (REMOTE OFF).
   Luego mantener presionado el botón de seguridad ubicado en la parte posterior del teach pendant (conocido como deadman switch) para habilitar el movimiento manual.

   ![image](https://github.com/user-attachments/assets/47c79ba7-4a51-49ac-8bca-000445df0322)

   El teach pendant permite controlar el robot en diferentes modos, como articulaciones, coordenadas cartesianas, coordenadas cilíndricas, coordenadas de la herramienta y coordenadas del usuario. Como modos principales se describe el        modo articulaciones y cartesiano:
   
   ### Modo Articulaciones
   En este modo, se permite el movimiento individual de cada uno de los seis ejes del robot (J1 a J6). Para activarlo se presiona el botón "COORD" en el teach pendant luego se selecciona la opción "Joint" y  aparecerán en la pantalla las    etiquetas J1 a J6, indicando el control por eje:

   ![image](https://github.com/user-attachments/assets/abd8ab4e-d2d5-4f67-b864-9fb5c6556a48)

   ### Modo Cartesiano
   Este modo permite el movimiento del efector final del robot en el espacio tridimensional, utilizando un sistema de coordenadas cartesiano. Para activarlo se presiona el botón "COORD" y se selecciona la opción "XYZ", por último se         elige el sistema de referencia deseado:
   - Base (WORLD): movimientos respecto al sistema fijo del robot.
   - Tool (HERRAMIENTA): movimientos respecto al efector final.
   
   ![image](https://github.com/user-attachments/assets/5f7cb60c-061f-467f-b584-4cc1026ac72c)

   #### Traslaciones en los Ejes X, Y, Z
   Con el modo cartesiano activado:
   - Usar las teclas de dirección o funciones específicas del teach pendant para mover el robot en el eje deseado (X, Y o Z).
   - Mantener presionado el botón de seguridad durante el movimiento.
   - El robot se desplazará linealmente según la dirección y eje seleccionados.
  
   ![image](https://github.com/user-attachments/assets/ea3a70e6-640e-4fa1-8cee-d8421be0ac0f)

   #### Rotaciones en los Ejes RX, RY, RZ
   Para realizar rotaciones del efector final:
   - Cambiar el modo a rotación cartesiana, generalmente identificado como RXYZ.
   - Seleccionar el sistema de coordenadas (se recomienda TOOL para rotar alrededor del efector final).
   - Utilizar los controles del teach pendant para aplicar rotación en los ejes RX, RY o RZ.
   - Mantener presionado el botón de seguridad para ejecutar el movimiento.

   ![image](https://github.com/user-attachments/assets/fd984270-8794-4ea6-b020-e05db08bd728)


   
4. Explicación completa sobre los niveles de velocidad para movimientos manuales, el proceso para cambiar entre niveles y cómo identificar el nivel establecido en la interfaz del robot. 
   Hay cuatro niveles de velocidad:  lento, medio, rápido, y avanzar poco a poco (inching).

5. Descripción de las principales funcionalidades de RoboDK, explicando cómo se comunica con el manipulador Motoman y qué procesos realiza para ejecutar movimientos.

   #### Funcionalidades principales de RoboDK
   - **Simulación 3D de celdas robóticas**: Permite crear entornos virtuales donde se simulan robots, piezas, herramientas, transportadores, sensores y otros elementos industriales.
   - **Programación offline**: Es posible programar trayectorias, ciclos de trabajo o rutinas completas sin detener la producción, ni tener el robot presente
   - **Generación automática de código para múltiples marcas**: RoboDK incluye postprocesadores para marcas como Yaskawa, ABB, KUKA, FANUC, UR, etc., generando archivos de código nativo directamente compatibles con el controlador del         robot.
   - **Cinemática inversa y planeación de trayectorias**: RoboDK calcula automáticamente las posiciones articulares necesarias para seguir trayectorias definidas en el espacio cartesiano, evitando colisiones y respetando los límites del      robot.
   - **Interfaz para calibración de herramientas y bases**: Incluye asistentes para calibrar herramientas (TCP) y sistemas de coordenadas (referencias), lo que mejora la precisión del robot en tareas reales.
   #### Comunicación con el manipulador
   En el caso específico de manipuladores Motoman (Yaskawa), RoboDK se comunica mediante la generación de código en el lenguaje nativo del controlador, como JBI para DX100/DX200 o SRC para YRC1000. Esta comunicación puede realizarse de     dos maneras:
   - Exportando el programa generado en RoboDK a un archivo JBI/SRC e importándolo manualmente al controlador
   - Usando una conexión directa a través de Ethernet/IP, FTP o sockets TCP/IP, lo cual permite transferir programas automáticamente o incluso controlar el robot en tiempo real en algunos casos avanzados. Para esto es necesario colocar       el robot en modo remoto ("REMOTE") y en el software RoboDK seleccionar la opción Conectar > Conectar al robot, luego se introduce la IP del robot y por último se selecciona la opción Conectar.
     
     ![image](https://github.com/user-attachments/assets/7c6468e8-4b58-4d0a-a64a-7b608ae9dc22)

   #### Proceso para ejecutar movimientos:
   1. **Creación de trayectoria**: Se define una serie de puntos cartesianos en el entorno 3D, ya sea manualmente, mediante la importación desde un archivo CAD/CAM, o generando trayectorias con scripts (por ejemplo, en Python).
   2. **Resolución de la cinemática inversa**: RoboDK calcula la posición de cada articulación del robot (ángulos de J1 a J6) necesaria para alcanzar cada punto cartesiano de la trayectoria.
   3. **Planeación de movimiento y verificación de colisiones**: RoboDK genera la secuencia completa de movimientos, asegurándose de evitar colisiones con el entorno o con el mismo robot, respetando los límites de velocidad y                  aceleración establecidos.
   4. **Generación de código nativo**: Una vez verificada la trayectoria, RoboDK utiliza un postprocesador específico para Yaskawa que traduce los movimientos en instrucciones JBI (o SRC) que el controlador del robot puede ejecutar            directamente.
   5. **Transferencia del programa al robot**: El archivo generado puede copearse al controlador via USB o FTP y se ejecuta desde el teach pendant, o tambíen se puede ejecutar via TCP/IP desde RoboDK
   6. **Ejecución física**: Una vez cargado el código al robot, este ejecuta los movimientos siguiendo exactamente lo programado en RoboDK. Gracias a la simulación previa y calibración de referencias, se logra una correspondencia              precisa entre el entorno virtual y el físico.

6. Análisis comparativo entre RoboDK y RobotStudio, destacando ventajas, limitaciones y aplicaciones de cada herramienta.

   #### Compatibilidad de marcas de robot.
   | Característica | RoboDK | RobotStudio|
   | :---         |     :---:      |          :---: |
   | Marcas compatibles  |  Multimarca: ABB, Yaskawa (Motoman), KUKA, FANUC, UR, Staubli, entre otras  | Exclusiva para robots ABB |
   | Postprocesadores  | Dispone de decenas de postprocesadores para generar código nativo de distintas marcas  | Solo genera código RAPID (ABB)  |
   
   RoboDK es ideal para entornos mixtos o donde se utilicen robots de diferentes fabricantes, en cambio, RobotStudio solo es aplicable a celdas ABB.

   #### Programación offline y generación de código
   | Característica | RoboDK | RobotStudio|
   | :---         |     :---:      |          :---: |
   | Lenguaje de programación | Genera código en lenguaje nativo del fabricante  | Genera código en lenguaje RAPID (ABB) |
   | Flexibilidad para procesos | Alto: permite crear scripts en Python, integración con CAM  | Muy detallado en lógica de automatización, pero limitado a RAPID  |

   RoboDK posee mayor flexibilidad con scripting y generación multiformato y RobotStudio un entorno potente de RAPID con funciones de debugging, breakpoint y simulación lógica.

   #### Comunicación con el robot físico
   | Característica | RoboDK | RobotStudio|
   | :---         |     :---:      |          :---: |
   | Transferencia de programas  | Vía USB, FTP o en línea (si se habilita) | Comunicación directa con robots ABB, incluso en tiempo real |
   | Control en línea | Limitado, depende del robot y configuración | Muy fluido con ABB; puede simular PLCs y E/S |

   RobotStudio ofrece simulación y conexión total con los robots ABB, sin embargo, RoboDK tiene un control en línea más limitado y dependiente de marca/configuración.
   
7. Código desarrollado en RoboDK para ejecutar una trayectoria polar, adjuntado como anexo dentro del repositorio.
   
   La trayectoria polar programada para el laboratorio se muestra a continuación, junto con la ecuación que la describe y la simulación realizada en RoboDK.

   ![image](https://github.com/user-attachments/assets/37c7fb38-03cb-4709-9306-eb812af1a57c)

   Por último el código python para la ejecución de las trayectorias además de el archivo .rdk se encuentran en el directorio <a href="MH6">MH6</a>

8. Video de simulación en RoboDK mostrando la trayectoria polar y evidencia de su implementación en el manipulador Motoman de forma física, controlado desde el PC.
   A continuación se presenta el video del desarrollo de este laboratorio. <a href="https://youtu.be/RXDfx6ayx6U">Video del desarrollo</a>
