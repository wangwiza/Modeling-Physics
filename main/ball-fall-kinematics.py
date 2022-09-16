GlowScript 3.1 VPython

#The Mistake Game 2: The falling ball

#Your name: William Wang
#Your name: Wiliam Wang (my second clone)

length=1.0 
ground = box(pos=vector(0,-0.05, 0), size=vector(length, 0.05, .1), color=color.cyan)
print("Enter the ball's starting height, below") 
# Add an input statement here to collect information from the user. 
# Call the inputted variable "startHeight." It has to be called
# "startHeight" because that variable is the one used on other lines.
startHeight = -1
while startHeight < 0: #my precious baby that kicks away negative values (only positive or null heights!)
    startHeight = float(input("What is x?"))
ball=sphere(pos=vector(0,startHeight,0),size=vector(0.1,0.1,0.1),color=color.orange)
ball.initialvel = vector(0, 0, 0) #inital velocity, vo in the kinematics equation (not very useful for now...)            
ball.accel=vector(0,-9.8,0) #acceleration in the y diection

t=0 # the start of the timer
dt = 0.01 #the time interval for the calculations

ball.initialposition = ball.pos # This is xo in the kinematics equation (not very useful for now...)
ball.vel=ball.initialvel #redundant for the model but good practice to clarify physics problem.
ground = 0 #a little extra fun ;)

# Type the conditions for the while statement such that the ball
# stops moving down when it hits the ground.

while ball.pos.y > ground + 0.05: #while edge of ball is above ground
    ball.pos=ball.pos+ball.vel*dt +.5*ball.accel*dt**2 #update ball position (replaced t for dt)
    ball.vel=ball.vel+ball.accel*dt #update ball velocity
    t=t+dt #update elapsed time
    #print(ball.pos, ball.vel, t) this line was used to visualize the variables updating
    rate(10) #computer tick speed, or animation speed...
print("= = = = = = = = = = = = = = = = = = = = ")
print('Hit the ground in ', t,' seconds')
