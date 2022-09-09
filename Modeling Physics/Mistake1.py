GlowScript 3.1 VPython
#Made by William Wang

#Cart and fan on track
length = 1.0 #1.0m long track 
track = box(pos = vector(0,-0.05, 0), size = vector(length, 0.05, .10), color = color.red)   #the track will be a rectangle
start = -0.5*length+0.05 #starting position, 1/2 the distance from the end of track
cart = box(pos = vector(start,0,0),size = vector(0.1,0.05,0.1),color = color.green)

#initial values 
cart.mass = 0.80
cart.vel = vector(0.5,0,0) #inital velocity, vo in the kinematics equation 
cart.force = -0.278 #force of the fan
cart.accel = vector(cart.force/cart.mass,0,0) #Acceleration vector is 3 dimensions x,y,z
dt = 0.02 #the time interval for the calculations
t = 0 # the start of the timer

while t<1:
    rate(100) #slow the computer down
    cart.pos = cart.pos + cart.vel*dt + (0.5)*(cart.accel)*dt**2 # Update the cart's position
    cart.vel = cart.vel + cart.accel*dt # Update the initial velocity
    t = t + dt # update the elapsed total
    
print("Great job. The program is over. v = ", cart.vel, "m/s")
print("You are ready to do the next mistake game")