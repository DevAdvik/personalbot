import requests

coindata = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false&price_change_percentage=1h%2C24h%2C7d')

# For no.1 coin
name1 = str(coindata.json()[0]['name'])
priceusd1 = str(coindata.json()[0]['current_price'])
symbol1 = str(coindata.json()[0]['symbol']).upper()
pricechange1 = str(coindata.json()[0]['price_change_percentage_24h'])[0:5]

# For no.2 coin
name2 = str(coindata.json()[1]['name'])
priceusd2 = str(coindata.json()[1]['current_price'])
symbol2 = str(coindata.json()[1]['symbol']).upper()
pricechange2 = str(coindata.json()[1]['price_change_percentage_24h'])[0:5]

# For no.3 coin
name3 = str(coindata.json()[2]['name'])
priceusd3 = str(coindata.json()[2]['current_price'])
symbol3 = str(coindata.json()[2]['symbol']).upper()
pricechange3 = str(coindata.json()[2]['price_change_percentage_24h'])[0:5]

# For no.4 coin
name4 = str(coindata.json()[3]['name'])
priceusd4 = str(coindata.json()[3]['current_price'])
symbol4 = str(coindata.json()[3]['symbol']).upper()
pricechange4 = str(coindata.json()[3]['price_change_percentage_24h'])[0:5]

# For no.5 coin
name5 = str(coindata.json()[4]['name'])
priceusd5 = str(coindata.json()[4]['current_price'])
symbol5 = str(coindata.json()[4]['symbol']).upper()
pricechange5 = str(coindata.json()[4]['price_change_percentage_24h'])[0:5]

# For no.6 coin
name6 = str(coindata.json()[5]['name'])
priceusd6 = str(coindata.json()[5]['current_price'])
symbol6 = str(coindata.json()[5]['symbol']).upper()
pricechange6 = str(coindata.json()[5]['price_change_percentage_24h'])[0:5]

# For no.7 coin
name7 = str(coindata.json()[6]['name'])
priceusd7 = str(coindata.json()[6]['current_price'])
symbol7 = str(coindata.json()[6]['symbol']).upper()
pricechange7 = str(coindata.json()[6]['price_change_percentage_24h'])[0:5]

# For no.8 coin
name8 = str(coindata.json()[7]['name'])
priceusd8 = str(coindata.json()[7]['current_price'])
symbol8 = str(coindata.json()[7]['symbol']).upper()
pricechange8 = str(coindata.json()[7]['price_change_percentage_24h'])[0:5]

# For no.9 coin
name9 = str(coindata.json()[8]['name'])
priceusd9 = str(coindata.json()[8]['current_price'])
symbol9 = str(coindata.json()[8]['symbol']).upper()
pricechange9 = str(coindata.json()[8]['price_change_percentage_24h'])[0:5]

# For no.10 coin
name10 = str(coindata.json()[9]['name'])
priceusd10 = str(coindata.json()[9]['current_price'])
symbol10 = str(coindata.json()[9]['symbol']).upper()
pricechange10 = str(coindata.json()[9]['price_change_percentage_24h'])[0:5]


#Storing required details in a variable
mdet1 = str("1. "+name1+"("+symbol1+"): $"+priceusd1+" ("+pricechange1+"%)")
mdet2 = str("2. "+name2+"("+symbol2+"): $"+priceusd2+" ("+pricechange2+"%)")
mdet3 = str("3. "+name3+"("+symbol3+"): $"+priceusd3+" ("+pricechange3+"%)")
mdet4 = str("4. "+name4+"("+symbol4+"): $"+priceusd4+" ("+pricechange4+"%)")
mdet5 = str("5. "+name5+"("+symbol5+"): $"+priceusd5+" ("+pricechange5+"%)")
mdet6 = str("6. "+name6+"("+symbol6+"): $"+priceusd6+" ("+pricechange6+"%)")
mdet7 = str("7. "+name7+"("+symbol7+"): $"+priceusd7+" ("+pricechange7+"%)")
mdet8 = str("8. "+name8+"("+symbol8+"): $"+priceusd8+" ("+pricechange8+"%)")
mdet9 = str("9. "+name9+"("+symbol9+"): $"+priceusd9+" ("+pricechange9+"%)")
mdet10 = str("10. "+name10+"("+symbol10+"): $"+priceusd10+" ("+pricechange10+"%)")

marketdetails = mdet1+'\n'+mdet2+'\n'+mdet3+'\n'+mdet4+'\n'+mdet5+'\n'+mdet6+'\n'+mdet7+'\n'+mdet8+'\n'+mdet9+'\n'+mdet10
#marketdetails variable now hold info about Top10 Crypto Currencies
