# Function to calculate total marks
def calculate_total_marks(marks):
    return sum(marks)

# Function to calculate average marks
def calculate_average_marks(marks):
    return sum(marks) / len(marks)

# Function to calculate grade based on average marks
def calculate_grade(average_marks):
    if average_marks >= 90:
        return "A+"
    elif average_marks >= 80:
        return "A"
    elif average_marks >= 70:
        return "B"
    elif average_marks >= 60:
        return "C"
    elif average_marks >= 50:
        return "D"
    else:
        return "F"


def main():
    
    subjects = ['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4', 'Subject 5']
    marks = []
    for subject in subjects:
        mark = float(input(f"Enter marks for {subject}: "))
        marks.append(mark)
    
    
    total_marks = calculate_total_marks(marks)
    
    average_marks = calculate_average_marks(marks)
    
  
    grade = calculate_grade(average_marks)
    
    
    print("\n********** Marksheet **********")
    for i in range(len(subjects)):
        print(f"{subjects[i]}: {marks[i]}")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()