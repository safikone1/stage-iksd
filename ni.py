def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print("1. Conversion de Celsius en Fahrenheit")
print("2. Conversion de Fahrenheit en Celsius")
choice = int(input("Choisissez une option (1 ou 2): "))

if choice == 1:
    celsius = float(input("Entrez une température en Celsius : "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print("La température en Fahrenheit est :", fahrenheit)
elif choice == 2:
    fahrenheit = float(input("Entrez une température en Fahrenheit : "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print("La température en Celsius est :", celsius)
else:
    print("Choix invalide. Veuillez choisir 1 ou 2.")
