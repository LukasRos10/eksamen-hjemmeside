from filecmp import clear_cache
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Velkommen til eksamen", )

st.title("Velkommen til vores eksamen i _____")

st.write("Vi har lavet denne hjemmeside for at præsentere vores eksamen i _____, hvor vi har arbejdet med _____ og _____.")


st.header("Vores problemformulering er _________")


st.write("Her er vores kildeliste:")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("- [Kilde 1](https://www.kilde1.com)")
st.image("https://newyorkerbyheart.dk/wp-content/uploads/2022/04/gammeldags-pandekager-1.jpg", width=100)

with col2:
    st.markdown("- [Kilde 2](https://www.kilde2.com)")

with col3:
    st.markdown("- [Kilde 3](https://www.kilde3.com)")

with col4:
    st.markdown("- [Kilde 4](https://www.kilde4.com)")

with col5:
    st.markdown("- [Kilde 5](https://www.kilde5.com)")