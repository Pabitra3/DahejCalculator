import streamlit as st

st.set_page_config(page_title="Ultimate Dowry Calculator", layout="centered")

st.title("Ultimate Dowry Calculator")
st.markdown("*Disclaimer:* This app is purely for educational/satirical purposes. Dowry is illegal and unethical.")

# 1. Personal Attributes
st.header("1. Personal Attributes")

education_levels = {
    "High School": 10000,
    "Bachelor's": 20000,
    "Master's": 30000,
    "PhD": 50000
}
education = st.selectbox("Education Level", list(education_levels.keys()))

income = st.number_input("Annual Income (₹)", min_value=0, value=10000, step=1000)
degrees = st.number_input("Number of Degrees", min_value=0, value=1)

job_types = {
    "Unemployed": 0,
    "Freelancer": 2000,
    "Private": 5000,
    "Government": 10000,
    "Abroad Job": 15000
}
job = st.selectbox("Job Type", list(job_types.keys()))

age = st.number_input("Age", min_value=18, value=25)
height = st.slider("Height (in feet)", 4.0, 7.0, 5.8)
appearance = st.slider("Physical Appearance (1–10)", 1, 10, 5)

skin_tone_values = {
    "Fair": 3000,
    "Wheatish": 1000,
    "Dark": 0
}
skin_tone = st.selectbox("Skin Tone", list(skin_tone_values.keys()))

# 2. Family & Background
st.header("2. Family & Background")

caste_values = {
    "General": 5000,
    "OBC": 3000,
    "SC/ST": 1000
}
caste = st.selectbox("Caste Category", list(caste_values.keys()))

family_income = st.number_input("Family Annual Income (₹)", min_value=0, value=50000)

father_job_values = {
    "Unemployed": 0,
    "Farmer": 2000,
    "Govt. Employee": 8000,
    "Businessman": 10000
}
father_job = st.selectbox("Father's Occupation", list(father_job_values.keys()))

mother_edu_values = {
    "Illiterate": 0,
    "High School": 1000,
    "Graduate": 3000,
    "Postgraduate": 5000
}
mother_edu = st.selectbox("Mother's Education", list(mother_edu_values.keys()))

siblings = st.number_input("Number of Siblings", min_value=0, value=1)

# 3. Assets & Location
st.header("3. Assets & Location")

location_values = {
    "Rural": 1000,
    "Tier 2 City": 3000,
    "Metro City": 5000
}
location = st.selectbox("Residence Type", list(location_values.keys()))

owns_house = st.checkbox("Owns a House")
owns_land = st.checkbox("Owns Land")

car_values = {
    "No Car": 0,
    "Hatchback": 2000,
    "Sedan": 4000,
    "SUV/Luxury": 10000
}
car = st.selectbox("Car Ownership", list(car_values.keys()))

# 4. Lifestyle & Habits
st.header("4. Lifestyle & Habits")

alcohol_values = {
    "Frequently": -5000,
    "Occasionally": 2000,
    "Never": 5000
}
alcohol = st.selectbox("Alcohol Consumption", list(alcohol_values.keys()))

smoke_values = {
    "Yes": -5000,
    "No": 3000
}
smoke = st.selectbox("Smoking Habit", list(smoke_values.keys()))

fitness = st.slider("Fitness Level (1–10)", 1, 10, 5)
has_gym = st.checkbox("Has a Gym Membership")

# 5. Tech, Superstition, Fun
st.header("5. Tech, Social & Fun Inputs")

phone_values = {
    "iPhone": 5000,
    "Samsung": 3000,
    "Porphix": 10000,
    "Xiaomi / Realme / Oppo / Vivo / OnePlus / Motorola / Huawei": -1000
}
phone = st.selectbox("Mobile Brand Owned", list(phone_values.keys()))

plays_games = st.checkbox("Plays Games Regularly")

followers_instagram = st.number_input("Instagram Followers", min_value=0, value=500)
followers_x = st.number_input("X (Twitter) Followers", min_value=0, value=0)
followers_linkedin = st.number_input("LinkedIn Followers", min_value=0, value=0)
followers_github = st.number_input("GitHub Followers", min_value=0, value=0)
followers_reddit = st.number_input("Reddit Followers", min_value=0, value=0)
followers_discord = st.number_input("Discord Followers", min_value=0, value=0)
followers_telegram = st.number_input("Telegram Followers", min_value=0, value=0)

