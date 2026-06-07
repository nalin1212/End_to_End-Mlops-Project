import sys ##sys module is used to get the details of the exception that occurred in the code
from types import TracebackType
from typing import Optional
from src.logger import logging
logging.basicConfig(level=logging.INFO)


def error_message_detail(error, error_detail):
    _,_,exc_tb = error_detail.exc_info()
    file_name =exc_tb.tb_frame.f_code.co_filename  # pyright: ignore[reportOptionalMemberAccess]
    error_message ="Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno if exc_tb else 0, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error
if __name__ == "__main__":
    try:
        a = 1/0
    except Exception as e:
            logging.info("Division by zero error occurred")
            raise CustomException(e, sys)
    
    