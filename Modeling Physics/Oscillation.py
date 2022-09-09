GlowScript 3.1 VPython
#set bg color
display(width=600, height=300, center=vector(6,0,0), background = color.white)
#objects for harmonic motion
dora = box(pos = vec(12,0,0), size = vec(1,1,1), color = color.blue)
boots = helix(pos = vec(0,0,0), axis = vec(12,0,0), radius = .4, thickness = .1, coils = 20, color = color.red)
#platforms
wall = box(pos = vec(-.125,.75,0), size = vec(.25,3,1), color = color.green)
floor = box(pos = vec(6.125,-.625,0), size = vec(12.75,.25,1), color = color.green)
#define variables
mass = 1
k = 1 #sprint constant
eq = vec(9,0,0) #equilibrium pos
vel = vec(0,0,0) 
t = 0 #initial time value
dt = 0.0001 #loop time increment
#sys energy graph
E_graph = graph(title = 'Kinetic and Potential Energy of Spring Mass System', xtitle = 't (s)', ytitle = 'Energy (J)')
K_curve = gcurve(color = color.cyan, label = "Kinetic Energy")
U_curve = gcurve(color = color.orange, label = "Potential Energy")
#step-by-step var. for harmonic motion
while t < 20:
    rate(10000)
    #update var.
    acc = (eq - dora.pos) * (k/mass) #box acceleration
    vel = vel + acc * dt #box velocity
    dora.pos = dora.pos + vel * dt + .5 * acc * dt**2 #box position
    boots.axis = (dora.pos - boots.pos) #update spring axis to match box pos
    ke = .5 * mass * vel.x**2 #kinetic energy
    ue = .5 * k * (eq.x-dora.pos.x)**2 #potential energy
    #plot energie values on graph
    K_curve.plot(t, ke)
    U_curve.plot(t, ue)
    t = t + dt #time counter
