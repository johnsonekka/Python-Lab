class Rectangle: 
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display_info(self):
        print(f"Rectangle: Length = {self.length}, Width = {self.width}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

if __name__ == "__main__":
    # Convert input to float to handle decimals
    length = float(input("Enter the length of rectangle: "))
    width = float(input("Enter the width of rectangle: "))

    # Create rectangle object
    rect1 = Rectangle(length, width)

    print("\nRectangle 1: ")
    rect1.display_info()

    # Create a second rectangle for demonstration
    # print("\nRectangle 2: ")
    # rect2 = Rectangle(5.5, 3.2)  # Example values
    # rect2.display_info()

    # Display individual properties
    print(f"\nArea of rect1: {rect1.area()}")
    # print(f"Perimeter of rect2: {rect2.perimeter()}")