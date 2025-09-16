# Moving Average Crossover Strategy

A simple backtesting project implementing a moving average crossover trading strategy using Python.

## Overview
This project simulates a trading strategy where:
- Buy when the 20-day SMA crosses **above** the 50-day SMA.
- Sell when the 20-day SMA crosses **below** the 50-day SMA.

It uses historical data fetched via Yahoo Finance.

## Tech Stack
- Python
- Pandas
- Matplotlib
- yFinance

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/moving_average_strategy.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python main.py
   ```

## Output
- Graph with buy/sell signals.
- Final cumulative returns printed in the console.