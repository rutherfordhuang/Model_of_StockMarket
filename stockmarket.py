from random import normalvariate
from sys import exit

# a small model of stock trading in China. Contains 2 stocks with different variations.
# Author: Hefu, from Dpet. Materials, Oxford


def price(list, beta):
	
# set the beta/standard variation
	risk = list[-1] * beta 
# assume that the variation follows normal distribution
	rand = normalvariate(0,risk * 2)
# 0.01 is the natural return rate of stock with same level of risks.
	delta = list[0] * risk / 20 + rand	
# set limitation of +/- 10% just as the regulation in China	
	if delta > risk:
		delta = risk
	elif delta < - risk:
		delta = - risk
	else:
		pass 
# get the new price
	new = list[-1] + delta
	new = round(100 * new) / 100
	list.append(new)
	return list
	

def decide(pricea, priceb):
	global cash 
	global holda 
	global holdb
	global quit

# this loop is for buy-in and sell-out within one day
	while True:
		print '*' * 30
		print 'Day: %d The information are listed here:' % day
		print 'Price          A: %f        B: %f' % (prices[0], prices[1])
		print 'Your account:  A: %d        B: %d' % (stocks[0], stocks[1])
		print '               Cash:', cash, '\n'
		print 'What do you want to do?'
		print '1. Buy in   2. Sell out   3. Hold    4.Quit'
		choice = raw_input('> ')
		
		if int(choice) == 1:
			buy()
		elif int(choice) == 2:
			sell()
		elif int(choice) == 3:
			break
		elif int(choice) == 4:
			cash = cash + prices[0] * stocks[0] + prices[1] * stocks[1]
			stocks[0] = stocks[1] = 0
			quit = 1
			break
		else:
			print 'Cannot understand'
			
			
def main():
# define how much money you start, and how many stocks you have, for stockA and stockB.
	global a
	global b
	global cash 
	global holda 
	global holdb
	global day
	global quit
# prices are the list of recent prices of stockA and stockB
	global prices 
# stocks are the list of how many stocks you have now
	global stocks
# the start price of stockA and stockB
	a = [10]
	b = [10]
	day = 1
	cash = 10000
	holda = 0
	holdb = 0
	prices = [a[-1], b[-1]]
	stocks = [holda, holdb]
	 
# this loop is to carry on
	while True:
		print '-' * 30
		decide(a[-1], b[-1])
# generate new prices and update prices
		a = price(a, 0.02)
		b = price(b, 0.01)
		prices = [a[-1], b[-1]]
		day += 1
# when decide to quit, it comes here
		if quit == 1:
			break
			
	print 'now you have', cash
	
def buy():
	global cash
	global holda
	global holdb
	global prices
	global stocks
	
	print 'which one you want to buy: 1. A     2. B '
# this is to use the list we defined: prices and stocks
	buywhich = int(raw_input('> ')) - 1
# make sure you have enough money to buy the stocks
	if buywhich != 0 and buywhich != 1:
		print 'not allowed'
	else:
		buymany = int(raw_input('how many you want to buy\n>'))
		if prices[buywhich] * buymany <= cash:
			cash -= prices[buywhich] * buymany
			stocks[buywhich] += buymany
		else: 
			print 'insufficient money', '!'*20
	
	
def sell():
	global cash
	global holda
	global holdb
	global prices
	global stocks
	
	print 'which one you want to sell: 1. A     2. B '
	sellwhich = int(raw_input('> ')) - 1
# make sure you have enough stocks to sell
	if sellwhich != 0 and sellwhich != 1:
		print 'not allowed', '!'*20
	else:
		sellmany = int(raw_input('how many you want to buy\n>'))
		if sellmany <= stocks[sellwhich]:
			cash += prices[sellwhich] * sellmany
			stocks[sellwhich] -= sellmany
		else: 
			print 'insufficient stocks'
	
	
main()
	
