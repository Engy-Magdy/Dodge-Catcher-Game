<div align="center">

# 🐢 DODGE CATCHER GAME 🐢

<p align="center">
  <b>A classic arcade dodging and catching game built completely from scratch using Python & Object-Oriented Programming (OOP) principles!</b>
</p>

---

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Paradigm](https://img.shields.io/badge/Paradigm-OOP-orange.svg)
![Graphics](https://img.shields.io/badge/Graphics-Turtle-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

</div>

---

## 🎮 Game Preview
<img width="980" height="726" alt="Dodge Catcher Game" src="https://github.com/user-attachments/assets/22ed8ee8-5a90-4ae6-ba56-957dfacaf60a" />

<!-- <p align="center">
  <img src="path_to_your_gif.gif" alt="Game Demo" width="600"/>
</p> -->

---

## 📋 Table of Contents
- [About The Project](#-about-the-project)
- [Game Rules & Scoring](#-game-rules--scoring)
- [Project Architecture & OOP Structure](#-project-architecture--oop-structure)
- [Controls](#-controls)
- [Getting Started & Installation](#-getting-started--installation)

---

## 🚀 About The Project
**Dodge Catcher Game** is an interactive, arcade-style desktop game developed in Python. The core objective is to control a paddle to catch incoming falling shapes and bonuses while avoiding dangerous traps. This project emphasizes clean modular code structure, real-time rendering control via `screen.tracer(0)`, and robust collision detection.

---

## 🎯 Game Rules & Scoring
The game features dynamic falling forms with distinct behaviors and logic:

| Item / Entity | Action / Effect | Score Impact |
| :--- | :--- | :--- |
| **🟢 Green Turtle** | Bonus catch | **+50 Points** |
| **⭐ Regular Forms** | Standard catch (Circles, Triangles, etc.) | **+10 Points** |
| **⚪ White Turtle** | Dangerous trap | **Game Over** |
| **🧱 Out of Bounds** | Item drops past screen boundaries | **Loop Reset / Skip** |

---

## 🏗️ Project Architecture & OOP Structure
The project follows strict **Object-Oriented Programming (OOP)** paradigms, divided into dedicated modular files for maximum maintainability:

* **`main.py`** — The entry point containing the core game loop, screen setup, event listeners, and collision checks.
* **`paddle.py`** (`class Paddle`) — Inherits from `Turtle`, managing player movement limits, geometry, and key bindings.
* **`forms.py`** (`class Forms`) — Inherits from `Turtle`, responsible for random shape and color generation, and falling animations.
* **`score.py`** (`class Score`) — Inherits from `Turtle`, handling live score tracking, text rendering, and screen updates.

---

## 🕹️ Controls
Use your keyboard arrow keys to maneuver the paddle:

```text
       [ ← ]  Move Left
       [ → ]  Move Right
