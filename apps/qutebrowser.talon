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
location markdown: "ym"
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
find new: "/"
find next: "n"
find last: "N"
find cancel: key(escape)


# YouTube related
mark tube: """oyou\n"""
mark tube new: """Oyou\n"""
mark tube history: """ohttps://www.youtube.com/feed/history\n"""
mark tube history new: """Ohttps://www.youtube.com/feed/history\n"""

tube search: user.move_click(884, 123)
tube change user:
    user.move_click(1850, 120)
    user.mouse_relative(0, 230, 500)

tube skip: user.move_click(1332, 784)
tube max: key(i f escape)
tube min: key(escape space)
tube like: user.move_click(822, 959) 
tube channel: user.move_click(132, 958)
