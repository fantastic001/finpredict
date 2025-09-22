
from orgasm import command_executor_main
from finpredict.data_collection import get_data
from finpredict.model_tickers import get_data as model_tickers
from finpredict.run_nb_training import train_nb
class Commands:
    def collect_data(self):
        return get_data()
    def model_tickers(self):
        return model_tickers()
    def train_nb(self):
        return train_nb()
if __name__ == "__main__":
    command_executor_main(Commands)
