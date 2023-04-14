app: Org.gnome.Nautilus
-
# movement commands
go back: key(backspace)
go into: key(enter)
go into top: key(home enter)
go into bottom: key(end enter)
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
mark documents: """~/Documents\n"""
mark downloads: """~/Downloads\n"""
mark music: """~/Music\n"""
mark pictures: """~/Pictures\n"""
mark videos: """~/Videos\n"""
mark talon: """~/my-stuff/talon\n"""
mark my stuff: """~/my-stuff\n"""
mark telegram: """~/Downloads/Telegram Desktop\n"""

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

# search
search: key(ctrl-3)
search location: key(ctrl-alt-o)

# misc
redo that: key(shift-ctrl-z)
location copy: key(ctrl-l ctrl-c escape)