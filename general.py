from talon import Module, actions, ctrl
import re
mod = Module()

@mod.action_class
class interperate:
    def move_click(x: int, y: int, sleep: int = 0, click: str = "True"):
        """moves and then clicks"""
        if sleep > 0: actions.sleep(f"{sleep}ms") # sleep if sleep value is not zero
        ctrl.mouse_move(x, y) # move mouse
        if click == "True": ctrl.mouse_click(0) # if click is true then click

    def mouse_relative(x: int, y: int, sleep: int = 0, click: str = "True"):
        """like move_click but it moves relative to the current position"""
        last_x, last_y = ctrl.mouse_pos()
        if sleep > 0: actions.sleep(f"{sleep}ms") # sleep if sleep value is not zero 
        if not (x == 0 and y == 0): ctrl.mouse_move(last_x + x, last_y + y) # if the relative position is the same then there's no need to move 
        if click == "True": ctrl.mouse_click(0) # if click is true then click

    def hold_key(key: str, sleep: int):
        """the key is held down for the specified amount of time"""
        actions.key(f"{key}:down")
        actions.sleep(f"{sleep}ms")
        actions.key(f"{key}:up")
        
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
            
            actions.auto_insert(re.sub(r"\\(?=\[|\])", "", x)) # removes the backslashes that are escaping the squares if any





def split_unless_escaped(string: str, character: str):
    """splits the string by the character unless it is followed by a backslash"""
    return re.split(fr"(?<!\\)\{character}", string)