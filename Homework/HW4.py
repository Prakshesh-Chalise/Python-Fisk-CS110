from collatz_conjecture import add_one
from collatz_conjecture import is_even
from collatz_conjecture import triple      
from collatz_conjecture import halve      
from collatz_conjecture import greater      
from collatz_conjecture import collatz      
from collatz_conjecture import collatz_loop
from collatz_conjecture import collatz_conjecture       
import unittest

class TestCollatzConjecture(unittest.TestCase):
  """
  Class for testing Collatz Conjecture.
  """

  def test_add_one(self):
    """
    Example of testing for add_one function

    You do not need to further test add_one
    """
    assert add_one(5) == 6
    assert add_one(-1) == 0
    assert add_one(20) == 21
    assert add_one(0) == 1

  # WRITE YOUR TESTS BELOW.
  # MAKE SURE ALL YOUR FUNCTION NAMES BEGIN WITH test_

  def test_is_even(self):

    assert is_even(5) == False
    assert is_even(20) == 21
    assert is_even(0) == 1
  
  def test_triple(self):
     
     assert triple(4) == 12
     assert triple(5) == 15
     assert triple(1) == 3
  
  def halve(self):
     
     assert halve(5)  == 2
     assert halve(10) == 5
     assert halve(15) == 7
  
  def greater(self):
     
     assert greater(-5, 5) == 5
     assert greater(4, 3) ==  4
     assert greater(2, 5) ==  5
  
  def collatz(self):
     
     assert collatz(6) == 3
     assert collatz(5) == 16
     assert collatz(2) == 1

  def collatz_loop(self):
     
     assert collatz_loop(1)  == 0
     assert collatz_loop(8)  == 3
     assert collatz_loop(5) == 5

  def collatz_conjecture(self):
     
     assert collatz_conjecture(2) == 1
     assert collatz_conjecture(5) == 7
     assert collatz_conjecture(10) == 19
   
if __name__ == '__main__':
    unittest.main()

   
   
   



