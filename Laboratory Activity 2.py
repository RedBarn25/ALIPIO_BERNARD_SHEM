#Set B: The Log File Parser

#1
def parse_log(log):
    parts = log.split()
    log_level = parts[0]
    message = "".join(parts[0])
    return log_level, message

#2
def format_log_summary(log_level, message):
    return "[{}] -> {}" , format(log_level, message)

#3
def find_all_emails(text):
    return[word for word in text.split() if "@" in word]

#4
def convert_to_title_case(s):
    return s.replace("_", " ").title()


def menu():
    while True:
        print("Laboratory Activity 2: ")
        print("1. Parse and Formatting: ")
        print("2. Validation & Search: ")
        print("3. Complex Manipulation: ")
        print("4. Exit ")
        choice = input("Enter Your Choice: ")
        
        
        if choice == "1":
            log = input("Enter The Log: ")
            if len(log.split()) >= 5:
                level, message = parse_log(log)
                print(format_log_summary(level, message))
            else:
                print("Invalid log format. Try: 'ERROR 2024-10-06 14:35:01 Database connection failed'")

        elif choice == "2":
            text = input("Enter text: ")
            emails = find_all_emails(text)
            print("Emails found:", emails)

        elif choice == "3":
            snake_str = input("Enter snake_case string: ")
            print("Converted:", convert_to_title_case(snake_str))

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")
        
if __name__ == "__menu__":
    menu()
    