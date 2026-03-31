# 🔐 Metadata Analyzer & Privacy Sanitization Tool

A Python-based security tool designed to analyze, sanitize, and manage image metadata to prevent unintended information leakage. This project focuses on privacy protection and secure handling of embedded data commonly found in digital images.

---
# 📌 Overview

Digital images often contain hidden metadata (EXIF) such as GPS location, device details, timestamps, and author information. This data can be exploited for **Open-Source Intelligence (OSINT)** and may lead to privacy breaches.

This tool enables users to:

- Inspect embedded metadata
- Identify potential privacy risks
- Remove or modify sensitive information before sharing files

---

## 📋 Features

- **🔍 Extract Metadata** - View all EXIF data and metadata embedded in image files
- **🧹 Remove Metadata** - Completely strip all metadata from images (create "ghost files")
- **✏️ Modify Metadata** - Modify specific metadata tags with custom values
  - Edit Artist, Software, Copyright, and Image Description tags
  - Edit multiple tags in a single session
  - Keep original values or replace them
- **🎨 Color-Coded Output** - Easy-to-read terminal interface with color highlighting
- **⚙️ User-Friendly** - Interactive menu-driven interface for all operations

---

## 🛠️ Requirements

- Python 3.7+
- PIL/Pillow
- piexif
- colorama

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Metadata-Analyzer-Sanitization-Tool.git
   cd Metadata-Analyzer-Sanitization-Tool
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install Pillow piexif colorama
   ```

---

## 🚀 Usage

Run the tool:
```bash
python main.py
```

### Interactive Menu

1. **Enter the path to your target image file**
2. **View extracted metadata** - All EXIF data will be displayed
3. **Select an operation:**
   - `[1]` **Ghost File** - Remove all metadata
   - `[2]` **Forge Data** - Modify metadata tags
   - `[3]` Abort operation

### Modifying Metadata

When you select option `[2]`:
- Choose which tag to edit (Artist, Software, Copyright, Image Description)
- Enter new value or press Enter to keep original
- Edit multiple tags in one session
- `[5]` Save and exit with a `_forged` file
- `[6]` Cancel all changes

### Removing Metadata

When you select option `[1]`:
- All metadata is stripped from the image
- A new `_no_metadata` file is created
- Original file remains unchanged

---

## 🔐 Security & Privacy Use Cases
- Prevent **unintentional data exposure** when sharing images
- Support **OSINT awareness and analysis**
- Assist in **digital forensics and metadata inspection**
- Demonstrate **data sanitization techniques** used in secure environments 
---

## 🔧 Supported Metadata Tags

Currently supports editing the following EXIF tags:
- **Artist** - Creator of the image
- **Software** - Software used to create the image
- **Copyright** - Copyright information
- **ImageDescription** - Description of the image

*Note: You can extend the `safe_tags` dictionary in `main.py` to support additional tags.*

---

## ⚠️ Privacy & Security

- **Data Safety** - Original files are never modified; new files are created
- **Complete Removal** - "Ghost File" mode completely removes all metadata
- **Forgery Detection** - Useful for testing security systems and understanding metadata vulnerabilities

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit pull requests or open issues for bug reports and feature requests.

---

## 📄 License

This project is open source. Feel free to use, modify, and distribute as needed.

---

## ⚡ Tips

- Always keep backups of original files
- Test with non-critical images first
- Use "Ghost File" mode for maximum privacy
- Metadata can contain GPS data, camera information, and timestamps - remove it if you're concerned about privacy

---

## 🐛 Troubleshooting

**"File not found" error:**
- Ensure the file path is correct and the file exists
- Use absolute paths for better reliability

**"No metadata detected" message:**
- Some images may not have EXIF data embedded
- This is normal for images created without metadata

**Permission errors:**
- Ensure you have read/write permissions in the directory
- Try running with elevated privileges if needed

---