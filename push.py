import os
with open("push.sh") as f:
	for i in f.read().splitlines():
		os.system(i)
