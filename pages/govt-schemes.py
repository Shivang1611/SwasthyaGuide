import streamlit as st

# Set page title
st.set_page_config(page_title="All Government Healthcare Schemes", layout="wide")

# Title of the app
st.title("All Government Healthcare Schemes")

# [Previous CSS styles remain the same as in the last artifact]
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f5f5;
        }
        .card {
            background-color: white;
            border-radius: 15px;
            padding: 25px;
            margin: 15px 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border-left: 5px solid #1976d2;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
        }
        .cards-wrapper {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .card-header {
            background-color: #1976d2;
            padding: 15px;
            color: white;
            border-radius: 10px;
            margin-bottom: 20px;
            text-align: center;
            font-size: 1.3em;
            font-weight: bold;
        }
        .card-content {
            padding: 10px 0;
        }
        .card-content p {
            margin: 15px 0;
            line-height: 1.6;
            color: #333;
        }
        .card-content strong {
            color: #1976d2;
            font-weight: 600;
        }
        .apply-button {
            display: inline-block;
            background-color: grey;
            color: black;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            margin-top: 15px;
            transition: background-color 0.3s ease;
        }
        .apply-button:hover {
            background-color: #1565c0;
        }
        h1 {
            color: #1976d2;
            text-align: center;
            margin-bottom: 30px;
            padding: 20px;
            border-bottom: 3px solid #1976d2;
        }
        @media (max-width: 768px) {
            .card {
                margin: 10px 0;
                padding: 15px;
            }
            .cards-wrapper {
                padding: 10px;
            }
        }
    </style>
""", unsafe_allow_html=True)

# [Previous create_card function remains the same]
def create_card(title, objective, eligibility, benefits, apply_link, details):
    card = f"""
    <div class="card">
        <div class="card-header">
            {title}
        </div>
        <div class="card-content">
            <p><strong>Objective:</strong> {objective}</p>
            <p><strong>Eligibility:</strong> {eligibility}</p>
            <p><strong>Benefits:</strong> {benefits}</p>
            <p><strong>Details:</strong> {details}</p>
            <a class="apply-button" href="{apply_link}" target="_blank">Apply Now</a>
        </div>
    </div>
    """
    return card

# Updated comprehensive list of schemes
schemes = [
    {
        "title": "Ayushman Bharat (PMJAY)",
        "objective": "Provides financial protection to economically disadvantaged families for accessing quality healthcare services.",
        "eligibility": "Families identified as BPL through SECC database. Special priority for women, children, and elderly.",
        "benefits": "Annual health coverage of ₹5 lakh per family. Cashless and paperless treatment at empaneled hospitals.",
        "details": "Covers over 1,500 medical packages including surgery, medical treatments, diagnostics, and day care procedures.",
        "apply_link": "https://pmjay.gov.in/"
    },
    {
        "title": "Central Government Health Scheme (CGHS)",
        "objective": "Provides comprehensive health care to central government employees and pensioners.",
        "eligibility": "Central government employees, pensioners, and their dependent family members.",
        "benefits": "Comprehensive healthcare including OPD, hospitalization, medicines, and specialist consultations.",
        "details": "Services available through wellness centers and empaneled private hospitals. Includes both modern and traditional medicine systems.",
        "apply_link": "https://cghs.gov.in/"
    },
    {
        "title": "Employees' State Insurance Scheme (ESIS)",
        "objective": "Social security scheme providing medical care and financial benefits to workers.",
        "eligibility": "Workers earning up to ₹21,000 per month in covered establishments.",
        "benefits": "Full medical care, maternity benefits, disability benefits, and dependent benefits.",
        "details": "Comprehensive medical care through network of hospitals and dispensaries. Includes preventive, primary, and specialist care.",
        "apply_link": "https://www.esic.gov.in/"
    },
    {
        "title": "Pradhan Mantri Suraksha Bima Yojana (PMSBY)",
        "objective": "Provides accidental death and disability coverage to citizens.",
        "eligibility": "Indians aged 18-70 years with a bank account.",
        "benefits": "₹2 lakh for accidental death; ₹1 lakh for partial disability.",
        "details": "Annual premium of just ₹12. Auto-debit facility from bank account. Renewable annually.",
        "apply_link": "https://www.jansuraksha.gov.in/"
    },
    {
        "title": "Chief Minister's Comprehensive Insurance Scheme (Tamil Nadu)",
        "objective": "Provides universal health coverage to residents of Tamil Nadu.",
        "eligibility": "All families in Tamil Nadu with annual income less than ₹72,000.",
        "benefits": "Coverage up to ₹5 lakh per family per year for specified procedures.",
        "details": "Covers 1,200+ procedures including specialist treatments and critical care.",
        "apply_link": "https://www.cmchistn.com/"
    },
    {
        "title": "Biju Swasthya Kalyan Yojana (Odisha)",
        "objective": "Universal healthcare coverage for people of Odisha.",
        "eligibility": "All families of Odisha with annual income below ₹3 lakh.",
        "benefits": "Coverage up to ₹5 lakh per family. Additional ₹7 lakh for women members.",
        "details": "Cashless treatment at empaneled hospitals. Covers secondary and tertiary care.",
        "apply_link": "https://www.bsky.odisha.gov.in/"
    },
    {
        "title": "Karunya Health Scheme (Kerala)",
        "objective": "Financial assistance for treatment of serious ailments.",
        "eligibility": "BPL families in Kerala suffering from specific critical illnesses.",
        "benefits": "Coverage up to ₹3 lakh for critical illness treatment.",
        "details": "Covers cancer, cardiac, kidney diseases, and other serious ailments. Treatment at empaneled hospitals.",
        "apply_link": "https://kerala.gov.in/karunya-benevolent-fund"
    },
    {
        "title": "Mahatma Jyotiba Phule Jan Arogya Yojana (Maharashtra)",
        "objective": "Provides health insurance coverage to economically vulnerable families.",
        "eligibility": "Yellow and orange ration card holders in Maharashtra.",
        "benefits": "Coverage up to ₹1.5 lakh per family per year.",
        "details": "Covers 996 surgeries/therapies/procedures across 30 specialized categories.",
        "apply_link": "https://www.jeevandayee.gov.in/"
    },
    {
        "title": "Mukhyamantri Amrutum Yojana (Gujarat)",
        "objective": "Health coverage for BPL families and lower income groups.",
        "eligibility": "BPL families and families with annual income below ₹3 lakh.",
        "benefits": "Coverage up to ₹3 lakh per family per year.",
        "details": "Cashless treatment for serious illnesses. Covers pre-existing conditions.",
        "apply_link": "https://www.magujarat.com/"
    },
    {
        "title": "Atal Ayushman Uttarakhand Yojana",
        "objective": "Universal health coverage for Uttarakhand residents.",
        "eligibility": "All permanent residents of Uttarakhand.",
        "benefits": "Annual health coverage of ₹5 lakh per family.",
        "details": "Covers 1,350+ treatment packages. Includes pre and post hospitalization expenses.",
        "apply_link": "https://aayu.uk.gov.in/"
    }
]

# Create a container for all cards
st.markdown('<div class="cards-wrapper">', unsafe_allow_html=True)

# Display cards in a single column
for scheme in schemes:
    st.markdown(
        create_card(
            scheme["title"],
            scheme["objective"],
            scheme["eligibility"],
            scheme["benefits"],
            scheme["apply_link"],
            scheme["details"]
        ),
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)