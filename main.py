print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose option: ")
temp = float(input("Enter temperature: "))

if choice == "1":
    result = (temp * 9/5) + 32
    print("Fahrenheit:", result)
elif choice == "2":
    result = (temp - 32) * 5/9
    print("Celsius:", result)
else:
    print("Invalid choice.")
