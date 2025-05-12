import unittest
from solution import encode, decode

class TestTopKFrequent(unittest.TestCase):
    def test_basic_case(self): # self refers to the test case instance
        print("\nTESTING BASIC CASE")
        list = ["I", "Love", "Boba", "Tea"]
        
        encoded = encode(list)
        decoded = decode(encoded)
        print(encoded)
        print(decoded)


        
        # self.assertEqual()
        

if __name__ == '__main__':
    unittest.main() 