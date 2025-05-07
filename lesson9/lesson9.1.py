def popular_words (text: str, words: list) -> dict:
    text = text.lower().split()
    slovnik = {word: 0 for word in words}
    for word in text:
        if word in words:
            slovnik[word] += 1
    return slovnik

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')