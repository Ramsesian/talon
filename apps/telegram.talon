app: TelegramDesktop
-
go saved: user.move_click(273, 181)
go settings: user.move_click(44, 91)

# deletes selected messages
confirm delete: 
    sleep(300ms)
    key(enter)

selection delete:
    key(delete)
    mimic("message confirm delete")

message delete:
    mouse_click(1)
    user.mouse_relative(20, 185)
    mimic("message confirm delete")

message edit:
    mouse_click(1)
    user.mouse_relative(20, 50)

message yank:
    mouse_click(1)
    user.mouse_relative(20, 120)

change user:
    mimic("go settings")
    user.mouse_relative(0, 170, 250, "False")
    mouse_drag(0)
    user.mouse_relative(0, -50)
    user.mouse_relative(0, 0, 100)