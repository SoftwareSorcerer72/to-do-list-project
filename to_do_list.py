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

