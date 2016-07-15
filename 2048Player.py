from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get("https://gabrielecirulli.github.io/2048/")

game = browser.find_element_by_class_name('container')
scoreText = browser.find_element_by_class_name('score-container')
message = browser.find_element_by_class_name('game-message')
retry = browser.find_element_by_class_name('retry-button')

numGames = 10
currentGame = 0

while currentGame < numGames:
	while message.is_displayed() == False:
		game.send_keys('wasd')
	currentGame += 1
	scoreMessage = scoreText.text.split('\n')
	score = scoreMessage[0]
	print('Game ' + str(currentGame) + ': ' +  str(score) + ' points')
	retry.click()

