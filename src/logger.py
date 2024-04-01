import logging 
import os 
from datetime import datetime #Imports the datetime class from the datetime module

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True) #The exist_ok=True argument ensures that no error is raised if the directory already exists.

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configures the logging system
logging.basicConfig(  
    filename=LOG_FILE_PATH,
    format= "[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO, #Sets the logging level to INFO, meaning only log messages with levels of INFO or higher will be recorded
)

