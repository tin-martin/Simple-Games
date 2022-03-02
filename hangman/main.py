import random
import time

z = True

def blanks_func():
  blacklist = []
  words = ['able', 'about', 'account', 'acid', 'across', 'act', 'addition', 'adjustment', 'advertisement', 'after', 'again', 'against', 'agreement', 'air', 'all', 'almost', 'among', 'amount', 'amusement', 'and', 'angle', 'angry', 'animal', 'answer', 'ant', 'any', 'apparatus', 'apple', 'approval', 'arch', 'argument', 'arm', 'army', 'art', 'as', 'at', 'attack', 'attempt', 'attention', 'attraction', 'authority', 'automatic', 'awake', 'baby', 'back', 'bad', 'bag', 'balance', 'ball', 'band', 'base', 'basin', 'basket', 'bath', 'be', 'beautiful', 'because', 'bed', 'bee', 'before', 'behaviour', 'belief', 'bell', 'bent', 'berry', 'between', 'bird', 'birth', 'bit', 'bite', 'bitter', 'black', 'blade', 'blood', 'blow', 'blue', 'board', 'boat', 'body', 'boiling', 'bone', 'book', 'boot', 'bottle', 'box', 'boy', 'brain', 'brake', 'branch', 'brass', 'bread', 'breath', 'brick', 'bridge', 'bright', 'broken', 'brother', 'brown', 'brush', 'bucket', 'building', 'bulb', 'burn', 'burst', 'business', 'but', 'butter', 'button', 'by', 'cake', 'camera', 'canvas', 'card', 'care', 'carriage', 'cart', 'cat', 'cause', 'certain', 'chain', 'chalk', 'chance', 'change', 'cheap', 'cheese', 'chemical', 'chest', 'chief', 'chin', 'church', 'circle', 'clean', 'clear', 'clock', 'cloth', 'cloud', 'coal', 'coat', 'cold', 'collar', 'colour', 'comb', 'come', 'comfort', 'committee', 'common', 'company', 'comparison', 'competition', 'complete', 'complex', 'condition', 'connection', 'conscious', 'control', 'cook', 'copper', 'copy', 'cord', 'cork', 'cotton', 'cough', 'country', 'cover', 'cow', 'crack', 'credit', 'crime', 'cruel', 'crush', 'cry', 'cup', 'cup', 'current', 'curtain', 'curve', 'cushion', 'damage', 'danger', 'dark', 'daughter', 'day', 'dead', 'dear', 'death', 'debt', 'decision', 'deep', 'degree', 'delicate', 'dependent', 'design', 'desire', 'destruction', 'detail', 'development', 'different', 'digestion', 'direction', 'dirty', 'discovery', 'discussion', 'disease', 'disgust', 'distance', 'distribution', 'division', 'do', 'dog', 'door', 'doubt', 'down', 'drain', 'drawer', 'dress', 'drink', 'driving', 'drop', 'dry', 'dust', 'ear', 'early', 'earth', 'east', 'edge', 'education', 'effect', 'egg', 'elastic', 'electric', 'end', 'engine', 'enough', 'equal', 'error', 'even', 'event', 'ever', 'every', 'example', 'exchange', 'existence', 'expansion', 'experience', 'expert', 'eye', 'face', 'fact', 'fall', 'false', 'family', 'far', 'farm', 'fat', 'father', 'fear', 'feather', 'feeble', 'feeling', 'female', 'fertile', 'fiction', 'field', 'fight', 'finger', 'fire', 'first', 'fish', 'fixed', 'flag', 'flame', 'flat', 'flight', 'floor', 'flower', 'fly', 'fold', 'food', 'foolish', 'foot', 'for', 'force', 'fork', 'form', 'forward', 'fowl', 'frame', 'free', 'frequent', 'friend', 'from', 'front', 'fruit', 'full', 'future', 'garden', 'general', 'get', 'girl', 'give', 'glass', 'glove', 'go', 'goat', 'gold', 'good', 'government', 'grain', 'grass', 'great', 'green', 'grey', 'grip', 'group', 'growth', 'guide', 'gun', 'hair', 'hammer', 'hand', 'hanging', 'happy', 'harbour', 'hard', 'harmony', 'hat', 'hate', 'have', 'he', 'head', 'healthy', 'hear', 'hearing', 'heart', 'heat', 'help', 'high', 'history', 'hole', 'hollow', 'hook', 'hope', 'horn', 'horse', 'hospital', 'hour', 'house', 'how', 'humour', 'I', 'ice', 'idea', 'if', 'ill', 'important', 'impulse', 'in', 'increase', 'industry', 'ink', 'insect', 'instrument', 'insurance', 'interest', 'invention', 'iron', 'island', 'jelly', 'jewel', 'join', 'journey', 'judge', 'jump', 'keep', 'kettle', 'key', 'kick', 'kind', 'kiss', 'knee', 'knife', 'knot', 'knowledge', 'land', 'language', 'last', 'late', 'laugh', 'law', 'lead', 'leaf', 'learning', 'leather', 'left', 'leg', 'let', 'letter', 'level', 'library', 'lift', 'light', 'like', 'limit', 'line', 'linen', 'lip', 'liquid', 'list', 'little', 'living', 'lock', 'long', 'look', 'loose', 'loss', 'loud', 'love', 'low', 'machine', 'make', 'male', 'man', 'manager', 'map', 'mark', 'market', 'married', 'mass', 'match', 'material', 'may', 'meal', 'measure', 'meat', 'medical', 'meeting', 'memory', 'metal', 'middle', 'military', 'milk', 'mind', 'mine', 'minute', 'mist', 'mixed', 'money', 'monkey', 'month', 'moon', 'morning', 'mother', 'motion', 'mountain', 'mouth', 'move', 'much', 'muscle', 'music', 'nail', 'name', 'narrow', 'nation', 'natural', 'near', 'necessary', 'neck', 'need', 'needle', 'nerve', 'net', 'new', 'news', 'night', 'no', 'noise', 'normal', 'north', 'nose', 'not', 'note', 'now', 'number', 'nut', 'observation', 'of', 'off', 'offer', 'office', 'oil', 'old', 'on', 'only', 'open', 'operation', 'opinion', 'opposite', 'or', 'orange', 'order', 'organization', 'ornament', 'other', 'out', 'oven', 'over', 'owner', 'page', 'pain', 'paint', 'paper', 'parallel', 'parcel', 'part', 'past', 'paste', 'payment', 'peace', 'pen', 'pencil', 'person', 'physical', 'picture', 'pig', 'pin', 'pipe', 'place', 'plane', 'plant', 'plate', 'play', 'please', 'pleasure', 'plough', 'pocket', 'point', 'poison', 'polish', 'political', 'poor', 'porter', 'position', 'possible', 'pot', 'potato', 'powder', 'power', 'present', 'price', 'print', 'prison', 'private', 'probable', 'process', 'produce', 'profit', 'property', 'prose', 'protest', 'public', 'pull', 'pump', 'punishment', 'purpose', 'push', 'put', 'quality', 'question', 'quick', 'quiet', 'quite', 'rail', 'rain', 'range', 'rat', 'rate', 'ray', 'reaction', 'reading', 'ready', 'reason', 'receipt', 'record', 'red', 'regret', 'regular', 'relation', 'religion', 'representative', 'request', 'respect', 'responsible', 'rest', 'reward', 'rhythm', 'rice', 'right', 'ring', 'river', 'road', 'rod', 'roll', 'roof', 'room', 'root', 'rough', 'round', 'rub', 'rule', 'run', 'sad', 'safe', 'sail', 'salt', 'same', 'sand', 'say', 'scale', 'school', 'science', 'scissors', 'screw', 'sea', 'seat', 'second', 'secret', 'secretary', 'see', 'seed', 'seem', 'selection', 'self', 'send', 'sense', 'separate', 'serious', 'servant', 'sex', 'shade', 'shake', 'shame', 'sharp', 'sheep', 'shelf', 'ship', 'shirt', 'shock', 'shoe', 'short', 'shut', 'side', 'sign', 'silk', 'silver', 'simple', 'sister', 'size', 'skin', '', 'skirt', 'sky', 'sleep', 'slip', 'slope', 'slow', 'small', 'smash', 'smell', 'smile', 'smoke', 'smooth', 'snake', 'sneeze', 'snow', 'so', 'soap', 'society', 'sock', 'soft', 'solid', 'some', '', 'son', 'song', 'sort', 'sound', 'soup', 'south', 'space', 'spade', 'special', 'sponge', 'spoon', 'spring', 'square', 'stage', 'stamp', 'star', 'start', 'statement', 'station', 'steam', 'steel', 'stem', 'step', 'stick', 'sticky', 'stiff', 'still', 'stitch', 'stocking', 'stomach', 'stone', 'stop', 'store', 'story', 'straight', 'strange', 'street', 'stretch', 'strong', 'structure', 'substance', 'such', 'sudden', 'sugar', 'suggestion', 'summer', 'sun', 'support', 'surprise', 'sweet', 'swim', 'system', 'table', 'tail', 'take', 'talk', 'tall', 'taste', 'tax', 'teaching', 'tendency', 'test', 'than', 'that', 'the', 'then', 'theory', 'there', 'thick', 'thin', 'thing', 'this', 'thought', 'thread', 'throat', 'through', 'through', 'thumb', 'thunder', 'ticket', 'tight', 'till', 'time', 'tin', 'tired', 'to', 'toe', 'together', 'tomorrow', 'tongue', 'tooth', 'top', 'touch', 'town', 'trade', 'train', 'transport', 'tray', 'tree', 'trick', 'trouble', 'trousers', 'true', 'turn', 'twist', 'umbrella', 'under', 'unit', 'up', 'use', 'value', 'verse', 'very', 'vessel', 'view', 'violent', 'voice', 'waiting', 'walk', 'wall', 'war', 'warm', 'wash', 'waste', 'watch', 'water', 'wave', 'wax', 'way', 'weather', 'week', 'weight', 'well', 'west', 'wet', 'wheel', 'when', 'where', 'while', 'whip', 'whistle', 'white', 'who', 'why', 'wide', 'will', 'wind', 'window', 'wine', 'wing', 'winter', 'wire', 'wise', 'with', 'woman', 'wood', 'wool', 'word', 'work', 'worm', 'wound', 'writing', 'wrong', 'year', 'yellow', 'yes', 'yesterday', 'you', 'young']
  Hangman = ["","D","D-","D--","D---","D----","D----o","D----o-","D----o-|","D----o-|-","D----o-|-<"]
  Hangman.reverse()
  blanks = []
  lives = 10
  print("")
  print("Lives: " + str(lives))
  newWord = words[random.randint(0,(len(words)-1))]
  x = len(newWord)
  for i in range(x):
    blanks.append("_")
  print(*blanks)
  input1 = "placehld"
  while True:    
    while True:
      input2 = input("type a letter to guess: ")
      if len(input2) != 1:
        print("invalid")
      else:
        break 
    if input2 in newWord:
      if input2 in blacklist:
        print("u already entered this answer.")
      else:
        print("correct")
        print("Lives: " + str(lives))
        print("Hangman status: " + str(Hangman[lives]))
        x = 0              
      while x < len(newWord):
        if input2 == newWord[x]:
          blanks.pop(x)
          blanks.insert(x,input2)
        x += 1
      print(*blanks)
      print("_____________________________________________________")
      print("")
    else:
      if input2 in blacklist:
        print("u already entered this answer.")
      else:
        print("incorrect")
        lives -= 1
        print("Lives: " + str(lives))
      print(*blanks)
      print("Hangman status: " + str(Hangman[lives]))
      print("_____________________________________________________")
      print("")
    if "_" not in blanks:
      print("you win lol")
      break
    if lives == 0:
      print("game over")
      print("The word was: " + newWord)
      print("x_x")
      print("")
      break
    blacklist.append(input2)
    
