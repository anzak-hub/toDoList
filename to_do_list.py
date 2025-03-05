class toDoList:
    def __init__(self):
        self.to_do_list = []

    def addTask(self, file_name=""):
        task = input("Enter a task = ").strip()
        if task:
            self.to_do_list.append(task)

            #write the task to a file
            if file_name:
                self.writeTaskToFile(task, file_name)

    def writeTaskToFile(self, task, file_name):
        # Append the task to the file
        with open(file_name, 'a') as file:
            file.write(task + "\n")

    
if __name__ == "__main__":
    to_do_list = toDoList()
    file_name = "to_do_list.txt"

    while True:
        print("Possible activities")
        print("1 to add a task")
        print("2 to quit")
        try:
            choice = int(input("Enter the number of the activity = ").strip())
        except (ValueError, TypeError):
            pass
        else:
            if choice > 2:
                choice = 2
            elif choice < 1:
                choice = 1
            if choice == 2: # End of the program
                break
            
            if choice == 1:
                to_do_list.addTask(file_named)
