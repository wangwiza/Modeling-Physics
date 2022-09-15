Web VPython 3.2


#Task 4: Sink or Float?

#Name:Flora-lee Bornette, Sierra Dustin, William Wang
#beaker
fluid = box(pos = vec(0,-5,0), size = vec(10,10,10), opacity = .4, color = color.blue)
#block
steve = box(pos = vec(0,5,0), size = vec(3,3,3), color = color.cyan)
alex = box(pos = vec(0,7.5,0), size = vec(2,2,2), color = color.green)
#force arrows
wforce = arrow(pos = vec(0,0,0), axis = vec(0,0,0),color = color.red, shaftwidth = .1, headwidth = .5, headlength = 1)
fbforce = arrow(pos = vec(0,0,0), axis = vec(0,0,0),color = color.magenta, shaftwidth = .1, headwidth = .5, headlength = 1)
#force labels
wlabel = label(pos = vec(0,0,0), text = 'System Weight', xoffset = 70, height = 8, font = 'sans')
fblabel = label(pos = vec(0,0,0), text = 'System Buoyancy Force', xoffset = 70, height = 8, font = 'sans')
fclabel = label(pos = vec(0,0,0), text = 'Contact Force', xoffset = 70, height = 8, font = 'sans')
vdlabel = label(pos = vec(-15,0,0), text = 'Volume of Displaced Fluid', height = 8, font = 'sans')
buglabel = label(pos = vec(0,12,0), text = 'Make top block denser than bottom block\nto avoid bugs!!!', height = 12, font = 'sans')

#widgets
def R(r):
    global dt
    if (r.checked == True):
      dt = .001
    if (r.checked == False):
      dt = 0
checkbox(bind=R, text='Run') # text to right of button
scene.append_to_caption('\n\n')

def fluidselect(m): #changing the fluid the blocks are submerged in
  if m.selected == "water":
    fluid.p = 1000
    fluid.color = color.blue
  elif m.selected == "lava":
    fluid.p = 3100
    fluid.color = color.red
  elif m.selected == "milk":
    fluid.p = 1035
    fluid.color = vec(254/255, 1, 217/255)
  elif m.selected == "olive oil":
    fluid.p = 900
    fluid.color = vec(116/255, 138/255, 116/255)
  elif m.selected == "magic water":
    fluid.p = 12
    fluid.color = vec(196/255, 0, 151/255)
  
fluidmenu = menu(choices=["Pick your poison", 'water', 'lava', 'milk', 'olive oil', 'magic water'], bind=fluidselect)
scene.append_to_caption('\n\n')

def den_s(sp): #density slider for lower block
    global sp
    wa.text = "lower block density = " + '{:1.2f}'.format(sp.value) #this is to define the format number
Sp = slider(pos = scene.caption_anchor, min = 1, max = 3000, value = 500, bind = den_s)
wa = wtext(text= "The density of the lower block is = " '{:1.2f}'.format(Sp.value))  #and to see your selected number on the side of the slider
scene.append_to_caption(' m^3 \n')  
scene.append_to_caption('\n\n')  #add line spacing

def den_a(ap):#density slider for upper block
    global ap
    wb.text = "upper block density = " + '{:1.2f}'.format(ap.value)         #this is to define the format number
Ap = slider(pos = scene.caption_anchor, min = 1, max = 3000, value = 500, bind = den_a)
wb = wtext(text= "The density of the upper block is = " '{:1.2f}'.format(Ap.value))  #and to see your selected number on the side of the slider
scene.append_to_caption(' m^3\n')  
scene.append_to_caption('\n\n')  #add line spacing



#initial variables
g = vec(0,-9.81,0)
Fc = vec(0,0,0)
fluid.p = 1000
sp = Sp.value
ap = Ap.value
steve.acc = vec(0,0,0)
steve.vel = vec(0,.01,0)
alex.acc = vec(0,0,0)
alex.vel = vec(0,.01,0)
steve.m = sp * steve.size.x * steve.size.y * steve.size.z #getting mass from volume and density
alex.m = ap * alex.size.x * alex.size.y * alex.size.z
dt = .000
t = 0

