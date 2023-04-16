app: Org.gnome.Nautilus
-
# movement commands
go back: key(backspace)
go into: 
    key(enter)
    sleep(200ms)
    key(down)

go into top: 
    key(home)
    mimic("go into")

go into bottom: 
    key(end)
    mimic("go into")

go into new: key(shift-enter)

go from bottom [<number>]:
    amount = number or 1
    amount = amount - 1
    key("end up:{amount}")

go from top [<number>]:
    amount = number or 1
    amount = amount - 1
    key("home down:{amount}")

peek: key(right)
depeek: key(left)

# bookmarks
mark home: key(alt-home)
mark documents: user.template("~/Documents[enter]")
mark downloads: user.template("~/Downloads[enter]")
mark telegram:  user.template("~/Downloads/Telegram Desktop[enter]")
mark music:     user.template("~/Music[enter]")
mark pictures:  user.template("~/Pictures[enter]")
mark videos:    user.template("~/Videos[enter]")
mark trash:     user.template("trash:///[enter]")
mark my stuff:  user.template("~/my-stuff[enter]")
mark talon:     user.template("~/my-stuff/talon[enter]")
mark web:       user.template("~/my-stuff/web[enter]")

# file commands
folder new: key(shift-ctrl-n)
file delete: key(delete)
file rename: key(f2)

# window commands
reload it: key(f5)
window new: key(ctrl-n)
open in term:
    key(f10)
    user.move_click(1248, 242, 400)

# misc
redo that: key(shift-ctrl-z)
location yank: key(ctrl-l ctrl-c escape)

# right click menu actions
open menu: mouse_click(1)
open with other application: key(down:2 enter)