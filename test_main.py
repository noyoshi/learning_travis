#!/usr/bin/env python3 

import unittest 
import main

class TestCalc(unittest.TestCase): 
    def test_add(self): 
        self.assertEqual(main.addme(5, 5), 10)
        self.assertEqual(main.addme(5, 0) 5)

    def test_sub(self): 
        self.assertEqual(main.subme(4, 2), 2) 
        self.assertEqual(main.subme(0, 2), -2)

    def test_mult(self): 
        self.assertEqual(main.multme(4, 2), 8)
        self.assertEqual(main.multme(2, 2), 4)

if __name__ == '__main__': 
    unittest.main()
