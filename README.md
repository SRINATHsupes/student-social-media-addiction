# student-social-media-addiction
Dash app analyzing student social media addiction data
This project analyzes social media addiction among students using interactive data visualizations and dashboards built with **Dash (Plotly)**, **Folium**, and **Pandas**. It aims to explore patterns, behaviors, and impacts of social media usage on students’ daily lives and mental health.
With the increasing use of social media, especially among students, it's crucial to understand:
- How much time is spent daily?
- Which platforms are most addictive?
- Are there correlations with sleep, stress, or academics?

This dashboard gives a **visual story** of survey data collected from students on their social media usage and its effects.
FEATURES 
> Interactive **Dash** dashboard  
> **Bar charts**, **Pie charts**, and other visualizations (Plotly)  
> **World map** showing geographical data using **Folium**  
> Clean layout with multiple graphs side-by-side  
> Real-time data visualization experience  

project structure 
README.md
dataclean_eda.ipynb
world_map.ipynb
dashboard_code.ipynb
train addiction model.py
smb prediction model.py
smb.zip (dataset)


in world_map.ipynb
The project includes a `folium` map to visualize:
- Locations of survey responses (if geolocation included)
- Hotspots of high social media usage
- Optional popups with student behavior summaries

> The map is saved as an HTML file and embedded in the Dash app or linked separately.



Visualizations
Bar Chart:
Shows distribution of hours spent on social media.
Pie Chart:
Percentage of platform usage (Instagram, YouTube, Snapchat, etc.)
Line Graphs:
Optional: Time trends or correlation with sleep/study.


used 
- Python 
- Dash (Plotly)
- Pandas
- Folium
- Jupyter (for EDA)
- RandomForestClassifier

imports 
pandas 
folium 
dash
Randome Forest 
sci-learn kit 