#--------------------------------------------------------------------------------------------------------------------------------------------
def custom_func():
  blacklist = []
  blanks = []
  Hangman = ["","D","D-","D--","D---","D----","D----o","D----o-","D----o-|","D----o-|-","D----o-|-<"] 
  Hangman.reverse()
  words = []
  z = True

  while z:
    word = input("Type one word you would like to add: ")
    words.append(word)
    q = True
    while q:
      question1 = input("Would you like to input another word? <Yes/No>: ")
      if "yes"  in question1:
        z = True
        q = False
      elif "Yes" in question1:
        z = True
        q = False
      elif "No" in question1:
        z = False
        q = False
      elif "no" in question1:
        z = False
        q = False
      else:
        print("Invalid")


      


    

  lives = 10
  print("")
  print("Lives: " + str(lives))
  newWord = words[random.randint(0,(len(words)-1))]
  x = len(newWord)
  for i in range(x):
    blanks.append("_")
  print(*blanks)
  input1 = "placehld"

  while True:    
    while True:
      input2 = input("type a letter to guess: ")
      if len(input2) != 1:
        print("invalid")
      else:
        break
    if input2 in newWord:
      if input2 in blacklist:
        print("u already entered this answer.")
      else:
        print("Correct")
        print("Lives: " + str(lives))
        print("Hangman status: " + str(Hangman[lives]))
      x = 0              
      while x < len(newWord):
        if input2 == newWord[x]:
          blanks.pop(x)
          blanks.insert(x,input2)
        x += 1
      print(*blanks)
      print("_____________________________________________________")
      print("")
    else:
      if input2 in blacklist:
        print("u already entered this answer.")
        print(*blanks)
      else:
        print("Incorrect")
        lives -= 1
        print("Lives: " + str(lives))
        print(*blanks)
        print("Hangman status: " + str(Hangman[lives]))
      print("_____________________________________________________")
      print("")
    if "_" not in blanks:
      print("gameover. you win lol")
      break
    if lives == 0:
      print("game over")
      print("The word was: " + newWord)
      print("x_x")
      print("")
      break
    blacklist.append(input2)
  
      

h = ""
a = ""
n = ""
g = ""
m = ""
ab = ""
nb = ""
def printHangman():
  print(h+a+n+g+m+ab+nb)

h = "H"
printHangman()
time.sleep(0.1)
a = "A"    
printHangman()
time.sleep(0.1) 
n = "N"     
printHangman()
time.sleep(0.1)
g = "G"      
printHangman()
time.sleep(0.1) 
m = "M"     
printHangman()
time.sleep(0.1)  
ab = "A"    
printHangman()
time.sleep(0.1)  
nb = "N"    
time.sleep(0.1)
printHangman()
time.sleep(0.1)
print("")
print("""BY: MERTIN      """)
time.sleep(0.3)
print("")
print("")


while True:  
  finalInput = input(
  """Type 1: Start game with randomized words
Type 2: Create game with selected words
  """)
  if str(1) in finalInput: 
    blanks_func()
  else:
    if str(2) in finalInput:
      custom_func()
    else:
      print(" ")
      print("Invalid")
      print(""" """)


