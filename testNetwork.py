import unittest
import read

class testNetwork(unittest.TestCase):

    def test_read(self):
        G = read.makeGraph('./struct_data/csv/test.csv')
        self.assertEqual(12, len(G.nodes))
        self.assertEqual(10, len(G.edges))


if __name__ == '__main__':
    unittest.main()
