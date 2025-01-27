def sentence(text):
    phrase = text.capitalize()
    interrogatives = ('how', 'why', 'when', 'where', 'whom', 'whose', 'what', 'will')

    if text.startswith(interrogatives):
        return '{}? '.format(phrase)
    else:
        return '{}. '.format(phrase)

result = []
while True:
    user_input = input('say something: ')
    if user_input == '\end':
        break
    else:
        result.append(sentence(user_input))

print(' '.join(result))