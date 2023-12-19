import re, string
from typing import List
from utils import apply_rules, RULES

# TODO: HANDLE COMPOUND WORDS SUCH AS ስነz

class AmharicTokenizer:
    def __init__(self, word_delimiters: set = None, sentence_delimiters: set = None):
        """
        Amharic Tokenizer for tokenization and sentence segmentation.

        Args:
        - sentence_punctuations (Set[str]): List of sentence-ending punctuations.
        - word_punctuations (Set[str]): List of word-ending punctuations.
        """
        self.word_delimiters = word_delimiters or { "[", " ", "፣", "።", ",", "፦", "!", ">", "&", "፧", "}", "^", ")", "፨", "<", "~", "]", "*", "{", "፤", "/", "፥", "(", "\\", "_", "+", ";", "#", "\"", ":", "=", " ", "%", "|", "`", "@", "'", "?", "$", }
        self.sentence_delimiters = sentence_delimiters or ["።", "፥", "፨", "::", "፡፡", "?", "!",'፧']
        self.compound_words_fix = [
            'ስነ','ቤተ', 'እግረ','ሥነ'
        ]

    def word_tokenize(self, text: str, include_punc=False, compound_words_as_one=True, clean=False):
        """
        Tokenize a text into a list of tokens.

        :param text: the text to tokenize
        :param include_punc: include punctuation in the tokens
        :param clean: apply basic cleaning rules to the text
        :return: a list of tokens
        """
        if clean: text = apply_rules(text, RULES)
        
        delimiters = self.word_delimiters
        compound_words = seld.compound_words_fix
        
        tokens = []
        curr_word = ""
        prev_word = None
        
        for char in text:
            if char not in delimiters:
                curr_word += char
            else:
                curr_word = curr_word.strip()
                if curr_word:
                    if compound_words_as_one and curr_word:
                        continue
                    tokens.append(curr_word)
                    prev_word = curr_word
                    if include_punc and char != ' ': tokens.append(char);prev_word = char;
                    curr_word = ""
                
                
        if curr_word.strip(): # if a word exists and is not whitespace
            tokens.append(curr_word.strip())
        return tokens

    def sentence_tokenize(self, text: str, clean=False):
        """
        Tokenize a text into a list of sentences.

        :param text: the text to tokenize
        :param clean: apply basic cleaning rules to the text
        :return: a list of sentences
        """
        # preprocess the text
        text = re.sub("\s+", " ", text) # replace multiple space with one
        text = re.sub("\n", "።", text) # replace newlines with sentence delimiter
        if clean: text = apply_rules(text, RULES)
                
        sentences = []
        current_sentence = ""
    
        for char in sentences:
            if char not in self.sentence_delimiters:
                current_sentence += char
            elif current_sentence.strip():
                sentences.append(current_sentence.strip())
                current_sentence = ""

        if current_sentence.strip():
            sentences.append(current_sentence.strip())
        return sentences

    @classmethod
    def __find_indexes(text, punct):
        """
        returns the index of the sentence delimiters in the text
        """
        return [i + len(punct) - 1 for i in range(len(text)) if text.startswith(punct, i)]
        