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

import pandas as pd


st.set_page_config(
    page_title="Congratss",
    page_icon=(":tada:"),
    layout="wide",
    # initial_sidebar_state="auto",
)

DSA_member_messages = {
    'Dr. Ong': {
        'pic':"pic/ohh.png",
        'pic_caption':'Dr. Ong',
        'gif':'messages/ohh_message.jfif',
        'gif_width': '380',
        'message': "The Virtual Get-together that you organised was a memorable one.  Don't be a stranger and let's keep in touch. Best wishes.",
        "text_color":"#52D273",
        'video':"https://www.youtube.com/watch?v=tbnzAVRZ9Xc",
        'video_text':"It takes courage to pursue a dream.",
    },
    'Chuan Hai':{
        'pic':"pic/nch_pp.jpg",
        'pic_caption':'Chuan Hai',
        'gif':'messages/feeling.gif',
        'gif_width': '380',
        'message': "Congratulations on your new job. Wishing you all the best.",
        "text_color":"#52D273",
        'video':"https://www.youtube.com/watch?v=sVJQZ16Da_A",
        'video_text':"",
    },
    'Mujahid':{
        'pic':"pic/Muja and Naz.jpeg",
        'pic_caption':'Me and Naz on our first hackathon win together!',
        'gif':'messages/im-happy-for-you-mia.gif',
        'gif_width': '380',
        'message': """
                <br>I do feel sad that you are leaving us, and I admit, the reasons for that are mainly for selfish reasons as I feel like I could still learn so much more from you. But it's sort of like a bittersweet thing; I do feel sad that you're leaving us, but at the same time, I feel very excited for you with this new opportunity and journey that you're partaking, and I'm excited, I'm really, really excited that you can finally spread your wings after feeling trapped for so long. \
                <br><br>I know it's going to be a lot of pressure for you, breaking the BNM bond is definitely not an easy decision to make but I'm proud of you for taking that step and doing what's right for you, for your career and for your future. I only hope that we stay in touch and keep the connection alive, and I wish you all the success in life.
        """,
        "text_color":"#52D273",
        'video':"https://www.youtube.com/watch?v=NqJ9I7HyYws",
        'video_text':"""This song is a letter for those afraid of losing their self due to life and the pressures that come with it. As you go through your next chapter in life, I hope this song can serve as reminder for you to stay your humble self and not forget the "kid you used to know".""",
    },
    'Peter':{
        'pic':"pic/peter.png",
        'pic_caption':'Peter',
        'gif':'messages/i-dont-always-win-the-hackathon-but-at-least-i-look-good-trying.jpg',
        'gif_width': '350',
        'message': "Otai never really goes way. They linger on , for what they have done will echo in eternity.<br>Makan with me ya when we can?",
        "text_color":"#46BCDE",
        'video':"https://www.youtube.com/watch?v=zuf1KuibAeY",
        'video_text':"Go where Naz has not gone before",
    },
    'Joshua':{
        'pic':"pic/josh_pp_brighter.png",
        'pic_caption':'Keep living the Google dream',
        'gif':'messages/bernie_meme.jpg',
        'gif_width': '350',
        'message': "No matter where you work, you will always be my friend until the end. Good luck with your new job. I know you’re going to do great.",
        "text_color":"#46BCDE",
        'video':"https://www.youtube.com/watch?v=jStNaVCW838",
        'video_text':"To the most jiwang man I know. Karaoke, we must.",
    },
    'Ken':{
        'pic':"pic/ken.png",
        'pic_caption':'Ken',
        'gif':'messages/ken_goodbye.png',
        'gif_width': '300',
        'message': "Good luck & all the best Naz! Appreciate your guidance and help all this while especially when I was still new to Python (plz forgive me for my spaghetti codes :wink:). Working with you was a pleasure and I personally learnt a lot from you. Hope someday our paths will cross again :hugging_face:",
        "text_color":"#46BCDE",
        'video':"https://www.youtube.com/watch?v=RgKAFK5djSk",
        'video_text':"",
    },
    'Eilyn':{
        'pic':"pic/eilyn_pp.jpg",
        'pic_caption':'Pika Eilyn',
        'gif':'messages/eilyn_message.png',
        'gif_width': '280',
        'message': "Naz, I am so glad to be working along with you over the past year! I will miss our Kpop chatter, ranting sesh, and the random conversations about our personal visions.  I hope our paths will cross again – let’s catch up whenever IU (or any GFriend members) releases her new album/single! Until then …",
        # "I hope your experience with your next employer is as fun as the time we had here. Best of luck and thank you for everything!",
        "text_color":"#C8A2C8",
        'video':"https://www.youtube.com/watch?v=v7bnOxV4jAc",
        'video_text':"As befitting your upcoming journey, I wish to dedicate for your listening pleasure IU’s Lilac, which means 'memories of youth' – a farewell to your past chapter and hopeful greetings for the next one.",
    },
    'Zhong Fei':{
        'pic':"pic/zhongfei_pp.jpeg",
        'pic_caption':'First time petting a rabbit',
        'gif':'messages/i-bid-you-farewell-good-luck.gif',
        'gif_width': '280',
        'message': "Sincerely thank you for all the knowledge you taught since I am in from day 1. Your new team is lucky to have you on board. Wishing you great success in your new role.",
        "text_color":"#C8A2C8",
        'video':"https://www.youtube.com/watch?v=D1PvIWdJ8xo",
        'video_text':"My go to song during down times... (and of course it's good during happy times too!)",
    },
}

