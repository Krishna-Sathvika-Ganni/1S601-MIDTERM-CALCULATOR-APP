import os
import logging
import pandas as pd
from config import CONFIG 

logger = logging.getLogger(__name__)

class history_manager:
    HISTORY_FILE = CONFIG['history_file']

    @classmethod
    def save_history(cls):
        # Delay import to avoid circular import
        from app.calculator.calculations import Calculations

        history = Calculations.get_history()
        if not history:
            print("There is no history to save")
            logger.warning("No history data")
            return
        
        os.makedirs(os.path.dirname(cls.HISTORY_FILE), exist_ok=True)
        data = pd.DataFrame([
            {"x": calc.x, "y": calc.y, "operation": calc.operation.__name__, "result": calc.perform()}
            for calc in history
        ])

        file_exists = os.path.exists(cls.HISTORY_FILE)
        data.to_csv(cls.HISTORY_FILE, mode='a', header=not file_exists, index=False)
        print("History saved.")
        logger.info("Saved History")

    @classmethod
    def load_history(cls):
        if not os.path.exists(cls.HISTORY_FILE):
            logger.error("Saved history not found")
            print("No saved history")
            return

        df = pd.read_csv(cls.HISTORY_FILE)
        print("Loaded History:")
        print(df)
        logger.info("History loaded successfully.")

    @classmethod
    def clear_history(cls):
        # Delay import to avoid circular import
        from app.calculator.calculations import Calculations

        if not Calculations.get_history():
            logger.warning("No in-memory history to clear.")
            print("No in-memory history to clear.")
            return
        
        Calculations.clear_history()
        logger.info("Cleared in-memory history.")
        print("In-memory history cleared.")

    @classmethod
    def delete_history(cls):
        if os.path.exists(cls.HISTORY_FILE):
            os.remove(cls.HISTORY_FILE)
            logger.info("History file deleted")
            print("Saved history deleted.")
        else:
            logger.warning("No saved history file found.")
            print("No saved history file found.")

    @classmethod
    def get_latest(cls):
        # Delay import to avoid circular import
        from app.calculator.calculations import Calculations

        history = Calculations.get_history()
        if history:
            return history[-1]
        return None

    @classmethod
    def find_by_operation(cls, operation_name):
        # Delay import to avoid circular import
        from app.calculator.calculations import Calculations

        history = Calculations.get_history()
        if not history:
            raise ValueError("No history available")
        filtered = [calc for calc in history if calc.operation.__name__ == operation_name]
        if not filtered:
            raise ValueError(f"Invalid operation: {operation_name}")
        return filtered
