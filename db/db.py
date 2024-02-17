


class DB:
    parking_space_to_car_mapping = dict()
    car_to_parking_space_mapping = dict()


    @staticmethod
    def get_parking_space_by_registration_number(registration_number):
        return DB.parking_space_to_car_mapping.get(registration_number, None)

    @staticmethod
    def get_car_by_parking_space(sequence_number):
        return DB.car_to_parking_space_mapping.get(sequence_number, None)

    @staticmethod
    def mark_parking_space(sequence_number, registration_number):
        DB.parking_space_to_car_mapping[registration_number] = sequence_number
        DB.car_to_parking_space_mapping[sequence_number] = registration_number

    @staticmethod
    def mark_parking_space_empty(sequence_number, registration_number):
        if registration_number in DB.parking_space_to_car_mapping:
            del DB.parking_space_to_car_mapping[registration_number]
        if sequence_number in DB.car_to_parking_space_mapping:
            del DB.car_to_parking_space_mapping[sequence_number]

    @staticmethod
    def get_empty_spaces():
        return [i for i in range(1, 101) if i not in DB.car_to_parking_space_mapping]


