from BybitWebsocket import BybitWebsocket
from candles import Candle
from time import gmtime, strftime, sleep
from datetime import datetime

# TODO: replace print statements with logging


class Recording:

    def __init__(self):
        self.ws = None
        self.curr_price = None
        # these are to keep track of the current candle's
        # open, high, low, & close price's
        self.thirty_min_candle = Candle()
        self.one_hour_candle = Candle()
        self.four_hour_candle = Candle()
        self.one_day_candle = Candle()
        self.clock = gmtime()

    def open_bybit_socket(self):
        print('Opening Bybit Socket')
        self.ws = BybitWebsocket(wsURL="wss://stream.bybit.com/realtime",
                                 api_key=None, api_secret=None)

    def subscribe_to_socket(self):
        print('Subscribing to BTCUSD')
        self.ws.subscribe_instrument_info('BTCUSD')

    def start(self):
        print('Starting recording')
        # subscribe to a current
        self.open_bybit_socket()
        self.subscribe_to_socket()

        # timer
        print('Listening')
        while True:
            # grab price data out of the web socket flow
            data = self.ws.get_data("instrument_info.100ms.BTCUSD")
            if data:
                # check if price data has updated
                if 'update' in data.keys():
                    data = data['update'][0]
                    for k, v in data.items():
                        # last traded price update
                        if k == 'last_price_e4':
                            self.curr_price = v

                    # keep track of time
                    tick = gmtime()
                    # TODO: put logic to handle candle stick data
                    # 30 minute open
                    if tick.tm_min is not self.clock.tm_min and tick.tm_min is 30:
                        strftime("%a, %d %b %Y %H:%M:%S +0000", self.clock)
                        print('30 min candle opening')
                    # hourly open
                    if tick.tm_hour is not self.clock.tm_hour:
                        strftime("%a, %d %b %Y %H:%M:%S +0000", self.clock)
                        print('30 min candle opening')
                        print('1 hr candle opening')
                        # 4 hour open
                        if tick.tm_hour % 4 is 0:
                            print('4 hr candle opening')
                    # daily open
                    if tick.tm_mday is not self.clock.tm_mday:
                        strftime("%a, %d %b %Y %H:%M:%S +0000", self.clock)
                        print('daily open')
                    # update clock
                    self.clock = tick
                    strftime("%a, %d %b %Y %H:%M:%S +0000", self.clock)

                sleep(1)
