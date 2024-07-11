import telebot
from docx2pdf import convert as doctopdf
import os
from pdf2docx import Converter
import pandas as pd
import openpyxl
bot = telebot.TeleBot('6015352484:AAEg0shL6k8fLkxq0Q2WBWryUFKxVMjagO8')

@bot.message_handler(commands=['start'])
def say(message):
    bot.send_message(message.chat.id, "Upload your Document to Convert [Note: Doc to PDF, PDF to Doc, Xlsx to CSV, CSV to Xlsx]")

@bot.message_handler(func=lambda msg: msg.text is not None and '/' not in msg.text)
def sayHi(message):
    if message.text == "Watcha Doin Fella":
         bot.reply_to(message, "Fuckin Your Mom Baby!")

    
@bot.message_handler(content_types=['document'])
def handle_document(message):
    print("Document recieved")
    file_id = message.document.file_id 
    file_info = bot.get_file(file_id)
    filename = message.document.file_name
    downloaded_file = bot.download_file(file_info.file_path)
    with open(filename, 'wb') as new_file:
        new_file.write(downloaded_file)
    
    conversion_options = {
        'PDF': 17,   # PDF format
        'XLSX': 51,  # Excel format
        'CSV': 6,    # CSV format
        'DOCX': 16,  # Word format
    }
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=3)
    for option in conversion_options:
        keyboard.add(telebot.types.KeyboardButton(option))
    bot.send_message(message.chat.id, 'Select a format to convert to:', reply_markup=keyboard)
    bot.register_next_step_handler(message, docstopdf, filename)
  
def docstopdf(message, filename):
    conversion_type = message.text
    print(conversion_type)
    try:
        if(conversion_type == 'PDF'):
            doctopdf(filename)
            with open(f'{os.path.splitext(filename)[0]}.{conversion_type.lower()}', 'rb') as f:
                bot.send_document(message.chat.id, f)
        
        elif(conversion_type == "DOCX"):
            cv_obj = Converter(filename)
            cv_obj.convert(filename+".docx")
            cv_obj.close()
            newmane = filename+".docx"
            with open(f'{os.path.splitext(newmane)[0]}.{"docx"}', 'rb') as f:
                bot.send_document(message.chat.id, f)

        elif(conversion_type == "CSV"):
            read_file = pd.read_excel(filename)
            read_file.to_csv (filename+".csv", index = None, header=True)
            newmane = filename+".csv"
            with open(f'{os.path.splitext(newmane)[0]}.{"csv"}', 'rb') as f:
                bot.send_document(message.chat.id, f)
        
        elif(conversion_type == "XLSX"):
            read_file = pd.read_csv(filename)
            read_file.to_excel(filename+".xlsx", index = None, header=True)
            newmane = filename+".xlsx"
            with open(f'{os.path.splitext(newmane)[0]}.{"xlsx"}', 'rb') as f:
                bot.send_document(message.chat.id, f)

        else:
            bot.send_message(message.chat.id, 'Unsupperted Format')
        
    except:
         bot.send_message(message.chat.id, 'An Exception Occured')
bot.polling()



