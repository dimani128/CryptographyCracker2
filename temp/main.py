
import os
from ceaser import decryptCaesarCipher
from score import Score
from logger import Logger

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def maxd(dictionary):
    if not dictionary:
        return None

    largest_pair = None

    for key, value in dictionary.items():
        if largest_pair is None or value > largest_pair[1]:
            largest_pair = (key, value)

    return largest_pair

def location(path):
    return os.path.join(__location__, path)

logger = Logger(location('latest.log'))

score = Score(location('english_quadgrams.txt'))
logger.log('Score object opened')

with open(location('test.txt')) as f:
    text = f.read()

logger.log(f'Test file readn\n\t{text}')

scores = {}
for i in range(26):
    logger.log(f'Calculating score: Ceaser, i={i}.')
    txt = decryptCaesarCipher(text, i)
    scores[txt] = score.score(txt)

logger.log('Done calculating ceaser score.')

mx = maxd(scores)
print(f'Cipher: Ceaser, Score: {mx[1]}, Text:\n-----\n{mx[0]}\n-----')
logger.log(f'Cipher: Ceaser, Score: {mx[1]}, Text:\n-----\n{mx[0]}\n-----')