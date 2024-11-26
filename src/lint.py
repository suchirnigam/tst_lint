# example.py

"""
This is an example Python script that adheres to PEP 8 and passes pylint without errors.
"""

import math

def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle given its radius.
    
    Parameters:
    radius (float): The radius of the circle.
    
    Returns:
    float: The area of the circle.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

def main():
    """
    Main function to execute the circle area calculation.
    """
    try:
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_area(radius)
        print(f"The area of the circle with radius {radius} is: {area:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
