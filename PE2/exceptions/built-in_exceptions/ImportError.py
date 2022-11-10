# Location: BaseException ← Exception ← StandardError ← ImportError

# Description: a concrete exception raised when an import operation fails

# One of these imports will fail - which one?

try:
    import math
    import time
    #import abracadabra

except:
    print('One of your imports has failed.')