def load_words(filepath):
    with open(filepath, 'r') as file:
        return set(word.strip().lower() for word in file)

def strip_url_or_hashtag(input_str):
    input_str = input_str.lower()
    if input_str.startswith('www.'):
        input_str = input_str[4:]
    if input_str.startswith('#'):
        input_str = input_str[1:]
    
    # Strip common domain extensions
    for ext in ['.com', '.co.uk', '.org', '.net', '.ru', '.in']:
        if input_str.endswith(ext):
            input_str = input_str[:input_str.rfind('.')]
            break
    
    return input_str

def segment_string(input_str, words_set):
    n = len(input_str)
    if n == 0:
        return ""

    # Use memoization to store results of previously segmented positions
    memo = {}

    def helper(start):
        if start in memo:
            return memo[start]
        
        if start == n:
            return []
        
        for end in range(start + 1, n + 1):
            word = input_str[start:end]
            if word in words_set or word.isdigit():
                remainder = helper(end)
                if remainder is not None:
                    memo[start] = [word] + remainder
                    return memo[start]
        
        memo[start] = None
        return None

    result = helper(0)
    return ' '.join(result) if result else input_str

def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')
    
    words_file_path = 'words.txt'
    words_set = load_words(words_file_path)
    
    n = int(data[0].strip())
    results = []
    for i in range(1, n + 1):
        if data[i].strip():
            cleaned_input = strip_url_or_hashtag(data[i].strip())
            segmented_text = segment_string(cleaned_input, words_set)
            results.append(segmented_text)
    
    for result in results:
        print(result)

if __name__ == '__main__':
    main()
