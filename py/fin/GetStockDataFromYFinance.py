# =============================================================================
# Prerequisites
#   1. yfinance
#   2. matplotlib

# Install the prerequisites
#   1. launch a CMD prompt with the 'Run as Administrator' option
#   2. python -m pip install --upgrade pip
#   3. pip install yfinance
#   4. pip install matplotlib

# Help Notes
#   pip list
#   pip search <module>
#   pip search yfinance
# =============================================================================

import yfinance as yf;
# msft = yf.Ticker("MSFT");
# data = msft.info;
# data = yf.download("MSFT", start="2000-01-01", end="2019-12-31")
data = yf.download("FB AAPL AMZN NFLX GOOGL MSFT", start="2000-01-01", end="2019-12-31")
print(data);

import matplotlib.pyplot as plt;
data.Close.plot();
plt.show();