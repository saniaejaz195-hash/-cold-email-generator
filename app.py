import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("❌ GROQ API key not found. Please check your .env file.")
    st.stop()

# Initialize Groq client
client = Groq(api_key=api_key)

# Page config
st.set_page_config(
    page_title="AI Cold Email Generator",
    page_icon="📧",
    layout="centered"
)

# App title
st.title("📧 AI Cold Email Generator")

# ----------- INPUT FIELDS -----------
name = st.text_input("Your Name")

company = st.text_input("Target Company")

purpose = st.text_area(
    "Purpose of Email",
    placeholder="e.g. Applying for a Python Developer role"
)

skills = st.text_area(
    "Your Skills",
    placeholder="e.g. Python, Django, Streamlit, APIs, AI"
)

job_description = st.text_area(
    "Job Description (Optional)",
    placeholder="Paste the job description here (optional)"
)

# ----------- BUTTON ACTION -----------
if st.button("Generate Cold Email"):
    if not name or not company or not purpose or not skills:
        st.warning("⚠️ Please fill all required fields (Name, Company, Purpose, Skills)")
    else:
        prompt = f"""
Write a professional and friendly cold email.

Sender Name: {name}
Target Company: {company}
Purpose of Email: {purpose}

My Skills:
{skills}

Job Description:
{job_description if job_description else "Not provided"}

Instructions:
- Keep the email short and convincing
- Highlight how my skills match the company or job
- End with a polite call to action
"""

        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            st.subheader("✅ Generated Cold Email")
            st.text_area(
                "Email Output",
                response.choices[0].message.content,
                height=300
            )

        except Exception as e:
            st.error(f"❌ Error generating email: {e}")

