# autogen-data-analyzer
AutoGen Data Analyzer GPT: Build an AI-Powered Data Analysis System

If your project folder does not have uv related files
then follow these steps

uv init --python 3.12.9
rm main.py
uv add --requirements requirements.txt 

If your project has uv related files, then just do this
uv sync


verify these uv related files are present
$ cat .python-version 
$ cat pyproject.toml
$ ls -alt # you should see uv.lock

