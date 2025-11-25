# Simple Python Code for computing the volume of a Sphere
# Formula: Volume = (4/3) * π * r^3

import math

# Function to calculate the volume of a sphere
def volume(rad):
    vol = (4/3) * math.pi * rad ** 3
    return vol

# Function to prompt user for input and display the volume
# This only runs if you execute sphere.py directly
def prompt():
    print()
    print("-----------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND VOLUME OF A SPHERE")
    print("-----------------------------------------------------------")
    radius = float(input("Please Enter the radius : "))
    print("\nThe Volume of a Sphere = ", volume(radius))

if __name__ == '__main__':
    prompt()