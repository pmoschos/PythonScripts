# 🧹 Console Clear Utility

![Total Views](https://views.whatilearened.today/views/github/pmoschos/pmoschos.svg)

## 📌 Project Overview

🔍 The Console Clear Utility is a lightweight Python helper script that
clears the terminal screen across **Windows**, **macOS**, and **Linux**
environments. It automatically detects the operating system and executes
the correct command to refresh the console output.

This makes it ideal for **CLI tools**, **interactive scripts**, and
**educational examples** where you want to simulate a "clean screen"
experience.

## ⭐ Key Features

-   🖥️ Cross-platform console clearing\
-   ⚙️ Automatic OS detection\
-   💨 Uses `subprocess.run` for reliable execution\
-   🎓 Simple and easy-to-read code --- perfect for teaching\
-   🧩 Can be imported in other scripts or executed directly

## 🖥️ Technical Requirements

-   🐍 Python 3.x

## 👥 Target Audience and Skill Level

This utility is ideal for:

-   Students learning CLI app development\
-   Educators demonstrating console behavior\
-   Python developers building terminal-based applications

## Installation 💾

1.  **🔗 Clone the Repository**

``` bash
git clone https://github.com/pmoschos/PythonScripts
```

2.  **📁 Navigate to the script directory**

``` bash
cd PythonScripts/console_clear
```

## 📌 Usage Example

### ▶️ Run the script directly:

``` bash
python clear_screen.py
```

### 🧩 Import into another script:

``` python
from clear_screen import clear_screen

clear_screen()
```

This clears the terminal screen before continuing execution.

## 📸 Running the Script

### 🏠 Script Startup

When executed, the script immediately clears the console based on your
OS.

### ⚙️ Behind the Scenes

-   On **Windows** → Uses: `cls`\
-   On **macOS/Linux** → Uses: `clear`

### 🔀 Detecting the OS

The script uses:

``` python
platform.system()
```

to determine the correct command.

## 📢 Stay Updated
Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---

<h1 align=center>Happy Coding 👨‍💻 </h1>
<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
