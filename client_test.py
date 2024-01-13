import unittest
from client3 import getDataPoint
from client3 import getRatio


class ClientTest(unittest.TestCase):

    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (
                quote['top_bid']['price'] + quote['top_ask']['price'])/2))
            # ^returns test data from function, then controlled data(stock name, bid price, ask price, average) to compare

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (
                quote['top_bid']['price'] + quote['top_ask']['price'])/2))
            # ^returns test data from function, then controlled data(stock name, bid price, ask price, average) to compare

    """ ------------ Add more unit tests ------------ """
# ----------------returns price a, divided by price b/make sure program exits when b=0, see what happens when a=0

    def test_getRatio_checkForZeroDivision(self):
        # numDump = [117.87, 2.00, 121.84, 119.2]
        # for x in range(len(numDump)):
        #     price_a = numDump[x], x=+1
        #     price_b = numDump[x]
        #     self.assertRaises(TypeError, getRatio(
        #         price_a, price_b), (price_a/price_b))
        #     print("---" + str(price_a) + "---" + str(price_b) + "---")

        price_a = price_b = 0
        print("\nPrice a: ", price_a, "\nPrice b: ", price_b)
        # simpler way to test if getRatio returns none and not ZeroDiv error
        self.assertIsNone(getRatio(price_a, price_b))


# --------------------------------------------------
if __name__ == '__main__':
    unittest.main()
