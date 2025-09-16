import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Fetch historical stock data
ticker = "AAPL"  # Apple stock
data = yf.download(ticker, start="2023-01-01", end="2024-01-01")

# Calculate moving averages
data['SMA_20'] = data['Close'].rolling(window=20).mean()
data['SMA_50'] = data['Close'].rolling(window=50).mean()

# Generate signals
data['Signal'] = 0
data['Signal'][20:] = (data['SMA_20'][20:] > data['SMA_50'][20:]).astype(int)
data['Position'] = data['Signal'].diff()

# Plot signals
plt.figure(figsize=(12,6))
plt.plot(data['Close'], label='Close Price', alpha=0.7)
plt.plot(data['SMA_20'], label='20-day SMA', alpha=0.7)
plt.plot(data['SMA_50'], label='50-day SMA', alpha=0.7)
plt.scatter(data[data['Position'] == 1].index, 
            data[data['Position'] == 1]['Close'], label='Buy Signal', marker='^', color='green')
plt.scatter(data[data['Position'] == -1].index, 
            data[data['Position'] == -1]['Close'], label='Sell Signal', marker='v', color='red')
plt.title(f'{ticker} Moving Average Crossover Strategy')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()

# Calculate returns
data['Returns'] = data['Close'].pct_change()
data['Strategy'] = data['Returns'] * data['Signal'].shift(1)

cumulative_returns = (1 + data['Strategy']).cumprod() - 1
print(f"Cumulative Returns: {cumulative_returns[-1]:.2%}")