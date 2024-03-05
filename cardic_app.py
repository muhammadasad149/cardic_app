import streamlit as st
from streamlit_chat import message
import google.generativeai as palm
import os
from dotenv import load_dotenv

# Streamlit app
def main():

    load_dotenv()  # take environment variables from .env (especially openai api key)

    palm.configure(api_key=os.environ["GOOGLE_API_KEY"])


    # Create a new conversation
    response = palm.chat(
        messages='Hello',
        temperature=0.5
    )


    st.title("Cardiac Surgery Expert")

    symptoms = [
        "Stomach", "Nausea", "Vomiting", "Acid reflux", "Improvement with Bending",
        "Localised", "Throat", "Diffuse", "Splitting", "Seconds", "Minutes", "Hours",
        "Days", "Weeks", "Months", "Years", "Central", "Exertional", "Retrosternal",
        "Left side", "Right side", "Radiates", "Jaw", "Left arm", "Right arm",
        "Radiating to Back", "Pressure", "Squeezing", "Gripping", "Heaviness",
        "Tightness", "Dull", "Ache", "Stabbing", "Tearing", "Ripping", "Burning",
        "Boring", "Sharp", "Pleuritic", "Positional", "Fleeting", "Sweating",
        "Tender", "Fever", "Cough", "Short of breath", "Sudden", "Gradual",
        "Severe", "Subacute", "Onset at rest", "Nitrate relief", "Syncope",
        "Persistent", "Intermittent", "Eating", "Infarct", "CAD (Coronary artery disease)",
        "Aortic dissection", "PE/DVT (Deep Vein Thrombosis and Pulmonary Embolism)",
        "CHF (congestive heart failure)", "Pericarditis", "AS/AI (Aortic Insufficiency)",
        "Coagulopathy", "CTD (connective tissue disease)", "Auto immune", "Esophagus",
        "G.I. (gastrointestinal)", "Musculoskeletal", "COPD (Chronic obstructive pulmonary disease)",
        "Age_65", "DM (Diabetes mellitus)", "HTN (Hypertension)", "HLD (Hyperlipidemia)",
        "GreaterCRF's (Chronic renal failure)", "CP1Day (cytopathologists)",
        "FH (Familial hypercholesterolemia)", "Bed ridden", "Recent surgery ",
        "TOB (Tobacco)", "Travel", "ASA", "Calf pain/swell", "Edema", "Abd tender",
        "Point tender", "S3", "R S3", "Murmur systolic", "Murmur Diastolic",
        "Pericardial rub", "JVD> 4cm (jugular venous distension greater than 4 centimeters)",
        "Diaphoresis", "Low carotid puls", "Un= pulses", "BP differential",
        "Rhonchi/wheeze", "HR>100 (heart rate greater than 100)",
        "T>100.4 (temperature is greater than 100.4)", "RR>20 (respiratory rate is greater than 20)",
        "Sbp>140 (systolic blood pressure is greater than 140)",
        "Sbp< 100 (ystolic blood pressure is less than 100)",
        "O2sat < 90 (oxygen saturation level is less than 90)",
        "Pleural Rub", "Rales", "CTA (Computed Tomography Angiography)"
    ]

    disease = ['Infarct', 'Ischemia', 'Aortic', 'Dissection', 'PE', 'CHF', 'Pericarditis',
               'AS/AI', 'Pulmonary', 'Eso', 'rupture', 'MS', 'GI']

    user_query = st.text_input("Ask a CARDIC question:")

    if user_query:
        prompt = f'''
                You are an expert in Cardiology Report. You have expertise in diagnose disease based on symptoms and treat disease,and specialties in Cardiology. You are an expert in Cardiology. You can only use the following symptoms and disease lists.                
                
                Symptoms: {symptoms}

                Paragraph: {user_query}

                disease: {disease}

                Task 1:
                List the symptoms from the list of symptoms that match the symptoms mentioned in the paragraph.

                Task 2:
                Identify the patient's age from the paragraph.

                Task 3:
                Task 1: in which thier is the symptoms and in Task 2: thier is the age of patient, 
                then list the disease from the list of disease that match the symptoms,and age mentioned in the Task1 AND Task2.
                disease should be given atleast 2 or 3 and why or describ it.


                Example:
                Symptoms: [fever, cough, sore throat]

                Paragraph:
                A 25-year-old male patient presented to the clinic with a 3-day history of fever, cough, and sore throat. He also reported having a headache and muscle aches. The patient's vital signs were within normal limits. A physical examination revealed a mild erythema of the pharynx and tonsils.

                Task 1:
                [fever, cough, sore throat]

                Task 2:
                25 years old

                Task 3:
                [Disease1, Disease2]
            '''
        response = response.reply(prompt)
        output = response.last
        st.write(f"Answer : {output}")
        
        
if __name__ == "__main__":
    main()