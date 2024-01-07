from PIL import Image
import streamlit as st
import base64
import requests
from streamlit_lottie import st_lottie



st.set_page_config(page_title="Mia Uy", page_icon=":bento_box:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_sew = load_lottieurl('')


# Function to get image as base64 for HTML embedding
def get_image_as_base64(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

#Load Assets

image_path = '/Users/miauy/Desktop/personalWeb/images/headshot2.png'
encoded_image = get_image_as_base64(image_path)
#ktp_logo = 'images/ktp.png'
#encoded_logo = get_image_as_base64(ktp_logo)


#Header Section
with st.container():
    st.title("Mia Uy")
    
    description, spacer, picture = st.columns([3, 1, 3])
    with description:
        st.write(
            """
            Mia, a Computer Science and Immersive Media major with a minor in Economics at the University of Miami, 
            is preparing for a role where she can combine her technical acumen with her creative insights at the intersection 
            of technology and business. As the Co-Founder and Co-President of Kappa Theta Pi, a professional technology fraternity, 
            she has developed her skills in organizational management and established her leadership prowess. Graduating in May 2026, 
            Mia balances her academic and professional pursuits with creative hobbies like cooking, pickleball, crocheting, and sewing, 
            that possess elements of art and science.   
            
            """
            )
    with picture:
        # border
        html_string = f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{encoded_image}" style="border: 15px solid #9d68bb; width: 400px; height: auto;">
            </div>
            """
        st.markdown(html_string, unsafe_allow_html=True)

    

    

# Include FontAwesome
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
        """, unsafe_allow_html=True)
    
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write("---")

#Footer Info
    footer = st.columns(1)

    

    with footer[0]:
        st.markdown("""
        <div style='text-align: center; font-size: 10px;'>
            <p style='margin-bottom: 0;'>Mia Uy</p>
            <p style='margin-top: 0;'><a href='mailto:miauy@miami.edu'>miauy@miami.edu</a></p>
            <p style='margin-top: 0;'>
                <a href="https://www.linkedin.com/in/mia-uy-817a5827a/" target="_blank" style='margin-right: 5px;'>
                    <i class="fab fa-linkedin"></i> LinkedIn
                </a>
                <a href="https://github.com/miauy" target="_blank">
                    <i class="fab fa-github"></i> GitHub
                </a>
            </p>
        </div>
        """, unsafe_allow_html=True)











    


