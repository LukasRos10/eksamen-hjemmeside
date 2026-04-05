from filecmp import clear_cache
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






st.title("Chatbot baseret på kildeliste")

# --- DINE KILDER HER ---
kilder = {
    "Danmarks statistik": "En graf da dst.dk viser at antallet af medlemmer i den danske folkekirke er faldet fra 90% i 1990 til 75% i 2020",
    "Kristelig dagblad": "Kristeligt Dagblad skriver at mange unge melder sig ud af folkekirken fordi de ikke føler at de får noget ud af at være der og hellere vil være sociale",
    "Testside.dk": "Testside.dk nævner at en ekspert har sagt i et interview at antallet af udmeldinger af folkekirken kan være et tilfældigt udsving",
}
# ------------------------

# Kombiner alle kilder til én tekst
samlet_kildetekst = "\n\n".join([f"{navn}: {tekst}" for navn, tekst in kilder.items()])

# Chat input
spørgsmål = st.text_input("Stil et spørgsmål:")

if spørgsmål:
    # Simpel “chatbot”: Den svarer kun ud fra kilderne
    svar = f"""
Jeg har kigget i dine kilder og her er et svar baseret på dem:

**Spørgsmål:** {spørgsmål}

**Svar (baseret på kilderne):**
Jeg kan kun svare ud fra følgende kilder:

{samlet_kildetekst}

Ud fra det ser det ud til, at:
- (Her kan du selv skrive logik til at matche tekst)
    """

    st.write(svar)
