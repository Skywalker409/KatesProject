import os
import subprocess
import time
#Red:  pigs p 17 255
#Green pigs p 22 255
#Blue  pigs p 24 255

def Red(value):
    subprocess.run(["pigs", "p", "24", str(value)])

def Green(value):
    subprocess.run(["pigs", "p", "23", str(value)])

def Blue(value):
    subprocess.run(["pigs", "p", "25", str(value)])

def RGB(R, G,B):
    Red(R)
    Green(G)
    Blue(B)

subprocess.run(["sudo", "pigpiod"])
RGB(255,0,0)

