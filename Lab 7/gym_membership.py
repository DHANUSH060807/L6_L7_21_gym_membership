def parse_plan(code):
    try:
        if not isinstance(code, str):
            return None

        parts = code.split("-")
        if len(parts) != 2:
            return None

        plan, months = parts

        if not plan.strip():
            return None

        months = int(months)
        if months <= 0:
            return None

        return plan.strip().upper(), months

    except (ValueError, TypeError):
        return None


def calculate_bmi(data):
    try:
        if not isinstance(data, str):
            return None

        parts = data.split(",")
        if len(parts) != 2:
            return None

        weight, height = parts
        weight = float(weight)
        height = float(height)

        if weight <= 0 or height <= 0:
            return None

        return round(weight / (height ** 2), 1)

    except (ValueError, TypeError, ZeroDivisionError):
        return None


def average_workout(minutes):
    try:
        if not isinstance(minutes, str) or not minutes.strip():
            return None

        values = [int(m) for m in minutes.split()]

        if not values or any(value < 0 for value in values):
            return None

        return sum(values) // len(values)

    except (ValueError, TypeError):
        return None


def main():
    print("==== Running parse_plan ====")
    user_input = input("Enter a plan code (e.g. GOLD-12): ")
    result = parse_plan(user_input)
    print("Plan and Months:", result)

    print("\n==== Running calculate_bmi ====")
    user_input = input("Enter weight and height (e.g. 70,1.75): ")
    result = calculate_bmi(user_input)
    print("BMI:", result)

    print("\n==== Running average_workout ====")
    user_input = input("Enter workout minutes separated by spaces (e.g. 45 60 30): ")
    result = average_workout(user_input)
    print("Average Minutes:", result)


if __name__ == "__main__":
    main()