def convert_length(value, from_unit, to_unit):
    units = {
        "m": 1.0, "km": 1000.0, "cm": 0.01, "mm": 0.001,
        "mile": 1609.34, "yard": 0.9144, "foot": 0.3048, "inch": 0.0254
    }
    if from_unit not in units or to_unit not in units:
        raise ValueError("Unsupported length unit.")
    return value * units[from_unit] / units[to_unit]
def convert_weight(value, from_unit, to_unit):
    units = {
        "kg": 1.0, "g": 0.001, "mg": 0.000001, "lb": 0.453592, "oz": 0.0283495
    }
    if from_unit not in units or to_unit not in units:
        raise ValueError("Unsupported weight unit.")
    return value * units[from_unit] / units[to_unit]
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "c":
        return value * 9/5 + 32 if to_unit == "f" else value + 273.15
    elif from_unit == "f":
        return (value - 32) * 5/9 if to_unit == "c" else (value - 32) * 5/9 + 273.15
    elif from_unit == "k":
        return value - 273.15 if to_unit == "c" else (value - 273.15) * 9/5 + 32
    else:
        raise ValueError("Unsupported temperature unit.")
def convert_volume(value, from_unit, to_unit):
    units = {
        "l": 1.0, "ml": 0.001, "gallon": 3.78541, "cup": 0.24
    }
    if from_unit not in units or to_unit not in units:
        raise ValueError("Unsupported volume unit.")
    return value * units[from_unit] / units[to_unit]
def convert_speed(value, from_unit, to_unit):
    units = {
        "m/s": 1.0, "km/h": 0.277778, "mph": 0.44704
    }
    if from_unit not in units or to_unit not in units:
        raise ValueError("Unsupported speed unit.")
    return value * units[from_unit] / units[to_unit]
def convert_pressure(value, from_unit, to_unit):
    units = {
        "pa": 1.0, "bar": 100000, "atm": 101325, "psi": 6894.76
    }
    if from_unit not in units or to_unit not in units:
        raise ValueError("Unsupported pressure unit.")
    return value * units[from_unit] / units[to_unit]
def unit_converter():
    print("\n Welcome to the Ultimate Unit Converter ")
    print("Categories: length, weight, temperature, volume, speed, pressure")
    while True:
        try:
            category = input("\nEnter category (or 'exit' to quit): ").strip().lower()
            if category == 'exit':
                print("Goodbye, Ajay!")
                break
            value = float(input("Enter value to convert: "))
            from_unit = input("From unit: ").strip().lower()
            to_unit = input("To unit: ").strip().lower()
            if category == "length":
                result = convert_length(value, from_unit, to_unit)
            elif category == "weight":
                result = convert_weight(value, from_unit, to_unit)
            elif category == "temperature":
                result = convert_temperature(value, from_unit, to_unit)
            elif category == "volume":
                result = convert_volume(value, from_unit, to_unit)
            elif category == "speed":
                result = convert_speed(value, from_unit, to_unit)
            elif category == "pressure":
                result = convert_pressure(value, from_unit, to_unit)
            else:
                raise ValueError("Unsupported category.")
            print(f" Result: {value} {from_unit} = {round(result, 5)} {to_unit}")

        except ValueError as e:
            print(f" Error: {e}")
        except Exception as e:
            print(f" Unexpected error: {e}")
unit_converter()
