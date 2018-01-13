#!/usr/bin/env python3

# DEPENDS: selenium, phantomjs (optional)

# DEPRECATED: bitlyauto is simpler and has fewer large dependencies

import os, sys, re, glob, time
from selenium import webdriver

if len(sys.argv) == 1:
    print("Usage: %s [url]" % os.path.basename(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]
try:
    browser = webdriver.PhantomJS()
except:
    print("PhantomJS not detected. Consider revaluating your life.")
    browser = webdriver.Chrome()

# os.system('./window_ninja')
browser.get('https://bitly.com/')
browser.find_element_by_id('shorten_url').send_keys(url)
time.sleep(2)
browser.find_element_by_id('shorten_btn').submit()
time.sleep(2)

mrl = browser.find_element_by_id('most_recent_link')
link = mrl.find_elements_by_class_name('shortened_link')[0]
shortened_url = link.text.split('\n')[2]
browser.close()
print(shortened_url)
