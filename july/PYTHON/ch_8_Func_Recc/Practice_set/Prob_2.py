def celsius_to_fahrenheit(c):
    f=c*9/5 + 32
    print(f"{c} Celsius is {f} Fahrenheit")

cel=int(input("Enter Celsius temperature: "))
celsius_to_fahrenheit(cel)