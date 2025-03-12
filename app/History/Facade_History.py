from app.History.Managing_History import history_manager

class HistoryFacade:
    def __init__(self):
        self.history_manager=history_manager()

    def save_history(self):
        self.history_manager.save_history()

    def load_history(self):
        self.history_manager.load_history()

    def clear_history(self):
        self.history_manager.clear_history()

    def delete_history(self):
        self.history_manager.delete_history()