from urllib.request import urlopen


def fetch_words(): 
    '''Fetchs the list of words form the url attached, decodes bytes to strings and returns a list of words'''
    story = urlopen('https://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split() #decode - from bytes to strings
        for word in line_words:
            story_words.append(word)
        return story_words #returns a list of the story words

def print_words(story_words):
    for word in story_words:
        print(word)        

def main():
    words = fetch_words()
    print(words)

if __name__ == '__main__': #detects if the module is run as script or imported as a module
    main()
