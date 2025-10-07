#Set B: The Text and Number Analyzer

#1
def is_palindrome(word):
    word = word.lower().replace(" " ,"")
    return word == word[::-1]

#2
def get_grade(grade):
    if grade >= 90 and grade <= 100:
        return "Your Grade is : A (90-100)"
    elif grade >= 80 and grade <= 89:
        return "Your Grade is : B (80-89)"
    elif grade >= 70 and grade <= 79:
        return "Your Grade is : C (70-79)"
    elif grade >= 60 and grade <= 69:
        return "Your Grade is : D (60-69)"
    else:
        return "Your Grade is : F (<60)"
    
#3
def multiply_all(*args):
    count = 1
    for num in args:
        count *= num
    return count
        
#4
def print_formatted_info(title, **kwargs):
    print("\n" + title.upper())
    for key, value in kwargs.items():
        print(f"{key}: {value}")
            

def menu():
    while True:
        print("\nLaboratory Activity 1: ")
        print("1. Basic Function")
        print("2. Return Statement")
        print("3. *args Practice")
        print("4. **kwargs Practice")
        print("5. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            word = input("Enter a Word: ")
            print("Is Palindrome?", is_palindrome(word))

        elif choice == "2":
            grade = float(input("Enter a Grade (0–100): "))
            print(get_grade(grade))

        elif choice == "3":
            num = input("Enter numbers separated by space: ")
            numbers = [float(n) for n in num.split()]
            print("Product of numbers:", multiply_all(*numbers))

        elif choice == "4":
            title = input("Enter a title: ")
            print("Enter key-value pairs:")
            data = {}
            while True:
                key = input("Key: ")
                if not key:
                    break
                value = input("Value: ")
                data[key] = value
            print_formatted_info(title, **data)

        elif choice == "5":
            break

        else:
            print("Invalid Input. Try again!")


if __name__ == "__main__":
    menu()
    
    
    