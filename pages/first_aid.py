import streamlit as st
import os
import shutil
import tempfile
from PIL import Image
from utils.style_loader import load_css

def show_first_aid_page():
    st.title("First Aid Guide")
    load_css()
    
    first_aid_data = {
        "Burns": {
            "description": "Cool the burn with running water for 10-15 minutes. Do not use ice. Cover with a sterile bandage.",
            "image": "static/burns.jpg"
        },
        "Cuts": {
            "description": "Clean the wound with soap and water. Apply pressure to stop bleeding. Cover with a bandage.",
            "image": "static/cuts.jpg"
        },
        "Sprains": {
            "description": "Rest, Ice, Compression, Elevation (RICE).",
            "image": "static/Sprains.jpg"
        },
        "Nosebleeds": {
            "description": "Sit upright and lean forward. Pinch your nostrils just below the bony bridge of your nose for 5-10 minutes. Breathe through your mouth.",
            "image": "static/nosebledd.jpg"
        },
        "Choking": {
            "description": "If someone is choking and cannot speak or breathe, perform the Heimlich maneuver. If unconscious, begin CPR.",
            "image": "static/choking.jpg"
        },
        "Allergic Reactions": {
            "description": "If someone has a severe allergic reaction (anaphylaxis), use an epinephrine auto-injector (EpiPen) if available and call emergency services immediately.",
            "image": "static/allergic.jpg"
        },
        "Heart Attack": {
            "description": "Recognize the signs: chest pain, shortness of breath, sweating, nausea. Call emergency services immediately.",
            "image": "static/heart_attack.jpg"
        },
        "Fainting": {
            "description": "If someone faints, lay them on their back and elevate their legs. Ensure they have fresh air. If they don't regain consciousness quickly, seek medical attention.",
            "image": "static/fainting.jpg"
        },
        "Head Injuries": {
            "description": "If someone has a head injury, keep them still and call for emergency medical help, especially if they lose consciousness, vomit, or have a seizure.",
            "image": "static/Head-injury.jpg"
        },
        "Insect Stings": {
            "description": "Remove the stinger if visible. Wash the area with soap and water. Apply a cold compress to reduce swelling. Watch for signs of an allergic reaction.",
            "image": "static/insect-string.jpg"
        },
        "Poisoning": {
            "description": "If someone has ingested poison, call your local poison control center or emergency services immediately. Do not induce vomiting unless instructed to do so.",
            "image": "static/poising.jpg"
        },
    }
    
    # Placeholder image path
    placeholder_path = "static/placeholder.webp"
    
    for topic, info in first_aid_data.items():
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader(topic)
            with st.expander("Show Details"):
                st.write(info["description"])
        
        with col2:
            image_url = info["image"]
            if os.path.exists(image_url):
                # Copy the image to Streamlit's temp directory to avoid file access issues
                temp_dir = tempfile.gettempdir()
                temp_path = os.path.join(temp_dir, os.path.basename(image_url))
                shutil.copy(image_url, temp_path)
                st.image(temp_path, caption=f"{topic} First Aid", use_container_width=True)
            else:
                st.image(placeholder_path, caption="Image Not Available", use_container_width=True)
                st.error(f"❌ Image not found: {image_url}")

# Run the first aid guide
show_first_aid_page()
