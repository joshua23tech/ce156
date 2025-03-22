import numpy as np

student_dtype = np.dtype([
    ('reg_number', 'i4'),    
    ('exam_mark', 'f4'),     
    ('coursework_mark', 'f4'), 
    ('overall_mark', 'f4'),  
    ('grade', 'U10')         
])

def calculate_grade(overall_mark):
    """Assign grade based on overall mark."""
    if overall_mark >= 70:
        return 'First Class'
    elif overall_mark >= 60:
        return 'Second Class Upper'
    elif overall_mark >= 50:
        return 'Second Class Lower'
    elif overall_mark >= 40:
        return 'Third Class'
    else:
        return 'Fail'

def process_file(file_name):
    """Process the student data from the given file."""
    
    try:
        with open(file_name, 'r') as f:
            num_students, coursework_percentage = map(int, f.readline().split())
            
            student_data = np.zeros((num_students, 4), dtype=np.float64)  
            
            for i in range(num_students):
                data = list(map(float, f.readline().split()))
                reg_number = int(data[0])
                exam_mark = data[1]
                coursework_mark = data[2]
                
                overall_mark = (exam_mark * (100 - coursework_percentage) / 100) + (coursework_mark * coursework_percentage / 100)
                
                student_data[i] = [reg_number, exam_mark, coursework_mark, overall_mark]
            
            student_results = np.zeros(num_students, dtype=student_dtype)
            
            for i in range(num_students):
                reg_number = student_data[i, 0]
                exam_mark = student_data[i, 1]
                coursework_mark = student_data[i, 2]
                overall_mark = round(student_data[i, 3])
                grade = calculate_grade(overall_mark)
                
                student_results[i] = (reg_number, exam_mark, coursework_mark, overall_mark, grade)
            
            student_results.sort(order='overall_mark')
            
            output_file = input("Enter the output file name: ")
            with open(output_file, 'w') as out_f:
                print(student_results, file=out_f)
            
            first_class = np.sum(student_results['grade'] == 'First Class')
            second_class_upper = np.sum(student_results['grade'] == 'Second Class Upper')
            second_class_lower = np.sum(student_results['grade'] == 'Second Class Lower')
            third_class = np.sum(student_results['grade'] == 'Third Class')
            fail_count = np.sum(student_results['grade'] == 'Fail')
            failed_students = student_results[student_results['grade'] == 'Fail']['reg_number']
            
            print(f"\nNumber of students in each category:")
            print(f"First Class: {first_class}")
            print(f"Second Class Upper: {second_class_upper}")
            print(f"Second Class Lower: {second_class_lower}")
            print(f"Third Class: {third_class}")
            print(f"Failed: {fail_count}")
            
            print(f"\nRegistration numbers of failing students:")
            print(failed_students)
    
    except FileNotFoundError:
        print(f"Error: File {file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_name = input("Enter the input file name: ")
    process_file(file_name)

if __name__ == "__main__":
    main()
