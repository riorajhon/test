from validator.module import calculate_phonetic_similarity, calculate_orthographic_similarity

def array_simple_similarity_score(original_name, array):
    """
    Calculate phonetic and orthographic similarity scores for each variation against original_name.
    
    Args:
        original_name: The original name to compare against
        array: List of variations to compare
        
    Returns:
        List of tuples containing (phonetic_score, orthographic_score) for each variation
    """
    results = []
    
    for variation in array:
        phonetic_score = calculate_phonetic_similarity(original_name.lower(), variation.lower())
        orthographic_score = calculate_orthographic_similarity(original_name.lower(), variation.lower())
        
        results.append((phonetic_score, orthographic_score))
    
    return results


if __name__ == "__main__":
    # Example usage
    original = "Isabella"
    variations = [
        "Isabell", 
        "Isabelle",
        "Isabel",
        "Ysabela",
        "Ysabel",
        "Izabella",
        "Elisabeta",
        "Lysabele",
        "Isbel",
        "Ishbel",
        "Bella",
        "Bellisa",
        "Elsiebelle",
        "Elisabetha",
        "Ysaybel",
        "Elizabella",
        "Elisabella",
        "Lysa",
        "Eliza",
        "Elisabetta",
        "Elisabet",
        "Esbella",
        "Esabletta",
        "Ezabell",
    ]
    
    scores = array_simple_similarity_score(original, variations)
    
    # for i, (phonetic, orthographic) in enumerate(scores):
    #     print(f"{variations[i]}:    {phonetic:.4f}, {orthographic:.4f}")
