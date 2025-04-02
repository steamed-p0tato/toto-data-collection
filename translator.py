import streamlit as st
import pandas as pd
import json
import streamlit.components.v1 as components
from datetime import datetime
import os

def main():
    st.set_page_config(page_title="Toto Input Tool", layout="wide")
    
    st.title("Toto data collection toolkit")
    st.markdown("Create Toto language entries with corresponding English translations")
    st.markdown("made by Ariyan |github: steamed-p0tato")

    # Define the Toto character range and information
    toto_char_info = {
        # Basic consonants
        0x1E290: {"char": chr(0x1E290), "name": "TOTO LETTER PA", "type": "consonant"},
        0x1E291: {"char": chr(0x1E291), "name": "TOTO LETTER BA", "type": "consonant"},
        0x1E292: {"char": chr(0x1E292), "name": "TOTO LETTER TA", "type": "consonant"},
        0x1E293: {"char": chr(0x1E293), "name": "TOTO LETTER DA", "type": "consonant"},
        0x1E294: {"char": chr(0x1E294), "name": "TOTO LETTER KA", "type": "consonant"},
        0x1E295: {"char": chr(0x1E295), "name": "TOTO LETTER GA", "type": "consonant"},
        0x1E296: {"char": chr(0x1E296), "name": "TOTO LETTER MA", "type": "consonant"},
        0x1E297: {"char": chr(0x1E297), "name": "TOTO LETTER NA", "type": "consonant"},
        0x1E298: {"char": chr(0x1E298), "name": "TOTO LETTER NGA", "type": "consonant"},
        0x1E299: {"char": chr(0x1E299), "name": "TOTO LETTER SA", "type": "consonant"},
        0x1E29A: {"char": chr(0x1E29A), "name": "TOTO LETTER CHA", "type": "consonant"},
        0x1E29B: {"char": chr(0x1E29B), "name": "TOTO LETTER YA", "type": "consonant"},
        0x1E29C: {"char": chr(0x1E29C), "name": "TOTO LETTER WA", "type": "consonant"},
        0x1E29D: {"char": chr(0x1E29D), "name": "TOTO LETTER JA", "type": "consonant"},
        0x1E29E: {"char": chr(0x1E29E), "name": "TOTO LETTER HA", "type": "consonant"},
        0x1E29F: {"char": chr(0x1E29F), "name": "TOTO LETTER RA", "type": "consonant"},
        0x1E2A0: {"char": chr(0x1E2A0), "name": "TOTO LETTER LA", "type": "consonant"},
        # Basic vowels
        0x1E2A1: {"char": chr(0x1E2A1), "name": "TOTO LETTER I", "type": "vowel"},
        0x1E2A2: {"char": chr(0x1E2A2), "name": "TOTO LETTER BREATHY I", "type": "vowel"},
        0x1E2A3: {"char": chr(0x1E2A3), "name": "TOTO LETTER IU", "type": "vowel"},
        0x1E2A4: {"char": chr(0x1E2A4), "name": "TOTO LETTER BREATHY IU", "type": "vowel"},
        0x1E2A5: {"char": chr(0x1E2A5), "name": "TOTO LETTER U", "type": "vowel"},
        0x1E2A6: {"char": chr(0x1E2A6), "name": "TOTO LETTER E", "type": "vowel"},
        0x1E2A7: {"char": chr(0x1E2A7), "name": "TOTO LETTER BREATHY E", "type": "vowel"},
        0x1E2A8: {"char": chr(0x1E2A8), "name": "TOTO LETTER EO", "type": "vowel"},
        0x1E2A9: {"char": chr(0x1E2A9), "name": "TOTO LETTER BREATHY EO", "type": "vowel"},
        0x1E2AA: {"char": chr(0x1E2AA), "name": "TOTO LETTER O", "type": "vowel"},
        0x1E2AB: {"char": chr(0x1E2AB), "name": "TOTO LETTER AE", "type": "vowel"},
        0x1E2AC: {"char": chr(0x1E2AC), "name": "TOTO LETTER BREATHY AE", "type": "vowel"},
        0x1E2AD: {"char": chr(0x1E2AD), "name": "TOTO LETTER A", "type": "vowel"},
        # Sign
        0x1E2AE: {"char": chr(0x1E2AE), "name": "TOTO SIGN RISING TONE", "type": "sign"},
    }
    
    # Initialize session state
    if 'entries' not in st.session_state:
        st.session_state.entries = []
    if 'current_toto' not in st.session_state:
        st.session_state.current_toto = ""
    if 'current_english' not in st.session_state:
        st.session_state.current_english = ""
    
    # Create two columns for inputs
    col1, col2 = st.columns(2)
    
    # Toto Input
    with col1:
        st.subheader("Toto")
        toto_text = st.text_area("Enter Toto text", value=st.session_state.current_toto, 
                                height=150, key="toto_input")
        st.session_state.current_toto = toto_text
    
    # English Translation Input
    with col2:
        st.subheader("English Translation")
        english_text = st.text_area("Enter English translation", value=st.session_state.current_english, 
                                height=150, key="english_input")
        st.session_state.current_english = english_text
    
    # Add entry button
    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("Add Entry", key="add_entry"):
            if st.session_state.current_toto and st.session_state.current_english:
                # Add the current entry to the list
                st.session_state.entries.append({
                    "toto": st.session_state.current_toto,
                    "english": st.session_state.current_english
                })
                # Clear the current inputs
                st.session_state.current_toto = ""
                st.session_state.current_english = ""
                st.rerun()
            else:
                st.error("Both Toto and English fields must be filled")
    
    # Create callback functions for the virtual keyboard
    if 'add_char' not in st.session_state:
        def add_char(char):
            st.session_state.current_toto += char
        st.session_state.add_char = add_char
        
    if 'backspace' not in st.session_state:
        def backspace():
            st.session_state.current_toto = st.session_state.current_toto[:-1] if st.session_state.current_toto else ""
        st.session_state.backspace = backspace
    
    # Custom JavaScript for the virtual keyboard (not used, keeping for reference)
    js_keyboard = """
    <script>
    // This JavaScript is not being used now
    // We're using Streamlit's native callbacks instead
    </script>
    """
    
    # Virtual Keyboard for Toto using Streamlit native components
    st.subheader("Toto Virtual Keyboard")
    
    # Helper function to create keyboard buttons with tooltips
    def create_keyboard_section(title, characters):
        st.markdown(f"##### {title}")
        cols = st.columns(9)  # Adjust number of columns as needed
        
        for i, (code_point, info) in enumerate(characters.items()):
            char = info["char"]
            name = info["name"]
            col_idx = i % 9
            
            with cols[col_idx]:
                st.button(
                    char, 
                    key=f"key_{code_point}",
                    help=name,
                    on_click=st.session_state.add_char,
                    args=(char,)
                )
    
    # Group characters by type
    consonants = {cp: info for cp, info in toto_char_info.items() if 0x1E290 <= cp < 0x1E2A1}
    vowels = {cp: info for cp, info in toto_char_info.items() if 0x1E2A1 <= cp < 0x1E2AE}
    signs = {cp: info for cp, info in toto_char_info.items() if cp == 0x1E2AE}
    
    # Create keyboard sections
    create_keyboard_section("Consonants", consonants)
    create_keyboard_section("Vowels", vowels)
    create_keyboard_section("Signs", signs)
    
    # Special keys (space and backspace)
    col1, col2, col3 = st.columns([1, 1, 7])
    with col1:
        st.button("Space", key="key_space", on_click=st.session_state.add_char, args=(" ",))
    with col2:
        st.button("⌫", key="key_backspace", on_click=st.session_state.backspace)
    
    # Saved entries section
    st.subheader("Saved Entries")
    if not st.session_state.entries:
        st.info("No entries added yet. Use the form above to add entries.")
    else:
        # Display entries in a table
        entries_df = pd.DataFrame(st.session_state.entries)
        st.dataframe(entries_df, use_container_width=True)
        
        # Export options
        st.subheader("Export Options")
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Generate JSON for download
            json_data = json.dumps(st.session_state.entries, indent=2, ensure_ascii=False)
            
            # Create a default filename with timestamp
            default_filename = f"toto_entries_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            filename = st.text_input("Filename", value=default_filename)
            
            if st.button("Export as JSON"):
                # Create download link
                st.download_button(
                    label="Download JSON", 
                    data=json_data,
                    file_name=filename,
                    mime="application/json"
                )
        
        with col2:
            if st.button("Clear All Entries"):
                st.session_state.entries = []
                st.rerun()
    
    # Character reference
    with st.expander("Toto Character Reference"):
        # Create a DataFrame for better display
        char_data = []
        for code_point, info in toto_char_info.items():
            char_data.append({
                "Code Point": f"U+{code_point:X}",
                "Character": info["char"],
                "Name": info["name"],
                "Type": info["type"].capitalize()
            })
        
        df = pd.DataFrame(char_data)
        st.dataframe(df, hide_index=True)

if __name__ == "__main__":
    main()
