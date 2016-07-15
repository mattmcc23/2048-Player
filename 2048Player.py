from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

browser = webdriver.Firefox()
browser.get("https://gabrielecirulli.github.io/2048/")

game = browser.find_element_by_class_name('container')
scoreText = browser.find_element_by_class_name('score-container')
message = browser.find_element_by_class_name('game-message')
retry = browser.find_element_by_class_name('retry-button')

numGames = 3
currentGame = 0

topScore = -1

if len(sys.argv) > 1:
	numGames = int(sys.argv[-1])

print('Playing ' + str(numGames) + ' games of 2048:')

while currentGame < numGames:
	while message.is_displayed() == False:
		game.send_keys('wasd')
	currentGame += 1
	scoreMessage = scoreText.text.split('\n')
	score = int(scoreMessage[0])
	if score > topScore:
		topScore = score
	print('Game ' + str(currentGame) + ': ' +  str(score) + ' points')
	retry.click()

if numGames > 1:
	print('Top Score: ' + str(topScore) + ' points')
