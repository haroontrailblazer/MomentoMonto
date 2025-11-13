from datetime import datetime
import matplotlib.pyplot as mp
import streamlit as st
import requests
import time
import re

# --- Page Configuration ---
st.set_page_config(
    page_title="MomentoMonto - Monitor your Servers",
    page_icon="https://github.com/haroontrailblazer/haroontrailblazer/blob/main/Project%20Pngs/MomentoMonto-icon.png?raw=true",
    layout="centered"
)
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .stActionButton {display: none;}  /* hides the stop/rerun icon */
    </style>
""", unsafe_allow_html=True)

# --- SEO META TAGS ---
st.markdown("""
<head>
  <title>MomentoMonto - Monitor Your Servers</title>
  <meta name="description" content="Check your Server Health and Analyze the Traffic of the server — a simple, secure, and smart tool.">
  <meta name="keywords" content="haroontrailblazer, Servers, security, Server Health checker, Server strength, MomentoMonto, Haroon K M">
  <meta name="robots" content="index, follow">
</head>
""", unsafe_allow_html=True)
# Title
st.markdown("""
    <h2 style='text-align:left; color:#00FFFF;'>MomentoMonto</h2>
    <p style='text-align:left; color:grey; font-size:11px; margin-top:-10px;'>Check your server health and analyze live response time</p>""", unsafe_allow_html=True)

# --- Input Section ---
url_req = st.text_input(label="URL", label_visibility="hidden", placeholder="Enter your Website-URL or IP-Address")
if not url_req:
    st.info("**Privacy Notice:** We don’t store, track, or share any URLs or server data you enter. All checks happen securely on your device in real-time.")
    # --- Footer ---
    st.markdown("""
    <div class="footer" style="background-color:black;color:#333;padding:18px;border-radius:12px;max-width:820px;margin:20px auto;text-align:center;font-family:Segoe UI, Tahoma, sans-serif;">
        <p style="margin:0 0 8px;font-size:14px;">
            <strong>Contact:</strong>
            <a href="mailto:hexra2025@gmail.com" style="color:#1a73e8;text-decoration:none;margin-left:8px;">hexra2025@gmail.com</a>
        </p>
        <p style="margin:0 0 12px;font-size:14px;">
            <a href="https://www.instagram.com/hexra_?igsh=dGFqY2MzMjQ1aGJo" target="_blank" style="color:#1a73e8;text-decoration:none;margin:0 8px;">Instagram</a> |
            <a href="https://github.com/haroontrailblazer" target="_blank" style="color:#1a73e8;text-decoration:none;margin:0 8px;">GitHub</a>
        </p>
        <hr style="border:none;border-top:1px solid #e6e6e6;margin:12px 0;">
        <p style="margin:8px 0 0;color:#555;font-size:13px;line-height:1.4;text-align:left;">
            <strong>About:</strong><br>
           MomentoMonto is an intelligent server monitoring and response time analysis tool designed to track, analyze, and visualize the performance of web servers in real-time. It helps developers, system administrators, and network engineers ensure high availability, stability, and speed of their online services.
        </p>
    </div>
    <br>
    """, unsafe_allow_html=True)
    st.stop()

# URL or IP Input Filter for HTTPS
if not re.match(r"https://", url_req):
    url_req = "https://" + url_req

# --- Streamlit Placeholders ---
status_placeholder = st.empty()
bar_placeholder = st.empty()
response_placeholder = st.empty()
chart_placeholder = st.empty()
stat_placeholder = st.empty()

# --- Setup Variables ---
timeout = 10
response_times = []
timestamps = []

# --- Monitoring Loop ---
while True:
    try:
        start_time = time.time()
        res = requests.get(url=url_req, timeout=5)
        end_time = time.time()

        response_time = round((end_time - start_time) * 1000, 2)  # in milliseconds
        response_times.append(response_time)
        timestamps.append(datetime.now().strftime("%H:%M:%S"))

        if len(response_times) > 15:  # keep chart clean with last 15 readings
            response_times.pop(0)
            timestamps.pop(0)

        if res.status_code == 200:
            color = "#00FFFF"
            text = "Server Active"
        if response_time < 100:
          progress_value = 100
        elif response_time < 200:
          progress_value = 75
        elif response_time < 300:
          progress_value = 50
        elif response_time >= 500:
          progress_value = 25
          
        else:
            color = "#FF0000"
            text = f"Server Error ({res.status_code})"
            progress_value = 0

    except Exception:
        color = "#FF0000"
        text = "Server Down"
        progress_value = 0
        response_time = 0
        response_times.append(0)
        timestamps.append(datetime.now().strftime("%H:%M:%S"))

    # --- Status Light ---
    status_html = f"""
    <div style='text-align:center;'>
        <div style='
            display:inline-block;
            width:25px;
            height:25px;
            border-radius:50%;
            background-color:{color};
            box-shadow:0 0 20px {color};
            margin:10px;'>
        </div>
        <p style='color:{color};font-weight:bold;font-size:18px;'>{text}</p>
    </div>
    """
    status_placeholder.markdown(status_html, unsafe_allow_html=True)

    # --- Progress Bar ---
    bar_placeholder.progress(progress_value)

    # --- Response Time Display ---
    response_placeholder.markdown(
        f"<p style='text-align:center;font-size:16px;color:gray;'>Response Time: <b>{response_time} ms</b></p>",
        unsafe_allow_html=True
    )
    st.markdown("<br></br>",unsafe_allow_html=True)
    
    # --- Response Time Line Chart (X: Hourly labels, Y: 0–5 MB) ---
    mp.close("all")
    mp.style.use("dark_background")
    fig, ax = mp.subplots(figsize=(6, 3))

    # Convert milliseconds to MB scale (demo scale: assuming 1 ms ≈ 0.001 MB)
    mb_values = [round(rt * 0.01, 2) for rt in response_times]

    ax.plot(timestamps, mb_values, color="#00FFFF", marker="o", linewidth=2)
    ax.set_xlabel("Time", fontsize=10, color="grey")
    ax.set_ylabel("Traffic(Sec)", fontsize=10, color="grey")
    ax.grid(alpha=0.3)

    # Format x-ticks → show only full hour marks (e.g., 10:00:00, 11:00:00)
    hour_labels, hour_positions = [], []
    for i, t in enumerate(timestamps):
        if t.endswith(":00:00"):
            hour_labels.append(t[:5])  # show only HH:MM
            hour_positions.append(i)

    if hour_labels:
        ax.set_xticks(hour_positions)
        ax.set_xticklabels(hour_labels, rotation=30, ha="right", fontsize=8, color="grey")
    else:
        ax.set_xticks([])
        
    ax.set_ylim(0, 5)
    ax.set_yticks([0, 1, 2, 3, 4, 5])
    ax.set_yticklabels([f"{i}" for i in range(6)], fontsize=9, color="gray")

    chart_placeholder.pyplot(fig, clear_figure=True)
    try:
        stat_placeholder.write(res.status_code)
    except:
        stat_placeholder.write("Code Error")
    time.sleep(timeout)
