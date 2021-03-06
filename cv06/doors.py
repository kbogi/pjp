
"""
@author: Krystof Bogar

dvéře

"""
def condition(a, b):
    """
    podminka sousedu
    """
    return a[-1] == b[0]
def solve_key(words):
    """
    resi ulohu s predzarovnym polem
    """
    if len(words) == 2:
        return condition(words[0], words[1])
    elif len(words)>1:
        for word in words[1:]:
            if(condition(words[0], word)):
                words.remove(word)
                words.insert(1, word)
                if solve_key(words[1:]) == True:
                    return True
    return False

def is_key(words):
    """
    resi podminku z pole slov
    """
    begl = []
    def add(word):
        f = word[0]
        l = word[-1]
        add = True
        for n in begl:
            if n[0]==f:
                n[1] += 1
                add = False
        if add:
            begl.append([f, 1])
        add = True
        for n in begl:
            if n[0]==l:
                n[1] -= 1
                add = False
        if add:
            begl.append([l, -1])
            
    
    for word in words:
        add(word)
    sumb = 0
    sume = 0
    
    
    for n in begl:
        if n[1] > 1 or n[1] < -1:
            return False
        if n[1] > 0:
            sumb += n[1]
        if n[1] < 0:
            sume -= n[1]
    if(sumb > 1 or sume > 1):
        return False
    for word in words:
        words.remove(word)
        words.insert(0, word)
        if solve_key(words) == True:
            return True
    return False
    
def run(fi):
    """
    nacte soubor doors.txt a vypise poporade spravnost klicu do konzole
    """
    f = open(fi)
    def readint():
        """
        precte integer ze vstupu
        """
        return int(f.readline())
    def readword():
        """
        precte slovo ze vstupu
        """
        line = f.readline()
        if line[-1] == '\n':
            return line[0:-1]
        return line
    num_of_keys = readint()
    while num_of_keys > 0:
        num_of_words = readint()
        word_list = []
        while num_of_words > 0:
            word_list.append(readword())
            num_of_words -= 1
        print(is_key(word_list))
        num_of_keys -= 1
if __name__ == "__main__":

    run("small.txt")
    run("large.txt")