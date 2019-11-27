#!/usr/bin/python3
#############################################################
## USBCAMERA GUI
## Contents (SKIP TO LINE)
## Line :Window Properties
## Line :Labels
## Line :Inputs
## Line :Displays
## Line :Function Commands
## Line :Buttons 
#############################################################

#############################################################
## IMPORTS
#############################################################

import tkinter as tk
import fcntl

#############################################################
#Window Properties
#############################################################
WindowBox = tk.Tk()
WindowBox.geometry("500x500")
WindowBox.title("USB Camera")
#############################################################

#############################################################
# Coords Variables (Xs, Ys)
#############################################################

#Default Label Coords
L_Xpos  = 25
L_Ypos  = 27

#Default Input BOX Coords
In_Xpos = 200
In_Ypos = 25

#Default Display Coords
D_Xpos  = 275
D_Ypos  = 27
#############################################################

#############################################################
#Variables:
#############################################################

CHANGEFLAG = 0x00

ScaleFactor  = tk.StringVar()  
minNeighbors = tk.StringVar()
minSize      = tk.StringVar()
#############################################################

#############################################################
#Labels:
#############################################################
#Scale Factor(X.X)
L_SclFct = tk.Label(WindowBox, text = "Scale Factor:" )
L_SclFct.place(x = L_Xpos, y =L_Ypos)

#minNeighbors
L_minNeighbors = tk.Label(WindowBox, text = "Minimal Neighbors:")
L_minNeighbors.place(x = L_Xpos , y = 2*L_Ypos)

#minSize
L_minSize = tk.Label(WindowBox, text = "Minimal Size:")
L_minSize.place(x = L_Xpos , y = 3*L_Ypos)
#############################################################


#############################################################
#Inputs:
#############################################################
#Scale Factor(X.X)
In_SclFct = tk.Entry(WindowBox, bd = 2, width = 5)
In_SclFct.place(x = In_Xpos, y = In_Ypos)

#minNeighbors(X)
In_minNeighbors = tk.Entry(WindowBox, bd = 2, width = 5)
In_minNeighbors.place(x = In_Xpos, y = 2*L_Ypos)

#minSize(X,Y)
In_minSize = tk.Entry(WindowBox, bd = 2, width = 5)
In_minSize.place(x = In_Xpos, y = 3*L_Ypos)
#############################################################

#############################################################
#
#Displays:
#
#############################################################

#############################################################
#WINDOW DISPLAY OBJECTS
#############################################################
#Scale Factor
D_SclFct = tk.Label(WindowBox, text = "0.0", relief = tk.RAISED, width = 5, textvariable = ScaleFactor )
D_SclFct.place(x = D_Xpos, y = D_Ypos)

#minNeighbors
D_minNeighbors = tk.Label(WindowBox, text = "0", relief = tk.RAISED, width = 5, textvariable = minNeighbors)
D_minNeighbors.place(x = D_Xpos, y = 2*D_Ypos)

#minSize
D_minSize = tk.Label(WindowBox, text = "0", relief = tk.RAISED, width = 5, textvariable = minSize)
D_minSize.place(x = D_Xpos, y = 3*D_Ypos)
#############################################################

#############################################################
#
#Interaction Layer
#
#############################################################
#Confidence Level?

#Faces (UNIQUE) Detected

#Frames Taken

#Current FPS

#############################################################
#
#Function Commands
#
#############################################################

#Text Change
def Change():
	if (In_SclFct.get() != ""):
		ScaleFactor.set(In_SclFct.get())	
		In_SclFct.delete(0, tk.END)	
		
	if (In_minNeighbors.get() != ""):	
		minNeighbors.set(In_minNeighbors.get())
		In_minNeighbors.delete(0, tk.END)	

	if (In_minSize.get() != ""):
		minSize.set(In_minSize.get())
		In_minSize.delete(0, tk.END)
	Output()

#Output to file

def Output():
	ParameterFile = open('Test', 'w')
#	fcntl.flock(ParameterFile, fcntl.LOCK_EX | fcntl.LOCK_NB)
	ParameterFile.write(ScaleFactor.get())
	ParameterFile.write('\n')
	ParameterFile.write(minNeighbors.get())
	ParameterFile.write('\n')
	ParameterFile.write(minSize.get())
	ParameterFile.write('\n')
#	fcntl.flock(ParameterFile, fcntl.LOCK_UN)
	ParameterFile.close()
#############################################################

#############################################################
#
#Buttons:
#
#############################################################
#Set Button
button = tk.Button(WindowBox, text='set', bd = 5, command=Change)
button.place(x = 25, y = 200)


WindowBox.mainloop()




