app: Org.gnome.Nautilus
-
out of: key(backspace)
into top: key(home enter)
into bottom: key(end enter)
into: key(enter)
into new: key(shift-enter)
into and close: key(shift-ctrl-down)
into home: key(alt-home)
into documents: 
    insert("~/Documents")
    key(enter)

into downloads: 
    insert("~/Downloads")
    key(enter)

into music: 
    insert("~/Music")
    key(enter)

into pictures: 
    insert("~/Pictures")
    key(enter)

into videos: 
    insert("~/Videos")
    key(enter)

into talon: 
    insert("~/my-stuff/talon")
    key(enter)

into my stuff: 
    insert("~/my-stuff")
    key(enter)

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
    mouse_move(1248, 242)
    sleep(400ms)
    mouse_click(0)

reload it: key(f5)
file delete: key(delete)
folder new: key(shift-ctrl-n)