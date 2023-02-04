# GNOJ8_odd_controls

## 1. Steps to setup the dev environment

### 1.1 Install Godot v3.5.1 (We use godot 3 since godot-python might not support godot4 yet)
* You can find the link to download the installation file here: https://godotengine.org/download/windows/

### 1.2 Import the project

### 1.3 Install godot-python addon

* Select `AssetLib` and serch for `PythonScript`. Download and install it. It might take a while just leave it there untils it is done.
  
* Remember not to install `PythonScript-Pypy`, it is a legacy version.
* Restart the project

### 1.4 Install dependencies
* Navigate to path: `cd <Your-Project-Path>\GNOJ8_odd_controls\addons\pythonscript\windows-64` in powershell
* Check you python version with:
    ```
    ./python.exe -V Python 3.8.5
    ```
  And it should show something like: `Python 3.8.5`
* Use command `./python.exe -m ensurepip` to install the pip and `./python.exe -m pip install -U pip` to update the pip
* Install packages required:
```shell
./python.exe -m pip install torch==1.13.1
./python.exe -m pip install transformers==4.25.1
```
