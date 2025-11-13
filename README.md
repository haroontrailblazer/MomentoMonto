# MomentoMonto
 Intelligent Server Monitor & Response Time Analyzer

[![Python](https://img.shields.io/badge/Python-3.13.8-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)](#)
[![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen.svg)](#)

---

## Overview

**MomentoMonto** is a server monitoring and response time analysis tool designed to **track, analyze, and visualize** the performance of web servers in real-time.  
It helps **developers**, **system administrators**, and **network engineers** ensure high **availability**, **stability**, and **speed** of their online services.

---

## Key Features

- **Real-Time Monitoring:** Continuously checks server uptime and performance.  
- **Response Time Tracking:** Measures latency and displays detailed analysis.  
- **Uptime Visualization:** View server stability through charts and metrics.  
- **Multi-Server Support:** Monitor multiple endpoints simultaneously.  
- **Smart Alerts (optional):** Detect downtime or slow responses automatically.  
- **Modern UI:** Interactive Streamlit dashboard for easy data visualization.

---

## Architecture & Workflow

MomentoMonto uses **Python** and **Streamlit** to periodically send HTTP requests to the configured servers and record:
- Response time (in milliseconds)  
- Server availability (Up/Down status)  
- Request timestamps  

The collected data is visualized with charts and response trends for intuitive performance tracking.

---

## Tech Stack

| Category | Technology |
|-----------|-------------|
| **Language** | Python |
| **Framework** | Streamlit |
| **Libraries** | `requests`, `time`, `datetime`, `matplotlib`, `re` |
| **License** | Apache 2.0 |

---

## Preview

> *(Add screenshots or GIFs of your app interface here once available.)*

---

##  Contributing

Contributions are always welcome!  
If you'd like to enhance **MomentoMonto** (for example, by adding **log exports**, **push notifications**, or **cloud sync**), feel free to:

1. Open an issue  
2. Submit a pull request  

---

## Author
**haroontrailblazer**  
AI Developer | Data Analyst | Machine Learning Engineer  

🔗 **GitHub:** [haroontrailblazer](https://github.com/haroontrailblazer)

---

## License

This project is licensed under the **Apache License 2.0**.  
You may obtain a copy of the License at:  
[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

---

## Installation & Setup

```bash
git clone https://github.com/haroontrailblazer/MomentoMonto.git
cd MomentoMonto

pip install -r requirements.txt

streamlit run main.py
