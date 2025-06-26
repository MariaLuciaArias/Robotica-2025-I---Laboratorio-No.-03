# Robótica 2025-I Laboratorio-No.03
***Robótica Industrial - Análisis y Operación del Manipulador Motoman MH6***  
  
Maria Lucia Arias Ortiz - `mariasor@unal.edu.co`  
Andrés Felipe Quenan Pozo - `aquenan@unal.edu.co`
***
# Introducción


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
  ![image](https://github.com/user-attachments/assets/3b2a775c-56c8-4bf8-8702-ed39f4814645)
  ![image](https://github.com/user-attachments/assets/16d9e717-3729-4cb7-9a2a-789202762118)

  ### Home 2
  ![image](https://github.com/user-attachments/assets/24638a88-d767-4977-afdb-4f538258bf43)
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


   
5. Explicación completa sobre los niveles de velocidad para movimientos manuales, el proceso para cambiar entre niveles y cómo identificar el nivel establecido en la interfaz del robot.
6. Descripción de las principales funcionalidades de RoboDK, explicando cómo se comunica con el manipulador Motoman y qué procesos realiza para ejecutar movimientos.
7. Análisis comparativo entre RoboDK y RobotStudio, destacando ventajas, limitaciones y aplicaciones de cada herramienta.
8. Código desarrollado en RoboDK para ejecutar una trayectoria polar, adjuntado como anexo dentro del repositorio.
9. Video de simulación en RoboDK mostrando la trayectoria polar y evidencia de su implementación en el manipulador Motoman de forma física, controlado desde el PC.
   A continuación se presenta el video del desarrollo de este laboratorio. <a href="">Video del desarrollo</a>
