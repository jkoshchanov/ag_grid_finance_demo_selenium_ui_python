# Instrument filter: filter the Instrument column by Bond, Crypto, ETF and Stock
# and check that each filter returns rows.

import unittest
from selenium import webdriver
from Pages.finance_grid_page import FinanceGridPage

instrument_filters = ["Bond", "Crypto", "ETF", "Stock"]

class TestSearchAndFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.page = FinanceGridPage(self.driver)

    def test_search_and_filter(self):
        row_counts = self.page.search_and_filter(instrument_filters)
        for instrument in instrument_filters:
            self.assertGreater(row_counts.get(instrument, 0), 0,
                               msg=f"Filtering by '{instrument}' returned no rows")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()