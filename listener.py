#!/usr/bin/env python
import MySQLdb
import feedparser

#database connection
#fill in the blanks in production
db = MySQLdb.connect(host="", user="", passwrd="", dbname="")

#cursor class necessary for queries in Python
cur = db.cursor()


#keywords

#Google News Listener
google_news_feed = "http://news.google.com/news?pz=1&cf=all&ned=us&hl=en&output=rss"


#Twitter Listener

