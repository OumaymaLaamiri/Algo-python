import random
def generate(start,end):
    adr=''
    adr+= str(random.randrange(start, end))
    adr+= '.'+str(random.randrange(0, 256))
    adr+= '.'+str(random.randrange(0, 256))
    adr+= '.'+str(random.randrange(0, 256))
    return adr

file1=open("FIB.txt", "w")
file2=open("entry.txt", "w")
trace=[]
trace2=[]


for i in range(500):
    genIp=generate(0, 128)
    while (genIp in trace):
        genIp = generate(0, 128)
    trace.append(genIp)
    file1.write(genIp+ " " + random.choice('ABCDE') + '\n')

for i in range(300):
    genIp=generate(128, 192)
    while (genIp in trace):
        genIp = generate(128, 192)
    trace.append(genIp)
    file1.write(genIp+ " " + random.choice('ABCDE') + '\n')

for i in range(200):
    genIp=generate(192, 224)
    while (genIp in trace):
        genIp = generate(192, 224)
    trace.append(genIp)
    file1.write(genIp+ " " + random.choice('ABCDE') + '\n')
file1.write("0.0.0.0 " + random.choice('ABCDE'))


for i in range(100):
    genIp=generate(0, 224)
    while (genIp in trace2):
        genIp = generate(0, 224)
    trace2.append(genIp)
    file2.write(genIp+ '\n')

file1.close()
file2.close()