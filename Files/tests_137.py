import unittest
from activities_136 import nap, eat,isfunny,laugh


class activity_tests(unittest.TestCase):
    
    
    def test_eat_healthy(self):
        self.assertEqual(eat("fries",True), 'Eating fries is healthy')
    def test_eat_unhealthy(self):
        """ Eat should be healthy """
        self.assertEqual(eat('pizza',False), 'Eating pizza is junk food')

    def test_nap(self):
        self.assertEqual(nap(1),"I'm feeling refreshed after my 1 hour nap")
    def test_napp(self):
        self.assertEqual(nap(3), "ugh i overslept, i didn't mean to nap for 3 hours")
    def test_isfunny_hossam(self):
        self.assertFalse(isfunny('s'),'')
if __name__ == '__main__':
    unittest.main()

# to see comments add -v at the end
