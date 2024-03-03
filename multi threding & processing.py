print("_______multithreading_______")

import threading
import time
from concurrent.futures import ThreadPoolExecutor
def fun(second):
    print(f"sleeping for {second} second")
    time.sleep(second)
    #print(f"sleeping for {second} second")
    return second

#normal code
#t=time.time()
#fun(4)
#fun(2)   # for this 3 fn call function will execute one by one 
#fun(1)
#print("\n",time.time()-t)

def main():   
    #code using multithreading
    t=time.time()
    t1=threading.Thread(target=fun,args=[4])
    t2=threading.Thread(target=fun,args=[2])
    t3=threading.Thread(target=fun,args=[1])
    #we have created 3 thread using above code 
    
    t1.start()
    t2.start()  #this will simply start the process of thread,so it will show 0 sec for execution
    t3.start()
    
    t1.join()
    t2.join()  # wait until thread procees is completely executed.
    t3.join()
    print("\n",time.time()-t)

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(fun,3)
        future2 = executor.submit(fun,2)
        future3 = executor.submit(fun,4)
        print(future1.result())
        print(future2.result())
        print(future3.result())
        #l = [3,5,1,2]
        #results = executor.map(fun,l)
        #for result in results:
        #    print(results)



print("_______multiprocessing_______")

import multiprocessing
import requests 
from concurrent.futures import ProcessPoolExecutor

def downloadfile(url,name):
    print(f"started downloading {name}")
    response = requests.get(url)
    open(f"file{name}.jpg","wb").write(response.content)
    print(f"Finished downloading {name}")

if __name__ == '__main__':   
    url="https://picsum.photos/200/300"
    #pros=[]
    #
    #for i in range(1,6):
    #    #normal code which will download jpg one by one
    #    #downloadfile(url,f"file{i}")
    #    p=multiprocessing.Process(target=downloadfile , args = [url,f"file{i}"])
    #    p.start()
    #    pros.append(p)
    #
    #for p in pros:
    #    p.join()
    
    ##by using concurrent module
    with ProcessPoolExecutor() as executor:
        l1=[url for i in range(10)]  #To generate and handle different URLs for each task
        l2=[i for i in range(1,11)]
        results = executor.map(downloadfile,l1,l2)
        for r in results:
            print(r)