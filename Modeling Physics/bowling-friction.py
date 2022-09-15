GlowScript 3.1 VPython
#From Sliding to Rolling
display(width=600, height=300, center=vector(0,0,0), background = color.white)
#constants
mu = float(input("What is the kinetic friction coefficient of the rough surface?"))  #prompt user for mu
L_ice = 5       #ice length
L_rough = 10     #rough length
R = float(input("What is the radius of the shape?")) #prompt user for radius/shape size
M = float(input("What is the mass of the shape?")) #prompt user for shape mass
I_x = float(input("What is the X coefficient of the moment of inertia of the shape?")) #prompt user for shape X coeff
I = I_x * M * R**2  #moment of inertia of shape
g = vec(0,-9.8,0) #gravitational constant
#initial variables
t = 0             #initial time (s)
dt = 0.0001       #time interval
vel = vec(1,0,0) #initial ball linear velocity
Ff = mu * M * mag(g) * vec(-1,0,0) #friction force acting opposite to motion
w = 0      #initial angular velocity
#energy graph
E_graph = graph(title = 'Kinetic Energy of Rolling Shape', xtitle = 's (t)', ytitle = 'Energy (J)')
Kv = gcurve(color = color.cyan, label = "Translational Kinetic Energy")
Kw = gcurve(color = color.orange, label = "Rotational Kinetic Energy")
Et = gcurve(color = color.green, label = "Total Mechanical Energy")
#velocity graph
V_graph = graph(title = 'Velocity of Rolling Shape', xtitle = 'x (m)', ytitle = 'Velocity (m/s)')
fv = gcurve(color = color.blue, label = "v")
fw = gcurve(color = color.red, label = "wR")
#the floor and the ball
wet_floor = box(pos=vec(-L_ice/2,-R-.125,0), size=vec(L_ice,.25,2*R), color = vec(204/255,1,1) )
granola_bar = box(pos=vec(L_rough/2,-R-.125,0), size=vec(L_rough,.25, 2*R), color = vec(181/255,122/255,63/255))
uranus = sphere(pos = vec(-L_ice,0,0), radius = R, texture = "https://i.imgur.com/mXHoSBC.jpeg")
#Slipping
while uranus.pos.x <= 0: #when shape is on ice
    rate(10000) #10000 computations per second
    uranus.pos = uranus.pos + vel * dt #linear kinematics, vel is constant since no force, no acceleration
    t = t + dt 
    ve = .5 * M * vel.x**2 #translational k energy
    we = .5 * I * w**2 #rotational k energy
    Kv.plot(t, ve)
    Kw.plot(t, we) 
    Et.plot(t, ve+we)
    fv.plot(uranus.pos.x, vel.x)  
    fw.plot(uranus.pos.x, -w*R)    
#Rolling and Slipping/Without Slipping
while 0 < uranus.pos.x <= L_rough: #when shape is on rough surface
    rate(10000)
    if -w * R >= mag(vel):
        Ff = vec(0,0,0) #friction = 0 as total velocity at contact point is 0
    acc = Ff / M #acceleration of ball 
    vel = vel + acc * dt # linearvelocity of ball
    uranus.pos = uranus.pos + vel * dt + .5 * acc * dt**2 #position of ball
    tau = R * mag(Ff) #torque caused by friction
    w = w - (tau/I) * dt #angular vel gain due to ang acceleration
    uranus.rotate(origin = uranus.pos, axis = vector(0,0,1), angle = w * dt) #rotate ball  
    t = t + dt #increment time
    ve = .5 * M * vel.x**2 #translational k energy
    we = .5 * I * w**2 #rotational k energy
    Kv.plot(t, ve)
    Kw.plot(t, we) 
    Et.plot(t, ve+we)
    fv.plot(uranus.pos.x, vel.x)  
    fw.plot(uranus.pos.x, -w*R)                         
print("v final = ", vel.x," m/s, w final = ", -w*R," m/s")

