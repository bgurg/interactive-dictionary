import os, json
from difflib import get_close_matches

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_dict(fname):
    '''
    Load dictionary from provided json filename.
    Lower case all terms in dictionary.
    Return dictionary with all terms lower cased.
    '''
    dict_data = json.load(open('data.json'))

    # lower case all keys
    dict_lower_terms = {k.lower():v for (k,v) in dict_data.items()}

    print(len(dict_lower_terms.keys()), 'dictionary terms loaded \n')
    return dict_lower_terms


def get_definition(dict_data, term):
    '''
    Lower case provided term and look it up in dictionary.
    If not found, provide appropriate error.
    If found, number and combine each definition for that term as string.
    Return definition string.
    '''
    try:
        definition  = dict_data[term.lower()]
    except:
        similar_terms = get_similar_terms(dict_data, term, 3)
        if len(similar_terms) > 0:
            return term + ' was not found in dictionary' + '\nSimilar terms found: ' + similar_terms + '\n'
        return term + ' not found in dictionary.  No similar items identified.\n'

    if type(definition) == list:
        value = ''
        for i in range(len(definition)):
            value += f'({str(i+1)}) ' + definition[i] + '\n'
        return value
    else:
        return '(1) ' + definition


def get_similar_terms(dict_data, term, num_matches):
    '''
    Use difflib.get_close_matches to identify a list of similiar terms in the dictionary
    Return a comma-separated string containing similar terms
    '''
    similar_terms_lst = get_close_matches(term, dict_data.keys(), n=num_matches)
    return ','.join(similar_terms_lst)


clear()
dict_data = load_dict('data.json')

term = ''
while term != 'qq':
    term = input('Enter term ("qq" to quit): ').lower()
    if term != 'qq':
        print(get_definition(dict_data, term))
