class Task:
    id_counter = 1

    def __init__(self, description):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.description = description
        self.completed = False

    def display(self):
        status = "Completed" if self.completed else "Not Completed"
        print(f'Task ID: {self.id}, Description: {self.description}, Status: {status}')

class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task.id] = task

     def remove_task(self, id):
        if id in self.tasks:
            del self.tasks[id]

    def update_task(self, id):
        if id in self.tasks:
            self.tasks[id].completed = not self.tasks[id].completed

    def show_tasks(self):
        for id, task in self.tasks.items():
            task.display()

todo_list = ToDoList()