from copy import deepcopy

class String(object):
    
    def __init__(self, char_list):
        self.char_list = char_list
        
    def __repr__(self):
        return "".join(self.char_list)
        
    def _index_check(self, index):
        if index >= self.length():
            raise Exception("index should be in the range 0..{}".format(self.length()))
        
    def length(self):
        return len(self.char_list)

    def concat(self, other_string):
        self.char_list += other_string.char_list
        
    def substr(self, start, end):
        _index_check(start)
        _index_check(end + 1)
        subset = deepcopy(self.char_list[start:end])
        return String(subset)
        
    def at(self, pos):
        _index_check(pos)
        return self.char_list[pos]
        
    def erase(self, start, end):
        _index_check(start)
        _index_check(end + 1)
        self.char_list = self.char_list[:start] + self.char_list[end:]
        
