# IT23822658 – Transliteration Accuracy Testing (ITPM Assignment 1)

**Student:** IT23822658  
**Unit:** IT3040 – IT Project Management  
**Option:** Option 1 – Transliteration Accuracy Testing (Sinhala-familiar)  
**Target application:** https://www.pixelssuite.com/chat-translator *(Chat Sinhala function only)*

---

## Repository structure

```
.
├── test_cases_data.py                        # 50 negative test cases (Python data)
├── generate_excel.py                         # Generates the submission Excel file
├── IT23822658 - Assignment 1 - Test cases.xlsx   # Generated Excel (submission file)
└── README.md
```

---

## Test case summary

| Metric | Value |
|---|---|
| Total negative test cases | **50** |
| Singlish input types covered | **24 / 24** (all, ≥ 2 each) |
| Length S (≤ 30 chars) | 20 |
| Length M (31 – 299 chars) | 29 |
| Length L (300 – 450 chars) | 1 |

### Input types covered

1. Question forms  
2. Command forms  
3. Greetings  
4. Requests  
5. Responses  
6. Repeated Words  
7. Inputs with Punctuation Marks  
8. Romanization / Spelling Variants  
9. Isolated English Word Insertions in Singlish  
10. Multi-Word English Phrases in Singlish  
11. English Digital Terms in Singlish  
12. Platform/App Names in Singlish  
13. English Abbreviations/Acronyms in Singlish  
14. English Clipped Forms in Singlish  
15. Place Names Embedded in Singlish  
16. Person Names Embedded in Singlish  
17. Inputs with Numbers and Numeric Suffixes  
18. Inputs with Currency  
19. Inputs with Time Formats  
20. Inputs with Dates  
21. Inputs with Unit of Measurements  
22. Inputs with Slang and Casual Phrasing  
23. Online Identifiers in Singlish  
24. Inputs Containing Emojis  

---

## How to regenerate the Excel file

```bash
pip install openpyxl
python generate_excel.py
```

The script reads `test_cases_data.py` and writes  
`IT23822658 - Assignment 1 - Test cases.xlsx`.

---

## Notes

- All test case IDs begin with `Neg_` as required (negative test cases only).  
- No test case reuses an example from Appendix 1 or Appendix 2 of the assignment brief.  
- The **Actual output** column records what the Chat Sinhala transliterator at the target URL  
  actually produced when the input was submitted during testing.
