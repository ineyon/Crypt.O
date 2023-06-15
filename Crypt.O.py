# -*- coding: utf-8 -*-
import requests
import json
import tkinter as tk
from tkinter import ttk, font, Canvas, Entry

# створення вікна
window = tk.Tk()

# функція кнопки
def calculate_button():
    getBestChainFunc()

window.title('CRYPT.o')

window.geometry('892x553')
window.resizable(False,False)

window.configure(background='#2B2B2B')

# ініціалізація шрифту

customFont20 = font.Font(family='Chakra Petch', size=20)
customFont15 = font.Font(family='Chakra Petch', size=15)
customFont10 = font.Font(family='Chakra Petch', size=8)

# створення заокругленого квадрату для інтерфейсу

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

# створення віджетів  
canvas = Canvas(window, width=892, height=553, background='#2B2B2B', highlightthickness=0)
canvas.pack()

canvas.create_rectangle(0,0,892,13, fill='#FF9900')

rectangleFromPanel = round_rectangle(29,73,231,226, radius=28, fill="#363636")
rectangleFromCoin = round_rectangle(41,114,219,154, radius=28, fill="#FF9900")
rectangleFromPrice = round_rectangle(41,164,219,204, radius=28, fill="#535353")

rectangleToPanel = round_rectangle(29,286,231,439, radius=28, fill="#363636")
rectangleToCoin = round_rectangle(41,327,219,367, radius=28, fill="#FF9900")
rectangleToPrice = round_rectangle(41,377,219,417, radius=28, fill="#535353")

rectangleCalculateButton = round_rectangle(29,468,231,526, radius=28, fill="#FF9900")
rectangleCalculateResult = round_rectangle(253,468,869,526, radius=28, fill="#363636")

rectanglePricePanel = round_rectangle(253,73,869,439, radius=28, fill="#363636")

rectangleCoinPanel1 = round_rectangle(281,98,841,151, radius=28, fill="#535353")
rectangleCoinPanel2 = round_rectangle(281,164,841,217, radius=28, fill="#535353")
rectangleCoinPanel3 = round_rectangle(281,230,841,283, radius=28, fill="#535353")
rectangleCoinPanel4 = round_rectangle(281,296,841,349, radius=28, fill="#535353")
rectangleCoinPanel5 = round_rectangle(281,362,841,415, radius=28, fill="#535353")

button = tk.Button(window, text="", width=25, height=3, bg="#FF9900", relief=tk.FLAT, highlightthickness=0, command=calculate_button)
button.place(x=38, y=470)

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
labelToText = ttk.Label(master=window, text = 'To', font =customFont15, background='#363636', foreground='white')
labelToText.place(x=117, y=286)
labelCalculateText = ttk.Label(master=window, text = 'Calculate', font =customFont15, background='#FF9900', foreground='white')
labelCalculateText.place(x=89, y=476)
labelBestChainText = ttk.Label(master=window, text = 'Best chain :', font =customFont10, background='#363636', foreground='white')
labelBestChainText.place(x=295, y=483)

entryFromCoin = Entry(window, background='#FF9900',foreground='white',justify='center', borderwidth=0, font=customFont15,width=12)
entryFromCoin.place(x=50,y=115)
entryFromPrice = Entry(window, background='#535353',foreground='white',justify='center', borderwidth=0, font=customFont15,width=12)
entryFromPrice.place(x=50,y=165)

entryToCoin = Entry(window, background='#FF9900',foreground='white',justify='center', borderwidth=0, font=customFont15,width=12)
entryToCoin.place(x=50,y=327)
labelToPrice = ttk.Label(window, background='#535353',foreground='white',justify='center', borderwidth=0, font=customFont15,width=12)
labelToPrice.place(x=50,y=377)

def get_coin_price(coin, exchange, side):
    if exchange.lower() == 'binance':
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}USDT"
        response = requests.get(url)
        data = json.loads(response.text)
        price = float(data['price'])
    elif exchange.lower() == 'coinbase':
        url = f"https://api.coinbase.com/v2/prices/{coin.upper()}-USD/{side.lower()}"
        response = requests.get(url)
        data = json.loads(response.text)
        price = float(data['data']['amount'])
    else:
        price = None
    return price

coins = ['btc', 'eth', 'doge', 'ltc', 'bch']
exchanges = ['binance', 'coinbase']
sides = ['buy', 'sell']



def getBestChainFunc():
    
    best_coin_pair = ''
    best_percentage = 0.00
    best_buy_exchange = ''
    best_sell_exchange = ''
    best_buy_price = 0
    best_sell_price = 0
    
    for coin in coins:
        for buy_exchange in exchanges:
            for sell_exchange in exchanges:
                if buy_exchange == sell_exchange:
                    continue
                buy_price = get_coin_price(coin, buy_exchange, 'buy')
                sell_price = get_coin_price(coin, sell_exchange, 'sell')
                if buy_price is None or sell_price is None:
                    continue
                percentage = (sell_price - buy_price) / buy_price * 100
                if percentage > best_percentage:
                    best_coin_pair = coin.upper()
                    best_percentage = percentage
                    best_buy_exchange = buy_exchange.capitalize()
                    best_sell_exchange = sell_exchange.capitalize()
                    best_buy_price = buy_price
                    best_sell_price = sell_price
                            
                    best_percentage = round(best_percentage, 2)
                            
                    best_chain_text = f"Best chain: {best_coin_pair} "
                    best_chain_text += f"Percentage: {best_percentage}% "
                    best_chain_text += f"bought on: {best_buy_exchange} ;"
                    best_chain_text += f"sold on: {best_sell_exchange} ;"
                    best_chain_text += f"Buy price: {best_buy_price} "
                    best_chain_text += f"Sell price: {best_sell_price}"

                    labelBestChainText.config(text=best_chain_text)

def get_binance_price(coin):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}USDT"
    response = requests.get(url)
    data = json.loads(response.text)
    buy_price = float(data['price'])
    
    url_sell = f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}USDT"
    response_sell = requests.get(url_sell)
    data_sell = json.loads(response_sell.text)
    sell_price = float(data_sell['price'])
    
    return f"{coin.upper()}, Binance Buy: {buy_price}, Binance Sell: {sell_price}"


# оновлення інтерфейсу
def update_interface():
   
    btc_info = get_binance_price('btc')
    eth_info = get_binance_price('eth')
    doge_info = get_binance_price('doge')
    ltc_info = get_binance_price('ltc')
    bch_info = get_binance_price('bch')

    labelCoin1.config(text=btc_info)
    labelCoin2.config(text=eth_info)
    labelCoin3.config(text=doge_info)
    labelCoin4.config(text=ltc_info)
    labelCoin5.config(text=bch_info)
    window.after(1000, update_interface)

update_interface()
# запуск вікна
window.mainloop()
