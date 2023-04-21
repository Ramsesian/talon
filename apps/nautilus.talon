app: Org.gnome.Nautilus
-
# movement commands
go back: key(backspace)
go into new: key(shift-enter)
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

go [<number>] from bottom:
    amount = number or 1
    amount = amount - 1
    key("end up:{amount}")

go [<number>] from top:
    amount = number or 1
    amount = amount - 1
    key("home down:{amount}")

peek: key(right)
depeek: key(left)

# bookmarks
mark home: key(alt-home)
mark documents: """~/Documents\n"""
mark downloads: """~/Downloads\n"""
mark telegram:  """~/Downloads/Telegram Desktop\n"""
mark music:     """~/Music\n"""
mark pictures:  """~/Pictures\n"""
mark videos:    """~/Videos\n"""
mark watching:  """~/Videos/show+movie/z-watching/"""
mark trash:     """trash:///\n"""
mark my stuff:  """~/my-stuff\n"""
mark talon:     """~/my-stuff/talon\n"""
mark web:       """~/my-stuff/web\n"""

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