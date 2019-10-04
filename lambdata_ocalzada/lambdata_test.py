import unittest
from df_utils import Splitter
import pandas as pd

class TestSplitter(unittest.TestCase):
    '''Testing Splitter function.'''

    def test_splitter1(self):
        df = pd.DataFrame({'Owner City State Zip': ["Fontana, CA 92336", "Los Angeles, CA 90006",
                        "Salt Lake City, UT 84106", "Brookline, MA 02445"]})
        s = Splitter(df)
        new_df = s.split_address()
        self.assertEqual(new_df.shape, (4,3))


if __name__ == '__main__':
    unittest.main()