# autogen-data-analyzer
AutoGen Data Analyzer GPT: Build an AI-Powered Data Analysis System

Installations
---------------
1)Download and Install Python. Dont install python 3.14 - many libraries are not yet supported in this latest version
https://www.python.org/downloads/release/python-3133/

2)Running python code
Open a terminal and type 
python3
You will see python shell prompt
>>> 
You can try python code snippets quickly using this shell eg.,
>>> a=5
>>> b=4
>>> print(a+b)
9
Once you are done type exit() to come out of shell
>>> exit()

3)Install uv - the build tool for python. 
Open the terminal and run this command
curl -LsSf https://astral.sh/uv/install.sh | sh

close the terminal and open a new terminal
verify uv is working . run this command
uv --version

For upgrading uv also, use the same curl command. It will detect uv is already
installed and upgrade

Setting up this project
--------------
After you cloned the project, go to project folder

Run this command to download the dependencies
$ uv sync

If your project folder does not have uv related files
then follow these steps (minimum you should have requirements.txt)

$ uv init --python 3.12.9 #we are pinning a specific version of python
$ rm main.py    #uv init generates this dummy file. You can delete it
$ uv add --requirements requirements.txt 

verify these uv related files are present in your project folder
$ cat .python-version 
$ cat pyproject.toml
$ ls -alt # you should see the file uv.lock and folder .venv

Check virtual environment is created. Activate it using this command
$ source .venv/bin/activate

Your command prompt will change to this
(autogen-data-analyzer) $ 

Execute which command. It should display the current project folder
It proves that your virtual environment is correctly configured

(autogen-data-analyzer) $ which python
~/projects/personal/krishnaik/industry-ready/autogen-data-analyzer/.venv/bin/python

Deactivate a virtual environment using this command
(autogen-data-analyzer) $ deactivate
$

Running a sample script
---------------
Pre-requisite
Your docker desktop must be running
In case of mac, U also need add a link . command will be like this
$ sudo ln -sf ~/.docker/run/docker.sock /var/run/docker.sock


For running a python script under agents folder use uv run command.
This automatically runs in virtual environment. U dont need to activate it
explicitly. If you are running the script using python command
then you need to activate virtual environment

$ uv run agents/code_executor_agent.py
result is : Hello Krishna
docker conainer stopped

If you see the output, congrats. You have succesfully setup the project

Note : the code executor agent will create tmp files under workdir
which can be ignored.

Setting up VsCode
------------
To run python scripts(.py  files) and jupyter notebooks (.ipynb files)
in VSCode you need to install two vscode  extensions
Python (by Microsoft)
Jupyter (by Microsoft)

Additionally you need to add a dependency to your project runtime
$ uv add jupyter

For .py files: Look at the bottom right corner of your VS Code window. 
Click on the Python version number (or "Select Interpreter"). Choose the path that 
points to ./venv/bin/python

For .ipynb files: Click "Select Kernel" in the top right of the notebook editor. 
Select "Python Environments..." and pick the one associated with your project's .venv folder

Configure your settings.json
$ mkdir -p .vscode
$ touch .vscode/settings.json

paste this content in settings.json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.terminal.activateEnvironment": true,
  "python.analysis.typeCheckingMode": "basic"
}

Watch a streamlit demo
Activate your virtual environment
$ source .venv/bin/activate
$ streamlit run streamlit_demo.py
press ctrl + c to stop the server


Docker must be running
$ streamlit run streamlit_app.py

Generate a bar chart of survived and expired for male and female
