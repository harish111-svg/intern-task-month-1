def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
def calculator():
    print("\nCalculator")
    a = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ").strip()
    b = float(input("Enter second number: "))
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        if b == 0:
            print("Error: division by zero is not allowed.")
            return
        result = a / b
    else:
        print("Invalid operator.")
        return
    print("Result:", result)

def average_temperature():
    raw = input("\nEnter temperatures in Celsius separated by commas: ")
    try:
        values = [float(value.strip()) for value in raw.split(",") if value.strip()]
        if not values:
            print("No temperatures were entered.")
            return
        print(f"Average temperature: {sum(values) / len(values):.2f} °C")
    except ValueError:
        print("Please enter numeric temperatures separated by commas.")

def main():

    intern_name = "Data Science Intern"  
    sample_count = 3                     
    example_temperature = 25.5           
    is_learning = True                   
    print("Python Basics Demonstration")
    print(intern_name, sample_count, example_temperature, is_learning)
    print("25°C in Fahrenheit:", celsius_to_fahrenheit(example_temperature))

    
    if example_temperature >= 30:
        print("Weather category: Hot")
    elif example_temperature >= 20:
        print("Weather category: Moderate")
    else:
        print("Weather category: Cool")

    
    print("Counting with for loop:")
    for number in range(1, 4):
        print(number)

    
    print("Counting with while loop:")
    counter = 1
    while counter <= 3:
        print(counter)
        counter += 1

    calculator()
    average_temperature()

if __name__ == "__main__":
    main()
