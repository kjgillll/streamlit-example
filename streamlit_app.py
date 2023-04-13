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

json = requests.get("https://devbusiness.un.org/solr-sitesearch-output/10//0/ds_field_last_updated/desc?bundle_fq=procurement_notice&sm_vid_Institutions_fq=&sm_vid_Procurement_Type_fq=&sm_vid_Countries_fq=&sm_vid_Sectors_fq=&sm_vid_Languages_fq=&sm_vid_Notice_Type_fq=&deadline_multifield_fq=&ts_field_project_name_fq=&label_fq=&sm_field_db_ref_no__fq=&sm_field_loan_no__fq=&dm_field_deadlineFrom_fq=&dm_field_deadlineTo_fq=&ds_field_future_posting_dateFrom_fq=&ds_field_future_posting_dateTo_fq=&bm_field_individual_consulting_fq=").json()
# st.write(json)
df = pd.DataFrame.from_dict(json)
st.write(df)
# from urllib3.util.ssl_ import create_urllib3_context

# ctx = create_urllib3_context()
# ctx.load_default_certs()
# ctx.options |= 0x4  # ssl.OP_LEGACY_SERVER_CONNECT

# with urllib3.PoolManager(ssl_context=ctx) as http:
#     r = requests.get("https://devbusiness.un.org/content/site-searchs")
#     print(r.content)


