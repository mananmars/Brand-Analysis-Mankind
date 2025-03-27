import streamlit as st
import os


st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Directories
AUDIO_DIR = "saved_audio"
TRANSCRIPT_DIR = "saved_transcripts"

# Available brands
brands = [
    {
        "Brand": "Virilax Tablet",
        "Price Sensitive": "Yes",
        "Competitor": "High",
        "Product USP Highlighted by MR": "Faster absorption",
        "Doctor Concerns": "Would prefer clinical studies",
    },
    {
        "Brand": "Ossopan D Syrup",
        "Price Sensitive": "No",
        "Competitor": "Medium",
        "Product USP Highlighted by MR": "High calcium content",
        "Doctor Concerns": "Good for long-term use",
    }
]

# Top Field Force Questions
field_force_questions = {
    "Virilax Tablet": [
        "How does it compare with Coenzyme Q10 in terms of composition?",
        "Why does Brillax require 45 days while Fertisure M is prescribed for 30 days?",
        "In how many days does it improve sperm motility and sperm count?",
        "Doctor asked about the reason for loose motion in a patient who took Virilex Tablet."
    ],
    "Ossopan D Syrup": [
        "Can Ossopan D Suspension can be given in pregnancy?",
        "Is Lupin’s claim of >90% absorption valid? How does MCSC compare with Algas Calcareous?",
    ]
}

# Function to list available audio files
def get_audio_files():
    return [f for f in os.listdir(AUDIO_DIR) if f.endswith(".ogg")]

# Custom CSS for grid layout and box styling
st.markdown("""
<style>
.brand-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
    margin-bottom: 20px;
}
.param-box-primary {
    background-color: #e6f2ff;
    border: 1px solid #91c5f2;
    border-radius: 10px;
    padding: 15px;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
}
.param-box-secondary {
    background-color: #f0e6ff;
    border: 1px solid #c5a3ff;
    border-radius: 10px;
    padding: 15px;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
}
.param-box-primary:hover,
.param-box-secondary:hover {
    transform: scale(1.05);
}
.param-box-primary strong {
    color: #0056b3;
    display: block;
    margin-bottom: 5px;
    font-size: 16px;
}
.param-box-secondary strong {
    color: #5200b3;
    display: block;
    margin-bottom: 5px;
    font-size: 16px;
}
.param-box-primary p,
.param-box-secondary p {
    margin: 0;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# Sidebar menu
st.sidebar.title("Options")
selected_option = st.sidebar.radio("Select an option", ["Brand Analysis", "Transcripts", "Top Field Force Question"])

if selected_option == "Brand Analysis":
    st.title("Brand Analysis")

    with st.expander(brands[0]["Brand"]):
        st.markdown(f"<h2>{brands[0]['Brand']}</h2>", unsafe_allow_html=True)

        # Creating 2x2 Grid Layout using Streamlit columns
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                f'<div style="background-color:#e6f2ff; border:1px solid #91c5f2; padding:15px; border-radius:10px; text-align:center;">'
                f'<strong style="color:#0056b3;">Price Sensitive (2)</strong><br>'
                f' <br>'
                f'{brands[0]["Price Sensitive"]}'
                f' <br>'
                f' <br>'
                f'</div>', unsafe_allow_html=True
            )
            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(
                f'<div style="background-color:#ffe6e6; border:1px solid #ff9999; padding:15px; border-radius:10px; text-align:center;">'
                f'<strong style="color:#b30000;">Doctor Concerns (4)</strong><br>'
         f'<ul style="text-align: left; padding-left: 20px;">'
        f'<li>Therapy Cost & Duration</li>'
        f'<li>Side Effects & Safety</li>'
        f'<li>Difference from Coenzyme Q10</li>'
        f'</ul>'
                f'</div>', unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                f'<div style="background-color:#f0e6ff; border:1px solid #c5a3ff; padding:15px; border-radius:10px; text-align:center;">'
                f'<strong style="color:#5200b3;">Competitor (3)</strong><br>'
                f' <br>'
                f'Fertisure M<br>'
                f' <br>'
                f'</div>', unsafe_allow_html=True
            )
            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(
                f'<div style="background-color:#e6ffe6; border:1px solid #99ff99; padding:15px; border-radius:10px; text-align:center;">'
                f'<strong style="color:#006600;">Product USP Highlighted by MR (2)</strong><br>'
        f'<ul style="text-align: left; padding-left: 20px;">'
        f'<li>More Molecules</li>'
        f'<li>Safe for Cardiac and Diabetic patients</li>'
        f'</ul>'
                f'</div>', unsafe_allow_html=True
            )
    with st.expander(brands[1]["Brand"]):
        st.markdown(f"<h2>{brands[1]['Brand']}</h2>", unsafe_allow_html=True)

        # Creating 2x2 Grid Layout using Streamlit columns
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                f'<div style="background-color:#e6f2ff; border:1px solid #91c5f2; padding:15px; border-radius:10px; text-align:center;">'
                f'<strong style="color:#0056b3;">Price Sensitive (0)</strong><br>'
                f' <br>'
                f'No'
                f' <br>'
                f' <br>'
                f'</div>', unsafe_allow_html=True
            )
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(
                f'<div style="background-color:#ffe6e6; border:1px solid #ff9999; padding:15px; border-radius:10px; text-align:center;">'
                f'<strong style="color:#b30000;">Doctor Concerns (3)</strong><br>'
        f'<ul style="text-align: left; padding-left: 20px;">'
        f'<li>Safety during Pregnancy</li>'
        f'<li>Competitor absorption claims</li>'
        f'<li>Lower Calcium than other brands</li>'
        f'</ul>'
                f'</div>', unsafe_allow_html=True
            )

        with col2:
            
            st.markdown(
                f'<div style="background-color:#f0e6ff; border:1px solid #c5a3ff; padding:15px; border-radius:10px; text-align:center;">'
                f'<strong style="color:#5200b3;">Competitor (2)</strong><br>'
                f' <br>'
                f'Lupin’s Almighty Plus'
                f' <br>'
                f' <br>'
                f'</div>', unsafe_allow_html=True
            )
            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(
                f'<div style="background-color:#e6ffe6; border:1px solid #99ff99; padding:15px; border-radius:10px; text-align:center;">'
                f'<strong style="color:#006600;">Product USP Highlighted by MR (3)</strong><br>'
        f'<ul style="text-align: left; padding-left: 20px;">'
        f'<li>MCSC Formulation</li>'
        f'<li>96% absorption rate</li>'
        f'<li>AIIMS Association</li>'
        f'</ul>'
                f'</div>', unsafe_allow_html=True
            )



# Transcripts Section
elif selected_option == "Transcripts":
    st.title("Transcripts")
    audio_files = get_audio_files()

    if audio_files:
        selected_audio = st.selectbox("Select an audio file", audio_files)
        
        # Display audio player
        st.audio(os.path.join(AUDIO_DIR, selected_audio))

        # Extract transcript filename
        transcript_file = f"{selected_audio}.txt"
        transcript_path = os.path.join(TRANSCRIPT_DIR, transcript_file)

        # Display transcript if available
        if os.path.exists(transcript_path):
            with open(transcript_path, "r", encoding="utf-8") as f:
                transcript = f.read()
            st.subheader("Transcript")
            st.write(transcript)
        else:
            st.error("Transcript not found.")
    else:
        st.warning("No audio files found.")

# Top Field Force Question Section
elif selected_option == "Top Field Force Question":
    st.title("Top Field Force Questions")
    for brand, questions in field_force_questions.items():
        st.subheader(brand)
        for question in questions:
            st.write(f"- {question}")