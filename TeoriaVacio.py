import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros estructurales
A = np.radians(30)   # Ángulo de salida (grados → radianes)
S = 3                # Número de giros (spin estructural)
W = 2 * np.pi        # Fase (ciclo completo)
B = 0.2              # Torsión helicoidal (apertura vertical)

# Eje angular para simular el tiempo de proyección
theta = np.linspace(0, S * 2 * np.pi, 1000)

# Ecuaciones paramétricas para la hélice proyectiva
x = np.cos(theta + W) * np.cos(A)
y = np.sin(theta + W) * np.cos(A)
z = B * theta  # torsión vertical

# Visualización 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, color='blue', label="Proyección desde ε₀")
ax.set_title("Estructura helicoidal proyectiva")
ax.set_xlabel("X (fase)")
ax.set_ylabel("Y (giro)")
ax.set_zlabel("Z (torsión)")
ax.legend()
plt.show()

# Visualización interactiva con sliders para proyección helicoidal
from matplotlib.widgets import Slider

fig_interact1 = plt.figure()
ax_interact1 = fig_interact1.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.25, bottom=0.25)

# Valores iniciales específicos de esa simulación
A0_1, S0_1, W0_1, B0_1 = np.radians(30), 3, 0, 0.2

def actualizar1(val):
    ax_interact1.cla()
    A = slider_A1.val
    S = slider_S1.val
    W = slider_W1.val
    B = slider_B1.val
    theta = np.linspace(0, S * 2 * np.pi, 1000)
    x = np.cos(theta + W) * np.cos(A)
    y = np.sin(theta + W) * np.cos(A)
    z = B * theta
    ax_interact1.plot(x, y, z, color='blue')
    ax_interact1.set_xlim([-1.5, 1.5])
    ax_interact1.set_ylim([-1.5, 1.5])
    ax_interact1.set_zlim([0, 3 * np.pi])
    ax_interact1.set_title("Proyección estructural interactiva")
    fig_interact1.canvas.draw_idle()

# Controles
axcolor = 'lightgoldenrodyellow'
ax_A1 = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_S1 = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=axcolor)
ax_W1 = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
ax_B1 = plt.axes([0.25, 0.00, 0.65, 0.03], facecolor=axcolor)

slider_A1 = Slider(ax_A1, 'Ángulo A', 0, np.pi/2, valinit=A0_1)
slider_S1 = Slider(ax_S1, 'Spin S', 1, 6, valinit=S0_1)
slider_W1 = Slider(ax_W1, 'Fase W', 0, 2*np.pi, valinit=W0_1)
slider_B1 = Slider(ax_B1, 'Torsión B', 0.05, 0.5, valinit=B0_1)

slider_A1.on_changed(actualizar1)
slider_S1.on_changed(actualizar1)
slider_W1.on_changed(actualizar1)
slider_B1.on_changed(actualizar1)

actualizar1(None)
plt.show()

# Simulación de múltiples proyecciones desde ε₀
parametros = [
    (np.radians(20), 2, 0, 0.1),
    (np.radians(45), 4, np.pi/2, 0.3),
    (np.radians(60), 1.5, np.pi, 0.15),
    (np.radians(80), 2.5, 3*np.pi/2, 0.25)
]

fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')
colores = ['red', 'green', 'purple', 'orange']

for i, (a, s, w, b) in enumerate(parametros):
    theta = np.linspace(0, s * 2 * np.pi, 1000)
    x = np.cos(theta + w) * np.cos(a)
    y = np.sin(theta + w) * np.cos(a)
    z = b * theta
    ax2.plot(x, y, z, color=colores[i], label=f"p{i+1}: A={np.degrees(a):.0f}° S={s} B={b}")

ax2.set_title("Múltiples proyecciones desde ε₀")
ax2.set_xlabel("X (fase)")
ax2.set_ylabel("Y (giro)")
ax2.set_zlabel("Z (torsión)")
ax2.legend()
plt.show()

# Visualización interactiva con sliders para múltiples proyecciones
from matplotlib.widgets import Slider

fig_interact2 = plt.figure()
ax_interact2 = fig_interact2.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.25, bottom=0.25)

# Valores iniciales: toma el primero de la lista
A0_2, S0_2, W0_2, B0_2 = parametros[0]

def actualizar2(val):
    ax_interact2.cla()
    A = slider_A2.val
    S = slider_S2.val
    W = slider_W2.val
    B = slider_B2.val
    theta = np.linspace(0, S * 2 * np.pi, 1000)
    x = np.cos(theta + W) * np.cos(A)
    y = np.sin(theta + W) * np.cos(A)
    z = B * theta
    ax_interact2.plot(x, y, z, color='blue')
    ax_interact2.set_xlim([-1.5, 1.5])
    ax_interact2.set_ylim([-1.5, 1.5])
    ax_interact2.set_zlim([0, 3 * np.pi])
    ax_interact2.set_title("Simulación interactiva de múltiples proyecciones")
    fig_interact2.canvas.draw_idle()

# Controles
ax_A2 = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_S2 = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_W2 = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_B2 = plt.axes([0.25, 0.00, 0.65, 0.03], facecolor='lightgoldenrodyellow')

slider_A2 = Slider(ax_A2, 'Ángulo A', 0, np.pi/2, valinit=A0_2)
slider_S2 = Slider(ax_S2, 'Spin S', 1, 6, valinit=S0_2)
slider_W2 = Slider(ax_W2, 'Fase W', 0, 2*np.pi, valinit=W0_2)
slider_B2 = Slider(ax_B2, 'Torsión B', 0.05, 0.5, valinit=B0_2)

slider_A2.on_changed(actualizar2)
slider_S2.on_changed(actualizar2)
slider_W2.on_changed(actualizar2)
slider_B2.on_changed(actualizar2)

actualizar2(None)
plt.show()

# Simulación de acoplamiento estructural entre dos proyecciones
from mpl_toolkits.mplot3d.art3d import juggle_axes

# Parámetros de dos partículas
a1, s1, w1, b1 = np.radians(30), 3, 0, 0.2
a2, s2, w2, b2 = np.radians(60), 2, np.pi/2, 0.2

theta = np.linspace(0, 4 * np.pi, 1000)
x1 = np.cos(theta + w1) * np.cos(a1)
y1 = np.sin(theta + w1) * np.cos(a1)
z1 = b1 * theta

x2 = np.cos(theta + w2) * np.cos(a2)
y2 = np.sin(theta + w2) * np.cos(a2)
z2 = b2 * theta

# Calcular distancias entre puntos de ambas trayectorias
distancias = np.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
indice_min = np.argmin(distancias)

# Punto de acoplamiento
x_acop, y_acop, z_acop = (x1[indice_min] + x2[indice_min]) / 2, (y1[indice_min] + y2[indice_min]) / 2, (z1[indice_min] + z2[indice_min]) / 2

# Graficar ambas trayectorias y el punto de acoplamiento
fig3 = plt.figure()
ax3 = fig3.add_subplot(111, projection='3d')
ax3.plot(x1, y1, z1, label='Proyección 1', color='blue')
ax3.plot(x2, y2, z2, label='Proyección 2', color='red')
ax3.scatter(x_acop, y_acop, z_acop, color='black', s=60, label='Acoplamiento')

ax3.set_title("Simulación de acoplamiento estructural")
ax3.set_xlabel("X")
ax3.set_ylabel("Y")
ax3.set_zlabel("Z")
ax3.legend()
plt.show()

# Visualización interactiva con sliders para acoplamiento estructural
from matplotlib.widgets import Slider

