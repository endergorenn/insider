# My Pytest Selenium Project

This project is a testing framework that utilizes Selenium with pytest to perform browser automation tests on both Firefox and Chrome browsers.

## Project Structure

```
my-pytest-selenium-project
├── tests
│   ├── test_example.py
│   └── conftest.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd my-pytest-selenium-project
   ```

2. **Install dependencies:**
   Make sure you have Python installed. Then, install the required packages using pip:
   ```
   pip install -r requirements.txt
   ```

3. **WebDriver Setup:**
   Ensure you have the appropriate WebDriver executables for Chrome and Firefox installed and available in your system's PATH. You can download them from:
   - [ChromeDriver](https://sites.google.com/chromium.org/driver/)
   - [GeckoDriver (Firefox)](https://github.com/mozilla/geckodriver/releases)

## Running Tests

To run the tests, use the following command:
```
pytest tests/
```

## Test Cases

The test cases are located in the `tests/test_example.py` file. They utilize Selenium to open web pages, interact with elements, and assert expected outcomes for both browsers.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.