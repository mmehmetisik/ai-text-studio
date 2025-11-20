"""
AI Text Generation Studio
Generates different types of text content using Groq API
"""

import streamlit as st  # Import Streamlit library
from utils.api_handler import generate_text  # Import text generation function
from config.settings import CONTENT_TYPES, TONE_OPTIONS, LENGTH_OPTIONS  # Import settings
from utils.text_processor import count_words  # Import word counting function


def load_css():
    """Loads CSS file and applies it to Streamlit"""
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Initialize session state - runs when app first opens
# If there's no list named history in session_state, create one
# This list will store all generated texts
if 'history' not in st.session_state:
    st.session_state.history = []  # Start with empty list

# Page configuration - this should always be at the top
st.set_page_config(
    page_title="AI Text Generation Studio",  # Title shown in browser tab
    page_icon="✍️",  # Tab icon
    layout="wide"  # Page width should be wide
)

# Load CSS file
load_css()

# Main title - appears large and bold
st.title("✍️ AI Text Generation Studio")

# Subtitle - for description
st.markdown("Create professional text content using Groq AI")

# Horizontal line - for visual separation
st.divider()

# Get topic input from user
# text_area creates multi-line text box
user_prompt = st.text_area(
    label="What topic would you like to generate text about?",
    placeholder="Example: Write a blog post about artificial intelligence...",
    height=100
)

# Selectbox creates dropdown menu
# User selects text type
content_type = st.selectbox(
    label="Select Content Type",
    options=list(CONTENT_TYPES.keys())  # Convert dictionary keys to list
)

# Show description of selected type
st.info(f"📝 {CONTENT_TYPES[content_type]}")

# Tone selection with radio buttons
# horizontal=True arranges buttons horizontally
tone = st.radio(
    label="Select Tone",
    options=list(TONE_OPTIONS.keys()),
    horizontal=True
)

# Show description of selected tone
st.caption(f"💬 {TONE_OPTIONS[tone]}")

# Length selection with select slider
length_choice = st.select_slider(
    label="Text Length",
    options=list(LENGTH_OPTIONS.keys())
)

# Show word range of selected length
min_words, max_words = LENGTH_OPTIONS[length_choice]  # Get values from tuple
st.caption(f"📏 Approximately {min_words}-{max_words} words")

# How many versions to generate?
# number_input is used for number entry
# min_value and max_value set minimum and maximum values
# value is the default value
num_versions = st.number_input(
    label="How many different versions to generate?",
    min_value=1,
    max_value=3,
    value=1,
    help="Increase to see different variations on the same topic"
)

# Add spacing
st.write("")

# Create button
# primary type makes button blue and highlighted
generate_button = st.button(
    label="🚀 Generate Text",
    type="primary",
    use_container_width=True  # Button should span page width
)

