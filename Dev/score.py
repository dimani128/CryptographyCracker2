class Score:
    def __init__(self, filename):
        self.quadgram_freq = {}
        with open(filename, 'r') as file:
            for line in file:
                quadgram, frequency = line.strip().split()
                self.quadgram_freq[quadgram] = int(frequency)

    def score(self, text):
        text = text.upper()  # Convert text to uppercase for case-insensitive matching
        score = 0
        text_length = len(text)

        for i in range(text_length - 3):
            quadgram = text[i:i+4]
            if quadgram in self.quadgram_freq:
                score += self.quadgram_freq[quadgram]

        return score

# Example usage
if __name__ == '__main__':
    import time

    quadgram_filename = 'Dev\\english_quadgrams.txt'
    text_to_score = "The quick brown fox jumps over the lazy dog."

    t1 = time.time()
    quadgram_scorer = Score(quadgram_filename)
    text_score = quadgram_scorer.score(text_to_score)
    print(time.time() - t1)
    print(f"Score for the text: {text_score}")
