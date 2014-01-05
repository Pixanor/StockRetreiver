# I am bored hence the test file.

import yahoostock
from pprint import pprint
# pprint(ystockquote.get_historical_prices('GOOG', '2011-01-03', '2013-01-08'))

print(yahoostock.get_price_book('GOOG'))
print(yahoostock.get_bid_realtime('GOOG'))

# Try 1 : Shit ~ Too long to query historical price.
# Try 2 : OoOoooO ... Looks like its working.
# Try 3 : Confirm Working. -> Push to Staging.