@st.experimental_memo#@st.cache()
def get_jps_messages():
    jps_survey = pd.read_excel("Farewell message to Khairul Nazran.xlsx")


    #### JPS messages
    survey_cols = jps_survey.columns
    jps_survey[survey_cols[7]] = jps_survey[survey_cols[7]].fillna("Anonymous")
    jps_messages = jps_survey.set_index(survey_cols[6]).to_dict()[survey_cols[7]]

    #### One word adjectives
    jps_survey[survey_cols[5]] = jps_survey[survey_cols[5]].str.replace("Serious but Not Serious","Serious_but_not_serious")
    jps_survey[survey_cols[5]] = jps_survey[survey_cols[5]].str.replace("(one word not enough ;p)",'')
    jps_survey[survey_cols[5]] = jps_survey[survey_cols[5]].str.replace("(Is there no problem he can’t fix)",'No_problem_he_cant_fix')
    jps_survey[survey_cols[5]] = jps_survey[survey_cols[5]].str.replace("Nice person",'Nice')

    jps_survey[survey_cols[5]] = jps_survey[survey_cols[5]].str.replace("?",'',regex=False)
    jps_survey[survey_cols[5]] = jps_survey[survey_cols[5]].str.replace("(",'',regex=False)
    jps_survey[survey_cols[5]] = jps_survey[survey_cols[5]].str.replace(")",'',regex=False)
    jps_survey[survey_cols[5]] = jps_survey[survey_cols[5]].str.title().str.strip()
    wordcloud_adjectives = ' '.join(jps_survey[survey_cols[5]].fillna(''))


    return jps_messages, wordcloud_adjectives

def show_message(member):

    eac_cols = st.columns([2.8,3,5.5])
    with eac_cols[0]:
        pp = Image.open(DSA_member_messages[member]['pic'])
        if member == "Joshua":
            st.image(pp, width=450,caption=DSA_member_messages[member]['pic_caption'])
        elif member =="Mujahid":
            st.image(pp, width=380,caption=DSA_member_messages[member]['pic_caption'])
            st.write(f"""<span style="color:{DSA_member_messages[member]['text_color']};font-size:21px">             Working with you felt really good. We would often bounce ideas off of each other and it felt really natural and exciting. You're more than a colleague to me; you're an inspiration, a mentor and a senpai to me. I appreciate the moments where you guided me in navigating the BNM world. You exposed me to the gems and you steered me away from the bullshit, and I take your advice very seriously. \
                <br><br>I would like to start off by thanking you for opening so many doors for me. The fact that I'm here in this team, in DSA, is because of you. Other opportunities like the hackathons, the wins, the exposure, the street cred and the connections that I've made in the community were none other because of you.</span>""",unsafe_allow_html=True)
        else:
            st.image(pp, width=380,caption=DSA_member_messages[member]['pic_caption'])
    with eac_cols[1]:
        # """### gif from local file"""
        file_ = open(DSA_member_messages[member]['gif'], "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.write(
            f"""<p style="text-align:center;"><img src="data:image/gif;base64,{data_url}" style="width:{DSA_member_messages[member]['gif_width']}px;height:400px;float:center"></p>""",
            unsafe_allow_html=True,
        )
        st.write(f"""<span style="color:{DSA_member_messages[member]['text_color']};font-size:21px"> {DSA_member_messages[member]['message']}</span>""",unsafe_allow_html=True)
    with eac_cols[2]:
        if DSA_member_messages[member]['video_text'] != '':
            st.write(f"""<span style="color:{DSA_member_messages[member]['text_color']};font-size:16px"> {DSA_member_messages[member]['video_text']}</span>""",unsafe_allow_html=True)
        st.video(DSA_member_messages[member]['video'])

