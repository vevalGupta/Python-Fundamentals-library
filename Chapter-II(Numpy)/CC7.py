import os;os.system('cls')
# Reshaping and manipulating the array
import numpy as n
"""
The first state-- change nd array to nd array
(without interrupting data)
"""
Re = n.array([1,5,34,2,4,24])
#sh=Re.reshape(2,3)
print(Re.reshape(2,3))
"""
Seecond State-- Flatterning array
2M -.ravel()  --> show the view of change in orginal array
   -.flatten() --> change in copy of array
"""
Fl =n.array([[12,32,21],[25,15,20]])
print(Fl.ravel())
print(Fl.flatten())
