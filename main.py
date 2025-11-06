from ping_game_theory_25 import Strategy, StrategyTester, Move, History, HistoryEntry


class Bot(Strategy):
    def __init__(self) -> None:
        self.author_netid = "" # Your netid here
        self.strategy_name = "" # Name of your strategy here
        self.strategy_desc = "" # Description of your strategy here

    def begin(self) -> Move:
        # Make your initial move here
        return Move.ROCK # Example: always starts with ROCK (modify it to implement your strategy)

    def turn(self, history: History) -> Move:
        # Make your move based on the history
        return Move.ROCK # Example: always plays ROCK (modify it to implement your strategy)


tester = StrategyTester(Bot)
tester.run()
