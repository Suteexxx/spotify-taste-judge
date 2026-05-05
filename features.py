import pandas as pd

def compute_features(tracks, audio_features):
    df_tracks = pd.DataFrame(tracks)
    df_features = pd.DataFrame(audio_features)

    df = pd.concat([df_tracks, df_features], axis=1)

    # Basic metrics
    avg_popularity = df['popularity'].mean()
    diversity = df['artist'].nunique()
    repetition = 1 - (diversity / len(df))

    avg_energy = df['energy'].mean()
    avg_valence = df['valence'].mean()

    mainstream_score = (df['popularity'] > 70).mean() * 100

    return {
        "avg_popularity": avg_popularity,
        "diversity": diversity,
        "repetition": repetition,
        "energy": avg_energy,
        "valence": avg_valence,
        "mainstream_score": mainstream_score
    }