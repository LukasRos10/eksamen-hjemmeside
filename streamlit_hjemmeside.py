from filecmp import clear_cache
from unicodedata import name
import streamlit as st
import pandas as pd
import datetime
st.set_page_config(layout="wide")
st.set_page_config(page_title="Velkommen til eksamen", )

st.date_input("Dato for eksamen:", value=datetime.date.today())
st.warning("Personlig note: Husk det her er eksamen, så tag jer fucking sammen")
st.title("Velkommen til vores eksamen i _____")

st.write("Vi har lavet denne hjemmeside for at præsentere vores eksamen i _____, hvor vi har arbejdet med _____ og _____.")

st.space("small")
st.header("Vores problemformulering er _________")

st.space("medium")
st.write("Her er vores kildeliste:")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("- [Danmarks statistik](https://www.kilde1.com)")
    st.image("https://newyorkerbyheart.dk/wp-content/uploads/2022/04/gammeldags-pandekager-1.jpg", width=100)

with col2:
    st.markdown("- [Kristelig dagblad](https://www.kilde2.com)")
    st.image("https://image2url.com/r2/default/images/1775306768660-aafd1dac-cffe-4578-b067-9e3136c68ede.jpg", width=100)

with col3:
    st.markdown("- [Testside.dk](https://www.kilde3.com)")
    st.image("https://image2url.com/r2/default/images/1775335870643-37b4fa95-4458-4c6a-ac08-98fe15c49567.webp", width=100)

with col4:
    st.markdown("- [Kilde 4](https://www.kilde4.com)")
    st.image("https://image2url.com/r2/default/images/1775338132154-b7c91706-632e-48fd-b7c0-dd96fc4583c7.png", width=100)

with col5:
    st.markdown("- [Kilde 5](https://www.kilde5.com)")
    st.image("https://image2url.com/r2/default/images/1775336000578-8b83a6f9-c42f-4746-a18f-05f24a7fd2a1.jpg", width=100)

st.space("medium")

col1, col2, col3 = st.columns(3)
with col1:

    st.header("Beskrivelse af problemstilling")
    st.subheader("Hvordan kan folkekirken få flere medlemmer?")
    st.write("Vores problemstilling handler om hvordan folkekirken kan få flere medlemmer")

with col2:
    st.header("Beskrivelse af metode")
    st.subheader("Metodisk fremgang")
    st.write("Vi har brugt en spørgeskemaundersøgelse for at finde ud af hvad folkekirkens medlemmer synes om deres medlemskab")

with col3:
    st.header("Beskrivelse af resultater")
    st.subheader("Vores resultater")
    st.write("Vi fandt ud af at mange medlemmer er utilfredse med folkekirken og derfor overvejer at melde sig ud")

st.header("Chatbot baseret på vores kilder")

# --- DINE KILDER (indsæt tekst fra Word-dokumenter her) ---
kilder = {
    "Graf fra Danmarks statistik": """
Grafen fra Danmarks statistik viser at antallet af medlemmer er faldet fra 90% i 1990 til 75% i 2020
""",
    "Kristeligt dagblad": """
En ekspert fra kristeligt dagblad fortæller i et interview at det faldende medlemstal højst sandsynligt er et tilfældigt udsving, men at folkekirken alligevel skal gøre mere for at få unge til
""",
}
# -----------------------------------------------------------

# Kombiner alle kilder til én tekst
samlet_kildetekst = "\n\n".join(
    [f"{navn}: {tekst}" for navn, tekst in kilder.items()]
)

# Få et spørgsmål fra brugeren
question = st.text_input("Stil et spørgsmål til vores chatbot her:", key="question")

if question:
    st.success("Du spurgte: " + question)

    st.write("### Svar baseret på dine kilder:")

    # Simpelt svar: vis kilderne og lad chatbotten svare ud fra dem
    st.write(samlet_kildetekst)

    st.write("### Mit svar (baseret på kilderne):")
    st.write("- Her kan du selv skrive logik til at finde det rigtige svar")