import streamlit as st
import os
from groq import Groq

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="AI Cold Email Generator",
    page_icon="📧",
    layout="centered"
)

st.title("📧 AI Cold Email Generator")

# ---------------- API KEY ----------------
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("❌ GROQ API key not found. Please add it in Streamlit Secrets.")
    st.stop()

client = Groq(api_key=api_key)

# ---------------- INPUT FIELDS ----------------
name = st.text_input("Your Name")

company = st.text_input("Target Company")

purpose = st.text_area(
    "Purpose of Email",
    placeholder="e.g. Applying for Python Developer role"
)

skills = st.text_area(
    "Your Skills",
    placeholder="e.g. Python, Django, Streamlit, APIs, AI"
)

job_description = st.text_area(
    "Job Description (Optional)",
    placeholder="Paste job description here (optional)"
)

# ---------------- BUTTON ACTION ----------------
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
- Use a polite and confident tone
- End with a clear call to action
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
                height=320
            )

        except Exception as e:
           st.error(f"❌ Error generating email: {e}")




