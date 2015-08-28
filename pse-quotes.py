#! /usr/bin/python

"""
    Python Script which retrieves PSE stock quotes from the Open PSE Initiative.
    See http://openpse.com/ for more information.
"""
__author__ = "John Lawrence M. Penafiel"
__copyright__ = "Copyright 2015, John Lawrence M. Penafiel"
__credits__ = ["John Lawrence M. Penafiel"]
__maintainer__ = ["John Lawrence M. Penafiel"]
__email__ = "penafieljlm@gmail.com"
__status__ = "Prototype"

import argparse
import datetime
import json
import requests

if __name__ == "__main__":
    # define date type
    def date(value):
        try:
            return datetime.date(*(int(x) for x in value.split('-')))
        except:
            raise argparse.ArgumentTypeError("%s is an invalid date value" % value)
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('stocks',
                        help='the symbols of the stocks to retrieve, separated by commas')
    parser.add_argument('-s', '--start',
                        type=date,
                        help='[yyyy-mm-dd] retrieve quotes beginning from this date',
                        default=datetime.date(1900, 1, 1).__str__())
    parser.add_argument('-e', '--end',
                        type=date,
                        help='[yyyy-mm-dd] retrieve quotes up until this date',
                        default=datetime.date.today().__str__())
    args = parser.parse_args()
    # prepare request url
    query = 'http://openpse.com/api/quotes/?stocks={stock}&from_date={start}&to_date={end}'.format(stock=args.stock, start=args.start, end=args.end)
    # perform actual request
    response = requests.get(query)
    # prepare results
    results = {
        'status': response.status_code,
        'data': []
    }
    if response.status_code == 200:
        results['data'] = json.loads(response.text)
    # dump output
    print json.dumps(results, sort_keys=True, indent=4, separators=(',', ': '))