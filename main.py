import time
#edit on branch edit2
#print(time.time())
tic = time.time()
print("hello world")
tac = time.time()
print("printing 'Hello World' used {} seconds".format(tac - tic))
from comm_tools.io import read_csv
print("时间=>",time.time())