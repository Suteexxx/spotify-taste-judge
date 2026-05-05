def calculate_score(features):
    score = (
        features["diversity"] * 5
        + (100 - features["mainstream_score"]) * 0.3
        + (1 - features["repetition"]) * 50
    )

    return min(100, round(score, 2))