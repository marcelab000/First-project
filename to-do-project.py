
# Basic (for now) to do app, using file manipulation.
import os

def view_tasks():
          try:
            with open("to-do-file.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                     if "done" in line:
                          print(line.strip()) 
                     else:
                          print(line.strip() + " - pending")         
          except FileNotFoundError:
             print("No tasks yet!")

          input("\nPress Enter to see menu...")

def add_task():
    task = input("Add to do task: ").strip()
    with open("to-do-file.txt", "a") as f:
        f.writelines(task + "\n")

def view_undone_tasks():
     try:
          with open("to-do-file.txt", "r") as f:
               lines = f.readlines()
               for line in lines:
                    if "done" not in line:
                         print(line.strip() + "- pending")
                    else:
                         print(line.strip())
     except FileNotFoundError:
          print("No tasks yet!")

     input("\nPress enter to see menu")

def mark_task():
        with open("to-do-file.txt", "r") as f:
             lines = f.readlines()
             for index, line in enumerate(lines):
                  if "done" in line:
                    print(f"{index + 1}.{line.strip()}")
                  else:
                       print(f"{index + 1}.{line.strip()}" + " - pending")

    
        choice = int(input(("Enter a number of a task you want to mark as done: ")))
        
        if 1 <= choice <= len(lines):
             lines[choice -1] = lines[choice -1].strip() + " - done\n"

        with open("to-do-file.txt", "w") as f: #Saving changes
             f.writelines(lines)


def remove_task():
     with open("to-do-file.txt", "r") as f:
          lines = f.readlines()

     for index, line in enumerate(lines):
               print(f"{index + 1}. {line.strip()}")
               
     choice = int(input("Enter a number of a task you want to remove: "))
     lines.pop(choice -1)

     with open("to-do-file.txt", "w") as f: #Saving changes
               f.writelines(lines)
          
def menu():

    while True:
        print("Welcome and see your options below!")
        print("-----MENU-----")
        print("1. View all tasks")
        print("2. Add a task")
        print("3. View undone tasks")
        print("4. Mark task as done")
        print("5. Remove a task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
             view_tasks()
        elif choice == "2":
             add_task()
        elif choice == "3":
             view_undone_tasks()
        elif choice == "4":
             mark_task()
        elif choice == "5":
             remove_task()
        elif choice =="6":
             exit()
        else:
             print("Wrong input! Please enter an integer 1-6")

menu()