fig_interact3 = plt.figure()
ax_interact3 = fig_interact3.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.25, bottom=0.25)

# Valores iniciales
A0_3, S0_3, W0_3, B0_3 = np.radians(30), 3, 0, 0.2
A1_3, S1_3, W1_3, B1_3 = np.radians(60), 2, np.pi/2, 0.2

def actualizar3(val):
    ax_interact3.cla()
    A1 = slider_A3.val
    S1 = slider_S3.val
    W1 = slider_W3.val
    B1 = slider_B3.val
    A2 = slider_A3b.val
    S2 = slider_S3b.val
    W2 = slider_W3b.val
    B2 = slider_B3b.val
    theta = np.linspace(0, 4 * np.pi, 1000)
    x1 = np.cos(theta + W1) * np.cos(A1)
    y1 = np.sin(theta + W1) * np.cos(A1)
    z1 = B1 * theta
    x2 = np.cos(theta + W2) * np.cos(A2)
    y2 = np.sin(theta + W2) * np.cos(A2)
    z2 = B2 * theta
    distancias = np.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    indice_min = np.argmin(distancias)
    x_acop, y_acop, z_acop = (x1[indice_min] + x2[indice_min]) / 2, (y1[indice_min] + y2[indice_min]) / 2, (z1[indice_min] + z2[indice_min]) / 2
    ax_interact3.plot(x1, y1, z1, label='Proyección 1', color='blue')
    ax_interact3.plot(x2, y2, z2, label='Proyección 2', color='red')
    ax_interact3.scatter(x_acop, y_acop, z_acop, color='black', s=60, label='Acoplamiento')
    ax_interact3.set_xlim([-2, 2])
    ax_interact3.set_ylim([-2, 2])
    ax_interact3.set_zlim([0, 4 * np.pi * 0.5])
    ax_interact3.set_title("Acoplamiento estructural interactivo")
    ax_interact3.legend()
    fig_interact3.canvas.draw_idle()

# Controles
ax_A3 = plt.axes([0.25, 0.20, 0.30, 0.02], facecolor='lightgoldenrodyellow')
ax_S3 = plt.axes([0.25, 0.17, 0.30, 0.02], facecolor='lightgoldenrodyellow')
ax_W3 = plt.axes([0.25, 0.14, 0.30, 0.02], facecolor='lightgoldenrodyellow')
ax_B3 = plt.axes([0.25, 0.11, 0.30, 0.02], facecolor='lightgoldenrodyellow')
ax_A3b = plt.axes([0.60, 0.20, 0.30, 0.02], facecolor='lightgoldenrodyellow')
ax_S3b = plt.axes([0.60, 0.17, 0.30, 0.02], facecolor='lightgoldenrodyellow')
ax_W3b = plt.axes([0.60, 0.14, 0.30, 0.02], facecolor='lightgoldenrodyellow')
ax_B3b = plt.axes([0.60, 0.11, 0.30, 0.02], facecolor='lightgoldenrodyellow')

slider_A3 = Slider(ax_A3, 'Ángulo A1', 0, np.pi/2, valinit=A0_3)
slider_S3 = Slider(ax_S3, 'Spin S1', 1, 6, valinit=S0_3)
slider_W3 = Slider(ax_W3, 'Fase W1', 0, 2*np.pi, valinit=W0_3)
slider_B3 = Slider(ax_B3, 'Torsión B1', 0.05, 0.5, valinit=B0_3)
slider_A3b = Slider(ax_A3b, 'Ángulo A2', 0, np.pi/2, valinit=A1_3)
slider_S3b = Slider(ax_S3b, 'Spin S2', 1, 6, valinit=S1_3)
slider_W3b = Slider(ax_W3b, 'Fase W2', 0, 2*np.pi, valinit=W1_3)
slider_B3b = Slider(ax_B3b, 'Torsión B2', 0.05, 0.5, valinit=B1_3)

slider_A3.on_changed(actualizar3)
slider_S3.on_changed(actualizar3)
slider_W3.on_changed(actualizar3)
slider_B3.on_changed(actualizar3)
slider_A3b.on_changed(actualizar3)
slider_S3b.on_changed(actualizar3)
slider_W3b.on_changed(actualizar3)
slider_B3b.on_changed(actualizar3)

actualizar3(None)
plt.show()

# Simulación de trayectoria modificada posterior al acoplamiento
# Supongamos que la partícula 1 cambia su torsión (B) después de acoplarse

# Nueva torsión estructural después del acoplamiento
B_modificado = 0.35
theta_post = np.linspace(0, 2 * np.pi, 1000)

# Traza modificada desde el punto de acoplamiento
x_mod = np.cos(theta_post + w1) * np.cos(a1) + x_acop
y_mod = np.sin(theta_post + w1) * np.cos(a1) + y_acop
z_mod = B_modificado * theta_post + z_acop

# Visualización
fig4 = plt.figure()
ax4 = fig4.add_subplot(111, projection='3d')
ax4.plot(x1, y1, z1, '--', color='blue', alpha=0.5, label='Proyección original')
ax4.plot(x_mod, y_mod, z_mod, color='cyan', label='Trayectoria modificada')
ax4.scatter(x_acop, y_acop, z_acop, color='black', s=60, label='Acoplamiento')

ax4.set_title("Modificación estructural posterior al acoplamiento")
ax4.set_xlabel("X")
ax4.set_ylabel("Y")
ax4.set_zlabel("Z")
ax4.legend()
plt.show()

# Visualización interactiva con sliders para modificación estructural posterior al acoplamiento
from matplotlib.widgets import Slider

fig_interact4 = plt.figure()
ax_interact4 = fig_interact4.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.25, bottom=0.25)

# Valores iniciales
A0_4, S0_4, W0_4, B0_4 = a1, 3, w1, 0.2
Bmod_4 = 0.35

def actualizar4(val):
    ax_interact4.cla()
    A = slider_A4.val
    S = slider_S4.val
    W = slider_W4.val
    B = slider_B4.val
    Bmod = slider_Bmod4.val
    theta = np.linspace(0, S * 2 * np.pi, 1000)
    theta_post = np.linspace(0, 2 * np.pi, 1000)
    # Trayectoria original
    x1 = np.cos(theta + W) * np.cos(A)
    y1 = np.sin(theta + W) * np.cos(A)
    z1 = B * theta
    # Acoplamiento
    A2 = a2
    S2 = 2
    W2 = w2
    B2 = 0.2
    x2 = np.cos(theta + W2) * np.cos(A2)
    y2 = np.sin(theta + W2) * np.cos(A2)
    z2 = B2 * theta
    distancias = np.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    indice_min = np.argmin(distancias)
    x_acop = (x1[indice_min] + x2[indice_min]) / 2
    y_acop = (y1[indice_min] + y2[indice_min]) / 2
    z_acop = (z1[indice_min] + z2[indice_min]) / 2
    # Trayectoria modificada
    x_mod = np.cos(theta_post + W) * np.cos(A) + x_acop
    y_mod = np.sin(theta_post + W) * np.cos(A) + y_acop
    z_mod = Bmod * theta_post + z_acop
    ax_interact4.plot(x1, y1, z1, '--', color='blue', alpha=0.5, label='Proyección original')
    ax_interact4.plot(x_mod, y_mod, z_mod, color='cyan', label='Trayectoria modificada')
    ax_interact4.scatter(x_acop, y_acop, z_acop, color='black', s=60, label='Acoplamiento')
    ax_interact4.set_xlim([-2, 2])
    ax_interact4.set_ylim([-2, 2])
    ax_interact4.set_zlim([0, 4 * np.pi * 0.5])
    ax_interact4.set_title("Modificación estructural interactiva")
    ax_interact4.legend()
    fig_interact4.canvas.draw_idle()

