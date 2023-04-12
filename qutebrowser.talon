app: qutebrowser
-
# url related
search: "o"
search new: "O"
follow: "f"
follow new: "F"
follow rapid: ";r"
follow yank: ";y"

# address related
address copy: key(y:2)
address bar: "go"
address bar new: "gO"
address paste: key(p:2)
address paste new: "Pp"

# tab related
tab next: "J"
tab last: "K"
tab move next: "gJ"
tab move last: "gK"
tab clone: "gC"
tab detach: "gD"
tab switch: key(ctrl-tab)
tab restore: "u"
tab close: "d"
go tab <user.number_key>: key("alt-{number_key}")

# session related
session save: ":w "
session load: ":session-load "

# zoom related
zoom in: "+"
zoom out: "-"
zoom reset: "="

# history related 
go back: "H"
[go] forward: "L"
reload it: "r"

# search related
find: "/"
find next: "n"
find last: "N"
find cancel: key(escape)

# YouTube related
YouTube home: user.template("ohttps://www.youtube.com[enter]")
YouTube home new: user.template("Ohttps://www.youtube.com[enter]")
YouTube search:
    mouse_move(884, 123)
    mouse_click(0)
    
YouTube change user:
    mouse_move(1865, 118)
    mouse_click(0)
    sleep(500ms)
    mouse_move(1681, 351)
    mouse_click(0)

YouTube skip:
    mouse_move(1332, 784)
    mouse_click(0)

YouTube max: key(i f escape)
YouTube min: key(escape space)
YouTube like: 
    mouse_move(822, 959)
    mouse_click(0)

YouTube channel:
    mouse_move(132, 958)
    mouse_click(0)
