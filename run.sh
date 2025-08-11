#!/bin/bash
# Script para ejecutar la aplicación TodoList con Python 3.13

# Configurar entorno para silenciar warnings
export TK_SILENCE_DEPRECATION=1

# Cambiar al directorio del proyecto
cd "/Users/bradrez/Documents/Hybridge/Proyecto Tkinter"

# Activar entorno virtual y ejecutar
source tkinter_todolist/bin/activate
python main.py