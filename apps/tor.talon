app: Tor Browser
-

# address related
address copy: key(ctrl:down l c ctrl:up)
address bar new: key(ctrl:down l c t v ctrl:up)
address paste: key(ctrl-t ctrl-v enter)
address paste new: key(ctrl-t ctrl-v enter)

# pirate bay
go pirate: user.move_click(252, 138)
pirate search: user.move_click(954, 520)
pirate get magnet:
    mouse_move(579, 786)
    mouse_click(1)
    user.mouse_relative(50, 110, 200)