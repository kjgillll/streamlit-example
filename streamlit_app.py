from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import certifi
import urllib3

from bs4 import BeautifulSoup

"""
# Welcome to Streamlit!

BeautifulSoup Scaper Testing
"""

# # print(certifi.where())
# verify = "/home/gitpod/.pyenv/versions/3.11.1/lib/python3.11/site-packages/certifi/cacert.pem"

URL = "https://devbusiness.un.org/content/site-search"
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')
st.write(soup)

# from urllib3.util.ssl_ import create_urllib3_context

# ctx = create_urllib3_context()
# ctx.load_default_certs()
# ctx.options |= 0x4  # ssl.OP_LEGACY_SERVER_CONNECT

# with urllib3.PoolManager(ssl_context=ctx) as http:
#     r = requests.get("https://devbusiness.un.org/content/site-searchs")
#     print(r.content)


