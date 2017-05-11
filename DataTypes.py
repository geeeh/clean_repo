def data_type(my_vars):
    if isinstance(my_vars, str):
        return len(my_vars)
    elif my_vars== None:
        return "no value"
    elif isinstance(my_vars, bool):
        return my_vars

    elif isinstance(my_vars, int):
        if my_vars<100:
            return "less than 100"
        elif my_vars>100:
            return"more than 100"
        else:
            return "equal to 100"
    elif isinstance(my_vars, list):
        if len(my_vars)>=3:
            return my_vars[2]
        else:
            return None


    else:
        return "please input data"

# import unittest

# class DataTypeTestCase(unittest.TestCase):
    
#   def test_none_type(self):
#     self.assertEqual('no value', data_type(None))

#   def test_array_type(self):
#     self.assertEqual(3, data_type([1, 2, 3]))

#   def test_small_array_type(self):
#     self.assertEqual(None, data_type([1, 2]))

#   def test_small_booleans_type(self):
#     self.assertEqual(True, data_type(True))

#   def test_small_integer_type(self):
#     self.assertEqual('less than 100', data_type(3))

#   def test_large_integer_type(self):
#     self.assertEqual('more than 100', data_type(200))
  
#   def test_str_type(self):
#     self.assertEqual(6, data_type('andela'))

# unittest.main()