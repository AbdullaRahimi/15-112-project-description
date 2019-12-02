#Name: Abdulla Rahimi
#AndrewID : arahimi

from math import *
from tkinter import messagebox
import tkinter
#drawing panel is a library found on github that makes it easy to plot to a window
from drawingpanel import *
import random
import pygame

    ######## projectile motion simulator ########

def projectile(panel, v0, angle):

    v1 = initialV()

    #gets the values of G based on user selection
    if v1 != '' and str(v1) not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ': 
        planet = planetList.get(planetList.curselection())

        if planet == 'Mars':
            G = -3.8

        if planet == 'Earth':
            G = -9.81

        if planet == 'Jupiter':
            G = -24.79

        #calculate the values for the projectile using physics equations
        ivy = v1 * sin(radians(angle))
        ivx = v1 * cos(radians(angle))

        totalTime = -2 * ivy / G
        dt = totalTime / 200
        
        finalVy = ivy + (G * totalTime)
        
        finalV = finalVy ** 2
        finalV += v1**2
        finalV = sqrt(finalV)

        #print the projectile to the screen
        for i in range(200):
            t = i * dt
            x = ivx * t
            y = displacement(ivy, G, t)
            panel.canvas.create_oval(x, 300 - y, x + 5, 305 - y, fill='black',
                                     outline='black')
            panel.sleep(dt * 100)

        messagebox.showinfo('Data', 'Time of flight is ' + str(round(totalTime, 2))
                            + '\n' + 'The final velocity is ' + str(round(finalV, 2)))
        
    #In case the user doesn't input any values or inputs letters
    
    else:
        messagebox.showerror('invalid input', 'please input a value for v')


def displacement(iv, a, t):
    return iv * t + 0.5 * a * t**2

#Initial values for the velocity and angle based on user input
def initialV():
    v1 = ivelocity.get()
    if v1 != '' and str(v1) not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        v1 = int(v1)
        if v1 < 0:
            messagebox.showerror('invalid input',
                                 'please input a value for v greater than 0')
            ivelocity.delete(0,'end')

    if str(v1) in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        messagebox.showerror('invalid input', 'please input a number for v')
        ivelocity.delete(0,'end')
        
    return v1

def initialA():
    a1 = iangle.get()
    if a1 != '' and a1 not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        a1 = int(a1)
        if a1 < 0 or a1 > 90:
            messagebox.showerror('invalid input',
                                 'please input a value for a between 0 and 90')
            iangle.delete(0,'end')

    if str(a1) in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        messagebox.showerror('invalid input', 'please input a number for a')
        iangle.delete(0,'end')
        
    return a1

#starts the simulation, plots using drawing panel    
def startProjectile():
    a = initialA()
    if a != '':
        panel = DrawingPanel(600, 400)
        projectile(panel, initialV(), a)

    else:
        messagebox.showerror('invalid input', 'please input a value for a')

#projectile simulation window 
def openProjectile():
    projectile = tkinter.Toplevel()
    projectile.title('Projectile Motion Simulator')
    projectile.geometry('500x500')
    btn = tkinter.Button(projectile, text = 'Start Simulation',
                         command = startProjectile)
    velocitylabel = tkinter.Label(projectile, text = 'Initial Velocity')
    velocitylabel.place(x = 150, y = 130)
    global ivelocity
    #user enters initial velocity
    ivelocity = tkinter.Entry(projectile, width = 20)
    ivelocity.place(x = 150, y = 150)
    ivelocityset = tkinter.Button(projectile, text = 'set', width = 5,
                                  command = initialV)
    ivelocityset.place(x = 255, y = 148)
    anglelabel = tkinter.Label(projectile, text = 'Initial Angle')
    anglelabel.place(x = 150, y = 180)
    global iangle
    #user enters angle of launch
    iangle = tkinter.Entry(projectile, width = 20)
    iangle.place(x = 150, y = 200)
    iangleset = tkinter.Button(projectile, text = 'set', width = 5,
                               command = initialA)
    iangleset.place(x = 255, y = 200)
    global planetList
    #user gets to choose between different gravitational forces based on
    #different planets
    planetList = tkinter.Listbox(projectile, height = 3)
    planetList.insert('end', 'Mars')
    planetList.insert('end', 'Earth')
    planetList.insert('end', 'Jupiter')
    planetList.place(x = 150, y = 240)
    btn.place(x = 150, y = 300)

                        ######## Pressure Simulator ########

