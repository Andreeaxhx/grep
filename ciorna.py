import re
from termcolor import colored

regex=re.compile(r"\d+")


file=open("words.txt")
lines=file.readlines()
for line in lines:
    print(regex)
    m=re.findall(regex, line)
    print(m)
    if m:
        for i in m:
            lista=line.split(i, 1)
            line=lista[0]+colored(i, 'red')+lista[1]
        print(line)
