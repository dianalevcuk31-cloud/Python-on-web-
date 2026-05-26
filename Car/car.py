class Car:
    def __init__(self, brand, model, fuel):
        """
        Конструктор класса Car
        :param brand: марка автомобиля
        :param model: модель автомобиля
        :param fuel: начальный уровень топлива
        """
        self.brand = brand
        self.model = model
        self.fuel = fuel
        self.max_fuel = 60
        self.is_engine_on = False
    
    def start_engine(self):
        """Запуск двигателя"""
        if self.is_engine_on:
            return f"Двигатель уже запущен"
        self.is_engine_on = True
        return f"Двигатель запущен"
    
    def stop_engine(self):
        """Остановка двигателя"""
        if not self.is_engine_on:
            return f"Двигатель уже остановлен"
        self.is_engine_on = False
        return f"Двигатель остановлен"
    
    def refuel(self, amount):
        """
        Заправка автомобиля
        :param amount: количество топлива для заправки
        """
        if amount <= 0:
            return f"Количество топлива должно быть положительным числом"
        
        if self.fuel + amount > self.max_fuel:
            possible_amount = self.max_fuel - self.fuel
            if possible_amount <= 0:
                return f"Бак полон. Заправка невозможна"
            self.fuel = self.max_fuel
            return f"Бак заполнен до максимума. Добавлено {possible_amount} л топлива"
        
        self.fuel += amount
        return f"Заправлено {amount} л топлива. Текущий уровень: {self.fuel}/{self.max_fuel} л"
    
    def drive(self, fuel_consumption):
        """
        Поездка на автомобиле
        :param fuel_consumption: расход топлива за поездку
        """
        if not self.is_engine_on:
            return f"Невозможно ехать: двигатель выключен"
        
        if fuel_consumption <= 0:
            return f"Расход топлива должен быть положительным числом"
        
        if self.fuel < fuel_consumption:
            return f"Недостаточно топлива. Нужно {fuel_consumption} л, доступно {self.fuel} л"
        
        self.fuel -= fuel_consumption
        return f"Поездка завершена. Израсходовано {fuel_consumption} л топлива. Остаток: {self.fuel}/{self.max_fuel} л"
    
    def get_fuel_level(self):
        """Получение текущего уровня топлива"""
        return f"Уровень топлива: {self.fuel}/{self.max_fuel} л"
    
    def get_engine_status(self):
        """Получение статуса двигателя"""
        status = "включен" if self.is_engine_on else "выключен"
        return f"Двигатель {status}"
    
    def get_car_info(self):
        """Получение полной информации об автомобиле"""
        return f"{self.brand} {self.model}"


if __name__ == "__main__":
    my_car = Car("Toyota", "Camry", 30)
    
    print(f"Автомобиль: {my_car.get_car_info()}")
    print(my_car.get_fuel_level())
    print(my_car.get_engine_status())
    print()
    
    print("Попытка поехать с выключенным двигателем:")
    print(my_car.drive(10))
    print()
    
    print("Запуск двигателя:")
    print(my_car.start_engine())
    print()
    
    print("Попытка поехать с недостатком топлива:")
    print(my_car.drive(40))
    print()
    
    print("Заправка автомобиля:")
    print(my_car.refuel(20))
    print()
    

    print("Поездка:")
    print(my_car.drive(15))
    print()
    
    print("Состояние после поездки:")
    print(my_car.get_fuel_level())
    print(my_car.get_engine_status())
    print()
    
    print("Остановка двигателя:")
    print(my_car.stop_engine())
    print(my_car.get_engine_status())
    print()
    
    print("Попытка заправиться сверх максимума:")
    print(my_car.refuel(50))
    print(my_car.get_fuel_level())