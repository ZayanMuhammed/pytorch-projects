PyTorch Vision Project
This is a lightweight computer vision project using PyTorch and OpenCV, centered around a single script: vision.py.

Overview
The project is designed for basic or experimental vision tasks such as real-time video processing, model inference, or frame-by-frame live view manipulation. It can serve as a foundation for more complex vision applications or just for quick testing with PyTorch and OpenCV.

Files Included
vision.py: Main script containing all logic for vision processing.

requirements.txt: Lists all necessary dependencies.

Setup & Installation
To get started, set up a Python environment and install the required libraries using the requirements.txt file. It includes core dependencies like torch and opencv-python.

Usage
After installing the dependencies, you can run vision.py directly. You can modify this script depending on the input source (webcam, image, video file) or the specific vision task you're working on.

Requirements
Python 3.x

PyTorch

OpenCV

Other minor packages as listed in requirements.txt

Notes
Make sure PyTorch is installed with CUDA if you're using a GPU.

Webcam or input image/video source is required if applicable.

This project is ideal for prototyping small vision tasks or testing models quickly.

License
Feel free to use, modify, and distribute under your preferred license.

*Installtion*
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

3.run the script(in the script folder)

```bash
python ./vision.py
```
4. have fun!!
