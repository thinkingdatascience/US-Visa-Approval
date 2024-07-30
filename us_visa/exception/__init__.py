import sys


def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno

    error_message = f"Error occured in python script name {file_name} line no {line_no} error message {str(error)}"
    return error_message


class USVisaException(Exception):
    def __init__(self, error_message, error_detail) -> None:
        super().__init__(error_message)
        self.error_message = error_message_details(
            error_message, error_detail=error_detail
        )

    def __str__(self) -> str:
        return self.error_message
