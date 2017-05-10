def word_counter(y):
    
    if not isinstance(y, str):
        return("only string allowed")
    else:
        g = y.lower().split()
        v = {}
        for x in g:
            if x in v:
                v[x] += 1
            else:
                v[x] = 1
        return v
    
        

# print(word_counter("ho many many Many"))