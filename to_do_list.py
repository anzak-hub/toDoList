class toDoItem:
    #contains a task with its priority
    def __init__(self, task, priority):
        self.task = task
        self.priority = priority

    def __repr__(self):
        if self.priority.upper() == "D":
            return f"{self.task} (Done)"
        return f"{self.task} (Priority: {self.priority})"

class toDoList:
    #contains a list of tasks

    #tasks priorities
    priorities = {"high" : "1",
                  "middle" : "2",
                  "low" : "3",
                  "done" : "D"}
    
    def __init__(self, file_name="to_do_list.txt"):
        self.to_do_list = []
        self.file_name = file_name
        self.getAllTasksFromFile()

    def addTask(self):
        #add a task with default priority low to a list.
        #append it to a file if file_name given

        task = input("Enter a task = ").strip()
        if task:
            #add a task with default priority low to a list.
            self.to_do_list.append(toDoItem(task, toDoList.priorities["low"]))

            #write the task to a file
            if self.file_name:
                self.writeTaskToFile(task, self.file_name)

    #def writeTaskToFile(self, task, file_name, priority=toDoList.priorities["low"]):
    def writeTaskToFile(self, task, priority=priorities["low"]):
        # Append the task to the file in the form:
        # "priority task"
        with open(self.file_name, 'a') as file:
            file.write(priority + " " + task + "\n")

    def writeAllTasksToFile(self):
        #rewrite all the tasks to the file in the form:
        # "priority task"
        with open(self.file_name, 'w') as file:
            for task in self.to_do_list:
                file.write(task.priority + " " + task.task + "\n")

    def getAllTasksFromFile(self):
        #read all the tasks from the file in the form:
        # "priority task"
        #into to_do_list
        with open(self.file_name, 'r') as file:
            self.to_do_list = [] #initialize to_do_list
            # Iterate over each task in the file
            for line in file:
            # Print the line or process it as needed
                line = line.strip()
                task = toDoItem(line[2:], line[0]) #create a task
                self.to_do_list.append(task)
            
    def sortTasks(self):
        #sort the tasks according to their priority
        self.to_do_list.sort(key=lambda x: x.priority)

    def readAllTasks(self):
        print("\nAll Tasks")
        for number, task in enumerate(self.to_do_list, 1):
            print(F"{number}. {task}")


    
if __name__ == "__main__":
    to_do_list = toDoList("to_do_list.txt")
    

    while True:
        print("Possible activities")
        print("1 to add a task")
        print("2 to mark a task as done")
        print("4 to read all the tasks")
        print("0 to quit")
        try:
            choice = int(input("Enter the number of the activity = ").strip())
        except (ValueError, TypeError):
            pass
        else:
            if choice > 4:
                choice = 4
            elif choice < 0:
                choice = 0
            if choice == 0: # End of the program
                break
            
            if choice == 1: #add task
                to_do_list.addTask()
            elif choice == 2: #mark as deleted
                for task in to_do_list.to_do_list:
                    print(task)
                    done = input("Enter 'D' or 'd' to mark the task as done or any other sign otherwise = ").strip()
                    if done and done.upper() == "D":
                        task.priority = "D"

                to_do_list.sortTasks()
                to_do_list.writeAllTasksToFile()
                #to_do_list.readAllTasks()
            elif choice == 4:
                to_do_list.readAllTasks()
            else:
                print("Enter a valid number of the activity")

