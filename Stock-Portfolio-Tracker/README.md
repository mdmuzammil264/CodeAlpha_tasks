# Stock Portfolio Tracker

**CodeAlpha Python Programming Internship — Task 3**

## Description
A simple console-based stock portfolio tracker that calculates the total investment value based on manually defined (hardcoded) stock prices. The user enters stock names and quantities, and the program displays a summary with the total value.

## Features
- Hardcoded dictionary of stock prices (AAPL, TSLA, GOOGL, AMZN, MSFT)
- User can add multiple stocks with quantities
- Calculates and displays total investment value
- Shows a formatted portfolio table
- Optionally saves the result to a `portfolio.csv` file

## How to Run
```bash
python task2_stock_tracker.py
```
1. Enter a stock symbol (from the list shown)
2. Enter the quantity you hold
3. Repeat for more stocks, or type `done` to finish
4. View your portfolio summary
5. Choose `yes` to save the result as a CSV file

## Sample Output
```
Stock      Qty      Price      Value
----------------------------------------
AAPL       10       $180       $1800
TSLA       5        $250       $1250
----------------------------------------
TOTAL                          $3050
```

## Hardcoded Stock Prices
| Stock | Price |
|-------|-------|
| AAPL  | $180  |
| TSLA  | $250  |
| GOOGL | $140  |
| AMZN  | $175  |
| MSFT  | $310  |

## Key Concepts Used
`dictionary`, `input/output`, `basic arithmetic`, `file handling (optional)`