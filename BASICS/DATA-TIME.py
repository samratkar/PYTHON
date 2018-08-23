1. all dates are computed from the epoch - jan 1st 1970
2. while importing you need not to use 'as' keyword as depicted in the comment below

===================================================================================================


#import time
#time.time()

import time as tm
import datetime as dt
# Time passed from epoch
tm.time()
#date
dt.datetime.fromtimestamp(tm.time())
#creating time window
delta = dt.timedelta (100)
today = dt.date.today()
print (today)
then = today - delta
print (then)