# Controles
ax_A4 = plt.axes([0.25, 0.15, 0.65, 0.02], facecolor='lightgoldenrodyellow')
ax_S4 = plt.axes([0.25, 0.12, 0.65, 0.02], facecolor='lightgoldenrodyellow')
ax_W4 = plt.axes([0.25, 0.09, 0.65, 0.02], facecolor='lightgoldenrodyellow')
ax_B4 = plt.axes([0.25, 0.06, 0.65, 0.02], facecolor='lightgoldenrodyellow')
ax_Bmod4 = plt.axes([0.25, 0.03, 0.65, 0.02], facecolor='lightgoldenrodyellow')

slider_A4 = Slider(ax_A4, 'Ángulo A', 0, np.pi/2, valinit=A0_4)
slider_S4 = Slider(ax_S4, 'Spin S', 1, 6, valinit=S0_4)
slider_W4 = Slider(ax_W4, 'Fase W', 0, 2*np.pi, valinit=W0_4)
slider_B4 = Slider(ax_B4, 'Torsión B', 0.05, 0.5, valinit=B0_4)
slider_Bmod4 = Slider(ax_Bmod4, 'Torsión Modificada', 0.05, 0.5, valinit=Bmod_4)

slider_A4.on_changed(actualizar4)
slider_S4.on_changed(actualizar4)
slider_W4.on_changed(actualizar4)
slider_B4.on_changed(actualizar4)
slider_Bmod4.on_changed(actualizar4)

actualizar4(None)
plt.show()

# Simulación de espacio proyectivo completo desde ε₀
num_particulas = 12
fig5 = plt.figure()
ax5 = fig5.add_subplot(111, projection='3d')

np.random.seed(42)  # reproducibilidad

for i in range(num_particulas):
    A = np.radians(np.random.uniform(10, 80))     # ángulo de salida
    S = np.random.uniform(1, 4)                    # spin (giros)
    W = np.random.uniform(0, 2 * np.pi)            # fase
    B = np.random.uniform(0.1, 0.35)               # torsión helicoidal
    color = plt.cm.viridis(i / num_particulas)    # color distinto

    theta = np.linspace(0, S * 2 * np.pi, 1000)
    x = np.cos(theta + W) * np.cos(A)
    y = np.sin(theta + W) * np.cos(A)
    z = B * theta

    ax5.plot(x, y, z, color=color, alpha=0.7)

ax5.set_title("Espacio proyectivo estructurado desde ε₀")
ax5.set_xlabel("X")
ax5.set_ylabel("Y")
ax5.set_zlabel("Z")
plt.show()

# Visualización interactiva con sliders para espacio proyectivo estructurado
from matplotlib.widgets import Slider

fig_interact5 = plt.figure()
ax_interact5 = fig_interact5.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.25, bottom=0.25)

# Valores iniciales
A0_5, S0_5, W0_5, B0_5 = np.radians(45), 2.5, 0, 0.2

def actualizar5(val):
    ax_interact5.cla()
    A = slider_A5.val
    S = slider_S5.val
    W = slider_W5.val
    B = slider_B5.val
    theta = np.linspace(0, S * 2 * np.pi, 1000)
    x = np.cos(theta + W) * np.cos(A)
    y = np.sin(theta + W) * np.cos(A)
    z = B * theta
    ax_interact5.plot(x, y, z, color='blue')
    ax_interact5.set_xlim([-1.5, 1.5])
    ax_interact5.set_ylim([-1.5, 1.5])
    ax_interact5.set_zlim([0, 3 * np.pi])
    ax_interact5.set_title("Espacio proyectivo interactivo")
    fig_interact5.canvas.draw_idle()

# Controles
ax_A5 = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_S5 = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_W5 = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_B5 = plt.axes([0.25, 0.00, 0.65, 0.03], facecolor='lightgoldenrodyellow')

slider_A5 = Slider(ax_A5, 'Ángulo A', 0, np.pi/2, valinit=A0_5)
slider_S5 = Slider(ax_S5, 'Spin S', 1, 6, valinit=S0_5)
slider_W5 = Slider(ax_W5, 'Fase W', 0, 2*np.pi, valinit=W0_5)
slider_B5 = Slider(ax_B5, 'Torsión B', 0.05, 0.5, valinit=B0_5)

slider_A5.on_changed(actualizar5)
slider_S5.on_changed(actualizar5)
slider_W5.on_changed(actualizar5)
slider_B5.on_changed(actualizar5)

actualizar5(None)
plt.show()

# Visualización estructural radial desde ε₀ (forma proyectiva real)
fig6 = plt.figure()
ax6 = fig6.add_subplot(111, projection='3d')

# Ángulos esféricos
phi = np.linspace(0, np.pi, 60)       # inclinación (0: polo norte, π: sur)
theta = np.linspace(0, 2 * np.pi, 60) # azimut (0 → 2π)
phi, theta = np.meshgrid(phi, theta)

# Parámetros de deformación estructural
torsion = 0.3 * np.sin(3 * phi)       # simula oscilaciones de presión/torsión
spin_mod = 0.2 * np.cos(2 * theta)    # simula variación por giro proyectado

# Radio proyectivo: unidad + variación estructural
R = 1 + torsion + spin_mod

# Coordenadas proyectadas desde el centro
X = R * np.sin(phi) * np.cos(theta)
Y = R * np.sin(phi) * np.sin(theta)
Z = R * np.cos(phi)

ax6.plot_surface(X, Y, Z, cmap='viridis', alpha=0.85, edgecolor='k', linewidth=0.3)
ax6.set_title("Campo estructural proyectivo desde ε₀ (visualización radial)")
ax6.set_xlabel("X")
ax6.set_ylabel("Y")
ax6.set_zlabel("Z")

# Visualización interactiva con sliders para campo estructural radial
from matplotlib.widgets import Slider

fig_interact6 = plt.figure()
ax_interact6 = fig_interact6.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.25, bottom=0.25)

# Valores iniciales
Torsion0_6, Spinmod0_6 = 0.3, 0.2

def actualizar6(val):
    ax_interact6.cla()
    torsion_amp = slider_Torsion6.val
    spinmod_amp = slider_Spinmod6.val
    phi = np.linspace(0, np.pi, 60)
    theta = np.linspace(0, 2 * np.pi, 60)
    phi, theta = np.meshgrid(phi, theta)
    torsion = torsion_amp * np.sin(3 * phi)
    spin_mod = spinmod_amp * np.cos(2 * theta)
    R = 1 + torsion + spin_mod
    X = R * np.sin(phi) * np.cos(theta)
    Y = R * np.sin(phi) * np.sin(theta)
    Z = R * np.cos(phi)
    ax_interact6.plot_surface(X, Y, Z, cmap='viridis', alpha=0.85, edgecolor='k', linewidth=0.3)
    ax_interact6.set_xlim([-2, 2])
    ax_interact6.set_ylim([-2, 2])
    ax_interact6.set_zlim([-2, 2])
    ax_interact6.set_title("Campo estructural radial interactivo")
    fig_interact6.canvas.draw_idle()

# Controles
ax_Torsion6 = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_Spinmod6 = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')

