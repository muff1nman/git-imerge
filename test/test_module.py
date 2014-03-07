#! /usr/bin/env python

"""

"""

import unittest

class TestProjectStructure(unittest.TestCase):

    #def setUp(self):
        #self.seq = range(10)

    def test_can_find_module():
        try:
            import gitimerge
        except ImportError:
            print("Could not import gitimerge.. is the project setup correctly?")



if __name__ == '__main__':
    unittest.main()
