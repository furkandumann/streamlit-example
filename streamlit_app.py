from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.title("Kaç yaşındasın")
dogum=st.number_input("Doğum tarihiniz")
yas=2022-dogum
st.subheader(yas)
