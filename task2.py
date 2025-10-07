print("My to-do list")

tasks = []

def todo_list():
    print("\nchoose an option")
    print("1-Add Task")
    print("2-show Tasks")
    print("3-Update Task")
    print("4-Delete Task")
    print("5-Exit")

def add():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added ")

def show():
    if len(tasks) == 0:
        print("No tasks found")
    else:
        print("\nMy Tasks:")
        for i in range(len(tasks)):
         print(f"{i+1}. {tasks[i]}")

def update():
    if len(tasks) == 0:
        print("No tasks to update")
    else:
        show()
        try:
            num = int(input("Enter task number to update: "))
            if 1 <= num <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[num-1] = new_task
                print("Task updated ")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

def delete():
    if len(tasks) == 0:
        print("No tasks to delete.")
    else:
        show()
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num-1)
                print(f"Task '{removed}' deleted successfully!")
            else:
                print("Invalid task number")
        except ValueError:
            print("Please enter a valid number")

def main():
   while True:
      todo_list ()
      choice = input("Enter your choice: ")
      if choice == '1':
            add()
      elif choice == '2':
            show()
      elif choice == '3':
         update()
      elif choice == '4':
            delete()
      elif choice == '5':
            print("Exiting To-Do List")
            break
      else:
            print(" Invalid choice ")


main()
