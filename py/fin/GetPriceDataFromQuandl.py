# =============================================================================
# Prerequisites:
#   1. quandl
#   2. matplotlib
#   3. An API key from https://www.quandl.com/

# Install the prerequisites
#   1. launch a CMD prompt with the 'Run as Administrator' option
#   2. python -m pip install --upgrade pip
#   3. pip install quandl
#   4. pip install matplotlib

# Help Notes
#   pip list
#   pip search <module>
#   pip search quandl
# =============================================================================

# auth_tok = "<your-api-key-here>";

import quandl as ql;
data = ql.get("WIKI/MSFT", start_date="2000-01-01", end_date="2019-12-31", authtoken=auth_tok);
print(data);

import matplotlib.pyplot as plt;
data.Close.plot();
plt.show();