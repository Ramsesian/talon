app: Tor Browser
-

# url related
search: key(ctrl:down l ctrl:up)
(search new | tab new): key(ctrl-t)

# address related
address copy:
    key(ctrl:down l ctrl:up)
    edit.copy()
    
address bar new: 
    mimic("address copy") 
    mimic("search new")
    edit.paste()
    
address paste: 
    mimic("search")
    edit.paste()
    key(enter)

address paste new:
    key(ctrl-t)
    edit.paste()
    key(enter)

# tap related
tab clone:
    mimic("address copy")
    mimic("address paste new")

tab last: key(ctrl-shift-tab)
tab next: key(ctrl-tab)
tab close: key(ctrl-w)

go tab <number>: key("alt-{number}")

go pirate: user.move_click(252, 138)
pirate search: user.move_click(954, 520)
pirate get magnet:
    mouse_move(579, 786)
    mouse_click(1)
    user.mouse_relative(50, 110, 200)