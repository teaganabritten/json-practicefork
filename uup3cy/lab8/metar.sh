#!/usr/bin/bash

#!/bin/bash

# Define the URL from which to fetch the METAR data
URL="https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85"

receiptTimes=$(curl -s $URL | jq -r '.[] | .receiptTime')

echo "$receiptTimes" | head -n 6