def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

@st.experimental_memo#@st.cache()
def get_wordcloud(text):
    naz_mask = np.array(Image.open("pic/naz-removebg-preview.png"))

    stopwords = set(STOPWORDS)
    stopwords.add("said")

    # generate word cloud
    wc = WordCloud(background_color="black", max_words=2000, mask=naz_mask,
                stopwords=stopwords, contour_width=0.8, contour_color='steelblue',width=1600, height=800).generate(text)

    return wc
jps_messages, wordcloud_adjectives = get_jps_messages()


def page_content(page_number):
    if page_number == 0:
        cols = st.columns([1,1,1])

        with cols[1]:
            # st.header("Congratulations! and goodbye...")
            st.write(
                f"""<span style="color:#00FFFF;font-size:33px"> <b> Congratulations! and goodbye... <br>to the Meme Master</b></span>""",
                unsafe_allow_html=True,
            )

            st.subheader("The Usual Naz... :male-office-worker:")
            naz_office = Image.open('naz_photos/naz_office.jpg')
            st.image(naz_office, width=455)
            naz_pp = Image.open('naz_photos/naz.png')
            st.image(naz_pp, width=380)

            # st.write("<br>",unsafe_allow_html=True)
            st.write("<br>",unsafe_allow_html=True)


            st.subheader("Naz after October 4th 2021... :tada: ")
            # st.write(
            #     f"""<p><img src="https://media3.giphy.com/media/6nuiJjOOQBBn2/200w.webp?cid=ecf05e47xcmnv9n8vasc1d01665fpyw6u8qee6tg305wyews&rid=200w.webp&ct=g" style="width:500px;height:450px;"></p>""",
            #     unsafe_allow_html=True,
            # )  #### Requires internet
            file_ = open('messages/celebration.gif', "rb")
            contents = file_.read()
            data_url = base64.b64encode(contents).decode("utf-8")
            file_.close()

            st.write(
                f"""<p><img src="data:image/gif;base64,{data_url}" style="width:500px;height:400px"></p>""",
                unsafe_allow_html=True,
            )
            st.write("\n")
    elif page_number == 1:
        st.write(
            f"""<span style="color:#52D273;font-size:40px"> <b> If work is your second home. Here is your 'second parent'</b></span>""",
            unsafe_allow_html=True,
        )
        show_message('Dr. Ong')

        st.write("***")
        st.write(
            f"""<span style="color:#52D273;font-size:40px"> <b> And here are your homies...</b></span>""",
            unsafe_allow_html=True,
        )
        show_message('Chuan Hai')   
        st.write("\n")
        st.write("\n")
        show_message('Mujahid')        

    elif page_number == 2:
        st.write(
            f"""<span style="color:#46BCDE;font-size:40px"> <b> Your nerdy neighbours...</b></span>""",
            unsafe_allow_html=True,
        )
        #### Peter
        show_message('Peter')   
        st.write("\n")
        st.write("\n")
        show_message('Joshua')     
        st.write("\n")
        st.write("\n")
        show_message('Ken')
        st.write("\n")
        st.write("\n")
        # st.write("***")
        # st.header("Neighbours next door...")

        # show_message('Eilyn')   
        # st.write("\n")
        # st.write("\n")
        # show_message('Zhong Fei')
    elif page_number == 3:
        st.write(
            f"""<span style="color:#C8A2C8;font-size:40px"> <b> And neighbours next door...</b></span>""",
            unsafe_allow_html=True,
        )
        show_message('Eilyn')   
        st.write("\n")
        st.write("\n")
        show_message('Zhong Fei')

    elif page_number == 4:
        st.header("In JPS-ians' memory, You're always... :sunglasses:")
        #### Change text here
        text = wordcloud_adjectives

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

    elif page_number == 5:
        st.header("""Messages from your fellow JPS-ians! :man-woman-girl-boy:""")
        st.write("<br>",unsafe_allow_html=True)
        st.write("<br>",unsafe_allow_html=True)
        # st.write(jps_messages)
        count = 0
        for message, people in jps_messages.items():
            if people == 'Li Ming':
                cols_to_write = st.columns ([1,6,1.5])
                cols_to_write[1].write(
                    f"""<span style="font-size:26px;color:#FFCC66"> {message.strip()}</span> <span style="color:#FFC0CB;font-size:28px;text-align:right"> - <b><i>{people}</i></b></span>""",
                    unsafe_allow_html=True,
                )
                # cols_to_write[1].write(
                #     f""" <p style="color:#FFC0CB;font-size:28px;text-align:right"> - <b><i>{people}</i></b></p>""",
                #     unsafe_allow_html=True,
                # )
        st.write("<br>",unsafe_allow_html=True)
        st.write("<br>",unsafe_allow_html=True)
        for message, people in jps_messages.items():
            if people != 'Li Ming':
                cols_to_write = st.columns([1,3,3,1.5])
                if count % 2 == 0:
                    col_picked = 1
                    # cols_to_write[col_picked].write(
                    #     f"""<p style="font-size:20px;"> {message.strip()}</p>""",
                    #     unsafe_allow_html=True,
                    # )
                    # cols_to_write[col_picked].write(
                    #     f""" <p style="color:#FFC0CB;font-size:20px;text-align:right"> - <b>{people}</b></p>""",
                    #     unsafe_allow_html=True,
                    # )
                else:
                    col_picked = 2
                    # cols_to_write[col_picked].write(
                    #     f"""<p style="font-size:20px;text-align:right"> {message.strip()}</p>""",
                    #     unsafe_allow_html=True,
                    # )
                    # cols_to_write[col_picked].write(
                    #     f""" <p style="color:#FFC0CB;font-size:20px;text-align:right"> - <b>{people}</b></p>""",
                    #     unsafe_allow_html=True,
                    # )
                cols_to_write[col_picked].write(
                    f"""<span style="font-size:20px"> {message.strip()}</span>  -  <span style="color:#FFC0CB;font-size:20px"> <b><i>{people}</i></b></span>""",
                    unsafe_allow_html=True,
                )

                count +=1

    elif page_number == 6:
        st.header("Unable to meet because of MCO... but we still have these!")

        #### Naz general photos
        cols = st.columns([1,1,1,0.5,2])
        naz_office = Image.open('naz_photos/naz_office.jpg')
        cols[0].image(naz_office, width=500)
        naz_pp = Image.open('naz_photos/naz.png')
        cols[2].image(naz_pp, width=280)
        gsy4 = Image.open('naz_photos/Hackathon win with Naz.jpeg')
        cols[4].image(gsy4, width=400)


        #### DSA
        cols = st.columns([1.8,2.5])
        naz_flower = Image.open('naz_photos/naz_flower.png')
        cols[0].image(naz_flower, width=600)
        dsa_flower = Image.open('naz_photos/dsa_flower.png')
        cols[1].image(dsa_flower, width=1020)
        #### With GSY
        cols = st.columns([1,1,1])
        gsy1 = Image.open('naz_photos/gsy1.jpeg')
        cols[0].image(gsy1, width=500)
        gsy2 = Image.open('naz_photos/gsy2.jpeg')
        cols[1].image(gsy2, width=500)
        gsy3 = Image.open('naz_photos/gsy3.jpeg')
        cols[2].image(gsy3, width=500)
        # gsy4 = Image.open('naz_photos/gsy4.jpeg')
        # cols[3].image(gsy4, width=400)

        st.write('\n\n')
        st.write(
            f"""<p style="text-align:right;color:#FFCC66;font-size:50px"> <b><i> Good Luck in Your Future Endeavors!</b></i></p>""",
            unsafe_allow_html=True,
        )

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
    if st.session_state['page_num'] != 6:
        st.button("Next", on_click=next_page)
