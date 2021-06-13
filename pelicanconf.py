#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from datetime import date

AUTHOR = "hexcowboy"
SITENAME = "hexcowboy"
SITEURL = ''

THEME = "themes/cowboy"
PATH = "content"

TIMEZONE = "America/Chicago"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('About', ''),)

# Social widget
SOCIAL = (
    ("Discord", "https://discordapp.com/users/418557177825853443"),
    ("GitHub", "https://github.com/hexcowboy"),
    ("Twitter", "https://twitter.com/hexcowboy"),
)

COPYRIGHT_YEAR = date.today().year
SITE_CONTACT = ("@hexcowboy", "https://twitter.com/hexcowboy")

DEFAULT_PAGINATION = 10

PLUGINS = ["readtime"]

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
