# Exercise for GSoC Green Project

## Setting up Code Carbon on your system
Steps to run Code Carbon on your system:
1. In the Command Prompt Terminal, type:
```   
pip install codecarbon
```
2. To create a minimal configuration file, type:
```
codecarbon config
```
3. You can use the same command to modify an existing configuration file.
4. To monitor your machine, type:
```
codecarbon monitor
```
5. CodeCarbon now runs in an infinite loop, monitoring the machine.
6. To stop monitoring, press CTRL+C.


## Code Profiling a ML/DL model using Code Carbon commands
1. Before training the deep learning model, add:
```
from codecarbon import EmissionsTracker
tracker = EmissionsTracker()
tracker.start()
```
2. And after training the model code, add:
```
tracker.stop()
```

## Setting up Baler
1. Install git for windows.
2. Go to your windows search bar and search for PowerShell. Right-click powershell and select "run as administrator"
3. Enable Linux subsystem by entering this into the PowerShell and hitting enter:
```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```
4. Go to the windows store and download Ubuntu 22.04.1 LTS.
5. Once downloaded, open the Ubuntu terminal
6. Then type in the following commands:
```
wsl.exe --update
```
```
sudo hwclock --hctosys
```
```
sudo apt-get update
```
```
git config --global credential.helper "/mnt/c/Program\ Files/Git/mingw64/bin/git-credential-manager-core.exe"
```
```
sudo apt-get install python3-pip
```
7. After this, you have a working Linux setup and now, type in the following commands:
```
export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring
```
```
pip install --upgrade pip #(pipx was not working for me, so I used pip)
```
```
pip install poetry
```
```
poetry --version # (if you get a version as output, then installation is successful)
```
```
git clone https://github.com/baler-collaboration/baler.git && cd baler #( clone the repository and move into the project)
```
```
poetry install # (install all dependencies)
```

## Code Profiling using Code Carbon Script in Baler
1. Run the following python script to monitor the energy consumption of the Fluid Dynamics Example using Baler:
```
poetry run python track_model1.py
```

2. Run the following python script to monitor the energy consumption of the High Energy Physics Example using Baler:
```
poetry run python track_model1.py
```



