import os,sys

def detailed_error_message(error_message:Exception,error_details:sys):
    _, _,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_number=exc_tb.tb_lineno
    
    error_message=f"""
        Error occurred in file {file_name},
        line number {line_number},
        error message is {str(error_message)}
    """
    
    return error_message

class CustomException(Exception):
    def __init__(self,error_message:Exception,error_details:sys):
        super().__init__(error_message)
        self.error_message= detailed_error_message(error_message=error_message,
                                                   error_details=error_details)
        
    def __str__(self):
        return self.error_message