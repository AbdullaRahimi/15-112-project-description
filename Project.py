#Name: Abdulla Rahimi
#AndrewID : arahimi

from math import sin, cos, radians, sqrt
from tkinter import messagebox
import tkinter
#drawing panel is a library found on github that makes it easy to plot to a window
from drawingpanel import *
import random

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
            panel.canvas.create_oval(x, 300 - y, x + 5, 305 - y, fill='black', outline='black')
            panel.sleep(dt * 100)

        messagebox.showinfo('Data', 'Time of flight is ' + str(round(totalTime, 2)) + '\n'
                                    + 'The final velocity is ' + str(round(finalV, 2)))
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
            messagebox.showerror('invalid input', 'please input a value for v greater than 0')
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
            messagebox.showerror('invalid input', 'please input a value for a between 0 and 90')
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
    btn = tkinter.Button(projectile, text = 'Start Simulation', command = startProjectile)
    velocitylabel = tkinter.Label(projectile, text = 'Initial Velocity')
    velocitylabel.place(x = 150, y = 130)
    global ivelocity
    #user enters initial velocity
    ivelocity = tkinter.Entry(projectile, width = 20)
    ivelocity.place(x = 150, y = 150)
    ivelocityset = tkinter.Button(projectile, text = 'set', width = 5, command = initialV)
    ivelocityset.place(x = 255, y = 148)
    anglelabel = tkinter.Label(projectile, text = 'Initial Angle')
    anglelabel.place(x = 150, y = 180)
    global iangle
    #user enters angle of launch
    iangle = tkinter.Entry(projectile, width = 20)
    iangle.place(x = 150, y = 200)
    iangleset = tkinter.Button(projectile, text = 'set', width = 5, command = initialA)
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
            messagebox.showerror('invalid input', 'please enter a value for T1 greater than -273')
            temperatureEntry.delete(0,'end')

    if str(T1) in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        messagebox.showerror('invalid input', 'please enter a number for the value of T1')
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
                pressureLabel = tkinter.Label(self.mainFrame, text = 'The pressure on the container is '
                                                              + str(round(self.pressure,2)) + ' torr')
                pressureLabel.pack()

                #user chooses the concentration level which determines how
                #many particles are in the container
                if concentration == '5':
                    for i in range(200):
                        self.Particles.append(Particle(random.randint(0,440),random.randint(0,440)))
                        for part in self.Particles:
                            part.draw(self.canv)
                    self.mainFrame.after(50,self.moveParticle)

                if concentration == '4':
                    for i in range(150):
                        self.Particles.append(Particle(random.randint(0,440),random.randint(0,440)))
                        for part in self.Particles:
                            part.draw(self.canv)
                    self.mainFrame.after(50,self.moveParticle)

                if concentration == '3':
                    for i in range(100):
                        self.Particles.append(Particle(random.randint(0,440),random.randint(0,440)))
                        for part in self.Particles:
                            part.draw(self.canv)
                    self.mainFrame.after(50,self.moveParticle)

                if concentration == '2':
                    for i in range(50):
                        self.Particles.append(Particle(random.randint(0,440),random.randint(0,440)))
                        for part in self.Particles:
                            part.draw(self.canv)
                    self.mainFrame.after(50,self.moveParticle)

                if concentration == '1':
                    for i in range(10):
                        self.Particles.append(Particle(random.randint(0,440),random.randint(0,440)))
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
    

                ########main screen########
    
root = tkinter.Tk()

mainFrame = tkinter.Frame()
mainFrame.pack()
canvas1 = tkinter.Canvas(mainFrame)
#buttons for each simulator
btn1 = tkinter.Button(mainFrame, text = 'Projectile Motion', command = openProjectile)
btn2 = tkinter.Button(mainFrame, text = 'Pressure Simulator', command = openPressure)
frame1 = tkinter.Frame(canvas1)
canvas1.pack()
frame1.pack()
btn1.pack(pady = 150)
btn2.pack()
root.title('Physics Simulator')
root.geometry('500x500')

root.mainloop()

