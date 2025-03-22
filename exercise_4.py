def filter_employees_by_salary(employee_list, salary1, salary2):
    min_salary = min(salary1, salary2)
    max_salary = max(salary1, salary2)
    
    filtered_employees = [emp for emp in employee_list if min_salary <= emp[2] <= max_salary]
    
    if not filtered_employees:
        print("No employees found within this salary range.")
        return

    filtered_employees.sort(key=lambda emp: emp[2], reverse=True)

    print(f"\n{'Name':<20}{'Job Title':<20}{'Salary':<10}")
    print('-' * 50)
    for emp in filtered_employees:
        print(f"{emp[0]:<20}{emp[1]:<20}{emp[2]:<10}")
    
def load_employee_data_from_file():
    while True:
        file_name = input("Enter the file name: ")
        try:
            with open(file_name, 'r') as file:
                employee_list = []
                for line in file:
                    name, job_title, salary = line.strip().split(',')
                    salary = int(salary)  
                    employee_list.append((name, job_title, salary))
                return employee_list
        except FileNotFoundError:
            print("File not found. Please try again.")
        except ValueError:
            print("File format is incorrect. Please ensure the data is correctly formatted.")

def main():
    employee_list = load_employee_data_from_file()

    print("\nEmployee List (for verification):")
    print(employee_list)

    while True:
        try:
            salary1 = int(input("\nEnter the first salary value: "))
            salary2 = int(input("Enter the second salary value: "))

            if salary1 < 0 or salary2 < 0:
                print("Salary values must be non-negative. Please try again.")
                continue

            filter_employees_by_salary(employee_list, salary1, salary2)

        except ValueError:
            print("Invalid input. Please enter numeric salary values.")

        again = input("\nDo you want to enter another salary range? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
