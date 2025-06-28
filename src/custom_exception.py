import traceback
import sys

class CustomException(Exception):
    def __init__(self, error_message, sys):
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message, sys)
        
    @staticmethod
    def get_detailed_error_message(error_message, error_details:sys) -> str:
        """
        Generates a detailed error message including the error message and stack trace.
        """
        _, _, exc_tb = error_details.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        detailed_message = f"Error occurred in script: {file_name} at line number: {line_number} with error message: {error_message}"
        return detailed_message 
    
    def __str__(self):
        return self.error_message