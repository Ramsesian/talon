app: Org.gnome.Nautilus
-
# movement commands
go back: key(backspace)
go into: key(enter)
go into top: key(home enter)
go into bottom: key(end enter)
go into new: key(shift-enter)
peek: key(right)
depeek: key(left)

# bookmarks
mark home: key(alt-home)
mark documents: user.template("~/Documents[enter]")
mark downloads: user.template("~/Downloads[enter]")
mark music: user.template("~/Music[enter]")
mark pictures: user.template("~/Pictures[enter]")
mark videos: user.template("~/Videos[enter]")
mark talon: user.template("~/my-stuff/talon[enter]")
mark my stuff: user.template("~/my-stuff[enter]")
mark telegram: user.template("~/Downloads/Telegram Desktop[enter]")

# file commands
folder new: key(shift-ctrl-n)
file delete: key(delete)
file rename: key(f2)
file trash: key(delete)

# window commands
reload it: key(f5)
window new: key(ctrl-n)
open in term:
    key(f10)
    user.move_click(1248, 242, 400)

# search
search: key(ctrl-3)
search location: key(ctrl-alt-o)

# misc
redo that: key(shift-ctrl-z)
location copy: 
    key(ctrl-l)
    edit.copy()
    key(escape)