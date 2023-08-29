from count_sentences import MyString

class TestMyString:
    def test_is_class(self):
        '''is a class with the name "MyString".'''
        string = MyString("This is a test.")
        assert isinstance(string, MyString)

    def test_is_sentence(self):
        '''returns True if the value ends in a period and False if it does not.'''
        string = MyString("This is a sentence.")
        assert string.is_sentence() is True
        string.value = "This is not a sentence"
        assert string.is_sentence() is False

    def test_is_question(self):
        '''returns True if the value ends with a question mark and False if it does not.'''
        string = MyString("Is this a question?")
        assert string.is_question() is True
        string.value = "This is not a question"
        assert string.is_question() is False

    def test_is_exclamation(self):
        '''returns True if the value ends with an exclamation mark and False if it does not.'''
        string = MyString("Wow, what a great day!")
        assert string.is_exclamation() is True
        string.value = "This is not an exclamation"
        assert string.is_exclamation() is False

    def test_count_sentences(self):
        '''returns the count of sentences in the value.'''
        string = MyString("This is a sentence. This is another sentence. And one more.")
        assert string.count_sentences() == 3
        string.value = "No sentences here"
        assert string.count_sentences() == 0
