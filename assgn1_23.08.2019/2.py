# Program to create a threaded class and run the 2 task in 1 program parallelly and print the result. 


import threading 

class Thread:
    def print_cube(num): 
        print("Cube: {}".format(num * num * num))
  
    def print_square(num): 
        print("Square: {}".format(num * num)) 

    # creating threads 
    t1 = threading.Thread(target=print_square, args=(5,)) 
    t2 = threading.Thread(target=print_cube, args=(10,)) 
  
    t1.start()   # starting thread 1 
    t2.start()   # starting thread 2
  
    t1.join()    # wait until thread 1 is completely executed 
    t2.join()    # wait until thread 2 is completely executed 
    
    print("Done!") 

