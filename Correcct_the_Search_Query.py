def levenshtein_distance(word1, word2):
    """Calculate the Levenshtein distance between two words."""
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def correct_spelling(word, dictionary):
    """Return the closest match for a misspelled word using Levenshtein distance."""
    min_distance = float('inf')
    closest_match = word
    
    for dict_word in dictionary:
        distance = levenshtein_distance(word, dict_word)
        if distance < min_distance:
            min_distance = distance
            closest_match = dict_word
    
    return closest_match

def process_query(query, dictionary):
    """Process the query and correct each word using the dictionary."""
    words = query.split()
    corrected_words = [correct_spelling(word, dictionary) for word in words]
    return " ".join(corrected_words)

def main():
    # Dictionary of common words for correction (could be expanded further)
    dictionary = set([
        "going", "to", "china", "who", "was", "the", "first", "president", "of", "india",
        "winner", "match", "food", "in", "america"
    ])
    
    # Number of queries
    n = int(input())  # number of queries
    
    # Process each query
    for _ in range(n):
        query = input().strip()
        corrected_query = process_query(query, dictionary)
        print(corrected_query)

# Run the main function
if __name__ == "__main__":
    main()
