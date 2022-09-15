GlowScript 3.1 VPython
#Task 3: The Sticky Putty

L = 5              #length of roddisplay(width=600, height=300, center=vector(0,0,0), background = color.white)
g = vec(0,-9.81,0) #gravitational constant
theta = 0          #initial angle with vertical in rad
dtheta = 0         #initial change in angle
#shapes for the ceiling, the rod and the putty and extra fun ;)
ceiling = box(pos = vec(0,0.125,0), size = vec(2*L,0.25,4), color = vec(185/255,255,211/255))
rod = cylinder(pos = vec(0,0,0), axis = vec(0,-L,0), radius = 0.05, color = vec(169/255,169/255,169/255))
putty = sphere(pos = vec(-5,-L,0), radius = .1, color = vec(1,60/255,0))
elmo_hell = box(pos = vec(0,-L/2,-2), size = vec(2*L,L,.001), texture = "https://i.imgur.com/Zs7EmHy.gif")
gaben_heaven = box(pos = vec(0,L/2,-2), size = vec(2*L,L,.001), texture = "https://i.imgur.com/CWEpu6G.jpg")
# prompt for initial variables
v0 = float(input("What is the linear velocity of the putty?")) #prompt user for initial putty velocity (m/s)
while (v0 < 0):
    if (v0 < 0):
        print("Hmm... that putty will never hit the rod :( Please enter a positive value.")
    v0 = float(input("What is the linear velocity of the putty?")) #prompt user for initial putty velocity (m/s)
M = float(input("What is the mass of the rod?")) #prompt user for rod mass (kg)
while (M < 0):    
    if (M < 0):
        print("Negative mass? Impossible!")
    M = float(input("What is the mass of the rod?")) #prompt user for rod mass (kg)
m = float(input("What is the mass of the putty?")) #prompt user for putty mass (kg)  
while (m < 0):
    if (m < 0):
        print("Negative mass? Impossible!")
    m = float(input("What is the mass of the putty?")) #prompt user for putty mass (kg)

putty.v = vec(v0,0,0) #initial velocity vector (m/s)
Is = (1/3)*M*L**2       #inertia of rod at one end
Ik = m*L**2             #inertia of point object about axis
I = Is + Ik             #total inertia 
t = 0                   #initial time
dt = 0.0001             #time increment
#make the putty moving forward until it reaches the rod
while (putty.pos.x < 0):
    rate(10000)
    putty.pos = putty.pos + putty.v * dt #update putty position
    t = t + dt
#Find the angular momentum before the collision and final angular velocity
L_i =  L * m * putty.v.x                                  #initial angular momentum
w_f =  L_i/I                                                #angular velocity after collision
cm = (M * (rod.axis/2) + m * putty.pos)/(M + m) #center of mass
#Include print statements for:
print("I_sys = ",I, " kg*m^2\nL_i = ",L_i,"; kg*m^2/s\nw_f = ",w_f," rad/s\ninitial com = ",cm," m")#Total moment of inertia, initial angular momentum, final angular velocity, center of mass
#maximum values of height and angle
K =  .5 * I * w_f**2             #Kfinal
Hcm = K/((M + m) * mag(g))       #final height theory
#putty and rod system movement till max amplitude
while w_f >= 0:
    rate(10000)
    com = (M * (rod.axis/2) + m * putty.pos)/(M + m) #update cm
    alpha = g.y/L*sin(theta)                                     #angular acceleration
    w_f = w_f + alpha * dt                                       #angular velocity
    theta = theta + w_f * dt                                     #angle with vertical (in rad)
    angledeg = theta*(180/3.141592653589793)                     #convert angle in degree
    dtheta =  w_f * dt                                           #change in angular position
    rod.rotate(angle = dtheta, axis = vector(0,0,1), origin = vector(0,0.125,0)) #rotate rod
    putty.pos = rod.axis                             #match putty pos to rod end
    t = t * dt
#Include print statements for:
print("max angle = ",angledeg," deg\nmax alpha = ",alpha," rad/s^2\ncom at amplitude = ",com," m\nHtheo = ",Hcm," m\nHsim = ",com.y-cm.y," m") #angle in degree, angular acceleration , center of mass, and the different tests requested
while t < 300:
    rate(10000)
    com = (M * (rod.axis/2) + m * putty.pos)/(M + m) #update cm pos
    alpha = g.y/L*sin(theta)                                     #angular acceleration
    w_f = w_f + alpha * dt                                       #angular velocity
    theta = theta + w_f * dt                                     #angle with vertical (in rad)
    angledeg = theta*(180/3.141592653589793)                     #convert angle in degree
    dtheta =  w_f * dt                                           #change in angular position
    rod.rotate(angle = dtheta, axis = vector(0,0,1), origin = vector(0,0.125,0)) #rotate rod
    putty.pos = rod.axis                             #match putty pos to rod end
    t = t * dt


