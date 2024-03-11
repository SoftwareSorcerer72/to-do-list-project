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

def run_program():
    run_program = '0'
    while run_program != '5':
        run_program = input('Welcome to the Task Manager. What would you like to do?\n\t To add a task type 1\n\t To remove a task type 2\n\t To update a task completion status type 3\n\t To view all tasks type 4\n\t To exit type 5\n')
        while not run_program.isdigit() or int(run_program) not in range(1, 6):
            run_program = input('Please enter a valid number between 1 and 5')

        if run_program == '1':
            description = input('Enter the description of the task you wish to add: ')
            todo_list.add_task(Task(description))
            print('I\'ve updated your tasks: ')
            todo_list.show_tasks()

        elif run_program == '2':
            id = int(input('Enter the ID of the task to remove: '))
            while id not in todo_list.tasks:
                id = int(input('Please enter a valid task ID to remove: '))
            todo_list.remove_task(id)
            print('I\'ve updated your tasks: ')
            todo_list.show_tasks()

        elif run_program == '3':
            id = int(input('Enter the ID of the task to update completion status: '))
            while id not in todo_list.tasks:
                id = int(input('Please enter a valid task ID to update: '))
            todo_list.update_task(id)
            print('I\'ve updated your tasks: ')
            todo_list.show_tasks()

        elif run_program == '4':
            print('Here are all your tasks: ')
            todo_list.show_tasks()

    print('Thank you for using the Task Manager. Here are all your tasks: ')
    todo_list.show_tasks()

run_program()