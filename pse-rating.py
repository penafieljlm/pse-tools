# pse-rating.py - a simple Python script which extracts the rating of a PSE Stock from Investing.com
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

import json
import lxml.html
import os
import requests
import sys

HOME_URL = 'http://www.investing.com'

SEARCH_URL = '{home}/search/service/search'.format(home=HOME_URL)
SEARCH_COUNTRYID = 45
SEARCH_QUERY = 'search_text={stock}&term={stock}&country_id={country}&tab_id=Stocks'.format(stock='{stock}', country=SEARCH_COUNTRYID)
SEARCH_HEADERS = {
	'Host': 'www.investing.com',
	'Proxy-Connection': 'keep-alive',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Origin': 'http://www.investing.com',
	'X-Requested-With': 'XMLHttpRequest',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Accept-Language': 'en-US,en;q=0.8'
}

VALUE_HEADERS = {
	'Host': 'www.investing.com',
	'Proxy-Connection': 'keep-alive',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Origin': 'http://www.investing.com',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
	'Content-Type': 'text/html',
	'Accept-Language': 'en-US,en;q=0.8'
}

def search(stock):
	query = SEARCH_QUERY.format(stock=stock)
	response = requests.post(SEARCH_URL, headers=SEARCH_HEADERS, data=query)
	if response.status_code == 200:
		return json.loads(response.text[1:])
	return None

def page(stock):
	results = search(stock)
	if results is None:
		return None
	for result in results['All']:
		if result['symbol'] == stock:
			return '{home}{link}-technical'.format(home=HOME_URL, link=result['link'])
	return None

def rating(stock, period):
	if period != 'week' and period != 'month' and not period.isdigit():
		return None
	if period.isdigit() and int(period) < 0:
		return None
	rating_page = page(stock)
	if rating_page is None:
		return None
	url = '{page}?period={period}'.format(page=rating_page, period=period)
	response = requests.get(url, headers=VALUE_HEADERS)
	if response.status_code != 200:
		return None
	tree = lxml.html.fromstring(response.content)
	return tree.xpath('//div[@class="summary"]/span/text()')[0]

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print >> sys.stderr
		print >> sys.stderr, '  Usage:'
		print >> sys.stderr, '    {script} STOCK PERIOD'.format(script=os.path.basename(__file__))
		print >> sys.stderr, '  Where:'
		print >> sys.stderr, '    STOCK: string'
		print >> sys.stderr, '      The symbol of the stock you are querying rating data for.'
		print >> sys.stderr, '    PERIOD: "month"|"week"|uint'
		print >> sys.stderr, '      The period you are querying rating data for.'
		print >> sys.stderr, '      Can be "month", "week", or number of seconds.'
		print >> sys.stderr
		exit(22)
	stock = sys.argv[1]
	period = sys.argv[2]
	print rating(stock, period)