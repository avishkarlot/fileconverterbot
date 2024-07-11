# fileconverterbot
This is a Telegram bot that helps you convert documents between different formats. The bot supports conversion of the following document types:
DOCX to PDF
PDF to DOCX
XLSX to CSV
CSV to XLSX

Prerequisites
Before running the bot, make sure you have the following installed:

Python 3.x
Installation
Clone this repository to your local machine and navigate into the project directory:

sh
Copy code
git clone <repository_url>
cd <repository_name>
Install the required Python dependencies using pip and the requirements.txt file:

sh
Copy code
pip install -r requirements.txt
Setting Up
Obtain a Telegram Bot API token from BotFather.
Replace the placeholder token in the code (bot.py) with your actual Telegram Bot API token.
Running the Bot
Run the bot using the following command:

sh
Copy code
python bot.py
Usage
Start a chat with your bot on Telegram.
Send the /start command to the bot.
Upload a document to the bot. Supported formats are DOCX, PDF, XLSX, and CSV.
The bot will prompt you to select a format to convert the document to.
The bot will convert the document and send the converted file back to you.
