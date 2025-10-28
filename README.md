# Raygin — Python Game Engine for Raylib

---

## 🛠️ Requirements

- **Python 3.11+** (3.11 to 3.14.9)
- [Poetry](https://python-poetry.org/) (for dependency management)
- [Raylib](https://www.raylib.com/) (via Python bindings)

> ⚠️ **Note**: This project uses a custom implementation of Raylib in Python. The `raylib` package in this project is a wrapper around the C-based Raylib library.

---

## 🚀 Installation

1. **Install Poetry** (if you don't have it yet):
   ```bash
   pip install poetry
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**:
   ```bash
   poetry install
   ```

4. **Run your game**:
   ```bash
   poetry run python main.py
   ```

---

## 📦 Building for Distribution

To package your game into a single executable file (for distribution):

1. **Install PyInstaller** (via Poetry):
   ```bash
   poetry install --dev
   ```

2. **Build the executable**:
   ```bash
   poetry run build
   ```

This will generate a `dist` folder with your game executable. The built executable supports:
- Windows (x64)
- macOS (x64)
- Linux (x64)

> 💡 **Tip**: The `build` command uses PyInstaller v6.16.0+ for optimal performance.

---

## 📚 Documentation

- [Raylib Official Documentation](https://github.com/raysan5/raylib/wiki)

---

## 📌 Notes

- The `raylib` package in this project is a custom wrapper for the C-based Raylib library.
- This implementation is designed for **2D games** only.

---

**Raygin v0.0.1** | [GitHub](https://github.com/ummo93/raygin) | [Poetry](https://python-poetry.org/)