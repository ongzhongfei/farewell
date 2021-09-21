import streamlit as st
import base64
from PIL import Image
# from pathlib import Path

#### Wordcloud
# from os import path
import numpy as np
import matplotlib.pyplot as plt
import random
from wordcloud import WordCloud, STOPWORDS

st.set_page_config(
    page_title="Congratss",
    page_icon=(":dancers:"),
    layout="wide",
    # initial_sidebar_state="auto",
)

DSA_member_messages = {
    'Dr. Ong': {
        'pic':"pic/ohh.png",
        'gif':'messages/good luck.gif',
        'message': "All the best to you!",
        'video':"https://www.youtube.com/watch?v=TM5RGrV77eI"
    },
    'Chuan Hai':{
        'pic':"pic/nch.png",
        'gif':'messages/good luck.gif',
        'message': "Congratulations on your new job. Wishing you all the best.",
        'video':"https://www.youtube.com/watch?v=TM5RGrV77eI"
    },
    'Mujahid':{
        'pic':"pic/muja.png",
        'gif':'messages/good luck.gif',
        'message': "It was an honor to work with a coworker who was committed to their success and their coworkers. You deserve nothing but the best!",
        'video':"https://www.youtube.com/watch?v=TM5RGrV77eI"
    },
    'Peter':{
        'pic':"pic/peter.png",
        'gif':'messages/good luck.gif',
        'message': "We will remember you with warm thoughts and memories. Best wishes to you in the future.",
        'video':"https://www.youtube.com/watch?v=TM5RGrV77eI"
    },
    'Joshua':{
        'pic':"pic/josh.png",
        'gif':'messages/good luck.gif',
        'message': "No matter where you work, you will always be my friend until the end. Good luck with your new job. I know you’re going to do great.",
        'video':"https://www.youtube.com/watch?v=TM5RGrV77eI"
    },
    'Ken':{
        'pic':"pic/ken.png",
        'gif':'messages/good luck.gif',
        'message': "Even though we were not able to work as closely together as I would have liked, I would love to stay in touch with you as you progress throughout your career. Best wishes!",
        'video':"https://www.youtube.com/watch?v=TM5RGrV77eI"
    },
    'Eilyn':{
        'pic':"pic/eilyn.png",
        'gif':'messages/good luck.gif',
        'message': "I hope your experience with your next employer is as fun as the time we had here. Best of luck and thank you for everything!",
        'video':"https://www.youtube.com/watch?v=TM5RGrV77eI"
    },
    'Zhong Fei':{
        'pic':"pic/ozf.png",
        'gif':'messages/good luck.gif',
        'message': "Your new team is lucky to have you on board. Wishing you great success in your new role.",
        'video':"https://www.youtube.com/watch?v=TM5RGrV77eI"
    },
}

def show_message(member):

    eac_cols = st.columns([3.5,3,5])
    with eac_cols[0]:
        pp = Image.open(DSA_member_messages[member]['pic'])
        st.image(pp, width=350,caption=member)
    with eac_cols[1]:
        # """### gif from local file"""
        file_ = open(DSA_member_messages[member]['gif'], "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.write(
            f"""<p style="text-align:center;"><img src="data:image/gif;base64,{data_url}" style="width:float:right;300px;height:240px;"></p>""",
            unsafe_allow_html=True,
        )
        st.write(DSA_member_messages[member]['message'])
    with eac_cols[2]:

        st.video(DSA_member_messages[member]['video'])

def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

@st.cache(allow_output_mutation=True)
def get_wordcloud(text):
    naz_mask = np.array(Image.open("pic/naz-removebg-preview.png"))

    stopwords = set(STOPWORDS)
    stopwords.add("said")

    # generate word cloud
    wc = WordCloud(background_color="black", max_words=2000, mask=naz_mask,
                stopwords=stopwords, contour_width=0.8, contour_color='steelblue',width=1600, height=800).generate(text)

    return wc

def page_content(page_number):
    if page_number == 0:
        cols = st.columns([1,1,1])

        with cols[1]:
            st.header("Congratulations! and goodbye...")
            st.write("\n")
            st.write(
                f"""<p style="text-align:center;"><img src="https://media3.giphy.com/media/6nuiJjOOQBBn2/200w.webp?cid=ecf05e47xcmnv9n8vasc1d01665fpyw6u8qee6tg305wyews&rid=200w.webp&ct=g" style="width:500px;height:450px;"></p>""",
                unsafe_allow_html=True,
            )
            st.write("\n")
    elif page_number == 1:
        st.header("""If work is your second home. Here is your 'second parent'""")
        show_message('Dr. Ong')

    elif page_number == 2:
        st.header("And here are your homies...")

        show_message('Chuan Hai')   
        st.write("\n")
        st.write("\n")
        show_message('Mujahid')        

    elif page_number == 3:
        st.header("Nerdy neighbours...")
        #### Peter
        show_message('Peter')   
        st.write("\n")
        st.write("\n")
        show_message('Joshua')     
        st.write("\n")
        st.write("\n")
        show_message('Ken')

    elif page_number == 4:
        st.header("Neighbours next door...")

        show_message('Eilyn')   
        st.write("\n")
        st.write("\n")
        show_message('Zhong Fei')

    elif page_number == 5:
        st.header("In JPS-ians' memory, Youa re always...")
        #### Change text here
        text = """I am a boy, good, good boy.
        The numpy library is one of the most popular and helpful libraries that is used for handling multi-dimensional arrays and matrices. It is also used in combination with Pandas library to perform data analysis.

        The Python os module is a built-in library, so you don't have to install it. To read more about handling files with os module, this DataCamp tutorial will be helpful.

        For visualization, matplotlib is a basic library that enables many other libraries to run and plot on its base including seaborn or wordcloud that you will use in this tutorial. The pillow library is a package that enables image reading. Its tutorial can be found here. Pillow is a wrapper for PIL - Python Imaging Library. You will need this library to read in image as the mask for the wordcloud.

        wordcloud can be a little tricky to install. If you only need it for plotting a basic wordcloud, then pip install wordcloud or conda install -c conda-forge wordcloud would be sufficient. However, the latest version with the ability to mask the cloud into any shape of your choice requires a different method of installation as below:
        """

        wc = get_wordcloud(text)
        # show
        fig = plt.figure(figsize=[20, 10], facecolor='k')
        # plt.imshow(wc, interpolation='bilinear')
        plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
                interpolation="bilinear")
        plt.axis("off")
        plt.tight_layout(pad=0)

        wc_cols = st.columns([0.7,1,0.7])
        with wc_cols[1]:
            st.pyplot(fig)

    elif page_number == 6:
        st.header("Messages from your fellow JPS-ians!")

    elif page_number == 7:
        st.header("Unable to meet because of MCO... but we still have these!")
        pp = Image.open('naz_photos/naz_office.jpg')
        st.image(pp, width=350)

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

with cols[1]:
    if st.session_state['page_num'] !=7:
        st.button("Next", on_click=next_page)
