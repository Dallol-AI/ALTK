from utils import read_file_line

# Stopwords Remover using custom stopword

def remove_stopwords(tokens: list, custom_stopwords: list =None):
    """
    Removes stopwords from tokens.

    :params tokens (list): The list of words from which stopwords should be removed.
    :params custom_stopwords (list, optional): The list of custom stopwords. Defaults to None which uses default stopwords list.

    :returns: The list of tokens with stopwords removed.
    """
    DEFAULT_PATH = "data/stopwords.txt"
    stopwords = set(read_file_line(DEFAULT_PATH)) if custom_stopwords is None else custom_stopwords
    
    cleaned_tokens = [token for token in tokens if token not in stopwords]
    
    return cleaned_tokens
    
