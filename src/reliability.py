def calculate_confidence(score, max_score=7):
    """
    Converts raw score into a confidence level
    """
    if score >= max_score * 0.8:
        return "High"
    elif score >= max_score * 0.5:
        return "Medium"
    else:
        return "Low"


def evaluate_match(song, user_profile):
    """
    Simple check: does song match key preferences
    """
    matches = 0

    if song["genre"] == user_profile["genre"]:
        matches += 1

    if song["mood"] == user_profile["mood"]:
        matches += 1

    if abs(song["energy"] - user_profile["energy"]) <= 0.2:
        matches += 1

    return matches