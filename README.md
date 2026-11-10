# Juego del Ahorcado (Hangman)

Implementación en Python de un juego del Ahorcado basado en consola. El jugador debe adivinar letra por letra una palabra o frase oculta seleccionada aleatoriamente desde un archivo de texto, antes de alcanzar el límite máximo de intentos fallidos.

---

## Reglas del Juego

1. El jugador debe adivinar la palabra oculta ingresando **una letra por turno**.
2. Solo se aceptan caracteres alfabéticos individuales como entrada válida (sin números, símbolos ni letras repetidas).
3. Cada intento incorrecto incrementa el contador de errores.
4. El jugador pierde la partida al alcanzar **6 intentos incorrectos**.
5. El jugador gana si logra descubrir todas las letras de la palabra antes de agotar sus intentos.
6. Después de cada intento se muestra el estado actual de la palabra, las letras acertadas, las letras incorrectas y los intentos restantes.
7. Los caracteres que no son letras (como espacios o guiones `-`) se revelan automáticamente desde el inicio y no descuentan intentos.

---

## Estructura de Archivos

```text
hangman_project/
│
├── main.py         # Punto de entrada y bucle principal del juego
├── game.py         # Clase HangmanGame (estado y lógica del juego)
├── utils.py        # Funciones auxiliares (carga de palabras y estado en consola)
├── wordlist.txt    # Lista de palabras y frases candidatas (una por línea)
└── README.md       # Instrucciones y descripción del juego
```

### Función de cada componente

- **`main.py`**: Gestiona la interacción con el usuario a través de la consola (`get_valid_letter`) y controla el ciclo de vida de la partida (`main`) hasta que se cumple la condición de victoria o derrota.
- **`game.py`**: Define la clase `HangmanGame`, que encapsula el estado del juego (`word`, `guessed_letters`, `wrong_letters`, `errors`, `max_errors`) y provee los métodos `process_guess()`, `display_progress()`, `is_won()` e `is_lost()`.
- **`utils.py`**: Contiene las funciones de soporte `get_random_word()` (lectura y filtrado de palabras desde `wordlist.txt`) y `show_status()` (impresión formateada del progreso en cada turno).
- **`wordlist.txt`**: Archivo de texto plano con el banco de palabras y frases disponibles para jugar.

---

## Cómo Ejecutar el Juego

Requisitos: **Python 3.x** instalado.

Desde la carpeta `hangman_project/`:

```bash
cd hangman_project
python main.py
```

O directamente desde la raíz del repositorio:

```bash
python hangman_project/main.py
```
