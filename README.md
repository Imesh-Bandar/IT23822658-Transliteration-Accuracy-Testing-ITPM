# IT23822658 - Transliteration Accuracy Testing

Automated test automation project for Sinhala transliteration accuracy testing using Playwright and Python. This project automates browser-based testing of transliteration functionality and records test results in Excel format.

## Requirements

- **Python 3.11 or higher**
- **Google Chrome** or Chromium (Playwright will install Chromium automatically if needed)
- **pip** (Python package manager)

## Installation

### 1. Clone or Download the Project

```bash
cd path/to/your/project
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the virtual environment:

**On Windows (PowerShell):**

```bash
.\venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**

```bash
venv\Scripts\activate.bat
```

**On macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
playwright install
```

## Running the Project

### Basic Execution

```bash
python test_automation.py
```

### With Custom Parameters

```bash
python test_automation.py \
  --url "https://www.pixelssuite.com/chat-translator" \
  --wait-ms 5000 \
  --type-delay-ms 80 \
  --slow-mo-ms 200 \
  --save-every 1 \
  --keep-open
```

### Command-Line Options

| Option            | Description                                      | Default                                       |
| ----------------- | ------------------------------------------------ | --------------------------------------------- |
| `--excel`         | Path to the Excel file containing test cases     | Auto-detected                                 |
| `--url`           | Target URL to test                               | `https://www.pixelssuite.com/chat-translator` |
| `--wait-ms`       | Wait time before execution starts (milliseconds) | 5000                                          |
| `--type-delay-ms` | Delay between keystrokes (milliseconds)          | 30                                            |
| `--slow-mo-ms`    | Slow down execution for debugging (milliseconds) | 0                                             |
| `--save-every`    | Save results after each test case                | 1                                             |
| `--keep-open`     | Keep the browser open after execution            | False                                         |
| `--retries`       | Number of retries for failed operations          | 8                                             |
| `--timeout-ms`    | Operation timeout (milliseconds)                 | 60000                                         |

## Project Structure

```
├── test_automation.py          # Main automation script
├── README.md                   # This file
├── requirements.txt            # Python dependencies
└── Assignment 1 - Test cases.xlsx   # Test cases and results spreadsheet
```

## How It Works

1. Reads test cases from an Excel file with columns for:
   - Test ID (TCID)
   - Singlish Input
   - Expected Sinhala Output
   - Actual Output (populated by automation)
   - Status (Pass/Fail)

2. Opens the specified URL in a browser
3. For each test case, enters the Singlish input and captures the transliteration output
4. Compares actual output with expected output
5. Saves results back to the Excel file

## Troubleshooting

### Playwright Installation Issues

If `playwright install` fails, try:

```bash
python -m playwright install chromium
```

### Excel File Not Found

Ensure the Excel file is in the project directory or specify the full path with `--excel` parameter.

### Connection Timeout

Increase `--wait-ms` and `--timeout-ms` values for slower connections.

## Notes

- The script automatically detects header columns in the Excel file
- Results are saved incrementally based on the `--save-every` parameter
- The project supports both merged cells and standard Excel formatting
- UTF-8 encoding is used for proper Sinhala script handling
