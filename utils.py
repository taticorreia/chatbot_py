import re
import unicodedata

def to_lower_remove_accents(message):
    if not message:
        return ''
    
    text = re.sub('[][,\.;*!?:"-/]', ' ', message.lower())
    text = re.sub('\s+', ' ', text)

    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError):
        pass

    return str(unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8')).strip()