# Visualizing Geo Data and Dashboard creation in Python

This project file basically deals with 2 things:
- How to visualize Geo Data using **Choropleths**
- How to create simple dashboards in python

### Choropleths
- A *choropleth map* is a type of statistical thematic map that uses pseudocolor, i.e., color corresponding with an aggregate summary of a geographic characteristic within spatial enumeration units, such as population density or per-capita income.
- The library I have used for plotting choropleths is `plotly.express`, you can download plotly in your local system using the command `pip install plotly`. It helps in creating interactive data visualizations 
### Dashboards 
- Python has a library called `dash`, which can be used to create interactive web app dashboards, this library innately uses `plotly` for graphing and `flask` for the web server part.

## About the datasets used and work done
- There have been 2 datasets used in this project 
  - one is the `milk_data.csv`, which is the year on year availablity of per capita availability of milk in a state in India. The dashboard created helps us visualize state wise difference w.r.t milk availability for a financial year
  - Second is `Statewise_income.csv.csv` which deals with statewise income disparity and compares it from 2001 to 2011.
  
 #### NOTE: On implementation you might hover over places like Telangana and Ladakh and get either no value or 0 value that is because the time period considered for this data, is prior to formation of the State and UT
 #### **Geojson File**(used for Indian Map): `https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson`
