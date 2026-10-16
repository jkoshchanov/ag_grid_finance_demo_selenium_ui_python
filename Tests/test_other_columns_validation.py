# Numeric column validation: every cell in the P&L, Total Value and Quantity
# columns must be numeric.

import unittest
from selenium import webdriver
from Pages.finance_grid_page import FinanceGridPage

# Keys are the grid's col-id values (the live demo's P&L id is literally "p&amp;l").
# The demo no longer has a Price column: it now shows Ticker, Timeline, Instrument,
# P&L, Total Value and Quantity, so Price is not checked.
numeric_columns = {"p&amp;l": "P&L",
                   "totalValue": "Total Value",
                   "quantity": "Quantity"}

class TestNumericColumnValidation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.page = FinanceGridPage(self.driver)

    def test_validate_numeric_columns(self):
        all_valid, msg = self.page.is_all_cells_valid(numeric_columns)
        self.assertTrue(all_valid, msg=msg)

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()