# Autologoff
Autologoff is a Python utility that monitors user inactivity and automatically logs off the user after a specified period. This tool enhances system security by ensuring unattended sessions are securely terminated, preventing unauthorized access.

## Tech Stack
* Python
* Windows API
* Tkinter GUI

## Key Features 
* Tracks user activity.
* Logs off users after one hour of inactivity.
* Runs in the background as a system utility.

## Challenges & Solutions
* **Detecting Inactivity**: Used Windows API hooks to track keyboard/mouse input.
* **Running as a Background Process**: Implemented a system tray application with PyQt.

## Future Improvements
* Add UI for configuration.
* Extend support to Mac/Linux.

## Installation 
1. **Clone the repository:**
   ```bash
   git clone https://github.com/red-grass/Autologoff.git
2. Use the package manager pip to install win32.
![image](https://github.com/user-attachments/assets/fc5c92fd-2a29-4449-99ff-d953640b59f7)

## Overview 
Here is what the prompt message to the user would appear as: 
![image](https://github.com/user-attachments/assets/6da9ec4a-96a1-496a-83e3-86183acec38d)

5 mins before logoff the program gives another message to user: 
![image](https://github.com/user-attachments/assets/a801daed-a8b0-4721-b99a-52eed85064e1)

Final warning message than program forces logoff but keeps tabs and applications running: 
![image](https://github.com/user-attachments/assets/49d0f4eb-9eae-475c-8676-015f602155b0)





