import requests
import json

cert = ('path to certificate/signed-certificate.pem', 'path to certificate/private-key.pem')

url = 'https://web.api.six-group.com/api/findata/v1/graphql'

# Define the headers for the request
headers = {
    'Content-Type': 'application/json',
}

# Define the query and variables
query = """
    query Instruments($scheme: InstrumentScheme!, $ids: [UserInputId!]!, $preferredLanguage: Language) {
        instruments(scheme: $scheme, ids: $ids, preferredLanguage: $preferredLanguage) {
            requestedId
            requestedScheme
            lookupStatus
            lookup {
                instrumentShortName
                instrumentStatus
                instrumentType
            }
            referenceData {
                instrumentBase {
                    instrumentShortName
                    instrumentNamePrefix
                    instrumentNameSuffix
                    instrumentProductName
                    valor
                    isin
                    instrumentType
                    securityType
                    instrumentStatus
                    language
                    issuer {
                        shortName
                        longName
                        lei
                        gk
                    }
                    mostLiquidMarket {
                        shortName
                        longName
                        bc
                        mic
                    }
                    nominalAmount
                    nominalCurrency
                    nominalPaidUp
                    instrumentUnitType
                    instrumentUnitSize
                    currentCouponRate
                    currentCouponType
                    maturityDate
                    maturityType
                    baseCurrency
                    tradingCurrency
                    baseCryptoSymbol
                    tradingCryptoSymbol
                    contractType
                    contractSymbol
                    underlyingInstrument {
                        shortName
                        valor
                        isin
                    }
                    ultimateUnderlyingInstrument {
                        shortName
                        valor
                        isin
                    }
                    optionType
                    optionStrikePrice
                    optionStrikePriceCurrency
                    exerciseType
                    expirationDate
                    contractSize
                    contractUnitType
                    contractMultiplier
                    sixVersionNumber
                }
            }
        }
    }
"""
variables = {
    "ids": ["CH0009980894", "IE00B5BMR087", "CH0559601544", "US0378331005", "JE00B1VS3770", "US037833AK68", "XXX"],
    "scheme": "ISIN"
}

response = requests.post(url, headers=headers, json={'query': query, 'variables': variables}, cert=cert)

pretty_r = json.dumps(json.loads(response.content), indent=2)

print(pretty_r)

# ensure the request was successful
if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")