import streamlit as st
from streamlit import session_state as state
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["Blockchain"]

if 'kw1' not in state:
    state['kw1'] = ''
if 'kw2' not in state:
    state['kw2'] = ''
if 'kw_list' not in state:
    state['kw_list'] = []
if 'trends' not in state:
    state['trends'] = []

def get_trends():
    state['kw1'] = key1
    state['kw2'] = key2
    state['kw_list'] = [state.kw1, state.kw2]
    pytrends.build_payload(state.kw_list, cat=0, timeframe='today 3-m', geo='', gprop='')
    state['trends'] = pytrends.interest_over_time()[[state.kw1, state.kw2]].values
    
with st.sidebar:
    st.title("Data sources Lab3")
    st.text("Google Trends comparison:")
    key1 = st.text_input("Keyword 1")
    key2 = st.text_input("Keyword 2")
    st.button("Compare !", type="primary", on_click=get_trends)

st.title('Trend plot:')

if state['trends'] != []:
    # st.table(state.trends)
    # fig = px.line(state['trends'], labels=[state.kw1, state.kw2])
    st.line_chart(state['trends'])