import unittest
import reader

class testNetwork(unittest.TestCase):

    def test_reader(self):
        G = reader.makeGraph('./struct_data/csv/test.csv')
        self.assertEqual(12, len(G.nodes))

if __name__ == '__main__':
    unittest.main()
