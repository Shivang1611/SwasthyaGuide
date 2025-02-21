import streamlit as st
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import requests
import time
import os

print("Current file path:", os.path.abspath(__file__))

def get_nearby_healthcare(lat, lon, radius=5000):
    """
    Use OpenStreetMap's Overpass API to find healthcare facilities.
    This is completely free and doesn't require an API key.
    """
    # Overpass API query to find hospitals and doctors
    overpass_url = "https://overpass-api.de/api/interpreter"
    overpass_query = f"""
    [out:json][timeout:25];
    (
      node["amenity"="hospital"](around:{radius},{lat},{lon});
      node["amenity"="clinic"](around:{radius},{lat},{lon});
      node["healthcare"="doctor"](around:{radius},{lat},{lon});
    );
    out body;
    >;
    out skel qt;
    """
    
    try:
        response = requests.post(overpass_url, data=overpass_query)
        data = response.json()
        return data.get('elements', [])
    except Exception as e:
        st.error(f"Error fetching healthcare providers: {str(e)}")
        return []

def find_healthcare_providers():
    st.title("🏥 Find Nearby Healthcare Providers")
    
    # Initialize session state for location
    if 'location' not in st.session_state:
        st.session_state.location = None
    
    # Location input
    st.write("### 📍 Your Location")
    location_method = st.radio(
        "How would you like to provide your location?",
        ["Enter Address", "Use Sample Location (New York)"]
    )
    
    if location_method == "Enter Address":
        address = st.text_input("Enter your address, city, or ZIP code:")
        if address:
            try:
                # Use Nominatim for geocoding (free)
                geolocator = Nominatim(user_agent="my_disease_app")
                location = geolocator.geocode(address)
                if location:
                    st.session_state.location = {
                        'lat': location.latitude,
                        'lng': location.longitude,
                        'address': location.address
                    }
                    st.success(f"📍 Location found: {location.address}")
                else:
                    st.error("Location not found. Please try a different address.")
            except Exception as e:
                st.error(f"Error finding location: {str(e)}")
    else:
        # Use sample location (New York)
        st.session_state.location = {
            'lat': 40.7128,
            'lng': -74.0060,
            'address': "New York, NY"
        }
        st.success("📍 Using sample location: New York, NY")
    
    # If we have a location, search for healthcare providers
    if st.session_state.location:
        with st.spinner("🔍 Searching for healthcare providers..."):
            # Add a small delay to avoid overwhelming the free API
            time.sleep(1)
            providers = get_nearby_healthcare(
                st.session_state.location['lat'],
                st.session_state.location['lng']
            )
            
            if providers:
                # Create map centered on user location
                m = folium.Map(
                    location=[st.session_state.location['lat'], 
                             st.session_state.location['lng']],
                    zoom_start=13
                )
                
                # Add user location marker
                folium.Marker(
                    [st.session_state.location['lat'], 
                     st.session_state.location['lng']],
                    popup='Your Location',
                    icon=folium.Icon(color='red', icon='info-sign')
                ).add_to(m)
                
                # Add healthcare provider markers
                for provider in providers:
                    if 'lat' in provider and 'lon' in provider:
                        # Calculate distance
                        provider_coords = (provider['lat'], provider['lon'])
                        user_coords = (st.session_state.location['lat'], 
                                     st.session_state.location['lng'])
                        distance = geodesic(user_coords, provider_coords).miles
                        
                        # Create popup content
                        popup_content = f"""
                        <b>{provider.get('tags', {}).get('name', 'Healthcare Provider')}</b><br>
                        Type: {provider.get('tags', {}).get('amenity', 'healthcare')}<br>
                        Distance: {distance:.1f} miles
                        """
                        
                        folium.Marker(
                            [provider['lat'], provider['lon']],
                            popup=popup_content,
                            icon=folium.Icon(color='blue', icon='plus')
                        ).add_to(m)
                
                # Display map
                st.write("### 🗺️ Healthcare Providers Near You")
                folium_static(m)
                
                # Display list of providers
                st.write("### 📋 Provider Details")
                for provider in providers:
                    if 'lat' in provider and 'lon' in provider:
                        tags = provider.get('tags', {})
                        provider_coords = (provider['lat'], provider['lon'])
                        distance = geodesic(user_coords, provider_coords).miles
                        
                        with st.expander(
                            f"🏥 {tags.get('name', 'Healthcare Provider')} "
                            f"({distance:.1f} miles)"
                        ):
                            st.write(f"**Type:** {tags.get('amenity', 'Healthcare')}")
                            if 'phone' in tags:
                                st.write(f"**Phone:** {tags['phone']}")
                            if 'website' in tags:
                                st.write(f"**Website:** {tags['website']}")
                            st.write(
                                f"**Coordinates:** {provider['lat']}, {provider['lon']}"
                            )
                
            else:
                st.warning(
                    "No healthcare providers found in your area. "
                    "Try a different location or increase the search radius."
                )
    
    # Add disclaimer
    st.markdown("""
    ---
    **Disclaimer:** 
    - This feature uses OpenStreetMap data, which may not include all healthcare providers.
    - Always verify provider information independently.
    - Consult with qualified healthcare professionals for medical advice.
    """)

if __name__ == "__main__":
    st.set_page_config(
        page_title="Healthcare Provider Finder",
        page_icon="🏥",
        layout="wide"
    )
    find_healthcare_providers()