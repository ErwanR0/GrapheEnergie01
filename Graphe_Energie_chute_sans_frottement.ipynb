import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button

# === Constantes physiques ===
g = 9.81      # Gravité
m = 1.0       # Masse (kg)
h0 = 20.0     # Hauteur initiale (m)
k = 0.0     # Coefficient de frottement fluide (kg/s)

# === Simulation numérique avec arrêt à y=0 ===
dt = 0.01
t_max = 5.0
t_vals_full = np.arange(0, t_max, dt)

y = h0
v = 0.0

t_vals = []
y_vals = []
v_vals = []

for t in t_vals_full:
    if y <= 0:
        break
    a = g - (k / m) * v
    v += a * dt
    y -= v * dt
    if y < 0:
        y = 0
    t_vals.append(t)
    y_vals.append(y)
    v_vals.append(v)

t_vals = np.array(t_vals)
y_vals = np.array(y_vals)
v_vals = np.array(v_vals)

Ep_vals = m * g * y_vals
Ec_vals = 0.5 * m * v_vals**2
Em_vals = Ep_vals + Ec_vals  # Énergie mécanique

# === Préparation de la figure ===
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)

ax.set_xlim(0, t_vals[-1])
ax.set_ylim(0, max(Ep_vals) * 1.1)
ax.set_xlabel("Temps (s)")
ax.set_ylabel("Énergie (J)")
ax.set_title("Énergies")
ax.grid()

line_ep, = ax.plot([], [], 'b-', label="Énergie potentielle")
line_ec, = ax.plot([], [], 'r-', label="Énergie cinétique")
line_em, = ax.plot([], [], 'g--', label="Énergie mécanique")  # Ne pas toucher !
ax.legend()

# === Données pour l'animation ===
t_data, ep_data, ec_data, em_data = [], [], [], []
ani = None
is_paused = False  # État de pause

# === Initialisation ===
def init():
    t_data.clear()
    ep_data.clear()
    ec_data.clear()
    em_data.clear()
    line_ep.set_data([], [])
    line_ec.set_data([], [])
    line_em.set_data([], [])
    return line_ep, line_ec, line_em

# === Animation ===
def update(frame):
    t = t_vals[frame]
    t_data.append(t)
    ep_data.append(Ep_vals[frame])
    ec_data.append(Ec_vals[frame])
    em_data.append(Em_vals[frame])
    line_ep.set_data(t_data, ep_data)
    line_ec.set_data(t_data, ec_data)
    line_em.set_data(t_data, em_data)
    return line_ep, line_ec, line_em

# === Bouton Start / Restart ===
def start_animation(event):
    global ani, is_paused
    is_paused = False
    if ani is not None:
        try:
            ani.event_source.stop()
            ani._stop()
        except Exception:
            pass
        ani = None

    init()
    ani = FuncAnimation(fig, update, frames=len(t_vals),
                        init_func=init, interval=30, blit=True, repeat=False)
    fig.canvas.draw_idle()

# === Bouton Pause / Reprendre ===
def toggle_pause(event):
    global is_paused
    if ani is not None:
        if is_paused:
            ani.event_source.start()
        else:
            ani.event_source.stop()
        is_paused = not is_paused

# === Création des boutons ===
ax_button_start = plt.axes([0.2, 0.05, 0.25, 0.075])
btn_start = Button(ax_button_start, "Start / Restart")
btn_start.on_clicked(start_animation)

ax_button_pause = plt.axes([0.55, 0.05, 0.25, 0.075])
btn_pause = Button(ax_button_pause, "Pause / Reprendre")
btn_pause.on_clicked(toggle_pause)

plt.show()
