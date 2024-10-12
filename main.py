
import streamlit as st
import requests

r = requests.get('https://api.coinlore.net/api/tickers/')  # r yerine response'da yazılabilir
veri = r.json()

coinler = veri['data']

coinfiyat = {}

for coin in coinler:
    sembol = coin['symbol']
    fiyat = coin['price_usd']

    coinfiyat.update({sembol: float(fiyat)})

# print(coinfiyat)

coinisimler = coinfiyat.keys()

coin1=st.sidebar.selectbox('Eldeki Coin',coinisimler)
miktar=st.sidebar.number_input('Miktar')
coin2=st.sidebar.selectbox('Hedef Coin',coinisimler)

c1 = coinfiyat.get(coin1)
miktar = 20
c2 = coinfiyat.get(coin2)

sonuc=miktar * c1 / c2

st.write(miktar,'adet',coin1,sonuc,'adet',coin2)
st.link_button('Satın Al',f'https://www.coinbase.com/tr/converter/{coin1}/{coin2}')