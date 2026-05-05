def generate_roast(features):
    if features["mainstream_score"] > 80:
        return "Your playlist screams: 'I trust Spotify more than myself.' 😂"
    
    elif features["valence"] < 0.3:
        return "This playlist needs therapy, not shuffle."
    
    elif features["diversity"] < 3:
        return "Same 3 artists? Bro this is not a personality."
    
    elif features["energy"] > 0.8:
        return "This is not a playlist, it's a gym steroid injection."
    
    else:
        return "Hmm… decent taste. You're hiding something."