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

            

def find_max_min(vars):
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

        y.append(z)
        y.append(m)
        if z==m:
            v=[len(vars)]
            return v

    return y
# import unittest

# class MaxMinTest(unittest.TestCase):
#     """docstring for MaxMinTest"""

#     def test_find_max_min_four(self):
#         self.assertListEqual([1, 4],
#                              find_max_min([1, 2, 3, 4]),
#                              msg='should return [1,4] for [1, 2, 3, 4]')

#     def test_find_max_min_one(self):
#         self.assertListEqual([4, 6],
#                              find_max_min([6, 4]),
#                              msg='should return [4, 6] for [6, 4]')

#     def test_find_max_min_two(self):
#         self.assertListEqual([2, 78],
#                              find_max_min([4, 66, 6, 44, 7, 78, 8, 68, 2]),
#                              msg='should return [2, 78] for [4, 66, 6, 44, 7, 78, 8, 68, 2]')

#     def test_find_max_min_three(self):
#         self.assertListEqual([1, 4],
#                              find_max_min([1, 2, 3, 4]),
#                              msg='should return [1,4] for [1, 2, 3, 4]')

#     def test_find_max_min_identity(self):
#         self.assertListEqual([4],
#                              find_max_min([4, 4, 4, 4]),
#                              msg='Return the number of elements in the list in a new list if the `min` and `max` are equal')            
# unittest.main()
