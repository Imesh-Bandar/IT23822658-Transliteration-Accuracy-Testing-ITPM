# IT23822658 — Transliteration Accuracy Testing

Automated browser-based testing of Sinhala transliteration accuracy using **Playwright** and **Python**.
The script reads Singlish test cases from an Excel file, submits each one to the target web translator,
captures the Sinhala output, and writes the result back into the **Actual output** and **Status** columns automatically.

---

## Requirements

| Requirement | Version |
|-------------|---------|
| Python | 3.11 or 3.12 |
| pip | latest |
| Google Chrome / Chromium | Any recent version (Playwright installs Chromium automatically) |

---

## Installation (one-time setup)

### 1. Open the project folder in Command Prompt or PowerShell

```cmd
cd "E:\3rd Year\IT23822658-Transliteration-Accuracy-Testing-ITPM"
```

### 2. Create and activate a virtual environment *(recommended)*

**PowerShell:**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Command Prompt:**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

### 3. Install dependencies

```cmd
pip install -U pip
pip install playwright openpyxl
playwright install
```

> If `playwright install` fails, try: `python -m playwright install chromium`

---

## Preparing the Excel File

Open `Assignment 1 - Test cases.xlsx` and fill in the following columns **only**:

| Column | What to enter |
|--------|--------------|
| `TC ID` | Test case identifier (e.g., TC01) |
| `Input length type` | Category of input (e.g., Short, Medium, Long) |
| `Input` | The Singlish text to test |
| `Expected output` | The correct Sinhala transliteration you expect |

> ⚠️ **Do NOT manually enter values** under `Actual output` or `Status` — those are filled automatically by the script.

---

## Running the Script

### ✅ Recommended command (PowerShell)

```powershell
python test_automation.py `
  --url "https://www.pixelssuite.com/chat-translator" `
  --wait-ms 5000 `
  --type-delay-ms 80 `
  --slow-mo-ms 200 `
  --save-every 1 `
  --keep-open
```

### ✅ Recommended command (Command Prompt — single line)

```cmd
python test_automation.py --url "https://www.pixelssuite.com/chat-translator" --wait-ms 5000 --type-delay-ms 80 --slow-mo-ms 200 --save-every 1 --keep-open
```

### Minimal command (uses all defaults, auto-detects Excel file)

```cmd
python test_automation.py
```

> **Important:** Always run from **inside** the project folder. Do not add a `test_automation/` prefix to the `--excel` path.

---

## Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--excel` | Path to the Excel file with test cases | Auto-detected (`Assignment 1 - Test cases.xlsx`) |
| `--sheet` | Worksheet name inside the Excel file | `" Test cases"` |
| `--url` | URL of the transliterator web page | `https://www.pixelssuite.com/chat-translator` |
| `--wait-ms` | Time to wait (ms) after clicking Transliterate before reading output | `5000` |
| `--type-delay-ms` | Delay between each keystroke (ms) — slows down typing to mimic a human | `30` |
| `--slow-mo-ms` | Slows down all Playwright actions (ms) — useful for watching execution | `0` |
| `--save-every` | Save the Excel file after every N rows (`1` = after every row) | `1` |
| `--retries` | Number of polling retries waiting for output to appear | `8` |
| `--retry-wait-ms` | Wait time (ms) between each retry | `1000` |
| `--timeout-ms` | Maximum wait for page/element operations (ms) | `60000` |
| `--keep-open` | Keep the browser open after all rows finish | `False` |
| `--headless` | Run browser invisibly (no UI window) | `False` |
| `--output` | Path to save the result Excel file (defaults to same as `--excel`) | Same as `--excel` |
| `--header-row` | Force a specific header row number (0 = auto-detect) | `0` |

---

## How It Works

```
Excel file (test cases)
        ↓
Script reads each row (Input + Expected output)
        ↓
Chromium browser opens → navigates to translator URL
        ↓
For each test row:
  1. Types the Singlish input into the input textarea
  2. Clicks the "Transliterate" button (or presses Enter)
  3. Waits for the output textarea to update
  4. Reads the Sinhala output
  5. Compares (Unicode NFC-normalized) with Expected output
  6. Writes Actual output + Status (PASS / FAIL / COLLECTED) to Excel
  7. Saves the file incrementally
        ↓
Final Excel file with all results filled in
```

### Status values

| Status | Meaning |
|--------|---------|
| **PASS** | Actual output exactly matches the Expected output (after Unicode normalization) |
| **FAIL** | Actual output differs from the Expected output |
| **COLLECTED** | Expected output column was empty — output was captured but not compared |
| **UI Error** | Browser interaction failed for this row |

---

## Project Structure

```
IT23822658-Transliteration-Accuracy-Testing-ITPM/
├── test_automation.py            # Main Playwright automation script
├── Assignment 1 - Test cases.xlsx  # Test cases + auto-filled results
├── requirements.txt              # Python dependencies (playwright, openpyxl)
└── README.md                     # This file
```

---

## Troubleshooting

### "Excel file not found"
- Make sure you are running the command **from inside the project folder**
- Do **not** prefix the path with `test_automation/`
- The script auto-scans the folder for any `.xlsx` file if the default path fails

### Browser closes before all rows finish
- Increase `--wait-ms` (e.g., `--wait-ms 8000`) for slower internet connections
- Increase `--timeout-ms` (e.g., `--timeout-ms 90000`)

### Output not being captured (blank Actual output)
- Increase `--wait-ms` to give the translator more time to respond
- Try adding `--retries 12` for more polling attempts

### Some rows show PASS unexpectedly
- The script does an **exact** Unicode-normalized comparison
- A PASS means the tool's output **exactly** matched your Expected output column
- Open the Excel file and check the Expected output for those rows — if the tool's Sinhala is correct for that input, it is a genuine PASS
- If you believe it should fail, update the Expected output in Excel to reflect what the **correct** transliteration should be

### KeyboardInterrupt / TargetClosedError at the end
- This is harmless — it happens when `--keep-open` is active and you close the browser window manually instead of pressing `CTRL+C`
- The Excel file is saved **before** the browser keep-open loop starts, so no data is lost

---

## Notes

- The script automatically detects header row and column names using fuzzy matching — it handles variations like `Expected Output`, `Expected output`, `Expected_Output`, etc.
- Both merged cells and standard Excel cells are supported
- All Sinhala text is handled with UTF-8 / Unicode NFC normalization
- Results are saved incrementally (after every row by default) so progress is never lost if the script is interrupted
