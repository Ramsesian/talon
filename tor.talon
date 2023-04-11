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

go tab <user.number_key>: key("alt-{number_key}")


pirate search:
    mouse_move(954, 520)
    mouse_click(0)

pirate get magnet:
    mouse_move(579, 786)
    mouse_click(1)
    sleep(200ms)
    mouse_move(594, 896)
    mouse_click(0)