app: TelegramDesktop
-
go saved: user.move_click(273, 181)
go settings: user.move_click(44, 91)

# deletes selected messages
message delete:
    key(delete)
    user.move_click(1069, 604, 300)

change user:
    mimic("go settings")
    user.mouse_relative(0, 170, 250, "False")
    mouse_drag(0)
    user.mouse_relative(0, -50)
    user.mouse_relative(0, 0, 100)