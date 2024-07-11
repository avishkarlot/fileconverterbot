Certainly! Here's a Markdown format for your `README.md` file:

```markdown
# Document Conversion Bot

This Telegram bot facilitates document conversion between various formats including DOCX, PDF, XLSX, and CSV.

## Prerequisites

- Python 3.x
- Installation of necessary libraries listed in `requirements.txt`

## Installation

Clone the repository:
```sh
git clone <repository_url>
cd <repository_name>
```

Install dependencies:
```sh
pip install -r requirements.txt
```

## Setup

1. Obtain a Telegram Bot API token from [BotFather](https://core.telegram.org/bots#botfather).
2. Replace the placeholder token in `bot.py` with your actual Telegram Bot API token.

## Running the Bot

Run the bot:
```sh
python bot.py
```

## Usage

1. Start a chat with your bot on Telegram.
2. Send the `/start` command to the bot.
3. Upload a document. Supported formats are DOCX, PDF, XLSX, and CSV.
4. Select a format to convert the document to using the provided options.
5. The bot will convert the document and send it back to you.

## Code

```python
# Python code snippet from bot.py
import telebot
from docx2pdf import convert as doctopdf
import os
from pdf2docx import Converter
import pandas as pd
import openpyxl

# Bot setup and message handling functions
# (Insert relevant code snippet from bot.py here)
```

## License

This project is licensed under the MIT License.

```

Replace `<repository_url>` and `<repository_name>` with your actual repository details. This Markdown file provides a structured overview of your bot's functionality, installation instructions, setup process, usage guidelines, and a placeholder for including a code snippet from `bot.py`.
