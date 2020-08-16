#!/usr/bin/env python
# -*- coding: utf-8 -*- # from __future__ import unicode_literals

AUTHOR = 'Andrew Dang-Tran'
SITENAME = ''
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'docs/'

TIMEZONE = 'PST8PDT'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('email', 'andrewdt1506@gmail.com'),
          ('linkedin', 'https://www.linkedin.com/in/andrew-dang-tran-a57144bb/'),
          ('github', 'https://github.com/AndrewDang-Tran'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

GITHUB_URL = 'https://github.com/AndrewDang-Tran'

# Specify name of a built-in theme and other theme stuff
THEME = 'pelican-hyde'
STATIC_PATHS = ['assets']
PROFILE_IMAGE = 'assets/avatar.jpg'
