import sys

if len(sys.argv) == 2:
    script_name = sys.argv[0]
    salary = float(sys.argv[1])
    print("User provided salary value:")
else:
    script_name = sys.argv[0]
    salary = 50000.0
    print("No input given - using default salary:")

bonus = salary * 0.10
total_salary = salary + bonus

print("\n--- Salary Details ---")
print("Script Name:", script_name)
print(f"Base Salary: ${salary:.2f}")
print(f"Bonus (10%): ${bonus:.2f}")
print(f"Total Salary: ${total_salary:.2f}")
