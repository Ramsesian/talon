app: Org.gnome.Nautilus
-
out of: key(backspace)
into top: key(home enter)
into bottom: key(end enter)
into: key(enter)
into new: key(shift-enter)
into and close: key(shift-ctrl-down)
into home: key(alt-home)

into documents: user.template("~/Documents[enter]")
into downloads: user.template("~/Downloads[enter]")
into music: user.template("~/Music[enter]")
into pictures: user.template("~/Pictures[enter]")
into videos: user.template("~/Videos[enter]")
into talon: user.template("~/my-stuff/talon[enter]")
into my stuff: user.template("~/my-stuff[enter]")

peek: key(right)
depeek: key(left)

window new: key(ctrl-n)

search: key(ctrl-3)
search location: key(ctrl-alt-o)

redo that: key(shift-ctrl-z)

file rename: key(f2)
file trash: key(delete)
location copy: 
    key(ctrl-l)
    edit.copy()
    key(escape)

open in term:
    key(f10)
    user.move_click(1248, 242, 400)

reload it: key(f5)
file delete: key(delete)
folder new: key(shift-ctrl-n)