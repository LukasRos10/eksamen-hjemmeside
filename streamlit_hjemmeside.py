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
#sæt et billede ind i kolonne 2
st.image("https://image2url.com/r2/default/images/1775306768660-aafd1dac-cffe-4578-b067-9e3136c68ede.jpg", width=100)

with col3:
    st.markdown("- [Kilde 3](https://www.kilde3.com)")
st.image("https://image2url.com/r2/default/images/1775335870643-37b4fa95-4458-4c6a-ac08-98fe15c49567.webp", width=100)
with col4:
    st.markdown("- [Kilde 4](https://www.kilde4.com)")
st.image("https://image2url.com/r2/default/images/1775335935496-b86386d9-32af-4ede-a2f7-2d8bf44f197c.jpg", width=100)
with col5:
    st.markdown("- [Kilde 5](https://www.kilde5.com)")
st.image("https://image2url.com/r2/default/images/1775336000578-8b83a6f9-c42f-4746-a18f-05f24a7fd2a1.jpg", width=100)