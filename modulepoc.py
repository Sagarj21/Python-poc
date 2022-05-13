import time
import mymath
from imp import reload
print("HELLO")
#module loaded only once
#for loading updated module
print("sleep for 10 secs")
time.sleep(2)
reload(mymath)
print("last line")
