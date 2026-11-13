def sum_of_squares(numbers):
    return sum(number ** 2 for number in numbers)

def filter_above_threshold(numbers, threshold):
    return [number for number in numbers if number > threshold]

def remove_duplicate_records(records):
    unique = []
    seen = set()
    for record in records:
        key = tuple(sorted(record.items()))
        if key not in seen:
            seen.add(key)
            unique.append(record)
    return unique

def clean_temperature_records(records, minimum=-10, maximum=55):
    cleaned = []
    seen = set()
    for row in records:
        try:
            temperature = float(row["temperature_c"])
        except (KeyError, TypeError, ValueError):
            continue
        if not minimum <= temperature <= maximum:
            continue
        normalized = dict(row)
        normalized["temperature_c"] = temperature
        key = tuple(sorted(normalized.items()))
        if key not in seen:
            seen.add(key)
            cleaned.append(normalized)
    return cleaned

def recursive_sum(numbers):
    if not numbers:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])

def main():
    temperatures = [29, 30, 28, 31, 27]
    fixed_coordinates = (13.08, 80.27)
    city_reading = {"city": "Chennai", "temperature_c": 29}
    unique_cities = {"Chennai", "Bengaluru", "Mumbai", "Chennai"}
    fahrenheit = [round((t * 9 / 5) + 32, 1) for t in temperatures]
    sorted_temperatures = sorted(temperatures, key=lambda value: value)

    print("List:", temperatures)
    print("Tuple:", fixed_coordinates)
    print("Dictionary:", city_reading)
    print("Set (unique cities):", unique_cities)
    print("Fahrenheit values:", fahrenheit)
    print("Sorted values using lambda:", sorted_temperatures)
    print("Sum of squares:", sum_of_squares(temperatures))
    print("Values above 29°C:", filter_above_threshold(temperatures, 29))
    print("Recursive sum:", recursive_sum(temperatures))

    sample_records = [
        {"city": "Chennai", "temperature_c": 29},
        {"city": "Chennai", "temperature_c": 29},
        {"city": "Bengaluru", "temperature_c": None},
        {"city": "Mumbai", "temperature_c": 28},
        {"city": "Example", "temperature_c": 90},
    ]
    print("De-duplicated records:", remove_duplicate_records(sample_records))
    print("Cleaned records:", clean_temperature_records(sample_records))

if __name__ == "__main__":
    main()
