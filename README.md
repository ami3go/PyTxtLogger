# PyTxtLogger
 Easy to use file logger based on logging library. 
 
 
 ## how to use: 
the initialisation block 
```
# importing class 
import Logging_class as logclass

logger = logclass.txt_logger()

# set the working folder 
folder = r"C:\Temp"
logger.set_folder(folder)

# set constant part of file name 
file_name = "log.txt"
logger.set_file_name(file_name)

#function init has additional part of name that can set
logger.init("CAN_")
```

