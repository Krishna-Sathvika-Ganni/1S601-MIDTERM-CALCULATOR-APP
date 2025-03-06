import os
import logging
import pandas as pd
from app.calculator.calculations import Calculations

logger = logging.getLogger(__name__)

class History_Manager:
    HISTORY_FILE="data/calculation_history.csv"

    @classmethod
    def saving_history(cls):
        history=Calculations.get_history()
        if not history:
            print("There is no history to save")
            logger.warning("No history data")
            return
        
        os.makedirs(os.path.dirname(cls.HISTORY_FILE), exist_ok=True)
        data=pd.DataFrame([
            {"x":calc.x, "y":calc.y, "operation":calc.operation.__name__, "result":calc.perform()} 
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
        Calculations.clear_history()
        logger.info("Cleared History")
        print("History cleared.")

    @classmethod
    def delete_history(cls):
        if os.path.exists(cls.HISTORY_FILE):
            os.remove(cls.HISTORY_FILE)
            logger.info("History file deleted")
            print("Saved history deleted.")
        else:
            logger.warning("No saved history file found.")
            print("No saved history file found.")