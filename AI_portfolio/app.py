import streamlit as st
import base64
import os
import requests
import matplotlib.pyplot as plt

# Function to encode the image to base64
def get_base64_encoded_image(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        st.error(f"File not found: {image_path}")
        return None

# Path to your local images
image_path = "images/3408105.jpg"
base64_image = get_base64_encoded_image(image_path)

profile_image_path = "images/profile.jpg"
base64_profile_image = get_base64_encoded_image(profile_image_path)

# Project images
project_image_paths = ["images/project2.jpg", "images/project3.jpg", "images/project1.jpg"]
project_images_base64 = [get_base64_encoded_image(img) for img in project_image_paths]

# Function to handle bot responses
def get_bot_response(user_input):
    responses = {
        "what is your name" or "what is your name" or "WHAT IS YOUR NAME" : "I'm John Doe, a data scientist and software engineer. 👨‍💻",
        "name" or "Name" : "I'm John Doe, a data scientist and software engineer. 👨‍💻",
        "what is your education": "I have a degree in Computer Science from XYZ University. 🎓",
        "education": "I have a degree in Computer Science from XYZ University. 🎓",
        "your skills": "I specialize in Python, machine learning, data analysis, and web development. 🛠️",
        "skills": "I specialize in Python, machine learning, data analysis, and web development. 🛠️",
        "your setup": "I work on a high-performance laptop with 16GB RAM and an Intel i7 processor. 💻",
        "setup": "I work on a high-performance laptop with 16GB RAM and an Intel i7 processor. 💻",
        "who are you": "I'm John Doe, a data scientist and software engineer. I have a degree in Computer Science from XYZ University. I specialize in Python, machine learning, data analysis, and web development. 👨‍💻",
        "default": "I'm not sure how to respond to that. Please ask me something about myself or my setup. 🤔"
    }
    return responses.get(user_input.lower(), responses["default"])

def get_github_profile(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    return response.json()

def get_github_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    return response.json()

def plot_languages():
    languages = {
        "Python": 60,
        "Jupyter Notebook": 20,
        "C": 10,
        "JavaScript": 10
    }
    fig, ax = plt.subplots()
    ax.pie(languages.values(), labels=languages.keys(), autopct='%1.1f%%')
    ax.axis('equal')
    return fig

def main():
    # CSS to set the background image and style adjustments
    st.markdown(
        f"""
        <style>
        body, .stApp {{
            overflow: hidden; /* Disable scrolling */
        }}
        .stApp {{
            background: url("data:image/jpeg;base64,{base64_image}") no-repeat center center fixed;
            background-size: cover;
        }}
        .sidebar .sidebar-content {{
            background: rgba(255, 255, 255, 0.8);
        }}
        .block-container {{
            background: rgba(0, 0, 0, 0.6);
            border-radius: 10px;
            padding: 2rem;
            max-width: 100% !important; /* Increase max width */
            width: 100% !important; /* Ensure full width */
            margin: 0 auto; /* Center align the content */
            color: white;
        }}
        h1 {{
            font-size: 60px !important;
            color: white;
            font-weight: 700;
        }}
        h2 {{
            font-size: 50px !important;
            color: white;
            font-weight: 700;
        }}
        h3 {{
            font-size: 40px !important;
            color: white;
            font-weight: 700;
        }}
        p, li {{
            font-size: 30px !important;
            color: white;
            font-weight: 400;
        }}
        input, textarea {{
            font-size: 30px !important;
            color: white;
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid white;
            border-radius: 5px;
            padding: 0.5rem;
        }}
        .navbar {{
            display: flex;
            justify-content: space-around;
            padding: 1rem;
            margin-bottom: 2rem;
            background: rgba(0, 0, 0, 0.6);
            border-radius: 10px;
            width: 100%; /* Ensure full width */
        }}
        .navbar div {{
            font-size: 50px;
            padding: 0.5rem 1rem;
            color: white;
            cursor: pointer;
            background: transparent;
            border: none;
            outline: none;
            box-shadow: none;
        }}
        .navbar div:hover {{
            color: #ccc;
        }}
        .about-image-container img {{
            margin-top: -30px; /* Adjust this value to move the image up */
            max-width: 100%; /* Adjust this value to set the maximum width */
            height: auto; /* Maintain aspect ratio */
            border-radius: 20px; /* Rounded rectangle shape */
            animation: float 3s ease-in-out infinite; /* Simple floating animation */
            width: 80%; /* Change this value to set the width of the image */
        }}
        @keyframes float {{
            0% {{
                transform: translatey(0px);
            }}
            50% {{
                transform: translatey(-10px);
            }}
            100% {{
                transform: translatey(0px);
            }}
        }}
        .home-emoji {{
            font-size: 100px;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 50vh; /* Center the emoji vertically and reduce height for more spacing */
            animation: bounce 1s infinite;
        }}
        @keyframes bounce {{
            0%, 100% {{
                transform: translateY(0);
            }}
            50% {{
                transform: translateY(-20px);
            }}
        }}
        .home-details {{
            text-align: center;
            font-size: 30px;
            margin-top: 20px;
        }}
        .project-image {{
            width: 300px;
            height: 300px;
            border-radius: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            animation: zoom 5s infinite;
        }}
        @keyframes zoom {{
            0%, 100% {{
                transform: scale(1);
            }}
            50% {{
                transform: scale(1.1);
            }}
        }}
        .contact-info {{
            font-size: 30px;
            line-height: 1.6;
        }}
        .contact-map {{
            width: 100%;
            height: 400px;
            border: none;
            border-radius: 10px;
            animation: zoom 5s infinite;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Welcome to my Portfolio")

    # Default page
    if 'page' not in st.session_state:
        st.session_state.page = 'Home'

    # Navigation texts
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col1:
        if st.button("Home"):
            st.session_state.page = 'Home'
    with col2:
        if st.button("About"):
            st.session_state.page = 'About'
    with col3:
        if st.button("Projects"):
            st.session_state.page = 'Projects'
    with col4:
        if st.button("Skills"):
            st.session_state.page = 'Skills'
    with col5:
        if st.button("Contact"):
            st.session_state.page = 'Contact'
    with col6:
        if st.button("AI Bot"):
            st.session_state.page = 'AIBot'
    with col7:
        if st.button("GitHub"):
            st.session_state.page = 'GitHub'

    # Page content based on the selected navigation text
    if st.session_state.page == 'Home':
        st.header("Welcome to My Portfolio")
        st.write("My personal portfolio with AI bot 🤖")
        st.markdown(
            """
            <div class="home-emoji">👋</div>
            <div class="home-details">Welcome to my portfolio website. Explore my projects, skills, and get to know more about me.</div>
            """,
            unsafe_allow_html=True
        )

    elif st.session_state.page == 'About':
        st.header("About Me")
        col1, col2 = st.columns([3, 2])
        with col1:
            st.write("A brief introduction about myself. 📖")
            st.write("I am a data scientist and software engineer with a passion for technology and innovation. I enjoy solving complex problems and building useful applications.")
        with col2:
            st.markdown(f"""
            <div class="about-image-container">
                <img src="data:image/jpeg;base64,{base64_profile_image}" alt="Profile Image">
            </div>
            """, unsafe_allow_html=True)

    elif st.session_state.page == 'Projects':
        st.header("Projects")
        st.write("Here are some of my live projects:")
        st.write("### AI Based Chatbot")
        st.image(f"data:image/jpeg;base64,{project_images_base64[0]}", caption="AI Based Chatbot", use_column_width=True)
        st.write("### Image Generator App")
        st.image(f"data:image/jpeg;base64,{project_images_base64[1]}", caption="Image Generator App", use_column_width=True)
        st.write("### Weed Detection App")
        st.image(f"data:image/jpeg;base64,{project_images_base64[2]}", caption="Weed Detection App", use_column_width=True)

    elif st.session_state.page == 'Skills':
        st.header("Skills")
        st.write("Here are some of my skills:")
        st.slider("Python", 0, 100, 70)
        st.slider("Machine Learning", 0, 100, 60)
        st.slider("Data Analysis", 0, 100, 50)
        st.slider("Web Development", 0, 100, 40)

    elif st.session_state.page == 'Contact':
        st.header("Contact Information")
        st.write("You can reach me via the following:")
        st.write("📞 Phone: +123-456-7890")
        st.write("📧 Email: johndoe@example.com")
        st.write("📍 Location: ATIN NLC Mandra")
        st.markdown(
            """
            <iframe class="contact-map" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d159254.17929657102!2d73.09867834804043!3d33.58392502072777!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x38dfb6c2df9b95b5%3A0x1dcb0fdce6579d37!2sATIN%20NLC%20Mandra!5e0!3m2!1sen!2sus!4v1599498267817!5m2!1sen!2sus" allowfullscreen="" loading="lazy"></iframe>
            """,
            unsafe_allow_html=True
        )

    elif st.session_state.page == 'AIBot':
        st.header("AI Bot")
        st.write("Interact with my AI bot below:")
        user_input = st.text_input("Ask me something:")
        if user_input:
            bot_response = get_bot_response(user_input)
            st.write(f"🤖 Bot: {bot_response}")

    elif st.session_state.page == 'GitHub':
        st.header("GitHub Profile")
        username = "mt111tayyab"
        profile = get_github_profile(username)
        repos = get_github_repositories(username)
        st.write(f"### {profile['name']}'s GitHub Profile")
        st.write(f"📌 Bio: {profile['bio']}")
        st.write(f"🔗 GitHub URL: [Link](https://github.com/{username})")

        # Plot languages used in repositories
        st.write("### Repository Languages")
        fig = plot_languages()
        st.pyplot(fig)

if __name__ == "__main__":
    main()
