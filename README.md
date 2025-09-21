# PyTorch Projects

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?logo=pytorch&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8.svg?logo=opencv&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)

> 🧠 A lightweight computer vision playground using **PyTorch** and **OpenCV** for experimenting with models, real-time inference, and vision tasks.

---

## 🚀 Overview

This repository serves as a starting point for computer vision projects.  
It combines **PyTorch** with **OpenCV** for:

- Real-time video or webcam inference  
- Image classification or detection experiments  
- Model prototyping with YOLO and Haarcascade  

---

## 📂 Project Structure

| File / Folder         | Description |
|------------------------|-------------|
| `vision.py`           | Main script for inference and video/image processing. |
| `requirements.txt`    | Python dependencies for the project. |
| `.gitignore`          | Files excluded from Git tracking (e.g., model weights). |
| `clear_cache.py`      | Utility script to clear cache/temp files. |
| `scripts/`            | Optional helper utilities. |
| `.vscode/`            | Editor configuration for VSCode. |

---

## 🎯 Models & Weights

This repo uses pretrained YOLO weights:

- `yolov5n.pt`, `yolov5s.pt`, `yolov11n.pt`  
- `yolov8n.pt`, `yolov8s.pt`, `yolov8m.pt`  

⚠️ These files are **large** and excluded from Git (`.gitignore`).  
If missing, download them directly from [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) or let your code handle automatic downloads.

Additionally, small Haarcascade XMLs (like `haarcascade_eye.xml`) are kept in the repo since they’re tiny and necessary for OpenCV-based detection.

---

## ⚙️ Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/ZayanMuhammed/pytorch-projects.git
   cd pytorch-projects
   ```

1. make a virtualenv(optional)

   ```bash
   python -m venv <environment_name>
   source <environment_name>/bin/activate #(on Linux/macOS)
   source <environment_name>\Scripts\activate #(on Windows).
   ```

2. install the libaries

   ```bash
   pip install -r requirments.txt
   ```

3.Run the script(in the script folder)

   ```bash
   python ./vision.py
   ```
4. (Optional) Ensure your PyTorch installation matches your CUDA version if you want GPU acceleration.


## ▶️ Usage

1. Run the main script:

   ```bash
   python vision.py
   ```

### 🥸 authors

-- Name: Zayan Muahmmmed
-- email : zayan.shameermv@gmail.com
