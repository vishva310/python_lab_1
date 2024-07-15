def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate: "))
time = float(input("Enter the time period: "))


simple_interest = calculate_simple_interest(principal, rate, time)


print(f"\nPrincipal Amount: {principal}")
print(f"Annual Interest Rate: {rate}%")
print(f"Time Period: {time} years")
print(f"Simple Interest: {simple_interest:.2f}")