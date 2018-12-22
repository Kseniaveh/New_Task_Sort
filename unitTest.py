import unittest

import function as func


print ("*"*30)
print(func.insertion([3,2,1]))
print ("*"*30)


 
class TestStringMethods(unittest.TestCase):  
      
  def test_normal_values(self):
      self.assertEqual(func.insertion([3,2,1]), [1,2,3])
      self.assertEqual(func.quick_sort([3,2,1]), [1,2,3])
      self.assertEqual(func.Smooth_Sort([3,2,1]), [1,2,3]) 
      
  def test_except_TypeError(self):            
    with self.assertRaises(TypeError):
          func.insertion(1)
    with self.assertRaises(TypeError):
            func.quick_sort(0.5)
    with self.assertRaises(TypeError):
            func.Smooth_Sort(0)

 

if __name__ == '__main__':
    unittest.main()
            