slider_Torsion6 = Slider(ax_Torsion6, 'Torsión', 0.05, 0.5, valinit=Torsion0_6)
slider_Spinmod6 = Slider(ax_Spinmod6, 'Spin Mod', 0.05, 0.5, valinit=Spinmod0_6)

slider_Torsion6.on_changed(actualizar6)
slider_Spinmod6.on_changed(actualizar6)

actualizar6(None)
plt.show()

 # Simulación de dispersión estructural posterior al acoplamiento
fig7 = plt.figure()
ax7 = fig7.add_subplot(111, projection='3d')

# Parámetros originales en el punto de acoplamiento
A1_new = a1 + np.radians(10)
A2_new = a2 - np.radians(15)
B1_new = 0.4
B2_new = 0.25
S1_new = 2.5
S2_new = 3

theta_disp = np.linspace(0, 2 * np.pi, 1000)

# Trayectorias dispersas desde el punto de acoplamiento
x1_disp = np.cos(theta_disp + w1) * np.cos(A1_new) + x_acop
y1_disp = np.sin(theta_disp + w1) * np.cos(A1_new) + y_acop
z1_disp = B1_new * theta_disp + z_acop

x2_disp = np.cos(theta_disp + w2) * np.cos(A2_new) + x_acop
y2_disp = np.sin(theta_disp + w2) * np.cos(A2_new) + y_acop
z2_disp = B2_new * theta_disp + z_acop

# Visualización
ax7.plot(x1_disp, y1_disp, z1_disp, color='darkblue', label='Dispersión p1')
ax7.plot(x2_disp, y2_disp, z2_disp, color='darkred', label='Dispersión p2')
ax7.scatter(x_acop, y_acop, z_acop, color='black', s=50, label='Punto de acoplamiento')

ax7.set_title("Dispersión estructural posterior al acoplamiento")
ax7.set_xlabel("X")
ax7.set_ylabel("Y")
ax7.set_zlabel("Z")
ax7.legend()
plt.show()

# Visualización interactiva con sliders para dispersión estructural posterior al acoplamiento
from matplotlib.widgets import Slider

fig_interact7 = plt.figure()
ax_interact7 = fig_interact7.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.25, bottom=0.25)

# Valores iniciales
A1n7, A2n7 = A1_new, A2_new
B1n7, B2n7 = B1_new, B2_new
S1n7, S2n7 = S1_new, S2_new

def actualizar7(val):
    ax_interact7.cla()
    A1 = slider_A1n7.val
    S1 = slider_S1n7.val
    B1 = slider_B1n7.val
    A2 = slider_A2n7.val
    S2 = slider_S2n7.val
    B2 = slider_B2n7.val
    theta_disp = np.linspace(0, 2 * np.pi, 1000)
    x1_disp = np.cos(theta_disp + w1) * np.cos(A1) + x_acop
    y1_disp = np.sin(theta_disp + w1) * np.cos(A1) + y_acop
    z1_disp = B1 * theta_disp + z_acop
    x2_disp = np.cos(theta_disp + w2) * np.cos(A2) + x_acop
    y2_disp = np.sin(theta_disp + w2) * np.cos(A2) + y_acop
    z2_disp = B2 * theta_disp + z_acop
    ax_interact7.plot(x1_disp, y1_disp, z1_disp, color='darkblue', label='Dispersión p1')
    ax_interact7.plot(x2_disp, y2_disp, z2_disp, color='darkred', label='Dispersión p2')
    ax_interact7.scatter(x_acop, y_acop, z_acop, color='black', s=50, label='Punto de acoplamiento')
    ax_interact7.set_xlim([-2, 2])
    ax_interact7.set_ylim([-2, 2])
    ax_interact7.set_zlim([0, 4 * np.pi * 0.5])
    ax_interact7.set_title("Dispersión estructural interactiva")
    ax_interact7.legend()
    fig_interact7.canvas.draw_idle()

# Controles
ax_A1n7 = plt.axes([0.25, 0.18, 0.30, 0.02], facecolor='lightgoldenrodyellow')
ax_S1n7 = plt.axes([0.25, 0.15, 0.30, 0.02], facecolor='lightgoldenrodyellow')
ax_B1n7 = plt.axes([0.25, 0.12, 0.30, 0.02], facecolor='lightgoldenrodyellow')
ax_A2n7 = plt.axes([0.60, 0.18, 0.30, 0.02], facecolor='lightgoldenrodyellow')
ax_S2n7 = plt.axes([0.60, 0.15, 0.30, 0.02], facecolor='lightgoldenrodyellow')
ax_B2n7 = plt.axes([0.60, 0.12, 0.30, 0.02], facecolor='lightgoldenrodyellow')

slider_A1n7 = Slider(ax_A1n7, 'Ángulo A1', 0, np.pi/2, valinit=A1n7)
slider_S1n7 = Slider(ax_S1n7, 'Spin S1', 1, 6, valinit=S1n7)
slider_B1n7 = Slider(ax_B1n7, 'Torsión B1', 0.05, 0.5, valinit=B1n7)
slider_A2n7 = Slider(ax_A2n7, 'Ángulo A2', 0, np.pi/2, valinit=A2n7)
slider_S2n7 = Slider(ax_S2n7, 'Spin S2', 1, 6, valinit=S2n7)
slider_B2n7 = Slider(ax_B2n7, 'Torsión B2', 0.05, 0.5, valinit=B2n7)

slider_A1n7.on_changed(actualizar7)
slider_S1n7.on_changed(actualizar7)
slider_B1n7.on_changed(actualizar7)
slider_A2n7.on_changed(actualizar7)
slider_S2n7.on_changed(actualizar7)
slider_B2n7.on_changed(actualizar7)

actualizar7(None)
plt.show()

# Simulación estructural de dispersión coherente desde ε₀ en forma toroidal
fig8 = plt.figure()
ax8 = fig8.add_subplot(111, projection='3d')

np.random.seed(123)
num_ramas = 30
longitud = 1000
theta_vals = np.linspace(0, 2 * np.pi, longitud)

for i in range(num_ramas):
    phi_dir = np.radians(np.random.uniform(10, 170))   # dirección polar
    theta_dir = np.random.uniform(0, 2 * np.pi)         # dirección azimutal
    torsion = np.random.uniform(0.15, 0.35)
    spin = np.random.uniform(1, 4)

    # Dirección vectorial de salida proyectiva
    dir_x = np.sin(phi_dir) * np.cos(theta_dir)
    dir_y = np.sin(phi_dir) * np.sin(theta_dir)
    dir_z = np.cos(phi_dir)

    # Trayectoria helicoidal en esa dirección
    x_disp = dir_x * np.cos(spin * theta_vals + i) + x_acop
    y_disp = dir_y * np.sin(spin * theta_vals + i) + y_acop
    z_disp = dir_z * torsion * theta_vals + z_acop

    color = plt.cm.coolwarm(i / num_ramas)
    ax8.plot(x_disp, y_disp, z_disp, color=color, alpha=0.8)

ax8.scatter(x_acop, y_acop, z_acop, color='black', s=60, label='Nodo inicial (ε₀)')
ax8.set_title("Dispersión estructurada en espacio toroidal desde ε₀")
ax8.set_xlabel("X")
ax8.set_ylabel("Y")
ax8.set_zlabel("Z")
ax8.legend()
plt.show()

# Visualización interactiva con sliders para dispersión toroidal
from matplotlib.widgets import Slider

fig_interact8 = plt.figure()
ax_interact8 = fig_interact8.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.25, bottom=0.25)

# Valores iniciales
Nramas8, Spin8, Torsion8 = 10, 2.0, 0.2

