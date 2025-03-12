import os
from pathlib import Path
import logging

# To log info level log in terminal => current timestamp    log message
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

# __init__.py is constructor file => it execute automatically
# helper.py is functionality
# setup.py is used to install as local package
list_of_files= [
    "src/__init.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trails.ipynb",
    # "test.py"
]

for file in list_of_files:
    filepath = Path(file)
    filedir,filename = os.path.split(filepath)
    
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Createing Directory; {filedir} for file: {filename}")
        
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating Empty Files: {filepath}")
            
    else:
        logging.info(f"{filename} is already exists")