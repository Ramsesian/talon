app: qutebrowser
-
# url related
search: "o"
search new: "O"
follow: "f"
follow new: "F"
follow rapid: ";r"
follow yank: ";y"

# URL related
location yank: "yy"
location bar: "go"
location bar new: "gO"
location paste: "pp"
location paste new: "Pp"
location from selection: key(ctrl-c p:2)
location from selection new: key(ctrl-c P p)

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
go tab <number>: key("alt-{number}")

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
tube home: """oyou\n"""
tube home new: """Oyou\n"""
tube search: user.move_click(884, 123)
tube change user:
    user.move_click(1865, 118)
    user.move_click(1681, 351, 500)

tube skip: user.move_click(1332, 784)
tube max: key(i f escape)
tube min: key(escape space)
tube like: user.move_click(822, 959) 
tube channel: user.move_click(132, 958)
