import os
import subprocess
import time

# === GPIO Pin Mapping ===
# Red   = GPIO 24
# Green = GPIO 23
# Blue  = GPIO 25

def Red(value):
    subprocess.run(["pigs", "p", "24", str(value)])

def Green(value):
    subprocess.run(["pigs", "p", "23", str(value)])

def Blue(value):
    subprocess.run(["pigs", "p", "25", str(value)])

def RGB(R, G, B):
    Red(R)
    Green(G)
    Blue(B)

# === Restart pigpiod safely ===
# Kill existing pigpiod (if any)
subprocess.run(["sudo", "killall", "pigpiod"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Wait a bit to ensure it's fully stopped
time.sleep(0.5)

# Start pigpiod
subprocess.run(["sudo", "pigpiod"])

# Wait for pigpiod to initialize
time.sleep(0.5)

# Set RGB color to red
for value in range(0, 255, 5):
    RGB(0, {value}, {255-value})
    time.sleep(0.1)
