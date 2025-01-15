def classify_sentence(sentence):
    sentence = sentence.lower()
    computer_keywords = ['input', 'device', 'click', 'computer', 'screen']
    animal_keywords = ['tail', 'fur', 'animal', 'scurry', 'rodent']
    
    computer_score = sum(word in sentence for word in computer_keywords)
    animal_score = sum(word in sentence for word in animal_keywords)
    
    return "computer-mouse" if computer_score >= animal_score else "animal"

def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')
    
    n = int(data[0].strip())
    sentences = [data[i].strip() for i in range(1, n + 1)]
    
    results = []
    for sentence in sentences:
        if sentence:
            classification = classify_sentence(sentence)
            results.append(classification)
    
    for result in results:
        print(result)

if __name__ == '__main__':
    main()
