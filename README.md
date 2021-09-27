# PyTxtLogger
 Easy to use file logger based on logging library. 
It allow you to easy set up logging in your program
 
 
 ## How to: 
the initialisation block 

1. importing class
``` 
import Logging_class as logclass
```
2. create instance of the class 
```
logger = logclass.txt_logger()
```

3. setting the working folder
``` 
folder = r"C:\Temp"
logger.set_folder(folder)
```
4. setting constant part of file name
``` 
file_name = "log.txt"
logger.set_file_name(file_name)
```

5. creating a file  
function init has additional part of name that can set
```
logger.init("CAN_")
```
this set up will result in log file name: C:\Temp\2021_09_27__23-43-11_CAN_log.txt

 ## Using : 
 
Stop logging and close the file:  
```
.stop_logging(message=None):
 ```
Writing to the file only:
```
.log(txt):
 ```
Printing to the terminal and to the log file at same time 
```
.print_and_log(txt):
```
Printing several lines of text to the terminal and to the log file at same time 
This one could be useful for ASCII art titles 

```   
.print_and_log_ml(multi_line_txt):
```
Inserting a number of blank lines to the log and terminal
Usually useful for separating key points in the log    
```
.insert_blank_lines(line_num=1):
```