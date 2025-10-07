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
        count += num
        return count
        
#4
def print_formatted_info(title, **kwargs):
    print(title.upper())
    for key, value in kwargs.items():
        print(f"{key}: {value}")
            

def menu():
    while True:
        print("Laboratory Activity 1: ")
        print("1. Basic Function: ")
        print("2. Return Statement: ")
        print("3. *args Practice: ")
        print("4. **kwargs Practice: ")
        print("5. Exit ")
        choice = input("Enter Your Choice: ")
        
        
        if choice == "1":
            word = input("Enter a Word: ")
            print("Is_Palindrome?", is_palindrome())
                
        elif choice == "2":
            grade = input("Enter a Grade: ")
            print("Your Grade Is: ", get_grade())
            
        elif choice == "3":
            num = input("Enter Numbers: ")
            print("Any Numbers Is: ", multiply_all(*num))
                
        elif choice == "4":
            print("Enter key-value pairs:")
            data = {}
            title = input("Enter a title: ")
            print_formatted_info(title, **data)
                
        elif choice == "5":
            print("Exit Program")
            break
        
        else:
            print("Invalid choice. Try again.")
        
if __name__ == "__menu__":
    menu()
    
    
    