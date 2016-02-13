#!/usr/bin/env python

def normalize(s):
    import unicodedata
    return unicodedata.normalize('NFKC', s).lower()

def extract_text_feature(text):
    touten  = text.count('、')
    kutouten = text.count('。')
    n = len(text)
    
    return {
        'touten': touten,
        'kuten':  kutouten,
        'length': n
    }


if __name__ == '__main__':
    import sys
    
    filename = sys.argv[1]

    with open(filename) as f:
        result = extract_text_feature(f.read())
        print(result)


    text = '今日は、2/14 である。'
    result = extract_text_feature(text)
    print(result)
    print(len(text))
        


        

