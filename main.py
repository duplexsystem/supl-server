import time

from supl_server import *

i = 0
while True:
    try:
        suplServer = SuplServer()
        suplServer.run()
    except:
        i += 1
        if (i > 3):
            time.sleep(1)
            i = 0
