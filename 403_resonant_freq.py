import math 
#pip install inquirer
#import inquirer

#For series and parallel
C = float(input("Enter capacitance value: "))
L = float(input("Enter inductance value: "))
w_res = 1 / (2* math.pi * math.sqrt(C * L))
print("Resonant frequency: " + str(w_res) + "Hz")

#For parallel (frequency which voltage and current are in phase)
rl = float(input("Resistor value in series with inductor: "))
rc = float(input("Resistor value in series with capacitor: "))
w0 = w_res * math.sqrt((rl**2 * C - L)/(rc**2 * C - L))
print("Resonant frequency: " + str(w0) + "rad/s")

#For parallel (max total impedance)
#Source: https://core.ac.uk/download/pdf/216844612.pdf
if rl > 0 and rc == 0:
    Q = math.sqrt(L/C) / rl
    max_z = rl * math.sqrt(Q**2 * (1 + Q**2))
    print("Resonant frequency: " + str(max_z) + "rad/s")
else:
    print("Resonant frequency general case")