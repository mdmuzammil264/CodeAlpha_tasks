# 🎮 Hangman Game

A feature-rich Python Hangman game with difficulty levels, a hint system, multiplayer mode, and a Tkinter GUI — all in one file.

---

## 📋 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Game Modes](#game-modes)
- [Difficulty Levels](#difficulty-levels)
- [Hint System](#hint-system)
- [Multiplayer Mode](#multiplayer-mode)
- [GUI Version](#gui-version)
- [Project Structure](#project-structure)
- [Concepts Used](#concepts-used)

---

## ✨ Features

| Feature | Description |
|---|---|
| Difficulty Levels | Easy, Medium, Hard — each with different word sets and wrong-guess limits |
| Hint System | One hint per round, revealed on demand |
| Multiplayer Mode | Two players take turns on the same word, tracked across rounds |
| Tkinter GUI | Graphical window with canvas gallows, colour-coded keyboard, and live scoring |
| Console Mode | Classic text-based gameplay with ASCII art gallows |

---

## ⚙️ Requirements

- Python 3.6+
- Tkinter (for GUI mode)

---

## 🔧 Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/Hangman-Game.git
cd Hangman-Game
```---

## 🧠 Concepts Used

- `random` — picks a random word each round
- `while` loop — keeps the game running until win or loss
- `if-else` — handles correct/wrong guesses and game state
- `strings` — word masking, input validation, display
- `lists` / `sets` — word bank storage and guessed-letter tracking
- `tkinter` — GUI window, canvas drawing, widgets, dialogs
- `classes` — `HangmanGUI` encapsulates all GUI state and logic
- `functions` — modular console game logic split across helpers

---

## 📝 License

This project is open source and free to use for learning purposes.

**2. Install Tkinter** (Linux/Ubuntu only — skip on Windows/macOS, it's bundled)

```bash
sudo apt install python3-tk -y
```

No other dependencies needed — the project uses only the Python standard library.

---

## ▶️ How to Run

```bash
python3 main.py
```
# 🎮 Hangman Game

A feature-rich Python Hangman game with difficulty levels, a hint system, multiplayer mode, and a Tkinter GUI — all in one file.

---

## 📋 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Game Modes](#game-modes)
- [Difficulty Levels](#difficulty-levels)
- [Hint System](#hint-system)
- [Multiplayer Mode](#multiplayer-mode)
- [GUI Version](#gui-version)
- [Project Structure](#project-structure)
- [Concepts Used](#concepts-used)

---

## ✨ Features

| Feature | Description |
|---|---|
| Difficulty Levels | Easy, Medium, Hard — each with different word sets and wrong-guess limits |
| Hint System | One hint per round, revealed on demand |
| Multiplayer Mode | Two players take turns on the same word, tracked across rounds |
| Tkinter GUI | Graphical window with canvas gallows, colour-coded keyboard, and live scoring |
| Console Mode | Classic text-based gameplay with ASCII art gallows |

---

## ⚙️ Requirements

- Python 3.6+
- Tkinter (for GUI mode)

---

## 🔧 Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/Hangman-Game.git
cd Hangman-Game
```

**2. Install Tkinter** (Linux/Ubuntu only — skip on Windows/macOS, it's bundled)

```bash
sudo apt install python3-tk -y
```

No other dependencies needed — the project uses only the Python standard library.

---

## ▶️ How to Run

```bash
python3 main.py
```
---

## 🕹️ Game Modes

### Single-player (Console)
- Pick a difficulty, then guess letters one at a time
- ASCII gallows fills with each wrong guess
- Type `hint` instead of a letter to reveal the hint

### Multiplayer (Console)
- Enter two player names and choose how many rounds
- Players alternate guessing the **same word**
- Final scoreboard displayed after all rounds

### GUI (Tkinter)
- Full graphical window — no terminal needed
- Click letter buttons to guess
- Switch difficulty and mode using radio buttons at the top

---

## 🎯 Difficulty Levels

| Level | Wrong Guesses Allowed | Word Examples |
|---|---|---|
| Easy | 8 | cat, dog, fish |
| Medium | 6 | python, science, laptop |
| Hard | 4 | algorithm, photosynthesis |

---

## 💡 Hint System

Each word has a custom hint. You get **1 hint per round**.

- **Console:** type `hint` when prompted for a letter
- **GUI:** click the purple **Use Hint** button

Once used, the hint button is disabled for the rest of that round.

---

## 👥 Multiplayer Mode

1. Enter Player 1 and Player 2 names
2. Choose number of rounds (default: 3)
3. Both players guess the **same word** in the same round
4. Points are awarded for each word guessed correctly
5. Final winner is announced after all rounds

---

## 🖥️ GUI Version

The Tkinter GUI includes:

- Canvas-drawn gallows (body parts appear progressively)
- Colour-coded on-screen keyboard:
  - 🟢 Green = correct letter
  - 🔴 Red = wrong letter
- Live wrong-guess counter and hint tracker
- Multiplayer setup dialog (names + round count)
- "New Game" button to restart instantly

---

## 📁 Project Structure

Hangman-Game/
│
├── hangman.py          # All game logic, GUI, and entry point
└── README.md        # This file

---

## 🧠 Concepts Used

- `random` — picks a random word each round
- `while` loop — keeps the game running until win or loss
- `if-else` — handles correct/wrong guesses and game state
- `strings` — word masking, input validation, display
- `lists` / `sets` — word bank storage and guessed-letter tracking
- `tkinter` — GUI window, canvas drawing, widgets, dialogs
- `classes` — `HangmanGUI` encapsulates all GUI state and logic
- `functions` — modular console game logic split across helpers

---

## 📝 License

This project is open source and free to use for learning purposes.