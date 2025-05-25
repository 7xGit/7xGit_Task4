Task 4 - Python File Manager Challenge  
=====================================

Welcome to the **File Manager Open Source Challenge**! This project simulates a basic file system using a **Red-Black Tree**. It supports commands like creating directories, listing files, navigating folders, and more... or at least, it should. 👀

Some code is **missing**, and it's up to **you** to find and fix it. Are you up for the challenge?

🧠 Challenge Overview  
---------------------

Your mission is to restore and improve the file manager’s functionality by identifying bugs, filling missing parts, and adding enhancements to `main.py`.

### What's the Twist?

* Some command behaviors are **incomplete** or **broken**.  
* Certain **corner cases** aren't handled properly.  
* Some functions are **present but not connected**.  

🎯 Your Objectives  
------------------

Explore the code and identify:

* Why certain commands don’t behave as expected.  
* Which methods are **not updating** the Red-Black Tree correctly?  
* What should happen when **deleting or navigating directories**?  
* Where **command output is missing or incorrect**?  

No direct solutions in the issues! It's up to contributors to debug and solve the problem. 🕵️‍♀️

📂 Supported Commands (or supposed to be)  
------------------------------------------

* `mkdir <dirname>` – Create a directory  
* `ls` – List current directory  
* `cd <dirname>` – Change current directory  
* `cd ..` – Go up one directory  
* `pwd` – Show current path  
* `rm <dirname>` – Delete a directory  
* `exit` – Exit the program  

⚠️ What’s Broken?  
-------------------

Some of these commands don’t work **as expected** — especially:

* `cd` doesn’t change directories correctly in edge cases  
* `rm` doesn’t delete directories from the tree  
* `ls` sometimes displays the wrong results  
* Tree connections might not reflect directory structure accurately  

(But we won't tell you exactly where. That’s the fun part 😉)

🚀 Run Locally  
--------------

1. Clone the repository:  
    ```bash
    git clone https://github.com/https://github.com/7xGit/7xGit_Task4.git
    ```

2. Navigate to the project folder:  
    ```bash
    cd [FolderName]
    ```

3. Run the program:  
    ```bash
    python3 main.py
    ```
    
---

Ready to become a **File System Debugging Ninja**? Jump in, find the bugs, and patch this file manager to perfection! 🐛🛠️

**Happy coding!** 🚀
