import re
import json

acc = 0

def walk(node):
    def contains_red(d):
        """Return True if d contains a property with the value 'red'
        """
        for key, item in d.items():
            if isinstance(item, str):
                if item == "red": 
                    return True
        return False
        
    def search(item):
        if isinstance(item, dict) or isinstance(item, list):
                walk(item)
        # leaf
        else:
            if isinstance(item, int):
                global acc
                acc += item
                
    # handle lists
    if isinstance(node, list):
        for item in node:
            search(item)
    # handle dicts
    else:
        if not contains_red(node):
            for key, item in node.items():
                search(item)
        
def main():
    # a way to solve part 1 without json parsing
    text = "".join(open("../inputs/input12.txt").readlines())
    res = re.findall( r"-\d+|\d+", text)
    print(sum([int(n) for n in res]))
    
    # for part 2 we have to parse the json object
    books = json.loads(text)
    walk(books)
    print(acc)
    
    #import pprint
    #pprint.PrettyPrinter().pprint(books)
    
if __name__ == "__main__":
    main()