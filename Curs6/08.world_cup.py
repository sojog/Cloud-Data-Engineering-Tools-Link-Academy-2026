import streamlit as st
import pandas as pd

st.set_page_config(page_title="World Cup 2026 Groups", layout="wide")

@st.cache_data
def load_data():
    teams = pd.read_csv("date_kaggle_world_cup/teams.csv")
    matches = pd.read_csv("date_kaggle_world_cup/matches.csv")
    return teams, matches

teams, matches = load_data()

st.title(" FIFA World Cup 2026  Grupe")


st.write("Preview dataset echipe:", teams.head())

if "group_letter" not in teams.columns:
    st.error("Nu există coloana 'group_letter' în dataset!")
    st.stop()

groups = sorted(teams["group_letter"].dropna().unique())


st.sidebar.header("Căutare")
search = st.sidebar.text_input("Caută echipă")

if search:
    result = teams[teams["team_name"].str.contains(search, case=False, na=False)]
    st.sidebar.write(result)


for g in groups:
    st.subheader(f"Grupa {g}")

    group_df = teams[teams["group_letter"] == g][["team_name"]]

   
    st.table(group_df.reset_index(drop=True))

    st.markdown("---")

st.subheader(" Statistici grupe")

count_df = teams.groupby("group_letter").size().reset_index(name="teams_count")
st.bar_chart(count_df.set_index("group_letter"))