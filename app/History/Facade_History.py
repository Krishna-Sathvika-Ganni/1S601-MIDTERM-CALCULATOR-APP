from app.History.Managing_History import History_Manager

class HistoryFacade:
    def __init__(self):
        self.history_manager=History_Manager()

    def save_history(self):
        self.history_manager.saving_history()

    def load_history(self):
        self.history_manager.load_history()

    def clear_history(self):
        self.history_manager.clear_history()

    def delete_history(self):
        self.history_manager.delete_history()