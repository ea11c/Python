'''Eric Adams ea11c'''

from __future__ import print_function
import requests
import json
import string
import sys


def get_username():
	username = raw_input("Enter username: ")
	return username


if __name__ == "__main__":
	user = get_username()
	data = []
	comments = []
	num = 0
	check = 0
	while True:
		url = "http://imgur.com/user/" + user + "/index/newest/page/" + str(num) + "/hit.json?scrolling"
		num = num + 1
		page = requests.get(url)
		if not page.text:
			break
		elif page.text == "":
			break			
		else:
			data.extend(json.loads(page.text)["data"]["captions"]["data"])
			check = check + 1
	if check == 0:
		print("User does not have any comments or does not exist.")
		sys.exit()
	for item in data:
		comments.append([item["hash"], item["points"], item["title"], item["datetime"]])
	comments.sort(key = lambda x: int(x[1]), reverse = True)
	i = 1
	while i < len(comments):
		print(i, ".", comments[i-1][0])
		print("Points: ", comments[i-1][1])
		print("Title: ", comments[i-1][2])
		print("Date: ", comments[i-1][3])
		i = i+1
		if i == 6:
			break
	
		
