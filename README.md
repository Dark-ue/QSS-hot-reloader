# QSS Hot Reloader

A Python utility for dynamically reloading QSS (Qt Style Sheets) in PyQt6 applications. This tool allows you to see real-time updates to your application's styles as you modify the QSS files, making UI development faster and more efficient.

---

## Features

- **Real-Time QSS Reloading**: Automatically applies changes to QSS files without restarting the application.
- **Debounce Mechanism**: Prevents excessive reloading when files are modified rapidly.
- **Simple Integration**: Easily integrate with any PyQt6 application.

---

## Requirements

- Python 3.7+
- PyQt6
- Watchdog

Install the required dependencies using pip:

```bash
pip install PyQt6 watchdog
```