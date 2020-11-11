class Candle:
    """Japanese Candle Stick
    Attributes:
        open_e4 (int): open price * 10^4
        high_e4 (int): high of this candle * 10^4
        low_e4 (int): low of this candle * 10^4
        close_e4 (int): close price * 10^4
    """

    def __init__(self, open_e4=None, high_e4=None, low_e4=None, close_e4=None):
        self.open_e4 = open_e4
        self.high_e4 = high_e4
        self.low_e4 = low_e4
        self.close_e4 = close_e4
