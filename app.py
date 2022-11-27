import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import pandas as pd

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Acharya Niraj", page_icon=":first_quarter_moon:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def get_yagya_data():
    data = {
        "Yagya": ['Navgrah yagya', 'Adbhut shanti yagya', 'Rudrabhishek', 'Durga yagya', 'Kaliya yagya',
                          'Rogan yagya', 'Vishnu yagya', 'Laxmi yagya'],
        "# Pandit(s)": [5, 5, 5, 5, 5, 5, 5, 5],
        "# Day(s)": [1, 7, 7, 9, 5, 11, 11, 11],
        "Amount": ['$100', '$300', '$500', '$600', '$300', '$700', '$600', '$500']
    }
    # load data into a DataFrame object:
    df = pd.DataFrame(data)

    return df


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_l8wu6ilf.json")
img_header = Image.open("images/HeaderPhoto.png")
img_guru_ji = Image.open("images/GuruJi1.jpg")
img_bala_ji = Image.open("images/Balaji.jpg")
img_acharya_ji = Image.open("images/AcharayaNiraj1.jpg")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- HEADER SECTION ----

with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        st.image(img_bala_ji, width=150,caption='Jai Balaji Maharaj')

    with col3:
        st.write(' ')
        # st.markdown("[Message us on Facebook](https://www.facebook.com/niraj.bajpai.37)")
        # st.markdown(
        #     "[Message us on Whatsapp](https://wa.me/917007656733?text=Hi,%20I'm%20coming%20here%20from%20your%20wbesite.)")
    with st.container():
        image_1_column, image_2_column = st.columns((1, 2))
        with image_1_column:
            # st.image(img_bala_ji, width=100)
            st.subheader("Jai Gurudev :pray:")
            st.title("Acharya Niraj")
            st.write(
                "Acharya Niraj has over 10 years of experience with 'Acharya' degree from Maharishi University and  'Jyotish' degree from Banaras Hindu University."
            )
            st.write("We offer following Yagyas:")
            st.table(get_yagya_data())
            st.markdown("[Message us on Facebook](https://www.facebook.com/niraj.bajpai.37)")
            st.markdown(
                "[Message us on Whatsapp](https://wa.me/917007656733?text=Hi,%20I'm%20coming%20here%20from%20your%20wbesite.)")
        with image_2_column:
            st.image(img_header, use_column_width=True)

# ---- Services Offered ----
# with st.container():
#     st.write("---")
#     left_column, right_column = st.columns(2)
#     with left_column:
#         st.header("Services Offered")
#         st.write("##")
#         st.write(
#             """
#             We offer following services:
#             - Numerology
#             - Horoscope
#             - Palm Reading
#             - Marriage Matching
#             - Vaastu Consultancy
#             """
#         )
#     with right_column:
#         st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
# with st.container():
#     st.write("---")
#     st.header("My Projects")
#     st.write("##")
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(img_lottie_animation)
#     with text_column:
#         st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
#         st.write(
#             """
#             Learn how to use Lottie Files in Streamlit!
#             Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
#             In this tutorial, I'll show you exactly how to do it
#             """
#         )
#         st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
# with st.container():
#     image_column, text_column = st.columns((1, 2))
#     with image_column:
#         st.image(img_contact_form)
#     with text_column:
#         st.subheader("How To Add A Contact Form To Your Streamlit App")
#         st.write(
#             """
#             Want to add a contact form to your Streamlit website?
#             In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
#             """
#         )
#         st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Us!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/ARPANMISHRA1996@GMAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message/questions here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
