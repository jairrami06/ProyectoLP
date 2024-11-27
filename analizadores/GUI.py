import tkinter as tk
from tkinter import scrolledtext, messagebox
from analizador_lexico import analizar_tokens  # Función de análisis léxico ya definida
from analizador_sintactico import test_parser  # Función de análisis sintáctico ya definida
from analizador_lexico import resultados_lexico  # Importamos el array resultados_lexico
from analizador_sintactico import resultados_sintactico  # Importamos el array resultados_sintactico
from analizador_sintactico import  resultados_semantico

def analizar_codigo(input_text, result_text):
    # Vaciar las listas de resultados antes de iniciar el análisis
    resultados_lexico.clear()  # Limpiar la lista de resultados léxicos
    resultados_sintactico.clear()  # Limpiar la lista de resultados sintácticos
    resultados_semantico.clear()  # Limpiar la lista de resultados semánticos

    # Obtener el código del área de texto
    codigo = input_text.get("1.0", tk.END).strip()

    if not codigo:
        messagebox.showwarning("Entrada Vacía", "Por favor, ingresa código antes de analizar.")
        return

    resultados = []

    # Análisis léxico: Llamar a la función analizar_tokens
    try:
        resultados.append("=== Análisis Léxico ===")
        analizar_tokens(codigo)  # Llamamos a la función de análisis léxico
        for tok in resultados_lexico:  # Iterar sobre el array resultados_lexico
            resultados.append(str(tok))  # Agregar los tokens al resultado
    except Exception as e:
        resultados.append(f"Error en el análisis léxico: {e}")

    # Análisis sintáctico: Llamar a test_parser
    try:
        resultados.append("\n=== Análisis Sintáctico ===")
        test_parser(codigo)  # Llamamos a test_parser para obtener los resultados del análisis sintáctico

        # Agregar los resultados sintácticos (que se almacenan en la lista resultados_sintactico)
        if len(resultados_sintactico) > 0:
            for error in resultados_sintactico:  # Agregar los errores sintácticos
                resultados.append(str(error))
        else:
            resultados.append("No syntax errors detected.")
    except Exception as e:
        resultados.append(f"Error en el análisis sintáctico: {e}")

    # Análisis semántico: Agregar los resultados semánticos
    try:
        resultados.append("\n=== Análisis Semántico ===")
        if len(resultados_semantico) > 0:
            for sem_error in resultados_semantico:  # Agregar los errores semánticos
                resultados.append(str(sem_error))
        else:
            resultados.append("No semantic errors detected.")
    except Exception as e:
        resultados.append(f"Error en el análisis semántico: {e}")

    # Mostrar los resultados en el área de resultados
    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)  # Limpiar el área de resultados
    result_text.insert(tk.END, "\n".join(resultados))  # Insertar los resultados
    result_text.config(state="disabled")

def crear_interfaz():
    root = tk.Tk()
    root.title("Analizador Léxico y Sintáctico de Dart")

    # Área de texto para ingresar el código
    input_label = tk.Label(root, text="Ingresa el código en Dart:")
    input_label.pack(pady=5)

    input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15)
    input_text.pack(padx=10, pady=5)

    # Botón para analizar el código
    analyze_button = tk.Button(root, text="Analizar Código", command=lambda: (
        resultados_lexico.clear(),  # Limpiar la lista de resultados léxicos
        resultados_sintactico.clear(),  # Limpiar la lista de resultados sintácticos
        resultados_semantico.clear(),  # Limpiar la lista de resultados semánticos
        analizar_codigo(input_text, result_text)  # Llamar a la función de análisis
    ))
    analyze_button.pack(pady=10)

    # Área para mostrar resultados
    result_label = tk.Label(root, text="Resultados del Análisis:")
    result_label.pack(pady=5)

    result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15, state="disabled")
    result_text.pack(padx=10, pady=5)

    root.mainloop()


# Inicializar la aplicación
if __name__ == "__main__":
    crear_interfaz()
