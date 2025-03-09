# config.py
import os

def get_log_level():
    return os.getenv('LOG_LEVEL', 'INFO').upper()

def get_log_output_file():
    return os.getenv('LOG_OUTPUT_FILE', None)
