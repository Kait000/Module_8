class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin, car_number):
        self.model = model
        self.__vin = None
        self.__numbers = None

        try:    # блок try повторяется для каждого нового объекта, вынес его в класс
            if self.__is_valid_vin(vin):
                self.__vin = vin
            if self.__is_valid_numbers(car_number):
                self.__numbers = car_number
        except IncorrectVinNumber as exc:
            print(exc.message)
        except IncorrectCarNumbers as exc:
            print(exc.message)
        else:
            print(f'{self.model} успешно создан')

    def __is_valid_vin(self, vin):
        if not isinstance(vin, int):
            raise IncorrectVinNumber('Некорректный тип для vin номера')
        if 1000000 <= vin <= 9999999:
            return True
        else:
            raise IncorrectVinNumber('Неверный диапазон vin номера')

    def __is_valid_numbers(self, car_number):
        if not isinstance(car_number, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номера')
        if len(car_number) == 6:
            return True
        else:
            raise IncorrectCarNumbers('Неверная длина номера')


first = Car('Model1', 1000000, 'f123dj')
second = Car('Model2', 300, 'т001тр')
third = Car('Model3', 2020202, 'нет номера')