def actualizar8(val):
    ax_interact8.cla()
    num_ramas = int(slider_Nramas8.val)
    spin = slider_Spin8.val
    torsion = slider_Torsion8.val
    longitud = 1000
    theta_vals = np.linspace(0, 2 * np.pi, longitud)
    np.random.seed(123)
    for i in range(num_ramas):
        phi_dir = np.radians(np.random.uniform(10, 170))
        theta_dir = np.random.uniform(0, 2 * np.pi)
        dir_x = np.sin(phi_dir) * np.cos(theta_dir)
        dir_y = np.sin(phi_dir) * np.sin(theta_dir)
        dir_z = np.cos(phi_dir)
        x_disp = dir_x * np.cos(spin * theta_vals + i) + x_acop
        y_disp = dir_y * np.sin(spin * theta_vals + i) + y_acop
        z_disp = dir_z * torsion * theta_vals + z_acop
        color = plt.cm.coolwarm(i / max(1, num_ramas))
        ax_interact8.plot(x_disp, y_disp, z_disp, color=color, alpha=0.8)
    ax_interact8.scatter(x_acop, y_acop, z_acop, color='black', s=60, label='Nodo inicial (ε₀)')
    ax_interact8.set_xlim([-2, 2])
    ax_interact8.set_ylim([-2, 2])
    ax_interact8.set_zlim([0, 4 * np.pi * 0.5])
    ax_interact8.set_title("Dispersión toroidal interactiva")
    ax_interact8.legend()
    fig_interact8.canvas.draw_idle()

# Controles
ax_Nramas8 = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_Spin8 = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_Torsion8 = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')

slider_Nramas8 = Slider(ax_Nramas8, 'Nº Ramas', 1, 30, valinit=Nramas8, valstep=1)
slider_Spin8 = Slider(ax_Spin8, 'Spin', 1, 6, valinit=Spin8)
slider_Torsion8 = Slider(ax_Torsion8, 'Torsión', 0.05, 0.5, valinit=Torsion8)

slider_Nramas8.on_changed(actualizar8)
slider_Spin8.on_changed(actualizar8)
slider_Torsion8.on_changed(actualizar8)

actualizar8(None)
plt.show()

# Simulación de proyección y acoplamiento con trayectorias helicoidales reales
fig9 = plt.figure()
ax9 = fig9.add_subplot(111, projection='3d')

# Parámetros base
r1, r2 = 1.0, 1.0  # radio de giro helicoidal
b1, b2 = 0.2, 0.3  # paso de hélice (torsión)
S1, S2 = 3, 2.5    # cantidad de giros
w1, w2 = 0, np.pi/3  # fases

theta_h = np.linspace(0, 2 * np.pi * S1, 1000)
phi_h = np.linspace(0, 2 * np.pi * S2, 1000)

# Trayectoria helicoidal 1
x1_h = r1 * np.cos(theta_h)
y1_h = r1 * np.sin(theta_h)
z1_h = b1 * theta_h

# Trayectoria helicoidal 2
x2_h = r2 * np.cos(phi_h + w2)
y2_h = r2 * np.sin(phi_h + w2)
z2_h = b2 * phi_h + 1.5  # desplazada en Z

# Calcular acoplamiento como mínima distancia
z1_interp = np.interp(np.linspace(0, 1, 1000), np.linspace(0, 1, len(z1_h)), z1_h)
z2_interp = np.interp(np.linspace(0, 1, 1000), np.linspace(0, 1, len(z2_h)), z2_h)
dist_h = np.sqrt((x1_h - x2_h)**2 + (y1_h - y2_h)**2 + (z1_interp - z2_interp)**2)
i_acop = np.argmin(dist_h)

x_acop_h = (x1_h[i_acop] + x2_h[i_acop]) / 2
y_acop_h = (y1_h[i_acop] + y2_h[i_acop]) / 2
z_acop_h = (z1_interp[i_acop] + z2_interp[i_acop]) / 2

# Graficar
ax9.plot(x1_h, y1_h, z1_h, label="Hélice 1", color='blue')
ax9.plot(x2_h, y2_h, z2_h, label="Hélice 2", color='red')
ax9.scatter(x_acop_h, y_acop_h, z_acop_h, s=60, color='black', label="Acoplamiento")

ax9.set_title("Acoplamiento con trayectorias helicoidales reales")
ax9.set_xlabel("X")
ax9.set_ylabel("Y")
ax9.set_zlabel("Z")

ax9.legend()
plt.show()

# Visualización interactiva con sliders para acoplamiento de hélices reales
from matplotlib.widgets import Slider

fig_interact9 = plt.figure()
ax_interact9 = fig_interact9.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.25, bottom=0.25)

# Valores iniciales
r10_9, r20_9 = 1.0, 1.0
b10_9, b20_9 = 0.2, 0.3
S10_9, S20_9 = 3, 2.5
w10_9, w20_9 = 0, np.pi/3

def actualizar9(val):
    ax_interact9.cla()
    r1 = slider_r1_9.val
    r2 = slider_r2_9.val
    b1 = slider_b1_9.val
    b2 = slider_b2_9.val
    S1 = slider_S1_9.val
    S2 = slider_S2_9.val
    w1 = slider_w1_9.val
    w2 = slider_w2_9.val
    theta_h = np.linspace(0, 2 * np.pi * S1, 1000)
    phi_h = np.linspace(0, 2 * np.pi * S2, 1000)
    x1_h = r1 * np.cos(theta_h)
    y1_h = r1 * np.sin(theta_h)
    z1_h = b1 * theta_h
    x2_h = r2 * np.cos(phi_h + w2)
    y2_h = r2 * np.sin(phi_h + w2)
    z2_h = b2 * phi_h + 1.5
    z1_interp = np.interp(np.linspace(0, 1, 1000), np.linspace(0, 1, len(z1_h)), z1_h)
    z2_interp = np.interp(np.linspace(0, 1, 1000), np.linspace(0, 1, len(z2_h)), z2_h)
    dist_h = np.sqrt((x1_h - x2_h)**2 + (y1_h - y2_h)**2 + (z1_interp - z2_interp)**2)
    i_acop = np.argmin(dist_h)
    x_acop_h = (x1_h[i_acop] + x2_h[i_acop]) / 2
    y_acop_h = (y1_h[i_acop] + y2_h[i_acop]) / 2
    z_acop_h = (z1_interp[i_acop] + z2_interp[i_acop]) / 2
    ax_interact9.plot(x1_h, y1_h, z1_h, label="Hélice 1", color='blue')
    ax_interact9.plot(x2_h, y2_h, z2_h, label="Hélice 2", color='red')
    ax_interact9.scatter(x_acop_h, y_acop_h, z_acop_h, s=60, color='black', label="Acoplamiento")
    ax_interact9.set_xlim([-2, 2])
    ax_interact9.set_ylim([-2, 2])
    ax_interact9.set_zlim([-1, 5])
    ax_interact9.set_title("Acoplamiento de hélices real interactivo")
    ax_interact9.legend()
    fig_interact9.canvas.draw_idle()

