# PSE Tools (pse-tools)
A collection of useful Python scripts involving the Philippine Stock Exchange.

## Tools
The list of tools included in this collection are as follows:

    ### pse-quotes.py
    Python Script which retrieves PSE stock quotes from the Open PSE Initiative.
    See http://openpse.com/ for more information.

        #### Usage
        The pse-quotes.py script is invoked in the following manner:
        ```
            pse-quotes.py <stocks> --start <yyyy-mm-dd> --end <yyyy-mm-dd>
        ```
        #### Arguments
        The pse-quotes.py script takes in the following Command-Line arguments:
        ```
            stocks: required, string
                The symbols of the stocks to retrieve, separated by commas.
            start: optional, string, default='1900-01-01'
                Retrieve quotes beginning from this date.
                This date should be in yyyy-mm-dd format.
            end: optional, string, default=datetime.date.today()
                Retrieve quotes up until this date.
                This date should be in yyyy-mm-dd format.
        ```
        
        #### Input
        The pse-quotes.py script does not read anything from Standard Input.
            
        #### Output
        The pse-quotes.py script dumps the following onto Standard Output upon completion:
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
        ```

## Development Notes
This project is being implemented using Python.

## References
* Open PSE Initiative: An open-source project which aims to store end-of-day quotes from the Philippines Stock Exchange and make it available to the public through a REST API. See http://openpse.com/ for more information.

## Author(s)
* Peñafiel, John Lawrence M. (https://github.com/penafieljlm/)

## Contact
Contact me at penafieljlm@gmail.com for any questions or concerns.
