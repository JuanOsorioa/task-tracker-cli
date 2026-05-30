# Importamos las funciones desde tu módulo de almacenamiento
from storage import save_tasks, load_tasks

# 1. Creamos una lista con datos ficticios (de prueba) que simulen ser tareas
tareas_de_prueba = [
    {
        "id": 1,
        "description": "Aprender a usar json.dump",
        "status": "done",
        "createdAt": "2026-05-30T12:00:00",
        "updatedAt": "2026-05-30T12:30:00"
    },
    {
        "id": 2,
        "description": "Probar la persistencia de datos",
        "status": "in-progress",
        "createdAt": "2026-05-30T15:00:00",
        "updatedAt": "2026-05-30T15:00:00"
    }
]

print("--- EJECUTANDO PRUEBA DE ESCRITURA ---")

# 2. Ejecutamos tu función pasándole la lista de prueba
save_tasks(tareas_de_prueba)
print("Se ha ejecutado guardar_todas_las_tareas().")

# 3. Comprobación cruzada: Intentamos leer el archivo usando tu función de carga
print("\n--- REVERIFICANDO LECTURA DEL ARCHIVO ---")
tareas_cargadas = load_tasks()

if tareas_cargadas == tareas_de_prueba:
    print("¡ÉXITO! Las tareas se guardaron y se recuperaron exactamente igual.")
else:
    print("❌ ALGO FALLÓ. Los datos guardados no coinciden con los recuperados.")