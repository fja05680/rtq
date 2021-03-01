"""
rtq
---------
get real time quotes from yahoo finance
"""

# imports
from pandas_datareader.data import get_quote_yahoo

def quote(symbols):
    """ returns the current quote for a list of symbols as a dict """
    d = get_quote_yahoo(symbols).price.to_dict()
    return d

'''
Example:
d = rtq('SPY')
print(d['SPY'])

d = rtq(['SPY', 'QQQ', 'TLT', 'GLD'])
print(d['SPY'], d['QQQ'], d['TLT'], d['GLD'])
'''