#initial temperature based on user input
def initialTemp():
    T1 = temperatureEntry.get()
    if T1 != '' and T1 not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        T1 = int(T1)
        if T1 < -273:
            messagebox.showerror('invalid input',
                                 'please enter a value for T1 greater than -273')
            temperatureEntry.delete(0,'end')

    if str(T1) in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        messagebox.showerror('invalid input',
                             'please enter a number for the value of T1')
        temperatureEntry.delete(0,'end')

        
    return T1

#starts the simulator
def startPressure():
    T1 = initialTemp()
    
    if T1 != '' and str(T1) not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        class Particle():
            def __init__(self,x,y):
                self.x = x
                self.y = y

                #movement of particles is based on their temperature
                if T1 >= 600:
                    self.dx = random.choice([-10,10])
                    self.dy = random.choice([-10,10])

                if T1 < 600 and T1 >= 500:
                    self.dx = random.choice([-9,9])
                    self.dy = random.choice([-9,9])

                if T1 < 500 and T1 >= 400:
                    self.dx = random.choice([-8,8])
                    self.dy = random.choice([-8,8])

                if T1 < 400 and T1 >= 300:
                    self.dx = random.choice([-7,7])
                    self.dy = random.choice([-7,7])

                if T1 < 300 and T1 >= 200:
                    self.dx = random.choice([-6,6])
                    self.dy = random.choice([-6,6])

                if T1 < 200 and T1 >= 100:
                    self.dx = random.choice([-5,5])
                    self.dy = random.choice([-5,5])

                if T1 < 100 and T1 >= 0:
                    self.dx = random.choice([-4,4])
                    self.dy = random.choice([-4,4])

                if T1 < 0 and T1 >= -100:
                    self.dx = random.choice([-3,3])
                    self.dy = random.choice([-3,3])

                if T1 < -100 and T1 >= -200:
                    self.dx = random.choice([-2,2])
                    self.dy = random.choice([-2,2])

                if T1 < -200 and T1 >= -273:
                    self.dx = random.choice([-1,1])
                    self.dy = random.choice([-1,1])
                    
                self.color = 'red'
                       
            def draw(self,c):
                c.create_oval(self.x, self.y, self.x + 10, self.y+10,fill=self.color)

            #makes the particles move  
            def move(self,mx,my):
                self.x += self.dx
                self.y += self.dy
                if self.x < 0 or self.x >mx:
                    self.dx = -self.dx
                if self.y < 0 or self.y >my:
                    self.dy = -self.dy
            
        class mainwnd():
            def __init__(self,root):
                concentration = concentrationList.get(concentrationList.curselection())
                T1 = initialTemp()
                self.mainFrame = tkinter.Frame(root)
                self.mainFrame.pack()
                self.Particles = []
                self.canv = tkinter.Canvas(self.mainFrame, bg = 'black' ,width = 450, height = 450)
                self.canv.pack()
                #pressure equation to calculate the total pressure on the container
                self.pressure = (float(concentration)*8.314*float(T1))/10.0
                pressureLabel = tkinter.Label(self.mainFrame,
                                              text = 'The pressure on the container is '
                                              + str(round(abs((self.pressure)))) + ' torr')
                pressureLabel.pack()

                #user chooses the concentration level which determines how
                #many particles are in the container
                if concentration == '5':
                    for i in range(200):
                        self.Particles.append(Particle(random.randint(0,440),
                                                       random.randint(0,440)))
                        for part in self.Particles:
                            part.draw(self.canv)
                    self.mainFrame.after(50,self.moveParticle)

                if concentration == '4':
                    for i in range(150):
                        self.Particles.append(Particle(random.randint(0,440),
                                                       random.randint(0,440)))
                        for part in self.Particles:
                            part.draw(self.canv)
                    self.mainFrame.after(50,self.moveParticle)

                if concentration == '3':
                    for i in range(100):
                        self.Particles.append(Particle(random.randint(0,440),
                                                       random.randint(0,440)))
                        for part in self.Particles:
                            part.draw(self.canv)
                    self.mainFrame.after(50,self.moveParticle)

                if concentration == '2':
                    for i in range(50):
                        self.Particles.append(Particle(random.randint(0,440),
                                                       random.randint(0,440)))
                        for part in self.Particles:
                            part.draw(self.canv)
                    self.mainFrame.after(50,self.moveParticle)

                if concentration == '1':
                    for i in range(10):
                        self.Particles.append(Particle(random.randint(0,440),
                                                       random.randint(0,440)))
                        for part in self.Particles:
                            part.draw(self.canv)
                    self.mainFrame.after(50,self.moveParticle)

            #allows the particles to move
            def moveParticle(self):
                for part in self.Particles:
                    part.move(450,450)
                self.canv.delete(tkinter.ALL)
                for part in self.Particles:
                    part.draw(self.canv)
                self.mainFrame.after(50,self.moveParticle)
                
        wnd = tkinter.Tk()
        wnd.geometry("500x500")
        wnd.title('Pressure Simulator')
        Sim = mainwnd(wnd)
        wnd.mainloop()

    else:
        messagebox.showerror('invalid input', 'please enter a value for T1')
        
