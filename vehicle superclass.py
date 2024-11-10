# Define the Vehicle superclass
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Define the Automobile subclass inheriting from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Function to get user input and create an Automobile object
def main():
    print("Please enter the details of your car:")

    # Vehicle type is set to "car" as per the requirements
    vehicle_type = "car"
    
    # Collect other automobile details from the user
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car (e.g., Toyota): ")
    model = input("Enter the model of the car (e.g., Corolla): ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    # Create an Automobile object
    car = Automobile(vehicle_type, year, make, model, doors, roof)

    # Display the collected information
    print("\nCar Details:")
    print(f"  Vehicle type: {car.vehicle_type}")
    print(f"  Year: {car.year}")
    print(f"  Make: {car.make}")
    print(f"  Model: {car.model}")
    print(f"  Number of doors: {car.doors}")
    print(f"  Type of roof: {car.roof}")

# Run the main function
if __name__ == "__main__":
    main()