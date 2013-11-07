def reverse_string(text):
    new_text = ''
    for letter in reversed(xrange(len(text))):
        new_text = new_text + text[letter]
    return new_text


print reverse_string('I will be reversed!!')