# Controles
ax_r1_9 = plt.axes([0.25, 0.20, 0.30, 0.02], facecolor='lightgoldenrodyellow')
ax_r2_9 = plt.axes([0.25, 0.17, 0.30, 0.02], facecolor='lightgoldenrodyellow')
ax_b1_9 = plt.axes([0.25, 0.14, 0.30, 0.02], facecolor='lightgoldenrodyellow')
ax_b2_9 = plt.axes([0.25, 0.11, 0.30, 0.02], facecolor='lightgoldenrodyellow')
ax_S1_9 = plt.axes([0.60, 0.20, 0.30, 0.02], facecolor='lightgoldenrodyellow')
ax_S2_9 = plt.axes([0.60, 0.17, 0.30, 0.02], facecolor='lightgoldenrodyellow')
ax_w1_9 = plt.axes([0.60, 0.14, 0.30, 0.02], facecolor='lightgoldenrodyellow')
ax_w2_9 = plt.axes([0.60, 0.11, 0.30, 0.02], facecolor='lightgoldenrodyellow')

slider_r1_9 = Slider(ax_r1_9, 'Radio 1', 0.5, 2, valinit=r10_9)
slider_r2_9 = Slider(ax_r2_9, 'Radio 2', 0.5, 2, valinit=r20_9)
slider_b1_9 = Slider(ax_b1_9, 'Torsión 1', 0.05, 0.5, valinit=b10_9)
slider_b2_9 = Slider(ax_b2_9, 'Torsión 2', 0.05, 0.5, valinit=b20_9)
slider_S1_9 = Slider(ax_S1_9, 'Spin 1', 1, 6, valinit=S10_9)
slider_S2_9 = Slider(ax_S2_9, 'Spin 2', 1, 6, valinit=S20_9)
slider_w1_9 = Slider(ax_w1_9, 'Fase 1', 0, 2*np.pi, valinit=w10_9)
slider_w2_9 = Slider(ax_w2_9, 'Fase 2', 0, 2*np.pi, valinit=w20_9)

slider_r1_9.on_changed(actualizar9)
slider_r2_9.on_changed(actualizar9)
slider_b1_9.on_changed(actualizar9)
slider_b2_9.on_changed(actualizar9)
slider_S1_9.on_changed(actualizar9)
slider_S2_9.on_changed(actualizar9)
slider_w1_9.on_changed(actualizar9)
slider_w2_9.on_changed(actualizar9)

actualizar9(None)
plt.show()

# Simulación de acoplamiento con rotación doble (spin estructural + giro propio)
fig10 = plt.figure()
ax10 = fig10.add_subplot(111, projection='3d')

# Parámetros principales del movimiento toroidal helicoidal
r = 1.0          # radio principal de giro
b = 0.05         # torsión helicoidal
S = 10           # número de vueltas toroidales
subspin = 5      # subgiros sobre el eje (giro interno)

theta_spin = np.linspace(0, 2 * np.pi * S, 2000)

# Trayectoria 1: giro toroidal + pequeño giro sobre su propio eje
x_spin1 = (r + 0.1 * np.cos(subspin * theta_spin)) * np.cos(theta_spin)
y_spin1 = (r + 0.1 * np.cos(subspin * theta_spin)) * np.sin(theta_spin)
z_spin1 = b * theta_spin + 0.05 * np.sin(subspin * theta_spin)

# Trayectoria 2: mismo patrón, desfasado ligeramente
x_spin2 = (r + 0.1 * np.cos(subspin * theta_spin + np.pi/2)) * np.cos(theta_spin)
y_spin2 = (r + 0.1 * np.cos(subspin * theta_spin + np.pi/2)) * np.sin(theta_spin)
z_spin2 = b * theta_spin + 0.05 * np.sin(subspin * theta_spin + np.pi/2)

# Visualización
ax10.plot(x_spin1, y_spin1, z_spin1, label="Partícula 1", color='blue')
ax10.plot(x_spin2, y_spin2, z_spin2, label="Partícula 2", color='red')
ax10.set_title("Acoplamiento con doble rotación (spin visible)")
ax10.set_xlabel("X")
ax10.set_ylabel("Y")
ax10.set_zlabel("Z")

ax10.legend()
plt.show()

# Visualización interactiva con sliders para acoplamiento con doble rotación
from matplotlib.widgets import Slider

fig_interact10 = plt.figure()
ax_interact10 = fig_interact10.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.25, bottom=0.25)

# Valores iniciales
r0_10, b0_10, S0_10, subspin0_10 = 1.0, 0.05, 10, 5

def actualizar10(val):
    ax_interact10.cla()
    r = slider_r10.val
    b = slider_b10.val
    S = slider_S10.val
    subspin = int(slider_subspin10.val)
    theta_spin = np.linspace(0, 2 * np.pi * S, 2000)
    x_spin1 = (r + 0.1 * np.cos(subspin * theta_spin)) * np.cos(theta_spin)
    y_spin1 = (r + 0.1 * np.cos(subspin * theta_spin)) * np.sin(theta_spin)
    z_spin1 = b * theta_spin + 0.05 * np.sin(subspin * theta_spin)
    x_spin2 = (r + 0.1 * np.cos(subspin * theta_spin + np.pi/2)) * np.cos(theta_spin)
    y_spin2 = (r + 0.1 * np.cos(subspin * theta_spin + np.pi/2)) * np.sin(theta_spin)
    z_spin2 = b * theta_spin + 0.05 * np.sin(subspin * theta_spin + np.pi/2)
    ax_interact10.plot(x_spin1, y_spin1, z_spin1, label="Partícula 1", color='blue')
    ax_interact10.plot(x_spin2, y_spin2, z_spin2, label="Partícula 2", color='red')
    ax_interact10.set_xlim([-2, 2])
    ax_interact10.set_ylim([-2, 2])
    ax_interact10.set_zlim([-1, 7])
    ax_interact10.set_title("Acoplamiento doble rotación interactivo")
    ax_interact10.legend()
    fig_interact10.canvas.draw_idle()

