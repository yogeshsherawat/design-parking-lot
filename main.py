
from managers.parking_manager import ParkingManager

while True:
    input = input("Enter command:")
    if "park car" in input:
        registration_number = input.split(" ")[-1]
        parking_space_sequence_number = ParkingManager.park_car(registration_number)
        print(f"Car with registration number {registration_number} is parked at space {parking_space_sequence_number}")