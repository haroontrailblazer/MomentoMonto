import streamlit as st
import requests
import time
import re

# Page Configuration
st.set_page_config(
    page_title="MomentoMonto - Monitor your Servers",
    page_icon="https://github.com/haroontrailblazer/haroontrailblazer/blob/main/Project%20Pngs/MomentoMonto-icon.png?raw=true",
    layout="centered"
    )
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)
 
 
# SEO META TAGS
st.markdown("""
<head>
  <title>MomentoMonto - Monitor Your Servers</title>
  <meta name="description" content="Check your Server Health and Analyze the Traffic of the server” a simple, secure, and smart tool.">
  <meta name="keywords" content="haroontrailblazer, Servers, security, Server Health checker, Server strength, MomentoMonto, Haroon K M">
  <meta name="robots" content="index, follow">
</head>
""", unsafe_allow_html=True)

# getting the Website URL
url_req = st.text_input(label="URL",label_visibility="hidden",placeholder="Enter your Website-URL or IP-Address")
if not url_req:
  st.stop()

# URL or IP Input Filter for Https
pt1 = r"https://"
if re.match(pt1, url_req):
  print("")
else:
  url_req = "https://"+url_req

# --- Initialize counters ---
total_outbound_bytes = 0
total_inbound_bytes = 0
timeout = 30

while True:
    
        # --- HTTPS CHECK ---
        res = requests.get(url=url_req)
        https_out = sum(len(f"{k}: {v}") for k, v in res.request.headers.items())
        https_in = sum(len(f"{k}: {v}") for k, v in res.headers.items()) + len(res.content)
        total_outbound_bytes += https_out
        total_inbound_bytes += https_in

        # --- Convert to MB ---
        total_out_mb = total_outbound_bytes / (1024 * 1024)
        total_in_mb = total_inbound_bytes / (1024 * 1024)

        time.sleep(timeout)