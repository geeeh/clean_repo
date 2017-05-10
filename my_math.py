class My_math():
    def __init__(self):
        pass


    def get_prime_numbers(self,n):
        p=[]
                
        if not isinstance(n, int):
            raise TypeError("only int arguments allowed")
        else:
            if n<2 and n>0:
                return p
            elif n<0:
                return "argument should be greater than 0"
                
            else:
                for x in range(2, n):
                    for y in range(2, x):
                        if(x%y==0): 
                            break

                    else:
                        p.append(x)

                return p        


# stf= My_math()
# print(stf.get_prime_numbers(1000))                  
