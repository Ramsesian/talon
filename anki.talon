app: Anki
-
go decks: "d"
go add: "a"
go browse: "b"
go stats: "t"
go edit: "e"
go study: "s" 
    
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

next: "4"