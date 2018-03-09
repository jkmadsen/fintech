import config
import json
import requests
from util import logger

class DataTypeError(BaseException): pass
class IntervalError(BaseException): pass

class Avapi(object):
    def __init__(self,
                 key,
                 headers={},
                 queries={},
                 verbose=False):

        #required
        self.key = key

        #options
        self.headers = headers
        self.queries = queries
        self.verbose = verbose

        #config
        self.logger = logger.Logger()

    # Log (stdout/stderr) msg at the specified level if verbose flag is passed
    def log(self, msg, level):
        if self.verbose:
            self.logger.write(msg, level)

    # Log  (stdout/stderr) msg at the specified level no matter what
    def crit(self, msg, level):
        self.logger.write(msg, level)

    # Basic GET 'constructor'
    def get(self, function, queries={}, headers={}):
        base_queries = {'apikey': self.key}
        base_queries.update(self.queries)
        base_queries.update(queries)
        base_queries.update({'function': function})
        datatype = base_queries.get('datatype', '')
        try:
            req = requests.get(config.base_url,
                               params=base_queries,
                               headers=headers)
            if datatype == 'csv':
                return req.text
            elif datatype == 'json' or datatype == '':
                return req.json()
            else:
                raise DataTypeError('An invalid datatype query was provided')
        except DataTypeError as e:
            self.crit(e, 'critical')
        except IntervalError as e:
            self.crit(e, 'critical')
        except Exception as e:
            self.crit('An error occurred whilst fetching stock data', 'critical')
            self.log(e, 'debug')

    # Custom functions for common routes

    def intraday(self, symbol, interval, queries={}, headers={}):
        if interval not in ['1min', '5min', '15min', '30min', '60min']:
            raise IntervalError('An invalid interval was passed in')
        queries.update({'symbol': symbol, 'interval': interval})
        return self.get('TIME_SERIES_INTRADAY', queries, headers)

    def daily(self, symbol, queries={}, headers={}):
        queries.update({'symbol': symbol})
        return self.get('TIME_SERIES_DAILY', queries, headers)

    def daily_adjusted(self, symbol, queries={}, headers={}):
        queries.update({'symbol':symbol})
        return self.get('TIME_SERIES_DAILY_ADJUSTED', queries, headers)

    def weekly(self, symbol, queries={}, headers={}):
        queries.update({'symbol':symbol})
        return self.get('TIME_SERIES_WEEKLY', queries, headers)

    def weekly_adjusted(self, symbol, queries={}, headers={}):
        queries.update({'symbol':symbol})
        return self.get('TIME_SERIES_WEEKLY_ADJUSTED', queries, headers)

    def monthly(self, symbol, queries={}, headers={}):
        queries.update({'symbol':symbol})
        return self.get('TIME_SERIES_MONTHLY', queries, headers)

    def monthly_adjusted(self, symbol, queries={}, headers={}):
        queries.update({'symbol':symbol})
        return self.get('TIME_SERIES_MONTHLY_ADJUSTED', queries, headers)

    def batch(self, symbols, queries={}, headers={}):
        queries.update({'symbols': symbols})
        return self.get('BATCH_STOCK_QUOTES', queries, headers)
