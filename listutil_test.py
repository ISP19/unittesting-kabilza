import unittest
from listutil import unique

class ListUtilTest(unittest.TestCase):

    def test_single_item_list(self):
        self.assertListEqual( ['hi'], unique(['hi']))
        self.assertListEqual( ['dad'], unique(['dad']))
        self.assertListEqual( ['hungry'], unique(['hungry']))

    def test_many_nested_list(self):
        self.assertListEqual([[1, 2, 3], [1, 2, 4], [4, 5, 6]], unique([[1,2,3],[1,2,4],[4,5,6]]))

    def test_string(self):
        self.assertListEqual( ['h','e','l','o'], unique('hello'))
        self.assertListEqual( ['m','o'], unique('mom'))
        self.assertListEqual( ['t','h','a','i','l','n','d'], unique('thailand'))

    def test_integer(self):
        with self.assertRaises(TypeError):
            lst = unique(1)
        with self.assertRaises(TypeError):
            lst = unique(99)
        with self.assertRaises(TypeError):
            lst = unique(256)

    def test_nested_empty_list(self):
        self.assertListEqual( [[]], unique([[],[],[]]))

    def test_empty_list(self):
        self.assertListEqual( [], unique([]))

    def test_many_items_list(self):
        self.assertListEqual( [1,2,3,4], unique([1,2,2,3,4,4]))
        self.assertListEqual( ['abd', 'cba', 'opc', 'o', 'a', 'b'], unique(['abd', 'cba', 'opc', 'o', 'o', 'a', 'b']))
        self.assertListEqual( ['op', 4, 5, 6, 'ab'], unique(['op', 4, 4, 5, 6, 5, 'ab', 'op']))

if __name__ == '__main__':
    unittest.main()