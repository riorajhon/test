from test import array_simple_similarity_score
import requests
import re
from test import array_simple_similarity_score

def generate_variations(original_name, count=30):
    r = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "latin-name-variant",
            # "model": "phonetic-variant",
            "prompt": f"Generate {count} variations of the name {original_name}",
            # "prompt": "Input name: {original_name}\nCount: {count}",
            "stream": False
        },
        proxies={"http": None, "https": None}
    )
    
    response = r.json()["response"]
    variations = []
    for line in response.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        # Skip lines that look like explanations/notes
        if line.startswith("(") or line.startswith("Note") or ":" in line:
            continue
        # Only keep lines that look like names (letters, spaces, hyphens, apostrophes)
        if re.match(r"^[A-Za-zÀ-ÿ\s\-\']+$", line):
            variations.append(line)
    return variations


if __name__ == "__main__":
    original_name = input("Enter original name: ")
    
    print(f"\nGenerating variations for '{original_name}'...\n")
    variations = generate_variations(original_name)
    
    print("Generated variations:")
    for v in variations:
        print(f"  {v}")
    
    print("\n--- Similarity Scores ---")
    scores = array_simple_similarity_score(original_name, variations)
    
    for i, (phonetic, orthographic) in enumerate(scores):
        print(f"{original_name} vs {variations[i]}: phonetic={phonetic:.4f}, orthographic={orthographic:.4f}")

# print(array_simple_similarity_score("Isabella",r.json()["response"] ))