# pse-ratings.py - a simple Python script which extracts the ratings of multiple PSE Stocks from Investing.com
# Copyright (C) 2016  John Lawrence M. Penafiel (penafieljlm@gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#   
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

import pse_rating

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print >> sys.stderr
		print >> sys.stderr, '  Usage:'
		print >> sys.stderr, '    {script} PERIOD < STOCKS'.format(script=os.path.basename(__file__))
		print >> sys.stderr, '  Where:'
		print >> sys.stderr, '    STOCKS: file'
		print >> sys.stderr, '      The name of the file containing a list of stock symbols to lookup.'
		print >> sys.stderr, '    PERIOD: "month"|"week"|uint'
		print >> sys.stderr, '      The period you are querying rating data for.'
		print >> sys.stderr, '      Can be "month", "week", or number of seconds.'
		print >> sys.stderr
		exit(22)
	period = sys.argv[1]
	for stock in sys.stdin:
		stock = stock.strip()
		print pse_rating.rating(stock, period)