#loop
while ():

    sp = Sp.value #receiving density from sliders
    ap = Ap.value
    steve.m = sp * steve.size.x * steve.size.y * steve.size.z #updating the masses of the blocks respectively
    alex.m = ap * alex.size.x * alex.size.y * alex.size.z

    rate(5000)
    fluid_top = fluid.pos.y + fluid.size.y/2 #defining key y-levels such as the top of the fluid and the top and bottoms of the blocks
    fluid_bot = fluid.pos.y - fluid.size.y/2
    steve_top = steve.pos.y + steve.size.y/2
    steve_bot = steve.pos.y - steve.size.y/2
    alex_top = alex.pos.y + alex.size.y/2
    alex_bot = alex.pos.y - alex.size.y/2

    if (steve_top <= fluid_top): #check if submerged
        steve_sub = steve.size.y
    else if (steve_bot >= fluid_top):
        steve_sub = 0 
    else:
        steve_sub = (fluid_top - steve_bot)
    if (alex_top <= fluid_top):
        alex_sub = alex.size.y
    else if (alex_bot >= fluid_top):
        alex_sub = 0 
    else:
        alex_sub = (fluid_top - alex_bot)
    alex_vsub = alex.size.x * alex_sub * alex.size.z
    steve_vsub = steve.size.x * steve_sub * steve.size.z
    fluid_vol = fluid.size.x * fluid.size.y * fluid.size.z
    if (steve_vsub != 0):
        fluid.size.y = (10*10*10+steve_vsub+alex_vsub)/(fluid.size.x*fluid.size.z)
    else:
        fluid.size.x = 10
        fluid.size.y = 10
        fluid.size.z = 10
    
    if (steve_bot < fluid_bot):
        steve.pos.y = fluid_bot + steve.size.y/2
        steve.vel = vec(0,0,0)
    if (steve_bot < fluid_top):
        Cds = -10000
    else:
        Cds = 0
    if (alex_bot < fluid_bot):
        alex.pos.y = fluid_bot + alex.size.y/2
        alex.vel = vec(0,0,0)

    if (alex_bot < fluid_top):
        Cda = -10000
    else:
        Cda = 0

    if (ap < sp):
      
    
        Fba = alex_vsub * fluid.p * -g
        weighta = alex.m * g
        Fdraga = Cda * alex.vel
        Fneta = Fba + Fdraga + weighta + Fc
        
        Fbs = steve_vsub * fluid.p * -g
        weights = steve.m * g
        Fdrags = Cds * steve.vel
        Fnets = Fbs + Fdrags + weights - Fc
        
        alex.acc = Fneta/alex.m
        if (alex_bot < steve_top):
            alex.pos.y = steve.pos.y + steve.size.y/2 + alex.size.y/2
            Fc = Fbs + weights + Fdrags - (steve.acc*steve.m)
        else:
            Fc = vec(0,0,0)
        Fneta = Fba + Fdraga + weighta + Fc
        alex.vel = alex.vel + alex.acc * dt
        alex.pos = alex.pos + alex.vel * dt
        
        Fnets = Fbs + Fdrags + weights - Fc
        if (alex_bot < steve_top):
            Fnets = Fbs + Fdrags + weights + weighta - Fc

        steve.acc = Fnets/steve.m
        steve.vel = steve.vel + steve.acc * dt
        steve.pos = steve.pos + steve.vel * dt
        
        if (Fc != 0):
            Fb = (alex_vsub+steve_vsub) * fluid.p * -g
            weight = (alex.m+steve.m) * g
            wforce.pos.y = steve_bot
            wforce.axis = weight/100000
            fbforce.pos.y = alex_top
            fbforce.axis = Fb/100000
            wlabel.pos = wforce.pos+wforce.axis/2
            fblabel.pos = fbforce.pos+fbforce.axis/2
            fclabel.pos.y = alex_bot
            wlabel.text = "System Weight: " + "{:.3f}".format(weight.y)," N"
            fblabel.text = "System Buoyancy Force: " + "{:.3f}".format(Fb.y)," N"
            fclabel.text = "Contact Force: ±" + "{:.3f}".format(Fc.y)," N"
            vdlabel.text = "Volume of Displaced Fluid: ",alex_vsub + steve_vsub," m^3"
        t = t + dt
    else:
        Fba = alex_vsub * fluid.p * -g
        weighta = alex.m * g
        
        Fbs = steve_vsub * fluid.p * -g
        weights = steve.m * g
        Fc = Fbs + weights
        
        Fb = (alex_vsub+steve_vsub) * fluid.p * -g
        weight = (alex.m+steve.m) * g
        if (steve_bot < fluid_top):
            Cd = -10000
        else:
            Cd = 0
        Fdrag = Cd * steve.vel
        Fnet = Fb + Fdrag + weight
        steve.acc = Fnet/(steve.m+alex.m)
        steve.vel = steve.vel + steve.acc * dt
        steve.pos = steve.pos + steve.vel * dt
        alex.pos.y = steve.pos.y + steve.size.y/2 + alex.size.y/2
        wforce.pos.y = steve_bot
        wforce.axis = weight/100000
        fbforce.pos.y = alex_top
        fbforce.axis = Fb/100000
        wlabel.pos = wforce.pos+wforce.axis/2
        fblabel.pos = fbforce.pos+fbforce.axis/2
        fclabel.pos.y = alex_bot
        wlabel.text = "System Weight: ", weight.y," N"
        fblabel.text = "System Buoyancy Force: ", Fb.y," N"
        fclabel.text = "Contact Force: ±", Fc.y," N"
        vdlabel.text = "Volume of Displaced Fluid: ",alex_vsub + steve_vsub," m^3"
        t = t + dt

#print...
