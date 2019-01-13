from Singleton_Inherited import *

import unittest
import logging
import sys
import copy

class Singleton_Test(unittest.TestCase):
    def test_many_instances_same_class(self):
        f1=F1()
        f2=F1()
        self.assertTrue(f1==f2)

        f1=F2()
        f2=F2()
        self.assertTrue(f1==f2)

        s1=S1_F1()
        s2=S1_F1()
        self.assertTrue(s1==s2)

        s1=S1_F2()
        s2=S1_F2()
        self.assertTrue(s1==s2)

        t1=T1_S1F1()
        t2=T1_S1F1()
        self.assertTrue(t1==t2)

        t1=T1_S2F1()
        t2=T1_S2F1()
        self.assertTrue(t1==t2)

    def test_different_classes(self):
        list_of_singletons=[F1(),
                            F2(),
                            S1_F1(),
                            S2_F1(),
                            S1_F2(),
                            S2_F2(),
                            T1_S1F1(),
                            T2_S1F1(),
                            T1_S2F1(),
                            T2_S2F1]

        for counter, element in enumerate(list_of_singletons):
            for another_element in list_of_singletons[:counter]:
                self.assertFalse(element==another_element)


if __name__ == '__main__':
    unittest.main()

