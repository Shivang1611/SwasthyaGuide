import streamlit as st
import os
from PIL import Image
from utils.style_loader import load_css 


def show_first_aid_page():
    st.title("First Aid Guide")
    load_css()
    
    
    first_aid_data = {
        "Burns": {
            "description": "Cool the burn with running water for 10-15 minutes. Do not use ice. Cover with a sterile bandage.",
            "image": r"C:\Users\User\Desktop\Disease\app\static\burns.jpg"
        },
        "Cuts": {
            "description": "Clean the wound with soap and water. Apply pressure to stop bleeding. Cover with a bandage.",
            "image": r"C:\Users\User\Desktop\Disease\app\static\cuts.jpg"
        },
        "Sprains": {
            "description": "Rest, Ice, Compression, Elevation (RICE).",
            "image": r"C:\Users\User\Desktop\Disease\app\static\Sprains.jpg"
        },
        "Nosebleeds": {
            "description": "Sit upright and lean forward. Pinch your nostrils just below the bony bridge of your nose for 5-10 minutes. Breathe through your mouth.",
            "image": r"C:\Users\User\Desktop\Disease\app\static\nosebledd.jpg"
        },
        "Choking": {
            "description": "If someone is choking and cannot speak or breathe, perform the Heimlich maneuver. If unconscious, begin CPR.",
            "image": r"C:\Users\User\Desktop\Disease\app\static\choking.jpg"
        },
        "Allergic Reactions": {
            "description": "If someone has a severe allergic reaction (anaphylaxis), use an epinephrine auto-injector (EpiPen) if available and call emergency services immediately.",
            "image": r"C:\Users\User\Desktop\Disease\app\static\allergic.jpg"
        },
        "Heart Attack": {
            "description": "Recognize the signs: chest pain, shortness of breath, sweating, nausea. Call emergency services immediately.",
            "image": r"C:\Users\User\Desktop\Disease\app\static\heart_attack.jpg"
        },
        "Fainting": {
            "description": "If someone faints, lay them on their back and elevate their legs. Ensure they have fresh air. If they don't regain consciousness quickly, seek medical attention.",
            "image": r"C:\Users\User\Desktop\Disease\app\static\fainting.jpg"  # Replace with your image
        },
        "Head Injuries": {
            "description": "If someone has a head injury, keep them still and call for emergency medical help, especially if they lose consciousness, vomit, or have a seizure.",
            "image": r"C:\Users\User\Desktop\Disease\app\static\Head-injury.jpg" # Replace with your image
        },
        "Insect Stings": {
            "description": "Remove the stinger if visible. Wash the area with soap and water. Apply a cold compress to reduce swelling. Watch for signs of an allergic reaction.",
            "image":r"C:\Users\User\Desktop\Disease\app\static\insect-string.jpg" # Replace with your image
        },
        "Poisoning": {
            "description": "If someone has ingested poison, call your local poison control center or emergency services immediately. Do not induce vomiting unless instructed to do so.",
            "image": r"C:\Users\User\Desktop\Disease\app\static\poising.jpg" # Replace with your image
        },
    }
    
    # Create columns for better layout
    for topic, info in first_aid_data.items():
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader(topic)
            with st.expander("Show Details"):
                st.write(info["description"])
        
        with col2:
            # Simplified image handling
            try:
                image_url = info["image"]
                image_path = 'app/static/placeholder.webp'
                if image_url != "":
                    st.image(image_url, caption=f"{topic} First Aid", use_container_width=True)
                else:
                    image = Image.open(image_path)
                    st.image(image, caption=f"{topic} First Aid", use_container_width=True)
                    st.write("Image not available")
            except Exception as e:
                st.write(f"Unable to load image: {str(e)}")

