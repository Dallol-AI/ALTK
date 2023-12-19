import re
from utils import RULES, apply_rules


def clean_amharic_text(text):
    """
    Cleans Amharic Text

    :param text: The text to be cleaned

    :returns: The cleaned text
    """

    # Apply Rules for preprocessing
    text = apply_rules(text, RULES)
    pattern = '[ሀ-፼\d!?;."\'\(\)\[\]\s]+'
    text = ' '.join(re.compile(pattern).findall(text))
    return text