# Controles
ax_r10 = plt.axes([0.25, 0.14, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_b10 = plt.axes([0.25, 0.11, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_S10 = plt.axes([0.25, 0.08, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_subspin10 = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')

slider_r10 = Slider(ax_r10, 'Radio', 0.5, 2, valinit=r0_10)
slider_b10 = Slider(ax_b10, 'Torsión', 0.01, 0.2, valinit=b0_10)
slider_S10 = Slider(ax_S10, 'Spin', 2, 20, valinit=S0_10)
slider_subspin10 = Slider(ax_subspin10, 'Subspin', 1, 15, valinit=subspin0_10, valstep=1)

slider_r10.on_changed(actualizar10)
slider_b10.on_changed(actualizar10)
slider_S10.on_changed(actualizar10)
slider_subspin10.on_changed(actualizar10)

actualizar10(None)
plt.show()

# Cálculo estructural de ħ desde hélice proyectada
import matplotlib.animation as animation

fig11 = plt.figure()
ax11 = fig11.add_subplot(111, projection='3d')

# Parámetros de partícula tipo electrón
masa = 9.11e-31  # kg
r = 1e-11        # m (radio helicoidal aproximado)
b = 1e-13        # paso helicoidal (distancia entre vueltas)
S = 1            # 1 giro completo
N = 1000         # resolución

theta_hbar = np.linspace(0, 2 * np.pi * S, N)
x_hbar = r * np.cos(theta_hbar)
y_hbar = r * np.sin(theta_hbar)
z_hbar = b * theta_hbar

# Cálculo de momento angular estructural
I = (2/5) * masa * r**2                  # momento de inercia de una esfera uniforme
omega = 2 * np.pi / (1e-15)             # frecuencia angular (~1 femtosegundo)
L = I * omega                           # momento angular
h_bar_estructural = L                   # nuestra interpretación de ħ estructural

# Mostrar valor calculado
print(f"ħ estructural aproximado: {h_bar_estructural:.2e} J·s")

# Simular energía estructural como variación
E_p = 0.5 * masa * omega**2 * r**2 * (1 + 0.1 * np.sin(3 * theta_hbar))

# Graficar hélice con energía codificada como color
for i in range(N - 1):
    ax11.plot([x_hbar[i], x_hbar[i+1]],
              [y_hbar[i], y_hbar[i+1]],
              [z_hbar[i], z_hbar[i+1]],
              color=plt.cm.plasma(E_p[i] / max(E_p)))

# Parámetros de segunda partícula para resonancia
fase2 = np.pi / 12
x2 = r * np.cos(theta_hbar + fase2)
y2 = r * np.sin(theta_hbar + fase2)
z2 = b * theta_hbar + 2e-11

# Condición de resonancia (fases cercanas)
delta_fase = np.abs(fase2)
resonante = delta_fase < np.pi / 8

if resonante:
    ax11.plot(x2, y2, z2, color='lime', label="Partícula resonante")
else:
    ax11.plot(x2, y2, z2, color='gray', label="Partícula no acoplada")

ax11.set_title("Cálculo estructural de ħ y resonancia proyectiva")
ax11.set_xlabel("X (m)")
ax11.set_ylabel("Y (m)")
ax11.set_zlabel("Z (m)")
ax11.legend()
plt.show()

# Lagrangiano estructural derivado de curvatura helicoidal
fig12 = plt.figure()
ax12 = fig12.add_subplot(111)

# Parámetros estructurales del modelo
masa = 9.11e-31      # kg
r = 1e-11            # m
b = 5e-13            # paso helicoidal (más realista)
omega = 2 * np.pi / 1e-15  # rad/s

# Tiempo real
t = np.linspace(0, 1e-15, 1000)

# Posición helicoidal
x = r * np.cos(omega * t)
y = r * np.sin(omega * t)
z = b * omega * t

# Derivadas
vx = -r * omega * np.sin(omega * t)
vy =  r * omega * np.cos(omega * t)
vz = b * omega * np.ones_like(t)

# Energía cinética real
T = 0.5 * masa * (vx**2 + vy**2 + vz**2)

# Energía potencial estructural basada en curvatura local
# Curvatura = cambio en dirección = torsión proyectiva estructural
curvatura = np.abs(np.gradient(np.arctan2(vy, vx)))
curvatura_norm = (curvatura - min(curvatura)) / (max(curvatura) - min(curvatura))

# V es alta donde hay más cambio de dirección → más torsión
V = T.max() * curvatura_norm**2  # energía estructural asociada a deformación proyectiva

# Lagrangiano
L = T - V

# Gráfico
ax12.plot(t * 1e15, T, label="Energía cinética T", color='blue')
ax12.plot(t * 1e15, V, label="Estructura proyectiva V", color='orange')
ax12.plot(t * 1e15, L, label="Lagrangiano estructural L = T - V", color='green', linewidth=2)

ax12.set_title("Lagrangiano desde curvatura helicoidal estructural")
ax12.set_xlabel("Tiempo (fs)")
ax12.set_ylabel("Energía (J)")
ax12.legend()
ax12.grid(True)
plt.tight_layout()
plt.show()

# Rotación automática para visualizaciones 3D
from matplotlib.animation import FuncAnimation

def rotar(figura, eje):
    def update(frame):
        eje.view_init(elev=30, azim=frame)
        return figura,
    return FuncAnimation(figura, update, frames=np.arange(0, 360, 2), interval=50)

# Aplicar rotación a figuras seleccionadas
rotar(fig6, ax6)
rotar(fig8, ax8)
rotar(fig9, ax9)
rotar(fig10, ax10)

# Visualización interactiva con sliders (proyección helicoidal)
from matplotlib.widgets import Slider

fig_int = plt.figure()
ax_int = fig_int.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.25, bottom=0.25)

# Valores iniciales
A0, S0, W0, B0 = np.radians(30), 3, 0, 0.2

def actualizar(val):
    ax_int.cla()
    A = slider_A.val
    S = slider_S.val
    W = slider_W.val
    B = slider_B.val
    theta = np.linspace(0, S * 2 * np.pi, 1000)
    x = np.cos(theta + W) * np.cos(A)
    y = np.sin(theta + W) * np.cos(A)
    z = B * theta
    ax_int.plot(x, y, z, color='blue')
    ax_int.set_xlim([-1, 1])
    ax_int.set_ylim([-1, 1])
    ax_int.set_zlim([0, 2 * np.pi])
    ax_int.set_title("Proyección estructural interactiva")
    fig_int.canvas.draw_idle()

# Controles
axcolor = 'lightgoldenrodyellow'
ax_A = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_S = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=axcolor)
ax_W = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
ax_B = plt.axes([0.25, 0.00, 0.65, 0.03], facecolor=axcolor)

slider_A = Slider(ax_A, 'Ángulo A', 0, np.pi/2, valinit=A0)
slider_S = Slider(ax_S, 'Spin S', 1, 6, valinit=S0)
slider_W = Slider(ax_W, 'Fase W', 0, 2*np.pi, valinit=W0)
slider_B = Slider(ax_B, 'Torsión B', 0.05, 0.5, valinit=B0)

slider_A.on_changed(actualizar)
slider_S.on_changed(actualizar)
slider_W.on_changed(actualizar)
slider_B.on_changed(actualizar)

actualizar(None)
plt.show()
###############################################################################
# NUEVA SIMULACIÓN: Derivación estructural completa del Lagrangiano desde ε₀
###############################################################################

# En esta simulación derivamos el Lagrangiano L = T - V partiendo de una proyección
# helicoidal real desde ε₀, mostrando paso a paso sus componentes:
# - T: energía cinética estructural
# - V: energía estructural basada en la curvatura local de la trayectoria
# - L: Lagrangiano total estructural
# Se visualiza la evolución de cada término con el tiempo.

import numpy as np
import matplotlib.pyplot as plt

# Parámetros estructurales nuevos (independientes)
masa = 4.2e-31           # kg (valor arbitrario, distinto de los anteriores)
r = 7e-12                # m (radio helicoidal)
b = 2.2e-13              # m (paso helicoidal)
omega = 2 * np.pi / 1.5e-15  # rad/s (frecuencia angular diferente)
fase = np.pi / 7         # fase de salida
S = 2.6                  # número de giros estructurales

# Tiempo simulado
t = np.linspace(0, 1.5e-15, 1200)

# Trayectoria helicoidal proyectiva real desde ε₀
theta = omega * t + fase
x = r * np.cos(theta)
y = r * np.sin(theta)
z = b * theta

# Derivadas respecto al tiempo
vx = -r * omega * np.sin(theta)
vy =  r * omega * np.cos(theta)
vz = b * omega * np.ones_like(t)

# 1. Energía cinética T
T = 0.5 * masa * (vx**2 + vy**2 + vz**2)

# 2. Energía estructural V asociada a la curvatura local
# Curvatura estructural: cambio de dirección local de la trayectoria
dx = np.gradient(x, t)
dy = np.gradient(y, t)
dz = np.gradient(z, t)
ddx = np.gradient(dx, t)
ddy = np.gradient(dy, t)
ddz = np.gradient(dz, t)
vel = np.sqrt(dx**2 + dy**2 + dz**2)
acel = np.sqrt(ddx**2 + ddy**2 + ddz**2)
# Curvatura de Frenet: |v x a| / |v|^3
num = np.sqrt((dy*ddz - dz*ddy)**2 + (dz*ddx - dx*ddz)**2 + (dx*ddy - dy*ddx)**2)
curvatura = num / (vel**3 + 1e-25)  # evitar división por cero

# Normalización y energía estructural (asociada a la deformación por curvatura)
curvatura_norm = (curvatura - np.min(curvatura)) / (np.max(curvatura) - np.min(curvatura) + 1e-25)
V = T.max() * (curvatura_norm**2)

# 3. Lagrangiano total
L = T - V

# --- Visualización ---
fig_lag = plt.figure()
ax_lag = fig_lag.add_subplot(111)

# Curvas principales
ax_lag.plot(t * 1e15, T, label="Energía cinética T", color='royalblue')
ax_lag.plot(t * 1e15, V, label="Energía estructural V (curvatura)", color='darkorange')
ax_lag.plot(t * 1e15, L, label="Lagrangiano total L = T - V", color='forestgreen', linewidth=2)

# Explicaciones de las curvas (comentarios):
# - T (azul): Energía cinética estructural de la proyección helicoidal real.
# - V (naranja): Energía estructural debida a la curvatura local de la trayectoria,
#                representa la "resistencia" estructural a deformaciones.
# - L (verde): Lagrangiano total estructural, que gobierna la dinámica proyectiva.

ax_lag.set_title("Derivación estructural completa del Lagrangiano desde ε₀")
ax_lag.set_xlabel("Tiempo (fs)")
ax_lag.set_ylabel("Energía (J)")
ax_lag.legend()
ax_lag.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Simulación de campo dinámico de acoplamientos estructurales en red
fig13 = plt.figure()
ax13 = fig13.add_subplot(111, projection='3d')

np.random.seed(2025)
num_particulas = 15
longitud = 1000
theta_vals = np.linspace(0, 2 * np.pi, longitud)
particulas = []

# Generar partículas proyectadas
for i in range(num_particulas):
    A = np.radians(np.random.uniform(15, 75))
    S = np.random.uniform(1, 4)
    W = np.random.uniform(0, 2 * np.pi)
    B = np.random.uniform(0.1, 0.35)

    theta = np.linspace(0, S * 2 * np.pi, longitud)
    x = np.cos(theta + W) * np.cos(A)
    y = np.sin(theta + W) * np.cos(A)
    z = B * theta

    particulas.append((x, y, z))
    color = plt.cm.viridis(i / num_particulas)
    ax13.plot(x, y, z, color=color, alpha=0.8)

# Calcular acoplamientos (conexiones si hay cercanía estructural)
threshold = 0.3  # umbral de acoplamiento (ajustable)
acoplamientos = []

for i in range(num_particulas):
    for j in range(i + 1, num_particulas):
        xi, yi, zi = particulas[i]
        xj, yj, zj = particulas[j]
        dists = np.sqrt((xi - xj)**2 + (yi - yj)**2 + (zi - zj)**2)
        min_dist = np.min(dists)
        if min_dist < threshold:
            idx = np.argmin(dists)
            punto_i = (xi[idx], yi[idx], zi[idx])
            punto_j = (xj[idx], yj[idx], zj[idx])
            acoplamientos.append((punto_i, punto_j))
            ax13.plot([punto_i[0], punto_j[0]],
                      [punto_i[1], punto_j[1]],
                      [punto_i[2], punto_j[2]],
                      color='black', linestyle='--', alpha=0.5)

ax13.set_title("Red dinámica de acoplamientos estructurales")
ax13.set_xlabel("X")
ax13.set_ylabel("Y")
ax13.set_zlabel("Z")
plt.show()
###############################################################################
# Simulación interactiva: derivadas estructurales fundamentales del modelo
###############################################################################

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Valores iniciales
r0_d, b0_d, omega0_d = 7e-12, 2.2e-13, 2 * np.pi / 1.5e-15
masa_d = 4.2e-31
t_d = np.linspace(0, 1.5e-15, 1200)

def calcular_derivadas(r, b, omega):
    theta = omega * t_d
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = b * theta
    dx = np.gradient(x, t_d)
    dy = np.gradient(y, t_d)
    dz = np.gradient(z, t_d)
    ddx = np.gradient(dx, t_d)
    ddy = np.gradient(dy, t_d)
    ddz = np.gradient(dz, t_d)
    vx = dx
    vy = dy
    vz = dz
    T = 0.5 * masa_d * (vx**2 + vy**2 + vz**2)
    vel = np.sqrt(dx**2 + dy**2 + dz**2)
    acel = np.sqrt(ddx**2 + ddy**2 + ddz**2)
    num = np.sqrt((dy*ddz - dz*ddy)**2 + (dz*ddx - dx*ddz)**2 + (dx*ddy - dy*ddx)**2)
    curvatura = num / (vel**3 + 1e-25)
    curvatura_norm = (curvatura - np.min(curvatura)) / (np.max(curvatura) - np.min(curvatura) + 1e-25)
    V = T.max() * (curvatura_norm**2)
    L = T - V
    return T, V, L, vx, vy, vz, ddx, ddy, ddz

fig_der = plt.figure(figsize=(10, 6))
ax_der = fig_der.add_subplot(111)
plt.subplots_adjust(left=0.25, bottom=0.35)

def actualizar_der(val):
    ax_der.cla()
    r = slider_r_d.val
    b = slider_b_d.val
    omega = slider_omega_d.val
    T, V, L, vx, vy, vz, axx, ayy, azz = calcular_derivadas(r, b, omega)
    tiempo_fs = t_d * 1e15
    ax_der.plot(tiempo_fs, T, label='T (Energía Cinética)', color='royalblue')
    ax_der.plot(tiempo_fs, V, label='V (Estructural)', color='darkorange')
    ax_der.plot(tiempo_fs, L, label='L = T - V', color='green')
    ax_der.plot(tiempo_fs, vx, '--', label='dx/dt', alpha=0.4)
    ax_der.plot(tiempo_fs, vy, '--', label='dy/dt', alpha=0.4)
    ax_der.plot(tiempo_fs, vz, '--', label='dz/dt', alpha=0.4)
    ax_der.plot(tiempo_fs, axx, ':', label='d²x/dt²', alpha=0.3)
    ax_der.plot(tiempo_fs, ayy, ':', label='d²y/dt²', alpha=0.3)
    ax_der.plot(tiempo_fs, azz, ':', label='d²z/dt²', alpha=0.3)
    ax_der.set_title("Derivadas estructurales fundamentales desde ε₀")
    ax_der.set_xlabel("Tiempo (fs)")
    ax_der.set_ylabel("Magnitud")
    ax_der.legend()
    ax_der.grid(True, alpha=0.3)
    fig_der.canvas.draw_idle()

# Sliders
ax_r_d = plt.axes([0.25, 0.23, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_b_d = plt.axes([0.25, 0.18, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_omega_d = plt.axes([0.25, 0.13, 0.65, 0.03], facecolor='lightgoldenrodyellow')

slider_r_d = Slider(ax_r_d, 'Radio r (m)', 1e-12, 2e-11, valinit=r0_d)
slider_b_d = Slider(ax_b_d, 'Torsión b (m)', 1e-13, 5e-13, valinit=b0_d)
slider_omega_d = Slider(ax_omega_d, 'Frecuencia ω (rad/s)', 2e15, 6e15, valinit=omega0_d)

slider_r_d.on_changed(actualizar_der)
slider_b_d.on_changed(actualizar_der)
slider_omega_d.on_changed(actualizar_der)

actualizar_der(None)
plt.show()