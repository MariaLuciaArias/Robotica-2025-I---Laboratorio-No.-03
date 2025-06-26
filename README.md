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
4. Explicación completa sobre los niveles de velocidad para movimientos manuales, el proceso para cambiar entre niveles y cómo identificar el nivel establecido en la interfaz del robot.
5. Descripción de las principales funcionalidades de RoboDK, explicando cómo se comunica con el manipulador Motoman y qué procesos realiza para ejecutar movimientos.
6. Análisis comparativo entre RoboDK y RobotStudio, destacando ventajas, limitaciones y aplicaciones de cada herramienta.
7. Código desarrollado en RoboDK para ejecutar una trayectoria polar, adjuntado como anexo dentro del repositorio.
8. Video de simulación en RoboDK mostrando la trayectoria polar y evidencia de su implementación en el manipulador Motoman de forma física, controlado desde el PC.
   A continuación se presenta el video del desarrollo de este laboratorio. <a href="">Video del desarrollo</a>
