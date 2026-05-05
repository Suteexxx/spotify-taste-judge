import streamlit as st
import matplotlib.pyplot as plt

from spotify_api import get_playlist_tracks, get_audio_features
from features import compute_features
from roast import generate_roast
from score import calculate_score

# ---------------- PAGE ----------------
st.set_page_config(page_title="Spotify Judge", layout="centered")

# ---------------- TITLE ----------------
st.title("🎧 AI Spotify Taste Judge")

# ---------------- INPUT ----------------
playlist_url = st.text_input("Enter Spotify Playlist URL")

# ---------------- FUNCTION ----------------
def plot_features(features):
    labels = ['Energy', 'Valence']
    values = [features['energy'], features['valence']]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_ylim(0, 1)

    st.pyplot(fig)

# ---------------- BUTTON ----------------
analyze = st.button("Analyze Playlist")

# ---------------- MAIN LOGIC ----------------
if analyze:

    if not playlist_url:
        st.warning("Please enter a playlist URL")
    else:
        try:
            tracks = get_playlist_tracks(playlist_url)
            track_ids = [t['id'] for t in tracks if t['id']]

            audio_features = get_audio_features(track_ids)

            features = compute_features(tracks, audio_features)
            score = calculate_score(features)
            roast = generate_roast(features)

            # OUTPUT
            st.subheader(f"🔥 Taste Score: {score}/100")

            st.write("### 📊 Insights")
            st.write(features)

            plot_features(features)

            st.write("### 😈 Roast")
            st.write(roast)

        except Exception as e:
            st.error(f"Error: {e}")