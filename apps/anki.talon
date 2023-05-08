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

go upload: user.move_click(804, 655)

change note type: key(ctrl-shift-m)
change note deck: key(ctrl-d)
(delete note | card delete): key(ctrl-delete)

move: "3"
next: "4"