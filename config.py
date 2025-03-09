import os
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
    'environment': os.getenv('ENVIRONMENT', 'development'),
    'log_level': os.getenv('LOG_LEVEL', 'DEBUG'),
    'history_file': os.getenv('HISTORY_FILE', 'data/calculation_history.csv')
}