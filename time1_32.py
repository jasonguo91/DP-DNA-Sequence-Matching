import random
import time
import numpy
import pylab

# import our algorithms for testing
from functions1_3 import nw
from functions1_3 import forwards
from functions1_3 import backwards
from functions1_3 import hirschberg

# Read alphabet and scores from text file
f = open("scores.txt", 'r')
alphabet = f.readline()
while(alphabet[-1] in ['\n', '\r']):
    alphabet = alphabet[:-1]
f.readline()
gapPenalty = int(f.readline())
f.readline()
simMatrix = []
line = f.readline()
while(line):
    row = list(int(x) for x in line.split())
    simMatrix.append(row)
    line = f.readline()
f.close()

# Create a 1-1 mapping from characters to integers, for simplicity in algorithm
alphEnum = dict([(alphabet[i], i) for i in range(len(alphabet))])

# Change this seed to control deterministic generation of random sequences
random.seed()

# Now begin trials
trials = 100
repeats = 5

table = []
nm_array = []
nwtime_array = []
hbtime_array = []

for t in range(trials):
    n = random.randint(1, 1001)
    m = random.randint(1, 1001)
    A = B = ""
    for i in range(n):
        A += random.choice(alphabet)
    for j in range(m):
        B += random.choice(alphabet)

    # Time the nw routine   
    t0 = time.clock()
    for k in range(repeats):
        nwout = nw(A, B, simMatrix, gapPenalty, alphEnum)
    t1 = time.clock()
    nwtime = (t1 - t0)/repeats

    # Time the hirschberg routine
    t0 = time.clock()
    for k in range(repeats):
        hbout = hirschberg(A, B, simMatrix, gapPenalty, alphEnum)
    t1 = time.clock()
    hbtime = (t1 - t0)/repeats

    table.append([n, m, n*m, nwtime, hbtime])
    nm_array.append(n*m)
    nwtime_array.append(nwtime)
    hbtime_array.append(hbtime)
    
    print table[-1]

# Plot the runtime comparisons
pylab.plot(nm_array, nwtime_array, '.')
pylab.plot(nm_array, hbtime_array, 'o')
pylab.legend(('N-W', 'Hirschberg'), 2)
pylab.xlabel('nm')
pylab.ylabel('running time (s)')
pylab.title('Comparison of Needleman-Wunsch and Hirschberg Runtimes')
pylab.savefig('running_times')
pylab.show()
