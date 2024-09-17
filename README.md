Telegram to WhatsApp Message Transfer
======================================

This tool automates the transfer of messages from a Telegram group or channel to WhatsApp using Python, Telethon, and Playwright.

Author: Aaryaman Gupta
Date: 15-Sep-2024
GitHub Repository: https://github.com/BoneyGupta/Telegram-To-Whatsapp-Message-Transfer

--------------------------------------
Building the Project:
--------------------------------------

1) Clone the project to your desired directory:
   git clone git@github.com:BoneyGupta/Telegram-To-Whatsapp-Message-Transfer.git

2) Add the required libraries:

   Prerequisites:
   - Python 3.7 or later
   - pip (Python package installer)

   Installation instructions:
   - **Windows**: Download and run the get-pip.py script from https://bootstrap.pypa.io/get-pip.py.
   - **macOS/Linux**: Run the following command:
     ```
     python3 -m pip install --upgrade pip
     ```     

   After that, install the necessary libraries:
   - Install Playwright:
     ```
     pip install playwright
     ```    

   - Install Playwright browser binaries:
     ```
     playwright install
     ```     

   - Install Telethon:
     ```
     pip install telethon
     ```

3) Add the `IDs.py` file to the project directory and fill it with the following values:
   api_id = 12345678 api_hash = "abc123abc123" bot_token = "xyz456xyz456" channel_id = -7654321 group_id = "abcxyzmno"


4) Set up Google Chrome for browser automation:
- Install Google Chrome.
- Copy the folder `C:\Program Files\Google\Chrome\Application` and add it to your project directory.
- Start Chrome in remote debugging mode by running the following command:
  ```
  chrome.exe --remote-debugging-port=9988 --user-data-dir=..\\chromedata
  ```
- Once Chrome opens, login to WhatsApp Web.

5) Run the program:
   ```
    python TelegramWhatsapp.py
   ```


The program will automatically transfer messages as new events occur in the Telegram group or channel.

--------------------------------------
License:
--------------------------------------
This project is licensed under the MIT License.


