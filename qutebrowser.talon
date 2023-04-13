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
address from selection:()
    edit.copy()
    mimic("address paste")

address from selection new:
    edit.copy()
    mimic("address paste new")

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
tube home: user.template("ohttps://www.youtube.com[enter]")
tube home new: user.template("Ohttps://www.youtube.com[enter]")
tube search: user.move_click(884, 123)
tube change user:
    user.move_click(1865, 118)
    user.move_click(1681, 351, 500)

tube skip: user.move_click(1332, 784)
tube max: key(i f escape)
tube min: key(escape space)
tube like: user.move_click(822, 959) 
tube channel: user.move_click(132, 958)
