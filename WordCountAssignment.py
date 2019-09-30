

def main(sample_word, punctuation_list):

    for punctuation in punctuation_list:
        if punctuation in sample_word:
            sample_word = sample_word.replace(punctuation, '')
            # print(f"{sample_word}")

    split_words = sample_word.lower().split()
    clean_words = []

    # print(f"new split words: {split_words}")

    for key, value in enumerate(split_words):
        if value.isalpha() is True:
            clean_words.append(value)

    print(f"Clean words:{clean_words}")

    words_dictionary = {}
    for item in split_words:
        if item in words_dictionary:
            words_dictionary[item][0] += 1
        else:
            words_dictionary[item] = [1]

    print(f"Words in dictionary count: {words_dictionary}")


punctuation_mark_lists = ['.', '?', '!']
sample_word_frequency = "Hello. How are you? Please say hello if you don’t love me!"
main(sample_word_frequency, punctuation_mark_lists)
