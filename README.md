# AG_Grid_Finance_Demo

Test automation suite for the AG-Grid Finance demo page, built with Python, Selenium and the Page Object Model. It verifies core functionality and data integrity of the finance grid UI component, runs locally from the terminal, and generates HTML reports.

**Live Demo:** https://www.ag-grid.com/example-finance/

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running Tests](#running-tests)
- [Test Coverage](#test-coverage)
- [Test Reports](#test-reports)
- [Troubleshooting](#troubleshooting)

## Overview

This test automation suite validates the AG-Grid Finance demo application by testing:
- Data sorting and filtering
- Column data type validation
- Grid interaction and DOM manipulation
- Filter functionality

All tests are implemented using Python 3.9+ and Selenium WebDriver, with automated HTML report generation.

## Requirements

### Test Coverage
This suite verifies the following functionality of the Finance demo grid:

1. **Sorting Functionality**
   - Verify that the grid can be sorted by the "Ticker" column in descending order

2. **Instrument Column Validation**
   - Ensure that the cells in the "Instrument" column contain one of the following values:
     - Bond
     - ETF
     - Crypto
     - Stock

3. **Numeric Columns Validation**
   - Confirm that the cells in the following columns contain numeric values:
     - P&L
     - Total Value
     - Quantity
   - The check fails if a column can't be read or no cells were checked, so a change to the page can't make it pass silently
   - (The demo no longer has a Price column, so Price is not checked)

4. **Additional Tests**
   - **Column Docking/Positioning:** Verify the grid allows dragging and repositioning columns
   - **Filtering:** Filter the Instrument column by Bond, Crypto, ETF and Stock and check that each filter returns rows

5. **Test Strategy**
   - Generate HTML reports for regression tracking
   - Use explicit waits with timeouts to handle dynamic content
   - Handle stale element references gracefully with retries

## Project Structure

```
AG_Grid_Finance_Demo/
├── README.md                                    # This file
├── requirements.txt                            # Python dependencies
├── run_tests_for_html_report.py                # Main test runner
├── Pages/
│   ├── __init__.py
│   └── finance_grid_page.py                    # Page Object Model
├── Tests/
│   ├── __init__.py
│   ├── test_ticker_sorting.py                  # Sorting
│   ├── test_instrument_validation.py           # Instrument validation
│   ├── test_other_columns_validation.py        # Numeric columns
│   ├── test_additional_docking_ticker_column.py# Column docking
│   └── test_additional_filtering_instrument_column.py  # Filtering
└── reports/                                    # HTML reports (generated, not committed)

```

## Setup Instructions

### Prerequisites
- Python 3.9 or higher
- macOS, Linux, or Windows
- Google Chrome browser
- Git (optional, for version control)

### Step 1: Clone the Project
```bash
git clone https://github.com/jkoshchanov/ag_grid_finance_demo_selenium_ui_python.git
cd ag_grid_finance_demo_selenium_ui_python
```

### Step 2: Create Virtual Environment
```bash
python3 -m venv .venv
```

### Step 3: Activate Virtual Environment
**macOS/Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### Step 4: Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 5: Verify Installation
```bash
pip list
```

You should see:
- `selenium` (version 4.36.0 or higher)
- `html-testRunner` (version 1.2.1 or higher)

## Running Tests

### Run All Tests with HTML Report
```bash
python run_tests_for_html_report.py
```

This command:
- Discovers all tests in the `Tests/` directory
- Executes tests sequentially
- Generates individual HTML reports in the `reports/` directory (created automatically; reports are not committed to the repo)
- Displays results in the terminal

### Run Individual Test File
```bash
python -m unittest Tests.test_ticker_sorting
python -m unittest Tests.test_instrument_validation
python -m unittest Tests.test_other_columns_validation
python -m unittest Tests.test_additional_docking_ticker_column
python -m unittest Tests.test_additional_filtering_instrument_column
```

### Run with Verbose Output
```bash
python -m unittest discover -s Tests -p "test_*.py" -v
```

## Test Coverage

| Test | File | Purpose | Status |
|------|------|---------|--------|
| Sort Ticker Descending | `test_ticker_sorting.py` | Verify grid sorting by ticker | ✅ Passing |
| Instrument Validation | `test_instrument_validation.py` | Validate instrument column values | ✅ Passing |
| Numeric Columns | `test_other_columns_validation.py` | Verify numeric data in P&L, Total Value, Quantity | ✅ Passing |
| Column Docking | `test_additional_docking_ticker_column.py` | Test column repositioning | ✅ Passing |
| Search & Filter | `test_additional_filtering_instrument_column.py` | Verify each instrument filter returns rows | ✅ Passing |

## Test Reports

### Accessing Reports
After running tests, view the HTML reports:

```bash
# Open specific report
open reports/Test_Report_test_ticker_sorting.TestTickerSorting_*.html

# List all reports
ls -lh reports/
```

### Report Contents
Each HTML report includes:
- Test execution summary (Pass/Fail/Error)
- Individual test results with execution time
- Error messages and stack traces (if any)
- Test start and end timestamps

## Troubleshooting

### Issue: "Command not found: python"
**Solution:** Use `python3` instead or ensure Python is in PATH
```bash
python3 run_tests_for_html_report.py
```

### Issue: Module not found errors (selenium, html-testRunner)
**Solution:** Ensure virtual environment is activated and packages are installed
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### Issue: Tests hang or timeout
**Solution:** This has been fixed with:
- 2-second timeouts on element waits
- 100-iteration safety limits per column
- Automatic retry logic for stale elements
- Graceful error handling with early loop exits

### Issue: Chrome browser crashes
**Solution:** Ensure you have a modern version of Chrome installed and Selenium WebDriver is compatible
```bash
pip install --upgrade selenium
```

### Issue: StaleElementReferenceException
**Solution:** This is handled automatically with retry logic in `retrieve_x_position()` and exception handling in `get_column_text()`

## Key Implementation Details

### Page Object Model
The `Pages/finance_grid_page.py` file implements:
- Locators for all grid elements (headers, cells, filters)
- Wait conditions for dynamic content
- Helper methods for sorting, filtering, and validation
- Exception handling for web driver interactions

### Test Data
- **Instrument values:** Bond, ETF, Crypto, Stock
- **Numeric columns:** P&L, Total Value, Quantity
- **Grid rows:** Approximately 50+ rows (scrollable)

### Waits and Timeouts
- Implicit waits: 10 seconds (default)
- Explicit waits: 2-10 seconds (specific operations)
- Retry attempts: Up to 3 times for stale elements

## Maintenance

### Updating Tests
If the AG-Grid Finance demo page structure changes:
1. Update XPath locators in `Pages/finance_grid_page.py`
2. Re-run tests to identify broken selectors
3. Use browser debugger to find new element paths

### Adding New Tests
1. Create test file in `Tests/` directory
2. Import `FinanceGridPage` from `Pages.finance_grid_page`
3. Inherit from `unittest.TestCase`
4. Implement `setUp()` and `tearDown()` methods
5. Add test method(s) starting with `test_`

Example:
```python
import unittest
from selenium import webdriver
from Pages.finance_grid_page import FinanceGridPage

class MyNewTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.page = FinanceGridPage(self.driver)
    
    def test_my_new_test(self):
        # Test implementation
        pass
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
```

## Notes

- Tests use Chrome WebDriver exclusively
- Tests maximize the browser window for consistency
- Each test creates a new driver instance for isolation
- Grid data is live and may change; tests validate structure/format, not specific values
- HTML reports are timestamped to avoid overwriting previous results
