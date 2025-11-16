import os
import platform
import subprocess

def clear_screen():
    """Clear the console screen on Windows, macOS, and Linux."""
    system_name = platform.system()

    if system_name == "Windows":
        # Works on cmd, PowerShell, Windows Terminal
        subprocess.run("cls", shell=True)
    else:
        # macOS / Linux
        subprocess.run("clear", shell=True)

if __name__ == "__main__":
    clear_screen()