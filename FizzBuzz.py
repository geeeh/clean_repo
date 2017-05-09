
def fizz_buzz(my_value):
    if not isinstance(my_value, int):
        return "only integers allowed"
    else:     

        if my_value%3==0 and not my_value%5==0:
            return "Fizz"
        elif my_value%5==0 and not my_value%3==0:
            return "Buzz"
        elif my_value%3==0 and my_value%5==0 :
            return "FizzBuzz"
        else:
            return my_value


    

        
    
