import PyTxtLogger.pytxtlogger as logclass

folder = r"C:\Temp"
file_name = "log.txt"
logger = logclass.pytxtlogger()
logger.set_folder(folder)
logger.set_file_name(file_name)
logger.init("CAN_")

logger.print_and_log("Hello")
logger.insert_blank_lines(16)
logger.stop_logging("stop logging, close the file")