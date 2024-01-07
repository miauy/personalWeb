import streamlit as st

#Resume Section

st.set_page_config(page_title="Mia Uy's Resume", page_icon=":bento_box:", layout="wide")

st.markdown("<h1 style='text-align: center;'>Resume</h1>", unsafe_allow_html=True)

with st.container():
    # Centered header with name and contact information
    st.markdown("""
    <div style='text-align: center;'>
        <strong>MIA A. UY</strong><br>
        Roswell GA • miauy@miami.edu • <a href='https://www.linkedin.com/in/mia-uy-817a5827a/' target='_blank'>LinkedIn</a> • U.S Citizen
    </div>
    """, unsafe_allow_html=True)

    # Rest of the resume content
    resume_col = st.columns(1)
    with resume_col[0]:
        st.markdown("""
        ### EDUCATION
        **University of Miami**  
        *College of Arts and Science and School of Communication, Coral Gables, Florida*  
        Bachelor of Arts in Computer Science & Bachelor of Science in Immersive Media & Minor in Economics  
        Expected 2026  
        - Merit Scholarships: President’s Scholarship  
        - GPA: 3.6  
        - Relevant Coursework: Computer Programming 1 and 2, Computer Organization and Architecture, Cybersecurity, Microeconomic Theory, Macroeconomic Theory, Discrete Mathematics 1  

        ### EXPERIENCE
        **INVESCO Advisers Inc.**  
        *Research Analyst Intern – Fixed Income Factors Team, Atlanta, Georgia*  
        June 2023 – July 2023  
        - Analyzed industry and peer group data for Fixed Income Mutual Funds.  
        - Utilized Excel and R for data analysis and PowerPoint for presentations.  
        - Assisted in building Excel-based models for EM Sovereign Credit Analysis and Macroeconomic Analysis.

        **Poke Factory**  
        *Server, Alpharetta, Georgia*  
        February 2021 - August 2022  
        - Prepared and served poke bowls and boba tea orders.

        ### LEADERSHIP
        **Kappa Theta Pi Professional Fraternity**  
        *President & Co-Founder, Coral Gables, Florida*  
        August 2023 – Present  
        - Established the first chapter of Kappa Theta Pi at the University of Miami.  
        - Organized semester rush and selected individuals with a passion for technology.  
        - Conducted bi-weekly meetings and organized workshops and speaker events.

        ### PROJECTS
        **Wordle Simulator**  
        *Java Developer, Coral Gables, Florida*  
        March 2023  
        - Developed a Wordle simulator in Java with input validation and user experience enhancements.

        ### SKILLS / INTERESTS
        - Technical: Java, Python, C++
        - Business Applications: Microsoft Office, Bloomberg
        - Certifications: Bloomberg Market Concepts, CPR
        - Interests: Sewing, Crocheting, Pickleball, Dance, Travel, Manicure Tech, Guitar, Hiking
        """, unsafe_allow_html=True)

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
