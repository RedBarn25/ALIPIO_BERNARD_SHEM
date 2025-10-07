# Set B: The Log File Parser

#1 Slicing & Methods
def parse_log(log):
    parts = log.split()
    log_level = parts[0] if len(parts) > 0 else "UNKNOWN"
    message = " ".join(parts[3:]) if len(parts) > 3 else "No message found"
    return log_level, message


#2 Formatting
def format_log_summary(log_level, message):
    return "[{}] -> {}".format(log_level, message)


#3 Validation & Search
def find_all_emails(text):
    return [word for word in text.split() if "@" in word]


#4 Complex Manipulation
def convert_to_title_case(s):
    return s.replace("_", " ").title()


# Main Menu
def menu():
    while True:
        print("\nLaboratory Activity 2: ")
        print("1. Slicing & Methods")
        print("2. Formatting")
        print("3. Validation & Search")
        print("4. Complex Manipulation")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            log = input("Enter log line (ex. 'ERROR 2024-10-06 14:35:01 Database connection failed'): ")
            log_level, message = parse_log(log)
            print("Log Level:", log_level)
            print("Message:", message)

        elif choice == "2":
            log = input("Enter log line (ex. 'ERROR 2024-10-06 14:35:01 Database connection failed'): ")
            log_level, message = parse_log(log)
            print(format_log_summary(log_level, message))

        elif choice == "3":
            text = input("Enter text: ")
            emails = find_all_emails(text)
            if emails:
                print("Emails found:", ", ".join(emails))
            else:
                print("No emails found.")

        elif choice == "4":
            underscores_word = input("Enter String with Underscores (ex. 'customer_account_id'): ")
            print("Converted:", convert_to_title_case(underscores_word))

        elif choice == "5":
            break

        else:
            print("Invalid Input. Try again!")


if __name__ == "__main__":
    menu()
