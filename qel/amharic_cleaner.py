import re
from utils import RULES, apply_rules

def clean_amharic_text(text, remove_non_amharic=True):
    """
    Cleans Amharic Text
    
    :param text: The text to be cleaned
    :param remove_non_amharic: Whether to remove all non-amharic characters from the text
    
    :returns: The cleaned text
    """
    
    text = apply_rules(text, RULES)
    if remove_non_amharic: text = ' '.join(re.compile('[ሀ-፼ ]+').findall(text))
    return text