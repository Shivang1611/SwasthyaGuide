import streamlit as st

# Set page title - This must be the first Streamlit command


# Title of the app
def show_govt_schemes():
    st.title("All Government Healthcare Schemes")

    # Import CSS from the static file
    with open("static/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Function to create a card
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

    # Display cards in a 2x2 grid layout
    num_columns = 2  # Number of columns
    columns = st.columns(num_columns)  # Create columns

    for index, scheme in enumerate(schemes):
        # Determine which column to place the card in
        col_index = index % num_columns  # This will alternate between 0 and 1
        with columns[col_index]:
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
        
        # After every 2 cards, move to the next row
        if (index + 1) % num_columns == 0:
            columns = st.columns(num_columns)  # Create new columns for the next row

    st.markdown('</div>', unsafe_allow_html=True)