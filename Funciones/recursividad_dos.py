'''el numero A siempre se sumara asi mismo al inicio y despues a su resultado'''

def fibonaci(A,b):
    
    A += 1
    
   
    while A < 100:
        b = fibonaci(A,b) 
    
        print(b)




def main():
    fibonaci(0,0)

if __name__== '__main__':
    main()
    
    