# 🗃️ Smart File Automation System

A Python-based tool to automate file management — organize, rename, archive, and clean files in a selected directory. Designed to be modular, scalable, and deployment-ready with a Streamlit GUI.

---

## 🚀 Features

- 📁 **Auto-Sorting**: Sorts files into folders by type (PDFs, images, documents, etc.)
- 🏷️ **File Renaming**: Rename files based on patterns like date or keywords
- 🧹 **Duplicate Detection**: Detects and optionally deletes duplicate files using hashing
- 📦 **Archiving**: Archive large or old files into ZIP format
- 📝 **Logging**: Logs all actions for auditing and debugging
- 💻 **User Interfaces**:
  - Command-Line Interface (CLI)
  - Graphical Interface using Streamlit (GUI)

---

## 📂 Folder Structure

smart-file-automation/
├── core/
│ ├── sorter.py # Handles file sorting logic
│ ├── renamer.py # File renaming logic
│ ├── duplicator.py # Duplicate detection/removal
│ ├── archiver.py # Archive utilities
│ └── logger.py # Logging system
│
├── utils/
│ └── helpers.py # Common helper functions
│
├── ui/
│ ├── cli.py # CLI interface using argparse
│ └── streamlit_ui.py # Streamlit GUI interface
│
├── config/
│ └── settings.yaml # Configurable settings
│
├── logs/
│ └── activity.log # Log file (auto-generated)
│
├── requirements.txt
├── README.md
└── main.py # Entry point
