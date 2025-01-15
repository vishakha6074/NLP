import re

def count_articles_and_dates(text):
    # Count occurrences of articles
    count_a = len(re.findall(r'\ba\b', text))
    count_an = len(re.findall(r'\ban\b', text))
    count_the = len(re.findall(r'\bthe\b', text))
    
    # Regex pattern to detect dates
    date_patterns = [
        # Matches day/month/year or day/month/yy format
        r'\b(\d{1,2})(st|nd|rd|th)?[\s/-](\d{1,2})[\s/-](\d{2,4})\b',  # Day/Month/Year
        # Matches Month day, year or Month day year (with or without "of")
        r'\b(\d{1,2})(st|nd|rd|th)?[\s]*(January|February|March|April|May|June|July|August|September|October|November|December)[a-zA-Z,]*[\s]+(\d{2,4})\b',
        # Matches "Day Month Year" format
        r'\b((January|February|March|April|May|June|July|August|September|October|November|December)[a-zA-Z,]*[\s]+(\d{1,2})(st|nd|rd|th)?[\s]+(\d{2,4}))\b',
        # Matches "Month Day, Year" format
        r'\b([a-zA-Z]+[\s]+(\d{1,2})(st|nd|rd|th)?[\s]*[\d{2,4}])\b'
    ]
    
    # Count dates using regex patterns
    date_count = 0
    for pattern in date_patterns:
        date_count += len(re.findall(pattern, text))
    
    return count_a, count_an, count_the, date_count

# Read input
T = int(input())  # Number of test cases
for _ in range(T):
    text = input().strip()
    
    # Process text fragment
    count_a, count_an, count_the, date_count = count_articles_and_dates(text)
    
    # Output the results for the current text fragment
    print(count_a)
    print(count_an)
    print(count_the)
    print(date_count)
    
    # Read the blank line (if necessary)
    if _ < T - 1:
        input()  # Skip the blank line
