import streamlit as st
import base64
from PIL import Image
from pathlib import Path


def page_content(page_number):
    if page_number == 0:

        st.header("Congratulations! and goodbye...")
        st.write("\n")
        st.write(
            f"""<p style="text-align:center;"><img src="https://media3.giphy.com/media/6nuiJjOOQBBn2/200w.webp?cid=ecf05e47xcmnv9n8vasc1d01665fpyw6u8qee6tg305wyews&rid=200w.webp&ct=g" style="width:500px;height:450px;"></p>""",
            unsafe_allow_html=True,
        )
        st.write("\n")
    elif page_number == 1:
        st.header("""If work is your second home. Here is your 'second parent'""")

        #### Dr. Ong
        eac_cols = st.columns([3.5,3])
        with eac_cols[0]:
            pp_path = Path(__file__).parents[0] / 'pic/ohh.png'
            pp = Image.open(pp_path)
            st.image(pp, width=350,caption="Dr. Ong")
        with eac_cols[1]:
            # """### gif from local file"""
            file_ = open("messages\good luck.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()

            st.write(
                f"""<p style="text-align:center;"><img src="data:image/gif;base64,{data_url}" style="width:float:right;300px;height:240px;"></p>""",
                unsafe_allow_html=True,
            )
            st.write("All the best to you!")

    elif page_number == 2:
        st.header("And here are your homies...")
        #### Chuan Hai
        eac_cols = st.columns([3.5,3])
        with eac_cols[0]:
            pp = Image.open(r'pic\nch.png')
            st.image(pp, width=350,caption="Chuan Hai")
        with eac_cols[1]:
            # """### gif from local file"""
            file_ = open("messages\good luck.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()

            st.write(
                f"""<p style="text-align:center;"><img src="data:image/gif;base64,{data_url}" style="width:float:right;300px;height:240px;"></p>""",
                unsafe_allow_html=True,
            )
            st.write("Congratulations on your new job. Wishing you all the best.")

        st.write("\n")
        st.write("\n")

        #### Muja
        eac_cols = st.columns([3.5,3])
        with eac_cols[0]:
            pp = Image.open(r'pic\muja.png')
            st.image(pp, width=350,caption="Mujahid")
        with eac_cols[1]:
            # """### gif from local file"""
            file_ = open("messages\good luck.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()

            st.write(
                f"""<p style="text-align:center;"><img src="data:image/gif;base64,{data_url}" style="width:float:right;300px;height:240px;"></p>""",
                unsafe_allow_html=True,
            )
            st.write("It was an honor to work with a coworker who was committed to their success and their coworkers. You deserve nothing but the best!")

    elif page_number == 3:
        st.header("Nerdy neighbours...")
        #### Peter
        eac_cols = st.columns([3.5,3])
        with eac_cols[0]:
            pp = Image.open(r'pic\peter.png')
            st.image(pp, width=350,caption="Peter")
        with eac_cols[1]:
            # """### gif from local file"""
            file_ = open("messages\good luck.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()

            st.write(
                f"""<p style="text-align:center;"><img src="data:image/gif;base64,{data_url}" style="width:float:right;300px;height:240px;"></p>""",
                unsafe_allow_html=True,
            )
            st.write("We will remember you with warm thoughts and memories. Best wishes to you in the future.")

        st.write("\n")
        st.write("\n")

        #### Josh
        eac_cols = st.columns([3.5,3])
        with eac_cols[0]:
            pp = Image.open(r'pic\josh.png')
            st.image(pp, width=350,caption="Joshua")
        with eac_cols[1]:
            # """### gif from local file"""
            file_ = open("messages\good luck.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()

            st.write(
                f"""<p style="text-align:center;"><img src="data:image/gif;base64,{data_url}" style="width:float:right;300px;height:240px;"></p>""",
                unsafe_allow_html=True,
            )
            st.write("No matter where you work, you will always be my friend until the end. Good luck with your new job. I know you’re going to do great.")

        #### Ken
        eac_cols = st.columns([3.5,3])
        with eac_cols[0]:
            pp = Image.open(r'pic\ken.png')
            st.image(pp, width=350,caption="Ken")
        with eac_cols[1]:
            # """### gif from local file"""
            file_ = open("messages\good luck.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()

            st.write(
                f"""<p style="text-align:center;"><img src="data:image/gif;base64,{data_url}" style="width:float:right;300px;height:240px;"></p>""",
                unsafe_allow_html=True,
            )
            st.write("Even though we were not able to work as closely together as I would have liked, I would love to stay in touch with you as you progress throughout your career. Best wishes!")

    elif page_number == 4:
        st.header("Neighbours next door...")
        #### Eilyn
        eac_cols = st.columns([3.5,3])
        with eac_cols[0]:
            pp = Image.open(r'pic\eilyn.png')
            st.image(pp, width=350,caption="Eilyn")
        with eac_cols[1]:
            # """### gif from local file"""
            file_ = open("messages\good luck.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()

            st.write(
                f"""<p style="text-align:center;"><img src="data:image/gif;base64,{data_url}" style="width:float:right;300px;height:240px;"></p>""",
                unsafe_allow_html=True,
            )
            st.write("I hope your experience with your next employer is as fun as the time we had here. Best of luck and thank you for everything!")

        st.write("\n")
        st.write("\n")

        #### Zhong Fei
        eac_cols = st.columns([3.5,3])
        with eac_cols[0]:
            pp = Image.open(r'pic\ozf.png')
            st.image(pp, width=350,caption="Zhong Fei")
        with eac_cols[1]:
            # """### gif from local file"""
            file_ = open("messages\good luck.gif", "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()

            st.write(
                f"""<p style="text-align:center;"><img src="data:image/gif;base64,{data_url}" style="width:float:right;300px;height:240px;"></p>""",
                unsafe_allow_html=True,
            )
            st.write("Your new team is lucky to have you on board. Wishing you great success in your new role.")

if 'page_num' not in st.session_state:
    st.session_state['page_num'] = 0
    page_content(st.session_state['page_num'])

# st.write(st.session_state.page_num)
# st.write(st.session_state)

def previous_page():
    st.balloons()
    st.session_state['page_num'] -= 1
    page_content(st.session_state['page_num'])


def next_page():
    st.balloons()
    st.session_state['page_num'] += 1
    page_content(st.session_state['page_num'])

cols = st.columns([8,1])
with cols[0]:
    if st.session_state['page_num'] != 0:  
        st.button("Previous", on_click=previous_page)
            # st.session_state['page_num'] -= 1

with cols[1]:
    if st.session_state['page_num'] !=4:
        st.button("Next", on_click=next_page)
            # st.session_state['page_num'] += 1