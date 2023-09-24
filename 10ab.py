from PyPDF2 import PdfWriter, PdfReader
num = int(input("Enter page number you want combine from multiple documents "))
pdf1 = open('program.pdf', 'rb')
pdf2 = open('aimlsyll.pdf', 'rb')
pdf_writer = PdfWriter()
pdf1_reader = PdfReader(pdf1)
page = pdf1_reader.pages[num - 1]
pdf_writer.add_page(page)
pdf2_reader = PdfReader(pdf2)
page = pdf2_reader.pages[num - 1]
pdf_writer.add_page(page)
with open('output.pdf', 'wb') as output:
    pdf_writer.write(output)


////////////////



import requests,json
api_key=""
base_url ="http://api.openweathermap.org/data2.5/weather?"
city_name = input("Enter city name:")
complete_url = base_url + "appid = "+api_key+"&q="+city_name
response = requests.get (complete_url)
x= response.json()
if x["cod"]!="404":
    y=x ["main"]
Current_temperature = y[" temp"]
       Current_pressure = y[" pressure"]
       Current_humidity = y[" humidity"]
        Z= x[" weather"]
        weather_description = Z[0]["description"]
        print(" Temperature (in Kelvin unit) = " + str(Current_temperature)+ "\n atmospheric pressure (inhPa unit] ="+str(Current_pressure)+"\n Humidity (in%)="+str(Current_humidity)+"\n description="+str(weather_description))
    else:
        print(" City Not Found")
        