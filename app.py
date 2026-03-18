import streamlit as st

st.title("Yapılacaklar Listesi")

if "gorevler" not in st.session_state:
    st.session_state["gorevler"] = []

yeni_gorev = st.text_input("Yeni görev ekle")
if st.button("Ekle") and yeni_gorev:
    st.session_state["gorevler"].append({"ad": yeni_gorev, "tamam": False})

for i, gorev in enumerate(st.session_state["gorevler"]):
    tamamlandi = st.checkbox(gorev["ad"], value=gorev["tamam"], key=i)
    st.session_state["gorevler"][i]["tamam"] = tamamlandi