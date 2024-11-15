import streamlit as st
import pandas as pd
import numpy as np

# Instellen van de pagina layout en de zijbalkmenu
st.set_page_config(page_title="Mijn Bedrijf", page_icon=":house:", layout="wide")

# Zijbalkmenu met radio buttons
st.sidebar.header("Navigatie")
menu_options = ["Home", "Inkoop", "Verkoop", "Logistiek"]
choice = st.sidebar.radio("Kies een pagina", menu_options)

# Voeg de jaar- en maandselectie toe aan de zijbalk
if choice == "Inkoop":
    st.sidebar.header("Selecteer tijdsperiode")

    # Keuze voor jaar of maand
    inkoop_optie = st.sidebar.selectbox("Kies een optie", ["Jaar", "Maand"])

    # Afhankelijk van de keuze in de sidebar, de juiste invoer tonen
    if inkoop_optie == "Jaar":
        jaar = st.sidebar.selectbox("Kies een jaar", [2020, 2021, 2022, 2023, 2024])
        tijdsperiode = f"Jaar: {jaar}"
    else:
        maand = st.sidebar.selectbox("Kies een maand", ["Januari", "Februari", "Maart", "April", "Mei", "Juni", 
                                                      "Juli", "Augustus", "September", "Oktober", "November", "December"])
        tijdsperiode = f"Maand: {maand}"

# Home pagina
if choice == "Home":
    st.title("Welkom bij Mijn Bedrijf")
    
    # Creëer twee kolommen voor de content op de Home pagina
    col1, col2 = st.columns(2)

    with col1:
        st.header("Over mij")
        st.write("""
            Hallo! Mijn naam is Jan Jansen en ik ben de oprichter van Mijn Bedrijf.
            Met jarenlange ervaring in inkoop en logistiek, help ik bedrijven om hun processen te optimaliseren.
            Neem gerust contact op als je vragen hebt of hulp nodig hebt!
        """)
        
        st.write("""
            ### Meer over ons
            Bij Mijn Bedrijf richten we ons op het leveren van de beste oplossingen op het gebied van inkoop.
            Ons team van experts staat klaar om jou te ondersteunen bij elke stap van het proces.
        """)

    with col2:
        # Voeg een afbeelding toe in de tweede kolom (met use_container_width)
        st.image("https://via.placeholder.com/600x300", caption="Dit ben ik", use_container_width=True)

# Inkoop pagina met tabs en verschillende selecties
elif choice == "Inkoop":
    st.title("Inkoop")

    # Toon de geselecteerde tijdsperiode
    st.write(f"Tijdsperiode: {tijdsperiode}")

    # Creëer tabs voor de verschillende inkoopsecties
    tab1, tab2 = st.tabs(["Inkoop NL", "Inkoop BE"])

    # Tab 1: Inkoop NL - Jaartalselectie
    with tab1:
        st.header("Inkoop Nederland")
        
        # Jaartalselectie voor Inkoop NL
        if inkoop_optie == "Jaar":
            # Dummy data voor de grafiek
            data = {
                2020: [100, 150, 200, 250],
                2021: [110, 160, 210, 260],
                2022: [120, 170, 220, 270],
                2023: [130, 180, 230, 280],
                2024: [140, 190, 240, 290]
            }
            
            # Maak een dataframe met de kosten per kwartaal voor het geselecteerde jaar
            df = pd.DataFrame({
                'Q1': data[jaar],
                'Q2': data[jaar],
                'Q3': data[jaar],
                'Q4': data[jaar]
            }, index=['Kosten 1', 'Kosten 2', 'Kosten 3', 'Kosten 4'])

            st.write(f"Kostenanalyse voor het jaar {jaar}:")
            st.bar_chart(df.T)  # .T is transponeren zodat de kwartaalweergave op de X-as komt

    # Tab 2: Inkoop BE - Maandselectie
    with tab2:
        st.header("Inkoop België")
        
        # Maandselectie voor Inkoop BE
        if inkoop_optie == "Maand":
            # Dummy data voor de grafiek (per maand)
            monthly_data = {
                "Januari": [50, 75, 100, 150],
                "Februari": [60, 80, 110, 160],
                "Maart": [70, 90, 120, 170],
                "April": [80, 100, 130, 180],
                "Mei": [90, 110, 140, 190],
                "Juni": [100, 120, 150, 200],
                "Juli": [110, 130, 160, 210],
                "Augustus": [120, 140, 170, 220],
                "September": [130, 150, 180, 230],
                "Oktober": [140, 160, 190, 240],
                "November": [150, 170, 200, 250],
                "December": [160, 180, 210, 260]
            }

            # Maak een dataframe met de kosten per kwartaal voor de geselecteerde maand
            df_monthly = pd.DataFrame({
                'Kosten 1': monthly_data[maand],
                'Kosten 2': monthly_data[maand],
                'Kosten 3': monthly_data[maand],
                'Kosten 4': monthly_data[maand]
            }, index=['Q1', 'Q2', 'Q3', 'Q4'])

            st.write(f"Kostenanalyse voor de maand {maand}:")
            st.bar_chart(df_monthly)  # Toont de grafiek op basis van de geselecteerde maand