#pressure simulator menu
def openPressure():
    pressure = tkinter.Toplevel()
    pressure.title('Pressure Simulator')
    pressure.geometry('500x500')
    temperaturelabel = tkinter.Label(pressure, text = 'Temperature')
    global temperatureEntry
    #temperature value based on user input
    temperatureEntry = tkinter.Entry(pressure, width = 20)
    btn = tkinter.Button(pressure, text = 'Start Simulation', command = startPressure)
    tempSet = tkinter.Button(pressure, text = 'set', width = 5, command = initialTemp)
    concentrationLevel = tkinter.Label(pressure, text = 'Concentration Level')
    global concentrationList
    #concentration level based on user input
    concentrationList = tkinter.Listbox(pressure, height = 5)
    concentrationList.insert('end', '1')
    concentrationList.insert('end', '2')
    concentrationList.insert('end', '3')
    concentrationList.insert('end', '4')
    concentrationList.insert('end', '5')
    temperaturelabel.place(x = 150, y = 100)
    temperatureEntry.place(x = 150, y = 120)
    tempSet.place(x = 270, y = 120)
    concentrationLevel.place(x = 150, y = 180)
    concentrationList.place(x = 150, y = 200)
    btn.place(x = 150, y = 300)

                    ######## Orbit Simulator ########


#code was written using answer on https://stackoverflow.com/questions/44814297/animating-an-object-to-move-in-a-circular-path-in-tkinter
#and the algorithm presented on https://stackoverflow.com/questions/41451690/how-to-make-tkinter-object-move-in-circlular-path
    

