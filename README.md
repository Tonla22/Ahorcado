# Ahorcado

Juego del ahorcado para la terminal, escrito en Python. En cada partida, el programa elige una palabra al azar y tenés hasta seis errores para adivinarla letra por letra.

## Cómo ejecutarlo

Necesitás Python 3. El juego usa la biblioteca estándar, así que no hace falta instalar paquetes adicionales.

```bash
git clone https://github.com/Tonla22/Ahorcado.git
cd Ahorcado/hangman_project
python main.py
```

Si tu sistema usa `python3`, ejecutá `python3 main.py`. Arrancá el juego desde la carpeta `hangman_project` porque el programa busca ahí el archivo `wordlist.txt`.

## Cómo jugar

1. Ingresá una letra y presioná Enter. El juego acepta mayúsculas y minúsculas.
2. Si acertás, se muestran todas las apariciones de la letra. Si errás, perdés un intento.
3. Las letras repetidas y las entradas inválidas se vuelven a pedir sin descontar intentos.
4. Ganás al revelar todas las letras. Si llegás a seis errores, el juego termina y muestra la palabra.

Durante la partida, la terminal muestra el progreso, las letras acertadas, las incorrectas y los intentos restantes.

## Archivos del proyecto

| Archivo | Función |
| --- | --- |
| `hangman_project/main.py` | Inicia la partida y valida las letras ingresadas. |
| `hangman_project/game.py` | Guarda el estado de la partida y determina si ganaste o perdiste. |
| `hangman_project/utils.py` | Elige una palabra al azar y muestra el estado de la partida. |
| `hangman_project/wordlist.txt` | Contiene la lista de palabras del juego. |

Para agregar palabras, editá `wordlist.txt` y escribí una por línea.
