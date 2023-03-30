import pyttsx3
import PyPDF2

print('1.How To Win Friends\n2.Think and Grow Rich')
choice = int(input('Book you want to listen: '))

if choice == 1:
    book = open('D:\Python Projects\Project-TexttoSpeech\HowtoWinFriends.pdf' , 'rb')
elif choice == 2:
    book = open('D:\Python Projects\Project-TexttoSpeech\ThinkandGrowRich.pdf' , 'rb')
else:
    print('Invalid Choice!!')

inp = int(input('Input Page Number:: '))

pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
speaker = pyttsx3.init()
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 120)
sound = speaker.getProperty('voices')
speaker.setProperty('voice', sound[1].id)

for num in range(inp,pages):
    page = pdfReader.getPage(num)
    print('You are on page',num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()