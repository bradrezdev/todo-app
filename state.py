import json

class TodoListBackend:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, task_text):
        """Agregar nueva tarea"""
        if task_text:
            task_data = {
                "text": task_text,
                "completed": False
            }
            self.tasks.append(task_data)
            self.save_tasks()
            return True
        return False

    def toggle_task_by_index(self, task_index):
        """Marcar/desmarcar tarea como completada"""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = not self.tasks[task_index]["completed"]
            self.save_tasks()
            return True
        return False

    def delete_task_by_index(self, task_index):
        """Eliminar tarea por índice"""
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
            self.save_tasks()
            return True
        return False

    def get_stats(self):
        """Obtener estadísticas de tareas"""
        total_count = len(self.tasks)
        done_count = sum(1 for task in self.tasks if task["completed"])
        pending_count = total_count - done_count
        
        if total_count == 0:
            percentage = 0
        else:
            percentage = (done_count / total_count) * 100
            
        return {
            "total": total_count,
            "completed": done_count,
            "pending": pending_count,
            "percentage": percentage
        }

    def get_all_tasks(self):
        """Obtener todas las tareas"""
        return self.tasks.copy()

    def load_tasks(self):
        """Cargar tareas desde archivo JSON"""
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        """Guardar tareas en archivo JSON"""
        tasks_data = []
        for task in self.tasks:
            tasks_data.append({
                "text": task["text"],
                "completed": task["completed"]
            })
        with open("tasks.json", "w") as file:
            json.dump(tasks_data, file, indent=2)