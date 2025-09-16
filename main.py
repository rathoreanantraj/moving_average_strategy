import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import warnings

# Ignore warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Fetch historical stock data
ticker = "TSLA"  # Use a volatile stock like Tesla
data = yf.download(ticker, start="2020-01-01", end="2024-01-01")

# Calculate moving averages
data['SMA_Short'] = data['Close'].rolling(window=20).mean()
data['SMA_Long'] = data['Close'].rolling(window=50).mean()

# Generate trading signals
data['Signal'] = (data['SMA_Short'] > data['SMA_Long']).astype(int)
data['Position'] = data['Signal'].diff()

# Debug: See number of trades triggered
print("Trade Signal Counts:\n", data['Position'].value_counts())

# Plot signals
plt.figure(figsize=(14,7))
plt.plot(data['Close'], label='Close Price', alpha=0.7)
plt.plot(data['SMA_Short'], label='20-day SMA', alpha=0.7)
plt.plot(data['SMA_Long'], label='50-day SMA', alpha=0.7)

# Buy signals
plt.scatter(data[data['Position'] == 1].index, 
            data[data['Position'] == 1]['Close'], 
            label='Buy Signal', marker='^', color='green', s=100)

# Sell signals
plt.scatter(data[data['Position'] == -1].index, 
            data[data['Position'] == -1]['Close'], 
            label='Sell Signal', marker='v', color='red', s=100)

plt.title(f'{ticker} Moving Average Crossover Strategy')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()

# Calculate returns
data['Returns'] = data['Close'].pct_change()
data['Strategy'] = data['Returns'] * data['Signal'].shift(1)
data.dropna(inplace=True)

cumulative_returns = (1 + data['Strategy']).cumprod() - 1
print(f"\nCumulative Returns: {cumulative_returns.iloc[-1]:.2%}")