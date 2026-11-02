# 🚀 PyOrganizer

**PyOrganizer** is a simple and efficient Python script that automatically organizes files into folders based on their file extensions.

Instead of manually sorting files, simply choose the directory you want to organize. PyOrganizer automatically sorts your files into folders based on their extensions, keeping everything clean and organized.

## ✨ Features

- 📂 Automatically lists files in a directory.
- 🔍 Identifies file extensions.
- 📁 Creates folders based on file extensions.
- 🚚 Moves files into their corresponding folders.
- 📊 Displays execution logs and a summary of the operation.
- ⚡ Simple, lightweight, and easy to use.

## 🛠️ Technologies

- **Python 3**
- `os` — Directory and file operations.
- `shutil` — Moving files.
- `time` — Execution delays.

## 📋 Requirements

- Python 3.10 or higher.
- No external dependencies required.

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/rngando/pyorganizer.git
```

Navigate to the project directory:

```bash
cd pyorganizer
```

## ▶️ Usage

Run the script:

```bash
python main.py
```

When the program starts, it will ask you to enter the directory you want to organize.

## Example:

```text
Enter the directory path: /home/user/Downloads
```

## 📂 Example

**Before:**

```text
Downloads/
├── image.png
├── document.pdf
├── music.mp3
├── video.mp4
└── script.py
```

**After:**

```text
Downloads/
├── PNG/
│   └── image.png
├── PDF/
│   └── document.pdf
├── MP3/
│   └── music.mp3
├── MP4/
│   └── video.mp4
└── PY/
    └── script.py
```

## 📊 Execution Logs

PyOrganizer provides terminal logs to track the organization process.

Example:

```text
[PROCESS] Starting file organization...
[SUCCESS] PDF folder created successfully.
[SUCCESS] PNG folder created successfully.
[SUCCESS] document.pdf → PDF/
[SUCCESS] image.png → PNG/
[INFO] 2 folders created.
[INFO] 2 files moved.
[SUCCESS] Organization completed!
```

## 🗺️ Future Improvements

- [ ] Support for files without extensions.
- [ ] Prevent overwriting files with identical names.
- [ ] Allow users to select directories through terminal input.
- [ ] Add a configurable logging system.
- [ ] Add support for recursive directory organization.
- [ ] Implement automated tests with Pytest.

## 👨‍💻 Author

**Ramiro Ngando**

- GitHub: [@rngando](https://github.com/rngando)

## 📄 License

This project is open-source.

---

⭐ If you find this project useful, consider giving it a star!