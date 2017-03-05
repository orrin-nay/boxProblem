from random import randint
import time
import copy
import threading
start = time.time()

cMT = 0 #correctMethodTries
cMTResults = []
threads = []
tries = 100000
numOfthreds = 5
tries = int(tries/numOfthreds)*numOfthreds
print("rounded tries to %i" % tries)


def runAGame():#boxNumList,boxCheckedList
    numberList = []
    bNL = []
    bCL = []
    for i in range(0,100):
        numberList.append(i)
    for i in range(0,100):
        ranNumber = randint(0,len(numberList)-1)
        bNL.append(numberList[ranNumber])
        bCL.append(False)
        del numberList[ranNumber]
        
    secretNum = randint(0,99)
    lastBox = secretNum
    randomeBox = 0
    while(randomeBox < 50):
        #print(randomeBox)
        boxNum = bNL[lastBox];
        if(bCL[lastBox]):
            #print("box %i already checked" % lastBox)
            lastBox = randint(0,99)
            #print("box %i picked" % lastBox)
            randomeBox -= 1
        else:
            bCL[lastBox] = True;
            if(boxNum==secretNum):
                #print("box %i contanied the secret value of %i" % (lastBox,boxNum))
                return 1
            else:
                #print("box %i contained the incorrect value of %i." % (lastBox,boxNum))
                #print("moving on to box %i" % boxNum)
                lastBox = boxNum
        randomeBox += 1;
    return 0
def worker(newCMT, index):
    holderCMT = 0
    for run in range(0,int(tries/numOfthreds)):
        #print(run)
        holderCMT += runAGame()
    print("workder %i done" %index)
    newCMT.append(holderCMT)

for i in range(numOfthreds):
    t = threading.Thread(target=worker, args=(cMTResults, i))
    threads.append(t)
    t.start()
    
for i in range(len(threads)):
    threads[i].join();
    
for i in range(len(threads)):
    cMT += cMTResults[i]
    
print("After %i tries the chance of winning is %.5f%%" %(tries, (100*cMT/tries)))
end = time.time()
print("Ran in %.5f seconds" % (end - start))
