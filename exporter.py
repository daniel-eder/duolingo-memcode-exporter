import asyncio
import duolingo
import xlsxwriter
from googletrans import Translator

async def main():
    username = input("Username: ")
    jwt = input("JWT: ")
    duo = duolingo.Duolingo(username=username, jwt=jwt)
    translator = Translator()


    vocabulary = duo.get_vocabulary(language_abbr="es")
    spanish_words = list(map(lambda word: word["word_string"], vocabulary["vocab_overview"]))

    ##translations = [translator.translate(s, src='es', dest='de').text for s in spanish_words]


    workbook = xlsxwriter.Workbook('known_words.xlsx')
    worksheet = workbook.add_worksheet()
    #worksheet.write("A1", "German")
    #worksheet.write("B1", "Spanish")
    #worksheet.write_column('A2', translations)
    #worksheet.write_column('B2', spanish_words)
    worksheet.write_column('A2', spanish_words)
    workbook.close()

asyncio.run(main())