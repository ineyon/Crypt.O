# -*- coding: utf-8 -*-
import requests
import tkinter as tk
from tkinter import ttk, font, Canvas, Entry

#створення вікна
window = tk.Tk()

window.title('CRYPT.o')

window.geometry('892x553')
window.resizable(False,False)

window.configure(background='#2B2B2B')

#ініціалізація шрифту

customFont20 = font.Font(family='Chakra Petch', size=20)
customFont15 = font.Font(family='Chakra Petch', size=15)
customFont10 = font.Font(family='Chakra Petch', size=10)

#створення заокругленого квадрату для інтерфейсу

def round_rectangle(x1, y1, x2, y2, radius=25, **kwargs):
        
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)

#створення віджетів  
canvas = Canvas(window, width=892, height=553, background='#2B2B2B', highlightthickness=0)
canvas.pack()

canvas.create_rectangle(0,0,892,13, fill='#FF9900')

rectangleFromPanel = round_rectangle(29,73,231,226, radius=28, fill="#363636")
rectangleFromCoin = round_rectangle(41,114,219,154, radius=28, fill="#FF9900")
rectangleFromPrice = round_rectangle(41,164,219,204, radius=28, fill="#535353")

rectangleToPanel = round_rectangle(29,286,231,439, radius=28, fill="#363636")
rectangleToCoin = round_rectangle(41,327,219,367, radius=28, fill="#FF9900")
rectangleToPrice = round_rectangle(41,377,219,417, radius=28, fill="#535353")

rectangleCalcucateButton = round_rectangle(29,468,231,526, radius=28, fill="#FF9900")
rectangleCalcucateResult = round_rectangle(253,468,869,526, radius=28, fill="#363636")

rectanglePricePanel = round_rectangle(253,73,869,439, radius=28, fill="#363636")

rectangleCoinPanel1 = round_rectangle(281,98,841,151, radius=28, fill="#535353")
rectangleCoinPanel2 = round_rectangle(281,164,841,217, radius=28, fill="#535353")
rectangleCoinPanel3 = round_rectangle(281,230,841,283, radius=28, fill="#535353")
rectangleCoinPanel4 = round_rectangle(281,296,841,349, radius=28, fill="#535353")
rectangleCoinPanel5 = round_rectangle(281,362,841,415, radius=28, fill="#535353")

labelCoin1 = ttk.Label(master=window, text = 'Updating...', font =customFont10, background='#535353', foreground='white')
labelCoin1.place(x=295, y=111)
labelCoin2 = ttk.Label(master=window, text = 'Updating...', font =customFont10, background='#535353', foreground='white')
labelCoin2.place(x=295, y=177)
labelCoin3 = ttk.Label(master=window, text = 'Updating...', font =customFont10, background='#535353', foreground='white')
labelCoin3.place(x=295, y=243)
labelCoin4 = ttk.Label(master=window, text = 'Updating...', font =customFont10, background='#535353', foreground='white')
labelCoin4.place(x=295, y=309)
labelCoin5 = ttk.Label(master=window, text = 'Updating...', font =customFont10, background='#535353', foreground='white')
labelCoin5.place(x=295, y=374)

labelProgramName = ttk.Label(master=window, text = 'CRYPT.o', font =customFont20, background='#2B2B2B', foreground='white')
labelProgramName.place(x=80, y=18)
labelFromText = ttk.Label(master=window, text = 'From', font =customFont15, background='#363636', foreground='white')
labelFromText.place(x=105, y=74)
labelFromText = ttk.Label(master=window, text = 'To', font =customFont15, background='#363636', foreground='white')
labelFromText.place(x=117, y=286)
labelFromText = ttk.Label(master=window, text = 'Calculate', font =customFont15, background='#FF9900', foreground='white')
labelFromText.place(x=89, y=476)
labelFromText = ttk.Label(master=window, text = 'Best chain :', font =customFont10, background='#363636', foreground='white')
labelFromText.place(x=295, y=483)

entryFromCoin = Entry(window, background='#FF9900',foreground='white',justify='center', borderwidth=0, font=customFont15,width=12)
entryFromCoin.place(x=50,y=115)
entryFromPrice = Entry(window, background='#535353',foreground='white',justify='center', borderwidth=0, font=customFont15,width=12)
entryFromPrice.place(x=50,y=165)

entryToCoin = Entry(window, background='#FF9900',foreground='white',justify='center', borderwidth=0, font=customFont15,width=12)
entryToCoin.place(x=50,y=327)
labelToPrice = ttk.Label(window, background='#535353',foreground='white',justify='center', borderwidth=0, font=customFont15,width=12)
labelToPrice.place(x=50,y=377)

#запуск вікна
window.mainloop()
