import logging
import datetime
import os


def get_time_stamp():
    time_var = datetime.datetime.now()
    return time_var.strftime("%y-%m-%d %H:%M:%S")


class txt_logger:

    def __init__(self):
        self.app = None
        self.file_name = None
        self.folder = None
        self.file_path = None

    def set_folder(self, folder):
        """
        Set the working folder where the log will be stored.
        Copy the path and insert it like below:

        Example: folder = r"C:\Temp"
                 .set_folder(folder)

        Note: "r"  at the start will convert the windows path in to python path

        :param folder: is a folder path in txt format
        :type folder: string
        :return: None
        """
        if os.path.isdir(folder):
            self.folder = folder
        else:
            print(f"Error. Folder not found: {folder}")
            print("Please check the path")

    def set_file_name(self, fname):
        """
           Set the constant part of the file name of the log

           Example file_name = "log.txt"
                   .set_file_name(file_name)

           Note: full file name will be like below:
                 2021_09_28__22-24-49_log.txt
                 if .init() was called with no text

           :param fname: is a last part of log file name
           :type  fname: string
           :return: None
        """
        self.file_name = fname

    def init(self, txt=""):
        """
        Init methods actually create the file.
        2021_09_28__22-24-49_log.txt if .init() will be call with no text

        Note: Before calling the .init() file name and folder should be set

        :param txt: middle part of the file name
        :type txt: str
        :return: None
        """
        if self.folder is not None:
            if self.file_name is not None:
                now = datetime.datetime.now()  # current date and time
                # get time and date formatted into file friendly string
                date_time_fname = now.strftime("%Y_%m_%d__%H-%M-%S")
                self.app = logging.getLogger(f'Logger_{date_time_fname}')

                file_name = date_time_fname + "_" + txt + self.file_name  # making a single string
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
        """
        Stop and close log file.

        :param message: print message into console and show log file location
        :type message: str
        :return: None
        """
        # self.app.flush()
        # self.app.close()
        if message is not None:
            print(f"{get_time_stamp()} !! {message}. ")
            print(f"{get_time_stamp()} !! File location: {self.file_path}")  # just to check
        self.app = None
        self.file_name = None

    def log(self, txt):
        """
        Only write message to log file.
        :param txt: message that will be logged
        :type txt: str
        :return: None
        """
        self.app.info(txt)

    def print_and_log(self, txt):
        """
        Printing into console and to a log file
        :param txt: message that will be logged and printed
        :type txt: str
        :return:
        """
        self.app.info(txt)
        # self.app.flush()
        print(get_time_stamp(), txt)

    def print_and_log_ml(self, multi_line_txt):
        """
        Printing into console and to a log file several lines of text

        :param multi_line_txt: message that will be logged and printed
        :type multi_line_txt: str
        :return: None
        """
        for x in range(len(multi_line_txt)):
            self.print_and_log(multi_line_txt[x])

    def insert_blank_lines(self, line_num=1):
        """
        Inserting a blank lines to the log file and console.

        :param line_num: number of blank lines. Should be 0 - 10 000
        :type line_num: int
        :return: None
        """
        if line_num <= 0:
            pass
        if line_num >= 10000:
            line_num = 10000
        for i in range(int(line_num)):
            txt = ""
            self.print_and_log(txt)


if __name__ == '__main__':
    pass
