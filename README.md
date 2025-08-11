# 📝 To-Do List App

Una aplicación de lista de tareas moderna y elegante construida con Python y CustomTkinter.

## ✨ Características

- ✅ **Agregar tareas** - Crea nuevas tareas fácilmente
- 🔄 **Marcar como completadas** - Organiza tus tareas por estado
- 📋 **Secciones separadas** - Tareas pendientes y completadas
- 🗑️ **Eliminar tareas** - Remueve tareas que ya no necesites
- 📊 **Estadísticas** - Ve tu progreso en tiempo real
- 💾 **Persistencia** - Tus tareas se guardan automáticamente
- 🎨 **Interfaz moderna** - Diseño limpio con CustomTkinter

## 📸 Vista Previa

```
📝 Lista de Tareas
┌─────────────────────────────────────┐
│ Crea una nueva tarea...    [+ Agregar] │
├─────────────────────────────────────┤
│ 📋 Tareas Pendientes               │
│ ┌─ Estudiar Python        [✓] [✗] │
│ ├─ Hacer ejercicio        [✓] [✗] │
│ └─ Leer libro            [✓] [✗] │
├─────────────────────────────────────┤
│ ✅ Tareas Terminadas               │
│ ┌─ Completar proyecto     [↶] [✗] │
│ └─ Revisar código        [↶] [✗] │
├─────────────────────────────────────┤
│        [Estatus de tareas]          │
│ 📊 Total: 5 | ⏳ Pendientes: 3 | ✅ Completadas: 2 | 📈 40.0% │
└─────────────────────────────────────┘
```

## 🚀 Instalación

### Prerrequisitos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Configuración

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/bradrezdev/todo-app.git
   cd todo-app
   ```

2. **Crea un entorno virtual:**
   ```bash
   python -m venv tkinter_todolist
   ```

3. **Activa el entorno virtual:**
   
   **En macOS/Linux:**
   ```bash
   source tkinter_todolist/bin/activate
   ```
   
   **En Windows:**
   ```bash
   tkinter_todolist\Scripts\activate
   ```

4. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ Uso

### Ejecutar la aplicación

```bash
python main.py
```

O usar el script de ejecución:

```bash
./run.sh
```

### Funcionalidades principales

- **➕ Agregar tarea**: Escribe en el campo de texto y presiona Enter o haz clic en "Agregar"
- **✅ Completar tarea**: Haz clic en el botón verde "✓" para marcar como completada
- **↶ Descompletar tarea**: Haz clic en el botón naranja "↶" para regresar a pendientes
- **🗑️ Eliminar tarea**: Haz clic en el botón rojo "✗" para eliminar permanentemente
- **📊 Ver estadísticas**: Haz clic en "Estatus de tareas" para ver un resumen detallado

## 🏗️ Estructura del Proyecto

```
📁 todo-list-app/
├── 📄 main.py              # Interfaz de usuario (Frontend)
├── 📄 state.py             # Lógica de datos (Backend)
├── 📄 requirements.txt     # Dependencias del proyecto
├── 📄 run.sh              # Script de ejecución
├── 📄 tasks.json          # Almacenamiento de tareas (generado automáticamente)
├── 📄 README.md           # Documentación
└── 📁 tkinter_todolist/   # Entorno virtual
```

## 🛠️ Tecnologías Utilizadas

- **Python 3.x** - Lenguaje de programación principal
- **CustomTkinter** - Framework de interfaz gráfica moderna
- **JSON** - Almacenamiento de datos local
- **Tkinter** - Base del sistema de ventanas

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Bryan Núñez** - [b.nunez@hotmail.es](mailto:b.nunez@hotmail.es)

Enlace del proyecto: [https://github.com/bradrezdev/todo-app](https://github.com/bradrezdev/todo-app)

---

⭐ ¡Dale una estrella al proyecto si te gustó!