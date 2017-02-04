'''Eric Adams ea11c'''
from __future__ import print_function
import requests
import re

url = "http://www.cs.fsu.edu/department/faculty/"
faculty_pages = []

def find_faculty():
	page = requests.get(url)
	links = re.findall(url + '[a-zA-z]+' + r'/"><img', page.text)
	for item in links:
		faculty_pages.append(item[:-6])


def get_info(faculty):
	page = requests.get(faculty)
	name_search = re.search(r'<h1 class="main_title">(.+?)</h1>', page.text)
	if name_search:
		name = name_search.group(1)
	print("Name: ", name)
	office_search = re.search(r'<td><strong>Office:</strong></td>(.?)<td>(.*?)</td>', page.text, re.S)
	if office_search:
		office = office_search.group(2)
		if len(office) < 2:
			office = "N/A"
	print("Office: ", office)
	phone_search = re.search(r'<td><strong>Telephone:</strong></td>(.?)<td>(.*?)</td>', page.text, re.S)
	if phone_search:
		phone = phone_search.group(2)
		if len(phone) < 2:
			phone = "N/A"
	print("Telephone: ", phone)
	alt_email_search = re.search(r'<a href="mailto:(.+?)" target="_blank">(.+?)</a>', page.text)
	if alt_email_search:
		email = alt_email_search.group(2)
	else:
		email_search = re.search(r'<td valign="top"><strong>E-Mail:</strong></td>(.?)<td>(.*?)</td>', page.text, re.S)
		if email_search:
			email = email_search.group(2)
	if len(email) < 2:
		email = "N/A"
	print("E-Mail: ", email)

if __name__ == "__main__":
	find_faculty()
	for item in faculty_pages:
		get_info(item)
		print('*************************************')
