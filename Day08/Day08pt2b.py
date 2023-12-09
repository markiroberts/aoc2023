# python -m venv advent
# source ./advent/bin/activate
# pip install -r requirements.txt

#import os
#import sys
#import json
#from pathlib import Path
#22199
#13207
#16579
#18827
#17141
#14893

def factor(a):
    factors = []
    for x in range(a-2):
        div = x + 2
        if a % ( div ) == 0:
            factors.append(div)
    return factors

print(factor(22199))
print(factor(13207))
print(factor(16579))
print(factor(18827))
print(factor(17141))
print(factor(14893))

print(79 * 47 * 59 * 67 * 61 * 53 * 281)