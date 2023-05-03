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

countries = ["Jamaica","Trinidad","Tobago","Guyana","Suriname","Bahamas","Belize","Guadeloupe","Martinque","Barbados","Curacao","Saint Lucia","Grenada","Aruba","Saint Vincent","The Grenedines","United States Virgin Islands","Antigua","Barbuda","Dominica","Cayman Islands","Saint Kitts and Nevis","Turks and Caicos","Sint Maarten","Anguilla","Montserrat"]

URL = "https://devbusiness.un.org/content/site-search"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
r = requests.get(URL, headers=headers)
soup = BeautifulSoup(r.content, 'html5lib')
#st.write(soup.prettify())

json = requests.get("https://devbusiness.un.org/solr-sitesearch-output/10//0/ds_field_last_updated/desc?bundle_fq=procurement_notice&sm_vid_Institutions_fq=&sm_vid_Procurement_Type_fq=&sm_vid_Countries_fq=&sm_vid_Sectors_fq=&sm_vid_Languages_fq=&sm_vid_Notice_Type_fq=&deadline_multifield_fq=&ts_field_project_name_fq=&label_fq=&sm_field_db_ref_no__fq=&sm_field_loan_no__fq=&dm_field_deadlineFrom_fq=&dm_field_deadlineTo_fq=&ds_field_future_posting_dateFrom_fq=&ds_field_future_posting_dateTo_fq=&bm_field_individual_consulting_fq=").json()
devb = json["response"]["docs"]
json = requests.get("https://devbusiness.un.org/solr-sitesearch-output/10//10/ds_field_last_updated/desc?bundle_fq=procurement_notice&sm_vid_Institutions_fq=&sm_vid_Procurement_Type_fq=&sm_vid_Countries_fq=&sm_vid_Sectors_fq=&sm_vid_Languages_fq=&sm_vid_Notice_Type_fq=&deadline_multifield_fq=&ts_field_project_name_fq=&label_fq=&sm_field_db_ref_no__fq=&sm_field_loan_no__fq=&dm_field_deadlineFrom_fq=&dm_field_deadlineTo_fq=&ds_field_future_posting_dateFrom_fq=&ds_field_future_posting_dateTo_fq=&bm_field_individual_consulting_fq=").json()
devb2 = json["response"]["docs"]
json = requests.get("https://devbusiness.un.org/solr-sitesearch-output/10//20/ds_field_last_updated/desc?bundle_fq=procurement_notice&sm_vid_Institutions_fq=&sm_vid_Procurement_Type_fq=&sm_vid_Countries_fq=&sm_vid_Sectors_fq=&sm_vid_Languages_fq=&sm_vid_Notice_Type_fq=&deadline_multifield_fq=&ts_field_project_name_fq=&label_fq=&sm_field_db_ref_no__fq=&sm_field_loan_no__fq=&dm_field_deadlineFrom_fq=&dm_field_deadlineTo_fq=&ds_field_future_posting_dateFrom_fq=&ds_field_future_posting_dateTo_fq=&bm_field_individual_consulting_fq=").json()
devb3 = json["response"]["docs"]
json = requests.get("https://devbusiness.un.org/solr-sitesearch-output/10//30/ds_field_last_updated/desc?bundle_fq=procurement_notice&sm_vid_Institutions_fq=&sm_vid_Procurement_Type_fq=&sm_vid_Countries_fq=&sm_vid_Sectors_fq=&sm_vid_Languages_fq=&sm_vid_Notice_Type_fq=&deadline_multifield_fq=&ts_field_project_name_fq=&label_fq=&sm_field_db_ref_no__fq=&sm_field_loan_no__fq=&dm_field_deadlineFrom_fq=&dm_field_deadlineTo_fq=&ds_field_future_posting_dateFrom_fq=&ds_field_future_posting_dateTo_fq=&bm_field_individual_consulting_fq=").json()
devb4 = json["response"]["docs"]
json = requests.get("https://devbusiness.un.org/solr-sitesearch-output/10//40/ds_field_last_updated/desc?bundle_fq=procurement_notice&sm_vid_Institutions_fq=&sm_vid_Procurement_Type_fq=&sm_vid_Countries_fq=&sm_vid_Sectors_fq=&sm_vid_Languages_fq=&sm_vid_Notice_Type_fq=&deadline_multifield_fq=&ts_field_project_name_fq=&label_fq=&sm_field_db_ref_no__fq=&sm_field_loan_no__fq=&dm_field_deadlineFrom_fq=&dm_field_deadlineTo_fq=&ds_field_future_posting_dateFrom_fq=&ds_field_future_posting_dateTo_fq=&bm_field_individual_consulting_fq=").json()
devb5 = json["response"]["docs"]
json = requests.get("https://devbusiness.un.org/solr-sitesearch-output/10//50/ds_field_last_updated/desc?bundle_fq=procurement_notice&sm_vid_Institutions_fq=&sm_vid_Procurement_Type_fq=&sm_vid_Countries_fq=&sm_vid_Sectors_fq=&sm_vid_Languages_fq=&sm_vid_Notice_Type_fq=&deadline_multifield_fq=&ts_field_project_name_fq=&label_fq=&sm_field_db_ref_no__fq=&sm_field_loan_no__fq=&dm_field_deadlineFrom_fq=&dm_field_deadlineTo_fq=&ds_field_future_posting_dateFrom_fq=&ds_field_future_posting_dateTo_fq=&bm_field_individual_consulting_fq=").json()
devb6 = json["response"]["docs"]
json = requests.get("https://devbusiness.un.org/solr-sitesearch-output/10//60/ds_field_last_updated/desc?bundle_fq=procurement_notice&sm_vid_Institutions_fq=&sm_vid_Procurement_Type_fq=&sm_vid_Countries_fq=&sm_vid_Sectors_fq=&sm_vid_Languages_fq=&sm_vid_Notice_Type_fq=&deadline_multifield_fq=&ts_field_project_name_fq=&label_fq=&sm_field_db_ref_no__fq=&sm_field_loan_no__fq=&dm_field_deadlineFrom_fq=&dm_field_deadlineTo_fq=&ds_field_future_posting_dateFrom_fq=&ds_field_future_posting_dateTo_fq=&bm_field_individual_consulting_fq=").json()
devb7 = json["response"]["docs"]
devbArray = []

