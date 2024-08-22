# Create a list of students
students = [
    {"name": "Kenyat", "hometown": "Philadelphia", "favorite_food": "halibut"},
    {"name": "John", "hometown": "Paris", "favorite_food": "fries"},
    {"name": "Max", "hometown": "New York", "favorite_food": "tacos"}
]


def list_names(student_list):
    """
   #Give a function that list all the names (iterate, enumerate, etc)converts a data collection object into an enumerate object
    """
    for index, student in enumerate(student_list):
        print(f"{index + 1}. {student['name']}")


def get_new_student():
    """
    Prompts the user for information about student and returns a dict
    """
    print("Please provide details for the new student.")
    name = input("Name: ").strip()
    hometown = input("Hometown: ").strip()
    favorite_food = input("Favorite Food: ").strip()

    return {
        "name": name,
        "hometown": hometown,
        "favorite_food": favorite_food
    }


def main():
    while True:
        # Main menu
        action = input(
            "Type 'add' to add a new student, 'view' to view existing students, or 'quit' to exit: ").lower()
        if action == "quit":
            print("Goodbye!")
            break

        elif action == "view":
            list_names(students)

            try:
                # Which student would you like to view
                student_index = int(input(f"Select a student number (1 to {len(students)}): ")) - 1

                if 0 <= student_index < len(students):
                    student = students[student_index]
                    print(f"Name: {student['name']}")

                    # What is the category?
                    category = input("Would you like to know their 'hometown' or 'favorite food'? ").strip().lower()

                    if category == "hometown":
                        print(f"Hometown: {student['hometown']}")

