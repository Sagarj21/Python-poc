import os
try:
    print("try")
    os._exit(0)
except ValueError:
    print("a")
finally:
    print("fin")