import logging
import datetime
import os

def get_time_stamp():
    time_var = datetime.datetime.now()
    return(time_var.strftime("%y-%m-%d %H:%M:%S"))


class txt_logger:

    def __init__(self):
        self.app = None
        self.file_name = None
        self.folder = None
        self.file_path = None

    def set_folder(self, folder):
        """
        set the working folder for storing log
        the easy way is to copy the path and insert it like below
        example: folder = r"C:\Temp"
                 .set_folder(folder)
        """
        if os.path.isdir(folder):
            self.folder = folder
        else:
            print(f"Error. Folder not found: {folder}")
            print("Please check the path")

    def set_file_name(self, file_name):
        """
           set the file name
        """
        self.file_name = file_name

    def init(self, txt=""):
        """
        Init methods actually create
        """

        if self.folder is not None:
            if self.file_name is not None:

                self.app = logging.getLogger('Logger')
                now = datetime.datetime.now()  # current date and time

                date_time_in_file_name = now.strftime("%Y_%m_%d__%H-%M-%S")  # get time and date formated into file friendly string
                file_name = date_time_in_file_name + "_" + txt + self.file_name  # making a single string
                self.file_path = os.path.join(self.folder, file_name)

                print("[Debug]: your CAN log file will be here -> ", self.file_path)  # just to check
                can_hdlr = logging.FileHandler(self.file_path)
                formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
                can_hdlr.setFormatter(formatter)
                self.app.addHandler(can_hdlr)
                self.app.setLevel(logging.INFO)  # set logging massage level

            else:
                print("Please set file name first")

        else:
            print("Please set folder first")


    def stop_logging(self, message=None):
        # self.app.flush()
        # self.app.close()
        if message is not None:
            print(f"{get_time_stamp()} !! {message}. ")
            print(f"{get_time_stamp()} !! File location: {self.file_path}")  # just to check
        self.app = None
        self.file_name = None

    def log(self, txt):
        self.app.info(txt)

    def print_and_log(self, txt):
        self.app.info(txt)
        # self.app.flush()
        print(get_time_stamp(), txt)

    def print_and_log_ml(self, multi_line_txt):
        for x in range(len(multi_line_txt)):
            self.print_and_log(multi_line_txt[x])

    def insert_blank_lines(self, line_num=1):
        for i in range(line_num):
            txt = ""
            self.print_and_log(txt)


if __name__ == '__main__':
    pass