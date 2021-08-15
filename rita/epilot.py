# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 20:39:39 2020

@author: ezeab
"""

# Python3 script to fetch top 10 starred
# repositories of a user on github
import urllib.request
import urllib.error
import urllib.parse
import http.cookiejar
import requests
from lxml import html
from bs4 import BeautifulSoup
import re
import operator

top_limit = 9


def openWebsite2():
    username = "msdeep14"  # str(input("enter GitHub username: "))
    repo_dict = {}

    url = "https://github.com/"+username+"?tab=repositories"

    while True:
        # open the website and get
        # the html of webpage into doc
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(cj))
        resp = opener.open(url)
        doc = html.fromstring(resp.read())

        # extract all the repository names
        repo_name = doc.xpath(
            '//li[@class="col-12 d-flex width-full py-4 border-bottom public source"]/div[@class="d-inline-block mb-1"]/h3/a/text()')

        # list to store repository names
        repo_list = []

        # get the repository name
        for name in repo_name:
            name = ' '.join(''.join(name).split())
            repo_list.append(name)
            repo_dict[name] = 0

        # print repo_list
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        ''' 
			The path mentioned to get the no. of 
			stargazers, you can get it by right 
			click on star symbol on Github page, 
			and then select inspect element 
		'''
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find_all(
            'li', {'class': 'col-12 d-block width-full py-4 border-bottom public source'})

        for d in div:
            temp = d.find_all('div', {'class': 'f6 text-gray mt-2'})
            for t in temp:
                # Get the no. of stars of
                # particular repository
                x = t.find_all('a', attrs={'href': re.compile(
                    "^\/[a-zA-Z0-9\-\_\.]+\/[a-zA-Z0-9\.\-\_]+\/stargazers")})

                # Get the url of the repository
                # and populate the values of dictionay
                # with no. of stars
                if len(x) != 0:
                    name = x[0].get('href')
                    name = name[len(username)+2:-11]
                    repo_dict[name] = int(x[0].text)

        # Check if next page exists
                # for more repositories
        div = soup.find('a', {'class': 'next_page'})

        # print div
        if div is not None:
            url = div.get('href')
            url = "https://github.com/"+url
        else:
            # if there is no next repository
            # page, then exit loop
            break

        # Get the sorted list of all
        # repos and print top 10
    i = 0
    sorted_repo = sorted(iter(repo_dict.items()), key=operator.itemgetter(1))
    print(sorted_repo)
# Print the sorted repos in
# reverse order
    for val in reversed(sorted_repo):
        repo_url = "https://github.com/" + username + "/" + val[0]
        print("\nrepo name : ", val[0], "\nrepo url : ",
              repo_url, "\nstars	 : ", val[1])
        i = i + 1
        if i > top_limit:
            break


openWebsite2()
