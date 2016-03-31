#! /usr/bin/python

"""
    Python Script which calculates trend lines from a set of stock quotes
    provided through the Standard Input.
    
    This script works well when reading quotes provided by the pse-quotes.py
    script.
"""
__author__ = "John Lawrence M. Penafiel"
__copyright__ = "Copyright 2015, John Lawrence M. Penafiel"
__credits__ = ["John Lawrence M. Penafiel"]
__maintainer__ = ["John Lawrence M. Penafiel"]
__email__ = "penafieljlm@gmail.com"
__status__ = "Prototype"

import datetime
import json
import os
import sys
import time

if __name__ == "__main__":
    # try to read data from stdin
    data = []
    for line in sys.stdin:
        data.append(line)
    data = '\n'.join(data)
    if len(data) <= 0:
        sys.exit(
                 '\n'.join(
                 (
                 'usage: pse-quotes.py [PARAMETERS] | pse-trends.py',
                 'usage: pse-trends.py < pse-quotes.json',
                 '{script}: error: no input provided'.format(script=os.path.basename(__file__)))
                 )
                 )
    # try to parse data from stdin
    quotes = None
    try:
        quotes = json.loads(data)
    except:
        sys.exit(
                 '\n'.join(
                 (
                 'usage: pse-quotes.py [PARAMETERS] | pse-trends.py',
                 'usage: pse-trends.py < pse-quotes.json',
                 '{script}: error: unable to parse input'.format(script=os.path.basename(__file__)))
                 )
                 )
    # graph stock quotes, determine stock ages
    graphs = {}
    ages = {}
    for quote in quotes:
        time = (datetime.date(*(int(x) for x in quote['quote_date'].split('-'))) - datetime.date(1900, 1, 1)).days
        value = float(quote['price_close'])
        if quote['symbol'] not in graphs:
            graphs[quote['symbol']] = {}
        graphs[quote['symbol']][time] = value
        if quote['symbol'] not in ages:
            ages[quote['symbol']] = {
                'min': datetime.timedelta.max.days,
                'max': datetime.timedelta.min.days
            }
        ages[quote['symbol']]['min'] = min(ages[quote['symbol']]['min'], time)
        ages[quote['symbol']]['max'] = max(ages[quote['symbol']]['max'], time)
    # calculate trend lines
    trends = {}
    for quote in graphs:
        n = len(graphs[quote])
        sum_xy = sum(x * graphs[quote][x] for x in graphs[quote])
        sum_x = sum(x for x in graphs[quote])
        sum_y = sum(graphs[quote][x] for x in graphs[quote])
        sum_x2 = sum(x * x for x in graphs[quote])
        slope = ((n * sum_xy) - (sum_x * sum_y)) / ((n * sum_x2) - (sum_x * sum_x))
        age = ages[quote]['max'] - ages[quote]['min']
        trends[quote] = {
            'slope': slope,
            'age': age
        }
    # format results into a csv friendly format
    results = []
    for quote in trend:
        results.append({
                       'symbol': quote,
                       'slope': quote['slope'],
                       'age': quote['age']
                       })
    # dump results
    print json.dumps(results, sort_keys=True, indent=4, separators=(',', ': '))