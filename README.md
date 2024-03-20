Financial Data API Client


This project provides a Python interface for interacting with the Financial Data API provided by SIX Group, allowing for easy access to financial instruments' data and market data. It includes functionality to perform secure API requests for instrument reference data and market data timeseries.

Features
Securely fetch financial instruments' data using custom certificates.
Parse and handle financial data in JSON format.
Access end-of-day historical data for financial listings.
Easy integration into financial analysis tools and workflows.
Prerequisites
Before you begin, ensure you have met the following requirements:

Python 3.6 or later.
SSL certificates provided by SIX Group for authentication.
Installation
Clone this repository to your local machine using:

sh

Copy code

git clone [https://](https://github.com/alexlanderzander/SIXAPIGRAPHQLPYTHON.git

Navigate into the project directory:

sh
Copy code
cd financial-data-api-client
Install the required dependencies:

sh
Copy code
pip install -r requirements.txt
Configuration
Place your SSL certificate (signed-certificate.pem) and private key (private-key.pem) in a secure directory accessible by the script. Update the certificate_path in the FinancialDataAPI class constructor to point to this directory.

Usage
To use the Financial Data API client, you can instantiate the FinancialDataAPI class and call its methods with appropriate parameters. For example:

python
Copy code
from financial_data_api import FinancialDataAPI

# Initialize the API client
findata = FinancialDataAPI('/path/to/your/certificates')

# Fetch basic instrument data
instrument_data = findata.instrumentBase("ISIN", ["BE6342120662"])
print(instrument_data)
Replace '/path/to/your/certificates' with the actual path to your certificate and key files.

Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This project utilizes the Financial Data API provided by SIX Group. It is an independent project and not officially affiliated with SIX Group.