horoscope = st.slider("Horoscope Match Score (1–10)", 1, 10, 5, 7)
manglik = st.radio("Manglik Status", ["Manglik", "Non-Manglik"])
initial = st.text_input("Name Starts With:")
cook = st.slider("Cooking Skills (1–10)", 1, 10, 5)
pet_lover = st.checkbox("Is a Pet Lover?")

indian_languages = [
    "Hindi", "Bengali", "Telugu", "Marathi", "Tamil", "Urdu", "Gujarati", "Kannada", "Odia", "Malayalam",
    "Punjabi", "Assamese", "Maithili", "Santali", "Kashmiri", "Nepali", "Konkani", "Sindhi", "Dogri",
    "Manipuri", "Bodo", "Sanskrit", "Santhali", "Rajasthani", "Bhili/Bhilodi", "Gondi", "Tulu", "Meitei",
    "Khasi", "Mizo", "Ladakhi", "Garhwali", "Kumaoni", "Magahi", "Chhattisgarhi", "Haryanvi", "Braj",
    "Awadhi", "Bhojpuri"
]

international_languages = [
    "English", "French", "German", "Spanish", "Portuguese", "Italian", "Russian", "Chinese (Mandarin)",
    "Japanese", "Korean", "Arabic", "Turkish", "Persian", "Hebrew", "Dutch", "Greek", "Polish", "Swedish",
    "Norwegian", "Finnish", "Danish", "Czech", "Hungarian", "Romanian", "Ukrainian", "Thai", "Vietnamese",
    "Indonesian", "Filipino", "Malay", "Swahili", "Zulu", "Afrikaans", "Amharic", "Somali", "Burmese",
    "Khmer", "Lao", "Mongolian", "Uzbek", "Kazakh", "Georgian", "Armenian", "Azerbaijani", "Serbian",
    "Croatian", "Bosnian", "Slovak", "Slovenian", "Bulgarian", "Albanian", "Macedonian", "Estonian",
    "Latvian", "Lithuanian"
]

all_languages = sorted(list(set(indian_languages + international_languages)))

languages = st.multiselect("Languages Known", all_languages)
branded_clothes = st.checkbox("Wears Branded Clothes")

# Final Result
if st.button("Calculate Final Dowry"):
    dowry = 0
    dowry += education_levels[education]
    dowry += income * 0.1
    dowry += degrees * 5000
    dowry += job_types[job]
    if age < 30:
        dowry += 5000
    elif age > 35:
        dowry -= 5000
    if height > 6.0:
        dowry += 5000
    elif height < 5.5:
        dowry -= 5000
    dowry += appearance * 1000
    dowry += skin_tone_values[skin_tone]
    dowry += caste_values[caste]
    dowry += family_income * 0.05
    dowry += father_job_values[father_job]
    dowry += mother_edu_values[mother_edu]
    if siblings > 2:
        dowry -= 2000
    dowry += location_values[location]
    if owns_house:
        dowry += 10000
    if owns_land:
        dowry += 15000
    dowry += car_values[car]
    dowry += alcohol_values[alcohol]
    dowry += smoke_values[smoke]
    dowry += fitness * 500
    if has_gym:
        dowry += 2000
    dowry += phone_values[phone]
    if plays_games:
        dowry -= 2000

    # Social followers logic
    if followers_instagram >= 10000:
        dowry += 1000
    elif followers_instagram < 1000:
        dowry -= 1000

    if followers_x >= 1000:
        dowry += 1000
    elif followers_x < 100:
        dowry -= 500

    if followers_linkedin >= 100:
        dowry += 1000
    elif followers_linkedin < 50:
        dowry -= 500

    if followers_github >= 10:
        dowry += 1000
    elif followers_github < 2:
        dowry -= 500

    if followers_reddit >= 1_000_000:
        dowry += 1000
    if followers_discord >= 1_000_000:
        dowry += 1000
    if followers_telegram >= 1_000_000:
        dowry += 1000

    dowry += horoscope * 500
    dowry += -3000 if manglik == "Manglik" else 3000
    if initial and initial[0].lower() in ['a', 's', 'p']:
        dowry += 1000
    dowry += cook * 300
    if pet_lover:
        dowry -= 1000
    dowry += len(languages) * 1000
    if branded_clothes:
        dowry += 2000

    st.success(f"Estimated Satirical Dowry: ₹{dowry:,.2f}")