def orbitSim():
    orbital = tkinter.Toplevel()
    
    planetName = orbitList.get(orbitList.curselection())
        
    orbital.geometry('1200x1000')

    class Celestial(object):
        # Constants
        cos_0, cos_180 = cos(0), cos(radians(180))
        sin_90, sin_270 = sin(radians(90)), sin(radians(270))

        def __init__(self, x, y, radius):
            self.x, self.y = x, y
            self.radius = radius

        def bounds(self):
            #Return coords of rectangle surrounding circular object. 
            return (self.x + self.radius*self.cos_0,   self.y + self.radius*self.sin_270,
                    self.x + self.radius*self.cos_180, self.y + self.radius*self.sin_90)
        
    def circular_path(x, y, radius, delta_ang, start_ang=0):
        #Endlessly generate coords of a circular path every delta angle degrees.
        ang = start_ang % 360
        while True:
            yield x + radius*cos(radians(ang)), y + radius*sin(radians(ang))
            ang = (ang+delta_ang) % 360

    def update_position(canvas, id, celestial_obj, path_iter):
        celestial_obj.x, celestial_obj.y = next(path_iter)  # iterate path and set new position
        # update the position of the corresponding canvas obj
        x0, y0, x1, y1 = canvas.coords(id)  # coordinates of canvas oval object
        oldx, oldy = (x0+x1) // 2, (y0+y1) // 2  # current center point
        dx, dy = celestial_obj.x - oldx, celestial_obj.y - oldy  # amount of movement
        canvas.move(id, dx, dy)  # move canvas oval object that much
        # repeat after delay
        canvas.after(100, update_position, canvas, id, celestial_obj, path_iter)

    sunObject = Celestial(550, 450, 50)
    earthObject = Celestial(550 + 100, 450, 15)
    orbital_radius = hypot(sunObject.x - (earthObject.x), sunObject.y - (earthObject.y))
        
    orbital.title('Orbital Simulation')
    
    if planetName == 'All':
        canvas = tkinter.Canvas(orbital, bg='black', height=1000, width=1200)
        canvas.pack()
        
    else:
        canvas = tkinter.Canvas(orbital, bg='black', height=900, width=1200)
        canvas.pack()
        
    sun = canvas.create_oval(sunObject.bounds(), fill = 'yellow', width=0)

    #Different conditions for different planet simulations
    
    if planetName == 'Mercury':

        #create mercury object which will allow it to move
        
        mercuryObject = Celestial(550, 450 , 12)
        
        #the actual visual representation of mercury
        
        mercury = canvas.create_oval(mercuryObject.bounds(), fill = 'gray', width=0)
        
        #orbital path for mercury

        mercuryOrbital = circular_path(sunObject.x, sunObject.y, (0.75*orbital_radius), 40)
        next(mercuryOrbital)
        
        #updates the position of mercury every 100 milliseconds to allow it
        #to orbit
        
        orbital.after(100, update_position, canvas, mercury, mercuryObject, mercuryOrbital)

        #presents the information about mercury's orbit
        
        orbitalTime = tkinter.Label(orbital, text  = 'Orbital time: 88 days')
        orbitalDistance = tkinter.Label(orbital, text  = 'Orbital distance: 0.4 Au')
        planetSize = tkinter.Label(orbital, text = 'Size of the planet: 1/3 Earths')
        orbitalTime.pack()
        orbitalDistance.pack()
        planetSize.pack()

    if planetName == 'Venus':
        venusObject = Celestial(550, 450 , 15)
        venus = canvas.create_oval(venusObject.bounds(), fill = 'orange', width=0)
        venusOrbital = circular_path(sunObject.x, sunObject.y, (orbital_radius + 10), 16)
        next(venusOrbital)
        orbital.after(100, update_position, canvas, venus, venusObject, venusOrbital)
        orbitalTime = tkinter.Label(orbital, text  = 'Orbital time: 235 days')
        orbitalDistance = tkinter.Label(orbital, text  = 'Orbital distance: 0.7 Au')
        planetSize = tkinter.Label(orbital, text = 'Size of the planet: 0.85 Earths')
        orbitalTime.pack()
        orbitalDistance.pack()
        planetSize.pack()

    if planetName == 'Earth':
        earthObject = Celestial(550 + 100, 450, 17)
        earth = canvas.create_oval(earthObject.bounds(), fill = 'blue', width=0)
        earthOrbital = circular_path(sunObject.x, sunObject.y, orbital_radius + 45, 10)
        next(earthOrbital)
        orbital.after(100, update_position, canvas, earth, earthObject, earthOrbital)
        orbitalTime = tkinter.Label(orbital, text  = 'Orbital time: 365 days')
        orbitalDistance = tkinter.Label(orbital, text  = 'Orbital distance: 1 Au')
        planetSize = tkinter.Label(orbital, text = 'Size of the planet: 1 Earth')
        orbitalTime.pack()
        orbitalDistance.pack()
        planetSize.pack()

    if planetName == 'Mars':
        marsObject = Celestial(550, 450 , 13)
        mars = canvas.create_oval(marsObject.bounds(), fill = 'red', width=0)
        marsOrbital = circular_path(sunObject.x, sunObject.y, (orbital_radius + 80), 5.3)
        next(marsOrbital)
        orbital.after(100, update_position, canvas, mars, marsObject, marsOrbital)
        orbitalTime = tkinter.Label(orbital, text  = 'Orbital time: 687 days')
        orbitalDistance = tkinter.Label(orbital, text  = 'Orbital distance: 1.5 Au')
        planetSize = tkinter.Label(orbital, text = 'Size of the planet: 1/2 Earths')
        orbitalTime.pack()
        orbitalDistance.pack()
        planetSize.pack()

    if planetName == 'Jupiter':
        jupiterObject = Celestial(550, 450 , 35)
        jupiter = canvas.create_oval(jupiterObject.bounds(), fill = 'brown', width=0)
        jupiterOrbital = circular_path(sunObject.x, sunObject.y, (orbital_radius + 140), 0.84)
        next(jupiterOrbital)
        orbital.after(100, update_position, canvas, jupiter, jupiterObject, jupiterOrbital)
        orbitalTime = tkinter.Label(orbital, text  = 'Orbital time: 4330 days')
        orbitalDistance = tkinter.Label(orbital, text  = 'Orbital distance: 11.8 Au')
        planetSize = tkinter.Label(orbital, text = 'Size of the planet: 11 Earths')
        orbitalTime.pack()
        orbitalDistance.pack()
        planetSize.pack()

    if planetName == 'Saturn':
        saturnObject = Celestial(550, 450 , 30)
        saturn = canvas.create_oval(saturnObject.bounds(), fill = 'burlywood2', width=0)
        saturnOrbital = circular_path(sunObject.x, sunObject.y, (orbital_radius + 220), 0.34)
        next(saturnOrbital)
        orbital.after(100, update_position, canvas, saturn, saturnObject, saturnOrbital)
        orbitalTime = tkinter.Label(orbital, text  = 'Orbital time: 10,755 days')
        orbitalDistance = tkinter.Label(orbital, text  = 'Orbital distance: 9.2 Au')
        planetSize = tkinter.Label(orbital, text = 'Size of the planet: 9.5 Earths')
        orbitalTime.pack()
        orbitalDistance.pack()
        planetSize.pack()
        
    if planetName == 'Uranus':
        uranusObject = Celestial(550, 450 , 20)
        uranus = canvas.create_oval(uranusObject.bounds(), fill ='blue', width=0)
        uranusOrbital = circular_path(sunObject.x, sunObject.y + 150, (orbital_radius + 250), 0.12)
        next(uranusOrbital)
        orbital.after(100, update_position, canvas, uranus, uranusObject, uranusOrbital)
        orbitalTime = tkinter.Label(orbital, text  = 'Orbital time: 30,660 days')
        orbitalDistance = tkinter.Label(orbital, text  = 'Orbital distance: 19.8 Au')
        planetSize = tkinter.Label(orbital, text = 'Size of the planet: 4 Earths')
        orbitalTime.pack()
        orbitalDistance.pack()
        planetSize.pack()

    if planetName == 'Neptune':
        neptuneObject = Celestial(550, 450, 20)
        neptune = canvas.create_oval(neptuneObject.bounds(), fill = 'cadetblue1', width=0)
        neptuneOrbital = circular_path(sunObject.x, sunObject.y - 100, (orbital_radius + 300), 0.06)
        next(neptuneOrbital)
        orbital.after(100, update_position, canvas, neptune, neptuneObject, neptuneOrbital)
        orbitalTime = tkinter.Label(orbital, text  = 'Orbital time: 60,255 days')
        orbitalDistance = tkinter.Label(orbital, text  = 'Orbital distance: 30.1 Au')
        planetSize = tkinter.Label(orbital, text = 'Size of the planet: 3.9 Earths')
        orbitalTime.pack()
        orbitalDistance.pack()
        planetSize.pack()

    if planetName == 'Pluto':
        plutoObject = Celestial(550, 450 , 10)
        pluto = canvas.create_oval(plutoObject.bounds(), fill = 'antique white', width=0)
        plutoOrbital = circular_path(sunObject.x, sunObject.y + 100, (orbital_radius + 350), 0.03)
        next(plutoOrbital)
        orbital.after(100, update_position, canvas, pluto, plutoObject, plutoOrbital)
        orbitalTime = tkinter.Label(orbital, text  = 'Orbital time: 90,520 days')
        orbitalDistance = tkinter.Label(orbital, text  = 'Orbital distance: 35 Au')
        planetSize = tkinter.Label(orbital, text = 'Size of the planet: 1/8 Earths')
        orbitalTime.pack()
        orbitalDistance.pack()
        planetSize.pack()
        
    #the whole solar system simulation   
    if planetName == 'All':
        
        earthObject = Celestial(550, 450, 17)
        mercuryObject = Celestial(550, 450 , 12)
        venusObject = Celestial(550, 450 , 15)
        marsObject = Celestial(550, 450 , 13)
        jupiterObject = Celestial(550, 450 , 35)
        saturnObject = Celestial(550, 450 , 30)
        uranusObject = Celestial(550, 450 , 20)
        neptuneObject = Celestial(550, 450, 20)
        plutoObject = Celestial(550, 450 , 10)

        #create all the planets and the Sun
        sun = canvas.create_oval(sunObject.bounds(), fill = 'yellow', width=0)
        earth = canvas.create_oval(earthObject.bounds(), fill = 'blue', width=0)
        mercury = canvas.create_oval(mercuryObject.bounds(), fill = 'gray', width=0)
        venus = canvas.create_oval(venusObject.bounds(), fill = 'orange', width=0)
        mars = canvas.create_oval(marsObject.bounds(), fill = 'red', width=0)
        jupiter = canvas.create_oval(jupiterObject.bounds(), fill = 'brown', width=0)
        saturn = canvas.create_oval(saturnObject.bounds(), fill = 'burlywood2', width=0)
        uranus = canvas.create_oval(uranusObject.bounds(), fill ='blue', width=0)
        neptune = canvas.create_oval(neptuneObject.bounds(), fill = 'cadetblue1', width=0)
        pluto = canvas.create_oval(plutoObject.bounds(), fill = 'antique white', width=0)

        #Orbital path for each of the planets
        earthOrbital = circular_path(sunObject.x, sunObject.y, orbital_radius + 45, 10)
        mercuryOrbital = circular_path(sunObject.x, sunObject.y, (0.75*orbital_radius), 40)
        venusOrbital = circular_path(sunObject.x, sunObject.y, (orbital_radius + 10), 16)
        marsOrbital = circular_path(sunObject.x, sunObject.y, (orbital_radius + 80), 5.3)
        jupiterOrbital = circular_path(sunObject.x, sunObject.y, (orbital_radius + 140), 0.84)
        saturnOrbital = circular_path(sunObject.x, sunObject.y, (orbital_radius + 220), 0.34)
        uranusOrbital = circular_path(sunObject.x, sunObject.y + 150, (orbital_radius + 250), 0.12)
        neptuneOrbital = circular_path(sunObject.x, sunObject.y - 100, (orbital_radius + 300), 0.06)
        plutoOrbital = circular_path(sunObject.x, sunObject.y + 100, (orbital_radius + 350), 0.03)
        
        next(earthOrbital) # prime generator
        next(mercuryOrbital)
        next(marsOrbital)
        next(venusOrbital)
        next(jupiterOrbital)
        next(saturnOrbital)
        next(uranusOrbital)
        next(neptuneOrbital)
        next(plutoOrbital)

        #updates the position of each planet after 100 milliseconds
        orbital.after(100, update_position, canvas, earth, earthObject, earthOrbital)
        orbital.after(100, update_position, canvas, mercury, mercuryObject, mercuryOrbital)
        orbital.after(100, update_position, canvas, venus, venusObject, venusOrbital)
        orbital.after(100, update_position, canvas, mars, marsObject, marsOrbital)
        orbital.after(100, update_position, canvas, jupiter, jupiterObject, jupiterOrbital)
        orbital.after(100, update_position, canvas, saturn, saturnObject, saturnOrbital)
        orbital.after(100, update_position, canvas, uranus, uranusObject, uranusOrbital)
        orbital.after(100, update_position, canvas, neptune, neptuneObject, neptuneOrbital)
        orbital.after(100, update_position, canvas, pluto, plutoObject, plutoOrbital)

    orbital.mainloop()

