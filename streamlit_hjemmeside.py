from filecmp import clear_cache
import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
st.set_page_config(page_title="Velkommen til eksamen", )

st.title("Velkommen til vores eksamen i _____")

st.write("Vi har lavet denne hjemmeside for at præsentere vores eksamen i _____, hvor vi har arbejdet med _____ og _____.")


st.header("Vores problemformulering er _________")


import streamlit as st

st.set_page_config(layout="wide")

# CSS: standardstørrelse + større i "fullscreen" (bred skærm)
st.markdown(
    """
    <style>
    .responsive-img {
      width: 120px;       /* standardstørrelse i normalt vindue */
      height: auto;
      display: block;
      margin: 0 auto;
    }

    /* Når viewport er bredere end breakpoint, gør billedet større */
    @media (min-width: 1200px) {
      .responsive-img {
        width: 60%;       /* fylder 60% af containeren i fullscreen */
        max-width: 900px; /* undgå ekstrem forstørrelse */
      }
    }

    /* Sørg for at Streamlit's egne billeder ikke overskrider container */
    .stImage img {
      max-width: 100%;
      height: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.write("Her er vores kildeliste:")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("- [Danmarks statistik](https://www.kilde1.com)")
    st.markdown(
        '<img src="https://newyorkerbyheart.dk/wp-content/uploads/2022/04/gammeldags-pandekager-1.jpg" class="responsive-img" alt="Danmarks statistik">',
        unsafe_allow_html=True,
    )

with col2:
    st.markdown("- [Kilde 2](https://www.kilde2.com)")
    st.markdown(
        '<img src="https://image2url.com/r2/default/images/1775306768660-aafd1dac-cffe-4578-b067-9e3136c68ede.jpg" class="responsive-img" alt="Kilde 2">',
        unsafe_allow_html=True,
    )

with col3:
    st.markdown("- [Kilde 3](https://www.kilde3.com)")
    st.markdown(
        '<img src="https://image2url.com/r2/default/images/1775335870643-37b4fa95-4458-4c6a-ac08-98fe15c49567.webp" class="responsive-img" alt="Kilde 3">',
        unsafe_allow_html=True,
    )

with col4:
    st.markdown("- [Kilde 4](https://www.kilde4.com)")
    st.markdown(
        '<img src="https://image2url.com/r2/default/images/1775335935496-b86386d9-32af-4ede-a2f7-2d8bf44f197c.jpg" class="responsive-img" alt="Kilde 4">',
        unsafe_allow_html=True,
    )

with col5:
    st.markdown("- [Kilde 5](https://www.kilde5.com)")
    st.markdown(
        '<img src="https://image2url.com/r2/default/images/1775336000578-8b83a6f9-c42f-4746-a18f-05f24a7fd2a1.jpg" class="responsive-img" alt="Kilde 5">',
        unsafe_allow_html=True,
    )



col1, col2, col3 = st.columns(3)
with col1:

    st.header("beskrivelse af problemstilling")
    st.subheader("Hvordan kan folkekirken få flere medlemmer?")
    st.write("Vores problemstilling handler om hvordan folkekirken kan få flere medlemmer")

with col2:
    st.header("beskrivelse af metode")
    st.write("Vi har brugt en spørgeskemaundersøgelse for at finde ud af hvad folkekirkens medlemmer synes om deres medlemskab")

with col3:
    st.header("beskrivelse af resultater")
    st.write("Vi fandt ud af at mange medlemmer er utilfredse med folkekirken og derfor overvejer at melde sig ud")