# Control what happens when button is clicked
if generate_button:
    # Check if user entered text
    if not user_prompt:
        st.warning("⚠️ Please enter a topic!")  # Yellow warning message
    else:
        # Show success message
        st.success(f"✅ Generating {num_versions} different version(s)...")

        # If multiple versions requested, create columns
        # Columns create side-by-side boxes, each version appears in its own column
        if num_versions > 1:
            # columns function determines how many columns we want
            # Creates num_versions columns, so 2 versions = 2 columns
            cols = st.columns(num_versions)

        # Start loop for each version
        # range(num_versions) generates numbers from 0 to num_versions
        # For example if num_versions=3, i values will be 0, 1, 2
        for i in range(num_versions):
            # Generate each version separately
            # Loading indicator shows user which version is being generated
            with st.spinner(f"✨ Generating version {i + 1}..."):
                # Call API and generate text
                # A new API call is made in each loop
                # Each version will be slightly different due to temperature
                generated_text = generate_text(
                    user_prompt,  # Topic entered by user
                    CONTENT_TYPES[content_type],  # Description of selected type
                    TONE_OPTIONS[tone],  # Description of selected tone
                    LENGTH_OPTIONS[length_choice]  # Min-max values of selected length
                )

            # If multiple versions, show each version in its own column
            # If single version, show in normal flow
            if num_versions > 1:
                # cols[i] selects the i-th column
                # Everything inside with block appears in that column
                with cols[i]:
                    # Add generated text to history
                    # Save each text as dictionary so we know what settings were used
                    st.session_state.history.append({
                        'prompt': user_prompt,  # Topic written by user
                        'content_type': content_type,  # Text type
                        'tone': tone,  # Tone
                        'length': length_choice,  # Length
                        'text': generated_text,  # Generated text
                        'version': i + 1  # Which version
                    })

                    # Version heading, shows which version it is
                    st.markdown(f"#### 📄 Version {i + 1}")
                    # Show generated text
                    st.write(generated_text)

                    # Calculate and show word count
                    word_count = count_words(generated_text)
                    st.metric(
                        label="📊 Word Count",
                        value=f"{word_count} words",
                        delta=f"Target: {min_words}-{max_words}"
                    )

                    # Separate download button for each version
                    # Version number added to filename to avoid confusion
                    st.download_button(
                        label="💾 Download",
                        data=generated_text,
                        file_name=f"{content_type.replace(' ', '_')}_v{i + 1}.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
            else:
                # Add to history for single version
                st.session_state.history.append({
                    'prompt': user_prompt,
                    'content_type': content_type,
                    'tone': tone,
                    'length': length_choice,
                    'text': generated_text,
                    'version': 1  # Single version
                })

                # For single version, show in old layout
                st.markdown("### 📝 Generated Text:")
                st.write(generated_text)

                # Calculate and show word count
                word_count = count_words(generated_text)
                st.metric(
                    label="📊 Word Count",
                    value=f"{word_count} words",
                    delta=f"Target: {min_words}-{max_words}"
                )

                # Download button
                st.download_button(
                    label="💾 Download Text (TXT)",
                    data=generated_text,
                    file_name=f"{content_type.replace(' ', '_')}_text.txt",
                    mime="text/plain",
                    use_container_width=True
                )

# ============================================================================
# SIDEBAR - TEXT HISTORY PANEL
# ============================================================================

# Sidebar title and description
# sidebar creates panel that opens on left side
st.sidebar.title("📚 Text History")
st.sidebar.markdown("All your generated texts are stored here")

# If there are no texts in history, show informative message
# len function gives list length, 0 means list is empty
if len(st.session_state.history) == 0:
    st.sidebar.info("You haven't generated any texts yet. Generated texts will appear here.")
else:
    # Show how many texts are in history
    # This shows user how much content they've generated
    st.sidebar.success(f"Total {len(st.session_state.history)} text(s) generated")

    # Add clear button
    # This button is for clearing all history
    if st.sidebar.button("🗑️ Clear History", use_container_width=True):
        # Empty history list
        # clear function deletes all elements from list
        st.session_state.history.clear()
        # Refresh page so change is immediately visible
        # rerun function reloads the page
        st.rerun()

    st.sidebar.divider()  # Add horizontal line for visual separation

    # Create card for each text in history
    # enumerate function provides both index and element
    # reversed reverses history so most recently generated appears at top
    for idx, item in enumerate(reversed(st.session_state.history)):
        # Show each text in an expander
        # expander creates clickable, expandable/collapsible boxes
        # Show first 30 characters of prompt in title so user knows what it is
        with st.sidebar.expander(
            f"📄 {item['prompt'][:30]}..." if len(item['prompt']) > 30 else f"📄 {item['prompt']}",
            expanded=False  # Initially closed, opens when user clicks
        ):
            # Show text information
            # caption creates small gray text, ideal for metadata
            st.caption(f"**Type:** {item['content_type']}")
            st.caption(f"**Tone:** {item['tone']}")
            st.caption(f"**Length:** {item['length']}")
            st.caption(f"**Version:** {item['version']}")

            # Small spacing
            st.write("")

            # Show text but in truncated form
            # Showing long texts scrolls sidebar too much, first 150 characters sufficient
            preview = item['text'][:150] + "..." if len(item['text']) > 150 else item['text']
            st.text_area(
                label="Text Preview",
                value=preview,
                height=100,
                disabled=True,  # disabled=True makes text non-editable, read-only
                key=f"preview_{idx}"  # Each text_area must have unique key
            )

            # View full text button
            # When user clicks, full text will appear on main page
            if st.button(f"👁️ View Full Text", key=f"view_{idx}", use_container_width=True):
                # Create variable named selected_text in session_state
                # This variable holds which text to display
                st.session_state.selected_text = item
                st.rerun()  # Refresh page so it appears on main page

            # Download button
            # Provide download option for each history text too
            st.download_button(
                label="💾 Download",
                data=item['text'],
                file_name=f"{item['content_type'].replace(' ', '_')}_v{item['version']}.txt",
                mime="text/plain",
                key=f"download_{idx}",  # Each button must have unique key
                use_container_width=True
            )

# ============================================================================
# SHOW SELECTED TEXT ON MAIN PAGE
# ============================================================================

# If user selected text from history, show it on main page
# If selected_text exists in session_state, means user wants to view a text
if 'selected_text' in st.session_state:
    # Show selected text on main page
    st.divider()  # Line for visual separation
    st.subheader("📖 Selected Text")

    # Show text information
    # Create three columns, information appears side by side
    col1, col2, col3 = st.columns(3)
    with col1:
        st.caption(f"**Type:** {st.session_state.selected_text['content_type']}")
    with col2:
        st.caption(f"**Tone:** {st.session_state.selected_text['tone']}")
    with col3:
        st.caption(f"**Length:** {st.session_state.selected_text['length']}")

    # Show full text
    st.write(st.session_state.selected_text['text'])

    # Word count
    word_count = count_words(st.session_state.selected_text['text'])
    st.metric(label="📊 Word Count", value=f"{word_count} words")

    # Download button
    st.download_button(
        label="💾 Download This Text",
        data=st.session_state.selected_text['text'],
        file_name=f"{st.session_state.selected_text['content_type'].replace(' ', '_')}_selected.txt",
        mime="text/plain",
        use_container_width=True
    )

    # Close button
    # User saw text, may want to close it
    if st.button("❌ Close", type="secondary"):
        # Delete selected_text variable from session_state
        # del command completely removes a variable
        del st.session_state.selected_text
        st.rerun()  # Refresh page