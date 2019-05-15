from unittest import TestCase
from Fibonacci import fibonacci_loop, fibonacci_rec

# Test Class 
class TestExample01(TestCase):
    def setUp(self):
        self.FSequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        self.F30 = 832040
        self.F50 = 12586269025

    def tearDown(self):
        pass

    def test_fibonacci_loop(self):
        for i in range(13):
            self.assertEqual(self.FSequence[i], fibonacci_loop(i))
        self.assertEqual(self.F30, fibonacci_loop(30))
        self.assertEqual(self.F50, fibonacci_loop(50))
    
    def test_fibonacci_rec(self):
        for i in range(13):
            self.assertEqual(self.FSequence[i], fibonacci_rec(i))
        self.assertEqual(self.F30, fibonacci_rec(30))