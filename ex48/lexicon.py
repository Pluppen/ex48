def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(input):
    directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
    verbs = ['go', 'stop', 'kill', 'eat']
    stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
    nouns = ['door', 'bear', 'princess', 'cabinet']

    input_msg = input.split(" ")
    answer = []
    for word in input_msg:
        if word in directions:
            answer.append(('direction', word))
        elif word in verbs:
            answer.append(('verb', word))
        elif word in stop_words:
            answer.append(('stop', word))
        elif word in nouns:
            answer.append(('noun', word))
        elif convert_number(word) != None:
            answer.append(('number', convert_number(word)))
        else:
            answer.append(('error', word))
    return answer