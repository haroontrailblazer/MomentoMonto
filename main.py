import streamlit as st
import requests
import re
import os

# Page Configuration
st.set_page_config(
    page_title="MomentoMonto - Monitor your Servers",
    page_icon="https://github.com/haroontrailblazer/haroontrailblazer/blob/main/Project%20Pngs/MomentoMonto-icon.png?raw=true",
    layout="centered"
    )
 
# SEO META TAGS
st.markdown("""
<head>
  <title>MomentoMonto - Monitor Your Servers</title>
  <meta name="description" content="Check your Server Health and Analyze the Traffic of the server” a simple, secure, and smart tool.">
  <meta name="keywords" content="Servers, security, Server Health checker, Server strength, MomentoMonto, Haroon K M">
  <meta name="robots" content="index, follow">
</head>
""", unsafe_allow_html=True)

# getting the Website URL
url_req = st.text_input(label="URL",label_visibility="hidden",placeholder="Enter your Website-URL or IP-Address")
if not url_req:
  st.stop()

# URL or IP Input Filter
unnessary = r"https://"
if re.match(unnessary, url_req):
  print("")
else:
  url_req = "https://"+url_req
  

# Checking the response from the Website
response = requests.get(url=url_req, timeout=5)
code_verify = response.status_code