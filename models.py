class CarConsumptionCalculator:
    """Клас за изчисляване на разход и цена на пътуване с автомобил."""

    def __init__(self, distance_km=0):
        self.distance_km = distance_km

    def set_distance(self, distance_km):
        """Записва разстоянието за пътуването."""
        if distance_km <= 0:
            raise ValueError("Разстоянието трябва да бъде положително число.")
        self.distance_km = distance_km

    def calculate_fuel_needed(self, fuel_consumption_l_per_100km):
        """Изчислява нужните литри гориво за зададеното разстояние."""
        if fuel_consumption_l_per_100km <= 0:
            raise ValueError("Разходът на гориво трябва да бъде положително число.")
        return self.distance_km * fuel_consumption_l_per_100km / 100

    def calculate_electricity_needed(self, electricity_consumption_kwh_per_100km):
        """Изчислява нужната електроенергия в kWh за зададеното разстояние."""
        if electricity_consumption_kwh_per_100km <= 0:
            raise ValueError("Разходът на електроенергия трябва да бъде положително число.")
        return self.distance_km * electricity_consumption_kwh_per_100km / 100

    def calculate_fuel_cost(self, fuel_consumption_l_per_100km, fuel_price_per_liter):
        """Изчислява цената на пътуване с автомобил на гориво."""
        if fuel_price_per_liter <= 0:
            raise ValueError("Цената на горивото трябва да бъде положително число.")
        fuel_needed = self.calculate_fuel_needed(fuel_consumption_l_per_100km)
        return fuel_needed * fuel_price_per_liter

    def calculate_electricity_cost(self, electricity_consumption_kwh_per_100km, electricity_price_per_kwh):
        """Изчислява цената на пътуване с електрически автомобил."""
        if electricity_price_per_kwh <= 0:
            raise ValueError("Цената на електроенергията трябва да бъде положително число.")
        electricity_needed = self.calculate_electricity_needed(electricity_consumption_kwh_per_100km)
        return electricity_needed * electricity_price_per_kwh

    def compare_trips(
        self,
        fuel_consumption_l_per_100km,
        fuel_price_per_liter,
        electricity_consumption_kwh_per_100km,
        electricity_price_per_kwh,
    ):
        """Сравнява цена на пътуване с автомобил на гориво и електрически автомобил."""
        fuel_needed = self.calculate_fuel_needed(fuel_consumption_l_per_100km)
        fuel_cost = self.calculate_fuel_cost(fuel_consumption_l_per_100km, fuel_price_per_liter)

        electricity_needed = self.calculate_electricity_needed(electricity_consumption_kwh_per_100km)
        electricity_cost = self.calculate_electricity_cost(
            electricity_consumption_kwh_per_100km,
            electricity_price_per_kwh,
        )

        difference = abs(fuel_cost - electricity_cost)

        if fuel_cost < electricity_cost:
            cheaper_option = "Автомобилът на гориво е по-евтин за това пътуване."
        elif electricity_cost < fuel_cost:
            cheaper_option = "Електрическият автомобил е по-евтин за това пътуване."
        else:
            cheaper_option = "Двата варианта имат еднаква цена за това пътуване."

        return {
            "distance_km": self.distance_km,
            "fuel_needed": fuel_needed,
            "fuel_cost": fuel_cost,
            "electricity_needed": electricity_needed,
            "electricity_cost": electricity_cost,
            "difference": difference,
            "cheaper_option": cheaper_option,
        }
