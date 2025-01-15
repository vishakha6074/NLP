import re

def extract_acronyms(snippets):
    acronym_dict = {}
    
    # Regular expression to match possible acronyms in the form of (ACRONYM)
    acronym_pattern = r"\((.*?)\)"  # Matches text inside parentheses
    full_form_pattern = r"([A-Za-z ]+)\s*\((.*?)\)"  # Matches full form followed by acronym in parentheses
    
    for snippet in snippets:
        matches = re.findall(full_form_pattern, snippet)
        for full_form, acronym in matches:
            acronym_dict[acronym.upper()] = full_form.strip()
    
    return acronym_dict

# Read input
N = int(input())  # Number of snippets
snippets = [input().strip() for _ in range(N)]
test_acronyms = [input().strip() for _ in range(N)]

# Extract acronyms and their expansions from the snippets
acronym_dict = extract_acronyms(snippets)

# For each test acronym, output the corresponding expansion
for acronym in test_acronyms:
    print(acronym_dict.get(acronym.upper(), "Unknown Acronym"))
