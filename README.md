# Camino-de-Hormigas
Este proyecto implementa una simulación básica de hormigas en Python, donde las hormigas buscan comida y dejan un rastro de feromonas para guiar a otras hormigas hacia la comida y al hormiguero.

## Funcionalidades

- Las hormigas se mueven aleatoriamente por un área cuadrada.
- Las hormigas dejan feromonas en su camino hacia la comida.
- Las feromonas se evaporan con el tiempo.
- Las hormigas no siguen directamente las feromonas, pero son atraídas por áreas con feromonas más intensas.
- Las hormigas comienzan su búsqueda desde un punto central (el hormiguero).
- Se pueden distribuir varias fuentes de comida en el área.

## Requisitos

- Python 3.x
- Matplotlib (para visualización)

## Uso

1. Ejecutar el script `Hormigas.py`

2. Para cerrar el programa solamente cerrar la ventana de simulación

## Parámetros personalizables

- `grid_size`: Tamaño del área cuadrada en la que se mueven las hormigas.
- `num_food_sources`: Número de fuentes de comida distribuidas en el área.
- `evaporation_rate`: Tasa de evaporación de las feromonas.
- `num_iterations`: Número de iteraciones (pasos de tiempo) en la simulación.
- `num_ants`: Número de hormigas en la simulación.

Estos parámetros se pueden ajustar en el script `Hormigas.py` según las necesidades de la simulación.