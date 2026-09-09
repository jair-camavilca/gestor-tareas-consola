# Aplicación de Gestión de Tareas (Consola)

[![SENATI](https://img.shields.io/badge/SENATI-00529B?style=for-the-badge)](https://www.senati.edu.pe/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

Sistema de gestión de tareas por consola desarrollado en Python, que implementa operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en memoria, control estricto de excepciones y validación de fechas límite mediante la librería estándar `datetime`.

---

### Funcionalidades

* **Crear tarea:** Solicita título, descripción y fecha límite, generando automáticamente el identificador (`id_tarea`), fecha de creación (`datetime.now()`) y estado inicial `"Pendiente"`.
* **Ver lista de tareas:** Muestra el reporte formateado en consola de todas las tareas registradas con sus campos (ID, Título, Descripción, Creación, Fecha límite y Estado).
* **Actualizar tarea:** Búsqueda por ID para modificar selectivamente título, descripción o estado (`Pendiente`, `En ejecución`, `Completado`).
* **Eliminar tarea:** Remoción de registros de la lista en memoria mediante coincidencia de ID.
* **Validación de entradas:** Control de excepciones con `try/except ValueError` para entradas no numéricas y validación de fechas en formato `dd-mm-aaaa` impidiendo registros con fechas anteriores a la actual.

---

### Tecnologías y Estructuras

| Componente | Detalle técnico |
| :--- | :--- |
| **Lenguaje** | Python 3 |
| **Módulos estándar** | `datetime` (`strptime`, `strftime`, `date()`) |
| **Estructuras de datos** | Listas y Diccionarios |
| **Control de flujo** | Bucles `while`, condicionales `if/elif/else` y manejo de excepciones con `try/except` |

---

### Ejecución

```bash
python main.py
```

---

### Contexto Académico
* **Curso:** Algoritmia para el Desarrollo de Programas con Python
