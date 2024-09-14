# Stock Trader

A quick script setup in python to trade stocks. 

## Setup and Run
1. Install requirements: `pip install -r requirements.txt`
2. Create a file called "token" in the directory with main.py, and put your Robinhood password there.
3. Create a file called "username" in the directory with main.py and put your Robinhood username there.
4. Run the script: `python main.py`
5. Follow the instructions to enter your MFA code (if it's your first time logging in on this computer).
6. Enjoy!

Please note: robin-stocks (the wrapper for the Robinhood API this project uses) is accessing a private Robinhood API.
Robinhood does not offer a public API, and does not necessarily want users to access its private API. Use the API as little as you can.
Use at your own risk!