#json["response"]["docs"][index]["url"]
#json["response"]["docs"][index]["label"]
#json["response"]["docs"][index]["ts_field_project_name"]
#json["response"]["docs"][index]["sm_vid_Notice_type"]
#json["response"]["docs"][index]["timestamp"]
for x in devb:
    #st.write(x["url"]+x["label"]+x["ts_field_project_name"]+x["sm_vid_Notice_type"]+x["timestamp"])
    if x["sm_vid_Countries"] in countries: devbArray.append({"label": x["label"], "url": x["url"], "timestamp": x["timestamp"]})
for x in devb2:
    #st.write(x["url"]+x["label"]+x["ts_field_project_name"]+x["sm_vid_Notice_type"]+x["timestamp"])
    if x["sm_vid_Countries"] in countries: devbArray.append({"label": x["label"], "url": x["url"], "timestamp": x["timestamp"]})
for x in devb3:
    #st.write(x["url"]+x["label"]+x["ts_field_project_name"]+x["sm_vid_Notice_type"]+x["timestamp"])
    if x["sm_vid_Countries"] in countries: devbArray.append({"label": x["label"], "url": x["url"], "timestamp": x["timestamp"]})
for x in devb4:
    #st.write(x["url"]+x["label"]+x["ts_field_project_name"]+x["sm_vid_Notice_type"]+x["timestamp"])
    if x["sm_vid_Countries"] in countries: devbArray.append({"label": x["label"], "url": x["url"], "timestamp": x["timestamp"]})
for x in devb5:
    #st.write(x["url"]+x["label"]+x["ts_field_project_name"]+x["sm_vid_Notice_type"]+x["timestamp"])
    if x["sm_vid_Countries"] in countries: devbArray.append({"label": x["label"], "url": x["url"], "timestamp": x["timestamp"]})
for x in devb6:
    #st.write(x["url"]+x["label"]+x["ts_field_project_name"]+x["sm_vid_Notice_type"]+x["timestamp"])
    if x["sm_vid_Countries"] in countries: devbArray.append({"label": x["label"], "url": x["url"], "timestamp": x["timestamp"]})
for x in devb7:
    #st.write(x["url"]+x["label"]+x["ts_field_project_name"]+x["sm_vid_Notice_type"]+x["timestamp"])
    if x["sm_vid_Countries"] in countries: devbArray.append({"label": x["label"], "url": x["url"], "timestamp": x["timestamp"]})

df = pd.DataFrame(devbArray);

st.write(df)
#st.write(json["response"]["docs"][4])

# from urllib3.util.ssl_ import create_urllib3_context

# ctx = create_urllib3_context()
# ctx.load_default_certs()
# ctx.options |= 0x4  # ssl.OP_LEGACY_SERVER_CONNECT

# with urllib3.PoolManager(ssl_context=ctx) as http:
#     r = requests.get("https://devbusiness.un.org/content/site-searchs")
#     print(r.content)


