from talon import Module, actions
#from re import split
import re
mod = Module()

@mod.action_class
class interpreted:
    def template(interpreted: str):
        """the string is passed to an insert while everything inside curly brackets are passed to a key4"""
        
        
        # list = re.split(r"(?<!\\)\[", interpreted)
        list = split_unless_escaped(interpreted, "[")
        for x in list:
            if re.search(r"(?<!\\)\]", x):
                #because its split by [ only, you'll get [insert, key]insert, key]]
                #So you split by ] and feed the first half into key and the second to insert
                temp = split_unless_escaped(x, "]")
                actions.key(temp[0])
                x = temp[1]
            
            actions.insert(re.sub(r"\\(?=\[|\])", "", x)) # removes the backslashes that are escaping the squares if any



def split_unless_escaped(string: str, character: str):
    """splits the string by the character unless it is followed by a backslash"""
    return re.split(fr"(?<!\\)\{character}", string)