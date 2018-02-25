import re
import sys

with open(sys.argv[1], 'r') as myfile:
    data = myfile.read()

host_re = re.search(r'Port ID$', data, re.DOTALL | re.M)

data = data[host_re.start() + 8:]

host_re = re.findall(r'^([A-Za-z0-9._-]+) ?', data, re.DOTALL | re.M)

host_re1 = re.findall(r' +(.+?)\s{2,}.*?\s+([A-Za-z]+[^CISCO0-9]\s?\d.*?)$', data, re.S | re.M)

for i in list(zip(host_re, host_re1)):
    print(i)
