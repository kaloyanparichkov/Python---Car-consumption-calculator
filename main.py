from models import CarConsumptionCalculator


def read_positive_float(message):
    """Чете положително число от потребителя."""
    while True:
        try:
            value = float(input(message).replace(",", "."))
            if value <= 0:
                print("Моля, въведете положително число.")
            else:
                return value
        except ValueError:
            print("Невалидна стойност. Моля, въведете число.")


def show_menu():
    """Показва основното меню."""
    print("\n=== Калкулатор за разход на автомобил ===")
    print("1. Изчисли разход и цена за автомобил на гориво")
    print("2. Изчисли разход и цена за електрически автомобил")
    print("3. Сравни автомобил на гориво и електрически автомобил")
    print("4. Изход")


def calculate_fuel_trip(calculator):
    distance = read_positive_float("Въведете разстояние в км: ")
    calculator.set_distance(distance)

    fuel_consumption = read_positive_float("Въведете среден разход на гориво (л/100 км): ")
    fuel_price = read_positive_float("Въведете цена на горивото (евро/литър): ")

    fuel_needed = calculator.calculate_fuel_needed(fuel_consumption)
    fuel_cost = calculator.calculate_fuel_cost(fuel_consumption, fuel_price)

    print("\n--- Резултат ---")
    print(f"Разстояние: {distance:.2f} км")
    print(f"Необходимо гориво: {fuel_needed:.2f} литра")
    print(f"Цена на пътуването: {fuel_cost:.2f} евро")


def calculate_electric_trip(calculator):
    distance = read_positive_float("Въведете разстояние в км: ")
    calculator.set_distance(distance)

    electricity_consumption = read_positive_float("Въведете среден разход на електроенергия (kWh/100 км): ")
    electricity_price = read_positive_float("Въведете цена на електроенергията (евро/kWh): ")

    electricity_needed = calculator.calculate_electricity_needed(electricity_consumption)
    electricity_cost = calculator.calculate_electricity_cost(electricity_consumption, electricity_price)

    print("\n--- Резултат ---")
    print(f"Разстояние: {distance:.2f} км")
    print(f"Необходима електроенергия: {electricity_needed:.2f} kWh")
    print(f"Цена на пътуването: {electricity_cost:.2f} евро")


def compare_fuel_and_electric(calculator):
    distance = read_positive_float("Въведете разстояние в км: ")
    calculator.set_distance(distance)

    fuel_consumption = read_positive_float("Въведете среден разход на гориво (л/100 км): ")
    fuel_price = read_positive_float("Въведете цена на горивото (евро/литър): ")

    electricity_consumption = read_positive_float("Въведете среден разход на електроенергия (kWh/100 км): ")
    electricity_price = read_positive_float("Въведете цена на електроенергията (евро/kWh): ")

    result = calculator.compare_trips(
        fuel_consumption,
        fuel_price,
        electricity_consumption,
        electricity_price,
    )

    print("\n--- Сравнение ---")
    print(f"Разстояние: {result['distance_km']:.2f} км")
    print("\nАвтомобил на гориво:")
    print(f"Необходимо гориво: {result['fuel_needed']:.2f} литра")
    print(f"Цена: {result['fuel_cost']:.2f} евро")

    print("\nЕлектрически автомобил:")
    print(f"Необходима електроенергия: {result['electricity_needed']:.2f} kWh")
    print(f"Цена: {result['electricity_cost']:.2f} евро")

    print("\nИзвод:")
    print(result["cheaper_option"])
    print(f"Разлика в цената: {result['difference']:.2f} евро")


def main():
    calculator = CarConsumptionCalculator()

    while True:
        show_menu()
        choice = input("Изберете опция: ")

        if choice == "1":
            calculate_fuel_trip(calculator)
        elif choice == "2":
            calculate_electric_trip(calculator)
        elif choice == "3":
            compare_fuel_and_electric(calculator)
        elif choice == "4":
            print("Край на програмата.")
            break
        else:
            print("Невалидна опция. Моля, опитайте отново.")


if __name__ == "__main__":
    main()
