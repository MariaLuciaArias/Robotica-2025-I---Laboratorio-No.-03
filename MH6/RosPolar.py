from robodk.robolink import *    # API para comunicarte con RoboDK
from robodk.robomath import *    # Funciones matemáticas
import math

#------------------------------------------------
# 1) Conexión a RoboDK e inicialización
#------------------------------------------------
RDK = Robolink()

# Elegir un robot (si hay varios, aparece un popup)
robot = RDK.ItemUserPick("Selecciona un robot", ITEM_TYPE_ROBOT)
if not robot.Valid():
    raise Exception("No se ha seleccionado un robot válido.")

'''
# Conectar al robot físico
if not robot.Connect():
    raise Exception("No se pudo conectar al robot. Verifica que esté en modo remoto y que la configuración sea correcta.")

# Confirmar conexión
if not robot.ConnectedState():
    raise Exception("El robot no está conectado correctamente. Revisa la conexión.")

print("Robot conectado correctamente.")
'''
#------------------------------------------------
# 2) Cargar Frame y Target Home
#------------------------------------------------
frame_name = "Frame_from_Target1"
frame = RDK.Item(frame_name, ITEM_TYPE_FRAME)
if not frame.Valid():
    raise Exception(f'No se encontró el Frame "{frame_name}" en la estación.')

robot.setPoseFrame(frame)
robot.setPoseTool(robot.PoseTool())

# Obtener el Target llamado "Home"
home_target = RDK.Item("Home", ITEM_TYPE_TARGET)
if not home_target.Valid():
    raise Exception('No se encontró un target llamado "Home". Crea uno con ese nombre o cambia el nombre en el código.')

#------------------------------------------------
# 3) Ir a posición Home antes de comenzar
#------------------------------------------------
robot.MoveJ(home_target)

# Ajustes de velocidad y blending
robot.setSpeed(300)   # mm/s
robot.setRounding(5)  # mm

#------------------------------------------------
# 4) Parámetros de la figura (rosa polar)
#------------------------------------------------
num_points = 720
A = 150
n = 5/4  # r = A * sin(n * theta)
z_surface = 0
z_safe = 50

#------------------------------------------------
# 5) Movimiento inicial al centro
#------------------------------------------------
robot.MoveJ(transl(0, 0, z_surface + z_safe))
robot.MoveL(transl(0, 0, z_surface))

#------------------------------------------------
# 6) Dibujar la rosa polar
#------------------------------------------------
turns = 8
max_theta = turns * 2 * math.pi

for i in range(num_points + 1):
    t = i / num_points
    theta = t * max_theta

    r = A * math.sin(n * theta)
    x = r * math.cos(theta)
    y = r * math.sin(theta)

    robot.MoveL(transl(x, y, z_surface))

# Al terminar, subir en Z
robot.MoveL(transl(x, y, z_surface + z_safe))

#------------------------------------------------
# 7) Regresar a Home
#------------------------------------------------
robot.MoveJ(home_target)

print(f"¡Figura completada en el frame '{frame_name}'!")