def openOrbit():
    orbit = tkinter.Toplevel()
    orbit.title('Orbital Simulator')
    orbit.geometry('500x500')
    orbitLabel = tkinter.Label(orbit, text = 'Choose the planet')
    global orbitList
    orbitList = tkinter.Listbox(orbit, height = 10, width = 20)
    orbitList.insert('end', 'Mercury')
    orbitList.insert('end', 'Venus')
    orbitList.insert('end', 'Earth')
    orbitList.insert('end', 'Mars')
    orbitList.insert('end', 'Jupiter')
    orbitList.insert('end', 'Saturn')
    orbitList.insert('end', 'Uranus')
    orbitList.insert('end', 'Neptune')
    orbitList.insert('end', 'Pluto')
    orbitList.insert('end', 'All')
    chooseButton = tkinter.Button(orbit, text = 'start', command = orbitSim)
    orbitLabel.place(x = 150, y = 100)
    orbitList.place(x = 150, y = 120)
    chooseButton.place(x = 180, y = 300)

                ########main screen########
    
root = tkinter.Tk()

mainFrame = tkinter.Frame()
mainFrame.pack()

#buttons for each simulator
btn1 = tkinter.Button(mainFrame, text = 'Projectile Motion', command = openProjectile)
btn2 = tkinter.Button(mainFrame, text = 'Pressure Simulator', command = openPressure)
btn3 = tkinter.Button(mainFrame, text = 'Orbital Simulator', command = openOrbit)
btn1.pack(pady = 50)
btn2.pack(pady = 25)
btn3.pack(pady = 50)
root.title('Physics Simulator')
root.geometry('500x500')

root.mainloop()


