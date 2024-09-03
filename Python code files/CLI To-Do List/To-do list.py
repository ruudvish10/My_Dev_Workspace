#Task class
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False
        
    def mark_complete(self):
        self.completed = True
    
    def __repr__(self):
        return f"{self.description} {'[x]' if self.completed else '[ ]'}"
    

#To-Do List class
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.description = description
        self.tasks.append(Task(description))

    def complete_task(self, index):
        if 0 <= index < len(self.tasks) and not self.tasks[index].completed:
            desc_before_complete = self.tasks[index].description
            self.tasks[index].mark_complete()
            print(f"The task '{desc_before_complete}' has been marked completed.")
        elif 0 <= index < len(self.tasks) and self.tasks[index].completed:
            desc_after_complete = self.tasks[index].description
            print(f"The task '{desc_after_complete}' has already been marked completed!")
        else:
            print("Invalid task number! Please select a valid task number to complete.")
       
    def list_task(self):
        #Check if list is empty
        if not self.tasks:
            print("Oops! There are no items in the list! ")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
             
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            desc_before_delete = self.tasks[index].description
            del self.tasks[index]
            print(f"The task '{desc_before_delete}' has been deleted.") 
        else:
            print("Please select a valid task number to delete.")

    #File handling for persistence
    def file_save(self, filename):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.description} | {task.completed}\n")
        #See contents saved to file - this is optional
        """with open(filename, "r") as file:
            print("Contents of file: ")
            file_contents = file.read()
            print(file_contents)"""

    def file_load(self,filename):
        try:
            #Allocating an empty list to start a fresh list at load time
            self.tasks = []
            with open(filename, "r") as file:
                for line in file:
                    description, completed = [part.strip() for part in line.split("|")]
                    task = Task(description)
                    task.completed = (completed == "True")
                    self.tasks.append(task)
                print("Task list loaded!")
        except FileNotFoundError:
            print(f"The file '{filename}' does not exist!")
            
        
    #repr method to join the str representations and the list
    def __repr__(self):
        return "\n".join(repr(task) for task in self.tasks)

#Main function to run the program
def main():
    to_do_list = ToDoList()
    print("\nWelcome to the To-Do-List App! Here you can maintain a list of to-do items to manage your day-to-day activities.")
    while True:
        try:
            print("\nPlease choose a number from the following options: ")
            print("1. Add a new task")
            print("2. View tasks")
            print("3. Complete a task")
            print("4. Delete a task")
            print("5. Load from file")
            print("6. Save to file")
            print("7. Exit")
            option = int(input("$ "))

            if option == 7:
                print("You have chosen to exit the app! When you launch the app again, please load your tasks using the 'Load from file' option. Thank you for using the To-Do-List app.\n")
                break
            elif option == 1:
                description = input("Describe your new task: ").title()
                to_do_list.add_task(description)
                print(f"The task '{description}' has been added to your to-do list.")
            elif option == 2:
                print("Here are a list of your tasks and statuses:")
                to_do_list.list_task()
            elif option == 3:
                index = int(input("Please enter a task number to mark complete: ")) - 1
                to_do_list.complete_task(index)
            elif option == 4:
                index = int(input("Please enter a task number to delete: ")) - 1
                to_do_list.delete_task(index)
            elif option == 5:
                to_do_list.file_load("save.txt")
            elif option == 6:
                to_do_list.file_save("save.txt")
                print("Task list saved!")
            else:
                print("Invalid task number! Please enter a valid number.")
        except ValueError:
            print("An exception occured! Please enter a valid number.")
    
if __name__ == "__main__":
    main()










