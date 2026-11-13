# Run this one

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dr. Manhattan",
    page_icon=None,
    layout="wide",  #could be centered
    initial_sidebar_state="collapsed"
)

# markdown code(.stapp is the main bg,.block-container for main content, stheader for inbuilt  )

st.markdown("""
<style>

#MainMenu, footer {
    visibility: visible;
}

.stApp {
    background: radial-gradient(circle at 70% 30%, #06447D, #020817 80%);
    color: white;
}

.block-container { 
    padding-top: 1rem;
}

header[data-testid="stHeader"] {
    background: transparent;
    visibility: visible;
}

[data-testid="stSidebarCollapsedControl"] {
    display: flex !important;
    visibility: visible !important;
    color: #65C8FF !important;
    background: transparent !important;
}

section[data-testid="stSidebar"] {
    background-color: #061B35;
    border-right: 1px solid #087DDA;
}

/* Headings */

h1 {
    color: #65C8FF;
    text-shadow: 0 0 15px #008CFF;
}

h2, h3 {
    color: #70CFFF;
}

p {
    color: #C5E7FF;
}

/* Images */

img {
    box-shadow: 0 0 25px #008CFF;
    border-radius: 10px;
}

/* Divider */

hr {
    border-color: #1264A3;
}

</style>
""", unsafe_allow_html=True)


# Sidebar

st.sidebar.title("DR. MANHATTAN")
st.sidebar.caption("WATCHMEN UNIVERSE")
st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    ["Overview", "Abilities", "About"]
)

st.sidebar.divider()

st.sidebar.write("Jonathan Osterman")
st.sidebar.caption("Beyond time. Beyond humanity.")


# Overview Page

if page == "Overview":

    st.title("DR. MANHATTAN")
    st.caption("JONATHAN OSTERMAN | THE GOD AMONG MEN")

    st.divider()

    left, right = st.columns([1, 3.3], gap ="large")

    with left:
        st.image("dr_manhattan.jpg")

    with right:
        st.header("The God Among Men")

        st.write("""
        Once a human physicist, Jonathan Osterman
        became an almost omnipotent being following
        a scientific accident.

        He exists beyond conventional human limitations,
        perceives time differently and possesses control
        over matter and energy.
        """)

        st.write("**Origin:** Intrinsic Field Subtractor accident")
        st.write("**Former Identity:** Physicist")
        st.write("**First Appearance:** Watchmen (1986)")


# Abilities Page

elif page == "Abilities":

    st.title("ABILITIES")
    st.caption("AN ANALYSIS OF DR. MANHATTAN'S POWERS")

    powers = {
        "Ability": [
            "Matter Manipulation",
            "Energy Projection",
            "Teleportation",
            "Regeneration",
            "Duplication",
            "Time Perception",
            "Super Strength"
        ],
        "Power Level": [
            100, 98, 95, 100, 95, 100, 90
        ]
    }

    df = pd.DataFrame(powers)

    # or just use st.table(df) 

    st.dataframe(
        df.style.set_properties(**{ "color": "#65C8FF"}),
        width="stretch",
        hide_index=True,
        column_config={
            "Power Level": st.column_config.ProgressColumn(
                "Power Level",
                min_value=0,
                max_value=100,
                format="%d%%",  #can directly use "percent" but for that keep the value on 0 and 1
                # 100/1*100
                color="blue"
            )
        }
    )

    # st.table(df)



# About Page

elif page == "About":

    st.title("ABOUT")
    st.caption("THE MAN BEHIND THE BLUE")

    st.write("""
    Dr. Manhattan is a fictional character from
    the Watchmen universe, created by Alan Moore
    and Dave Gibbons.

    His transformation fundamentally changed
    his understanding of humanity, existence
    and the passage of time.
    """)

    st.subheader("Character Details")

    st.write("Real Name: Jonathan Osterman")
    st.write("Occupation: Former Physicist")
    st.write("Universe: DC Comics")
    st.write("First Appearance: Watchmen (1986)")


# Footer

st.divider()

st.markdown("""
<center>
<p style="color:#55BFFF; letter-spacing:4px;">
BEYOND TIME. BEYOND HUMANITY.
</p>
</center>
""", unsafe_allow_html=True)
