import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk # Theme descargado.
from state import TodoListBackend

# Configurar appearance mode y theme.
ctk.set_appearance_mode("system")  # Modes: "System" (standard), "Dark", "Light".
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue".

class TodoListApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("📝 To-Do App")
        self.geometry("900x700")
        
        # Instancia del backend.
        self.backend = TodoListBackend()
        
        # Crear la interfaz
        self.create_widgets()
        
        # Cargar tareas guardadas al iniciar.
        self.refresh_ui()

    def create_widgets(self):
        # Título
        title_label = ctk.CTkLabel(self, text="📝 Lista de Tareas", 
                                  font=ctk.CTkFont(size=20, weight="bold"))
        title_label.pack(pady=(20, 10))
        
        # Frame invisible para input y botón en la misma fila.
        input_row = ctk.CTkFrame(self, fg_color="transparent")
        input_row.pack(pady=10, padx=20, fill="x")
        
        # Input para nueva tarea.
        self.task_input = ctk.CTkEntry(
            input_row,
            height=40,
            placeholder_text="Crea una nueva tarea...",
            font=ctk.CTkFont(size=12)
        )
        self.task_input.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        # Evento para el input. Puedes hacer "Enter" para agregar la tarea.
        self.task_input.bind("<Return>", lambda e: self.add_task())

        # Botón para agregar tarea.
        self.add_button = ctk.CTkButton(
            input_row, 
            text="+  Agregar",
            command=self.add_task,
            width=100,
            height=40,
            fg_color="#6a1893",
            hover_color="#5a1081",
            font=ctk.CTkFont(size=12, weight="bold")
        )
        self.add_button.pack(side="right")
        
        # Sección de tareas pendientes
        pending_title = ctk.CTkLabel(self, text="📋 Tareas Pendientes", 
                                   font=ctk.CTkFont(size=16, weight="bold"))
        pending_title.pack(pady=(10, 5))
        
        # Lista de tareas pendientes
        self.task_list_frame = ctk.CTkScrollableFrame(self, height=180)
        self.task_list_frame.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        # Sección de tareas terminadas
        completed_title = ctk.CTkLabel(self, text="✅ Tareas Terminadas", 
                                     font=ctk.CTkFont(size=16, weight="bold"))
        completed_title.pack(pady=(10, 5))
        
        # Lista de tareas terminadas
        self.completed_task_list_frame = ctk.CTkScrollableFrame(self, height=180)
        self.completed_task_list_frame.pack(fill="both", expand=True, padx=20, pady=(0, 10))
        
        # Label para información.
        self.info_label = ctk.CTkLabel(self, font=ctk.CTkFont(size=12))
        self.info_label.pack(pady=(0, 10))

    def create_task_buttons(self, task_frame, task_index, is_completed=False):
        """Crear botones consistentes para marcar como completada y eliminar"""
        if is_completed:
            # Botón para desmarcar como completada (regresar a pendientes)
            uncheck_button = ctk.CTkButton(
                task_frame,
                text="↶",
                width=30,
                height=30,
                fg_color="#f39c12",
                hover_color="#d68910",
                command=lambda idx=task_index: self.toggle_task_by_index(idx)
            )
            uncheck_button.pack(side="right", padx=5, pady=5)
        else:
            # Botón para marcar como completada
            check_button = ctk.CTkButton(
                task_frame,
                text="✓",
                width=30,
                height=30,
                fg_color="#27ae60",
                hover_color="#1e8449",
                command=lambda idx=task_index: self.toggle_task_by_index(idx)
            )
            check_button.pack(side="right", padx=5, pady=5)
        
        # Botón para eliminar (disponible para ambas secciones)
        delete_button = ctk.CTkButton(
            task_frame,
            text="✗",
            width=30,
            height=30,
            fg_color="#ed3030",
            hover_color="#ae2222",
            command=lambda idx=task_index: self.delete_task_by_index(idx)
        )
        delete_button.pack(side="right", padx=5, pady=5)

    def add_task(self):
        task = self.task_input.get()
        if self.backend.add_task(task):
            # Limpiar input
            self.task_input.delete(0, tk.END)
            self.refresh_ui()

    def toggle_task_by_index(self, task_index):
        if self.backend.toggle_task_by_index(task_index):
            self.refresh_ui()

    def delete_task_by_index(self, task_index):
        tasks = self.backend.get_all_tasks()
        if 0 <= task_index < len(tasks):
            task_data = tasks[task_index]
            if messagebox.askyesno("Confirmar", f"¿Estás seguro de que quieres eliminar la tarea:\n'{task_data['text']}'?"):
                if self.backend.delete_task_by_index(task_index):
                    self.refresh_ui()

    def refresh_ui(self):
        """Actualizar toda la interfaz con los datos del backend"""
        # Limpiar ambas vistas actuales
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()
        for widget in self.completed_task_list_frame.winfo_children():
            widget.destroy()
        
        # Obtener tareas del backend
        tasks = self.backend.get_all_tasks()
        
        # Separar tareas por estado
        pending_tasks = []
        completed_tasks = []
        
        for task_index, task_data in enumerate(tasks):
            if task_data["completed"]:
                completed_tasks.append((task_index, task_data))
            else:
                pending_tasks.append((task_index, task_data))
        
        # Crear tareas pendientes
        for task_index, task_data in pending_tasks:
            self.create_task_item(self.task_list_frame, task_index, task_data, is_completed=False)
        
        # Crear tareas completadas
        for task_index, task_data in completed_tasks:
            self.create_task_item(self.completed_task_list_frame, task_index, task_data, is_completed=True)
        
        self.update_info_label()

    def create_task_item(self, parent_frame, task_index, task_data, is_completed=False):
        """Crear un elemento de tarea en el frame especificado"""
        # Crear frame para la tarea
        task_frame = ctk.CTkFrame(parent_frame)
        task_frame.pack(fill="x", padx=5, pady=2)
        
        # Label con el texto de la tarea
        task_label = ctk.CTkLabel(
            task_frame, 
            text=task_data["text"], 
            font=ctk.CTkFont(size=12),
            anchor="w"
        )
        task_label.pack(side="left", fill="x", expand=True, padx=10, pady=5)
        
        # Crear botones usando función helper
        self.create_task_buttons(task_frame, task_index, is_completed)
        
        # Aplicar estilo según el estado
        if is_completed:
            task_label.configure(text_color="#27ae60")
            task_frame.configure(fg_color="#1a4d2e")

    def update_info_label(self):
        stats = self.backend.get_stats()
        if stats["total"] == 0:
            self.info_label.configure(text="No hay tareas. ¡Agrega tu primera tarea!")
        else:
            self.info_label.configure(text=f"📊 Total: {stats['total']} | ⏳ Pendientes: {stats['pending']} | ✅ Completadas: {stats['completed']} | 📈 {stats['percentage']:.1f}%")

    

if __name__ == "__main__":
    app = TodoListApp()
    app.mainloop()