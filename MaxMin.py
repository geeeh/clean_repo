def maxmin(vars):
    y=[]
    m=vars[0]
    z=vars[0]
    if not isinstance(vars,list):
        return "only lists allowed"

    else:
        for x in vars:
            if x<z:
                z=x
                
            elif x>m:
                m=x

            else:
                pass

        y.append([z,m])

    return y

            