# Verkoop pagina
elif choice == "Verkoop":
    st.title("Verkoop")

    # Container voorbeeld
    with st.container():
        st.header("Container Voorbeeld")
        st.write("""
            Dit is een container waarin we meerdere elementen hebben gegroepeerd. 
            Containers zijn handig om inhoud logisch te structureren of dynamisch toe te voegen.
        """)
        st.image("https://via.placeholder.com/400x250", caption="Verkoopproduct", use_container_width=True)

    # Formulier voorbeeld
    st.header("Formulier Voorbeeld")
    with st.form(key='verkoop_form'):
        product_name = st.text_input("Productnaam")
        quantity = st.number_input("Aantal", min_value=1, step=1)
        price = st.number_input("Prijs per eenheid", min_value=0.01, format="%.2f")
        submit_button = st.form_submit_button("Verstuur bestelling")

        if submit_button:
            st.write(f"Bestelling geplaatst voor: {quantity} x {product_name} à {price} EUR")
            st.success("De bestelling is succesvol geplaatst!")

    # Markdown en HTML voorbeelden
    st.header("Markdown en HTML Voorbeelden")
    st.markdown("""
        ### Dit is een **Markdown** voorbeeld
        Je kunt **vetgedrukte** tekst gebruiken, _cursieve_ tekst, en lijsten:
        
        - Item 1
        - Item 2
        - Item 3

        Dit is een **[link](https://www.example.com)** naar een externe website.

        ## HTML Voorbeeld
        <div style="color: blue; font-size: 20px;">
            Dit is een voorbeeld van **HTML** binnen Streamlit.
        </div>
    """, unsafe_allow_html=True)

    # Logistiek pagina
elif choice == "Logistiek":
    st.title("Logistiek")

    # Tekstsectie voor Logistiek
    st.write("""
        In deze sectie gaan we in op de logistieke processen binnen Mijn Bedrijf. Logistiek speelt een cruciale rol in de 
        efficiëntie van het bedrijf. Wij zorgen ervoor dat producten tijdig en op de juiste locatie aankomen, door een goed 
        netwerk van leveranciers en transportdiensten te onderhouden.
    """)

    # 3 Kolommen voor Logistiek
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Voorraadbeheer")
        st.write("""
            We houden nauwlettend toezicht op de voorraadniveaus om ervoor te zorgen dat we altijd de juiste producten op 
            het juiste moment hebben. Dit minimaliseert de kosten en maximaliseert de klanttevredenheid.
        """)

    with col2:
        st.header("Verzendmethoden")
        st.write("""
            Wij bieden een breed scala aan verzendopties, van reguliere verzendingen tot expressleveringen, om te zorgen 
            dat producten op tijd bij de klanten aankomen.
        """)

    with col3:
        st.header("Retourlogistiek")
        st.write("""Wij hebben een efficiënt retourproces ingericht waarmee klanten snel hun producten kunnen""")

        # Tekstsectie voor Logistiek
    st.write("""
        In deze sectie gaan we in op de logistieke processen binnen Mijn Bedrijf. Logistiek speelt een cruciale rol in de 
        efficiëntie van het bedrijf. Wij zorgen ervoor dat producten tijdig en op de juiste locatie aankomen, door een goed 
        netwerk van leveranciers en transportdiensten te onderhouden.
    """)

# Footer onderaan de pagina
st.sidebar.markdown("---")
st.sidebar.write("© 2024 MGID.Nl")
