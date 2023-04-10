app: Anki
-
go decks: key(d)
go add: key(a)
go browse: key(b)
go stats: key(t)
go edit: key(e)
go study: key(s) 
    
go answer: mouse_move(814, 1042)
go answer reset: 
    tracking.control_toggle()
    mouse_move(814, 1042)

go upload: 
    mouse_move(804, 655)
    mouse_click(0)

card change note: key(ctrl-shift-m)
card change deck: key(ctrl-d)
card delete: key(ctrl-delete)

next: key(4)