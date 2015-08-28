# PSE Tools (pse-tools)
A Collection of Programs and Scripts Involving the Philippine Stock Exchange

## Tools
The list of tools included in this collection are as follows:

### pse-quotes.py
Python Script which retrieves PSE stock quotes from the Open PSE Initiative.
See http://openpse.com/ for more information.

Usage
```
    pse-quotes.py <stocks> --start <yyyy-mm-dd> --end <yyyy-mm-dd>
```
    
Output
```
    {
        "status": <status-code>,
        "data": [
            {
                "name": "<stock-name>",
                "price_close": "<closing-price>",
                "price_high": "<high-price>",
                "price_low": "<low-price>",
                "price_open": "<opening-price>",
                "quote_date": "<yyyy-mm-dd>",
                "symbol": "<stock-symbol>",
                "volume": <trade-volume>
            }
        ]
    }
