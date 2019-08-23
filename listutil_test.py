import unittest
from listutil import unique

class ListUtilTest(unittest.TestCase):

    def test_single_item_list(self):
        self.assertListEqual( ['hi'], unique(['hi']))
        self.assertListEqual( ['dad'], unique(['dad']))
        self.assertListEqual( ['hungry'], unique(['hungry']))
        self.assertListEqual( ['computer'], unique(['computer']))
        self.assertListEqual( ['fly'], unique(['fly']))
        self.assertListEqual( ['isp'], unique(['isp']))

    def test_many_nested_list(self):
        self.assertListEqual([[1, 2, 3], [1, 2, 4], [4, 5, 6]], unique([[1,2,3],[1,2,4],[4,5,6]]))
        self.assertListEqual([[1, 2, 4], [4, 5, 6]], unique([[1,2,4],[4,5,6]]))
        self.assertListEqual([[9, 8 ,7], [4, 3, 6]], unique([[9,8,7],[9,8,7],[4,3,6]]))
        self.assertListEqual([[1, 2, 3], [1, 2, 4], [4, 5, 6], [9, 8 ,7], [4, 3, 6]], unique([[1,2,3],[1,2,4],[4,5,6],[9,8,7],[4,3,6],[4,3,6]]))

    def test_string(self):
        self.assertListEqual( ['h','e','l','o'], unique('hello'))
        self.assertListEqual( ['m','o'], unique('mom'))
        self.assertListEqual( ['t','h','a','i','l','n','d'], unique('thailand'))
        self.assertListEqual( ['d','i','s','c','r','e','t'], unique('discrete'))

    def test_integer(self):
        with self.assertRaises(TypeError):
            lst = unique(1)
        with self.assertRaises(TypeError):
            lst = unique(99)
        with self.assertRaises(TypeError):
            lst = unique(256)
        with self.assertRaises(TypeError):
            lst = unique(346)
        with self.assertRaises(TypeError):
            lst = unique(999)

    def test_nested_empty_list(self):
        self.assertListEqual([[]], unique([[],[],[]]))

    def test_empty_list(self):
        self.assertListEqual([], unique([]))

    def test_many_items_str_and_int_list(self):
        self.assertListEqual( [1,2,3,4], unique([1,2,2,3,4,4]))
        self.assertListEqual( ['abd', 'cba', 'opc', 'o', 'a', 'b'], unique(['abd', 'cba', 'opc', 'o', 'o', 'a', 'b']))
        self.assertListEqual( ['op', 4, 5, 6, 'ab'], unique(['op', 4, 4, 5, 6, 5, 'ab', 'op']))
        self.assertListEqual( ['lol','uni',78], unique(['lol','lol','uni',78,78]))

if __name__ == '__main__':
    unittest.main()