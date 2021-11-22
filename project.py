# -*- coding: utf-8 -*-

'''
By: Diego Gómez
diegoalejandrogomezg@gmail.com

Description: 
The script looks for matching between the NBA's players from a integer number 
that is provided by the user and generate a list of all pairs of players whose 
height added are equal to the number given.

For a Mach Eight "Sample Project" assigamnet.
(2021)
'''

import csv
import requests
import logging
import io
import datetime
import time
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


## Function main for set the connection and data list format.
def main(url):
	logging.info('Welcome to NBA player heights searcher!')
	logging.info('Loading data from {}...'.format(url))
	time.sleep(2)
	os.system("clear")

	## Requests to the data location.
	response = requests.get(url, headers = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"})
	conn = response.status_code

	if conn == 200:
		response = response.content
		logging.info('Data successfully obtained!')

		data = csv.reader(io.StringIO(response.decode('utf-8')), delimiter=",")
		next(data)
		data = list(data)

		select = int(input('''
			Choose an option:

			[1] Do match
			[2] Exit
		'''))

		if select == 1:
			matcher(data)
		else:
			os.system("clear")
			pass
	
	else:
		logging.info('Connection could not be established!')

		select = int(input('''
			Choose an option:

			[1] Search 
			[2] Exit
		'''))

		if select == 1:
			start(url)
		else:
			os.system("clear")
			pass

def matcher(data):
	
	## The number is the user input for do match in players.
	number = int(input('Please, enter a number: '))

	os.system("clear")

	logging.info('Searching...')
	stTime = datetime.datetime.now()

	## Create a list with players who match with filter for save only unique results.
	hits = 0
	result = []

	for idx, row in enumerate(data):
		player = int(idx)
		player_height = data[idx][3]

		for i, row in enumerate(data):
			if player != i:
				match = int(player_height) + int(row[3])

				if match == number:
					if player > i:
						add = (row[1]+" "+row[0],data[player][1]+" "+data[player][0])
					else:
						add = (data[player][1]+" "+data[player][0],row[1]+" "+row[0])
					if add not in result:
						result.append(add)
						hits += 1

	## Calculate time take for the query.
	endTime = datetime.datetime.now()
	takeTime = endTime - stTime

	os.system("clear")
	
	## Printable results with resume by query
	if hits > 0:
		print('''             OUTPUT''')
		for matching in result:
			print('''-------------------------------
 {} and {}'''.format(matching[0],matching[1]))
		print('''-------------------------------''')

		print('''
 ------------------------------------------------
| {} | {} matches were found in {}! |
 ------------------------------------------------ '''.format(number,hits,takeTime))

	else:
		print("No matches found for ",number)

	select = int(input('''
			Choose an option:

			[1] New
			[2] Exit
		'''))

	if select == 1:
		matcher(data)
	else:
		os.system("clear")
		pass

if __name__ == '__main__':
	os.system("clear")
	url = 'https://www.openintro.org/data/csv/nba_heights.csv'
	main(url)