# Basic configuration for the project

# List of stocks to analyze
TICKERS = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']

# Start date for historical data
START_DATE = '2020-01-01'

# End date for Historical data
END_DATE = '2025-01-01'


# Main Stocks for Modeling
TARGET_TICKERS = ['AAPL', 'MSFT', 'AMZN']
TEST_SIZE = 0.2
RANDOM_STATE = 42
LSTM_SEQ_LEN = 30