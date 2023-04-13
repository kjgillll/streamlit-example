from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import certifi
import urllib3
import html5lib

from bs4 import BeautifulSoup

"""
# Welcome to Streamlit!

BeautifulSoup Scaper Testing
"""

# # print(certifi.where())
# verify = "/home/gitpod/.pyenv/versions/3.11.1/lib/python3.11/site-packages/certifi/cacert.pem"

URL = "https://devbusiness.un.org/content/site-search"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
r = requests.get(URL, headers=headers)
soup = BeautifulSoup(r.content, 'html5lib')
st.write(soup.prettify())

# from urllib3.util.ssl_ import create_urllib3_context

# ctx = create_urllib3_context()
# ctx.load_default_certs()
# ctx.options |= 0x4  # ssl.OP_LEGACY_SERVER_CONNECT

# with urllib3.PoolManager(ssl_context=ctx) as http:
#     r = requests.get("https://devbusiness.un.org/content/site-searchs")
#     print(r.content)


