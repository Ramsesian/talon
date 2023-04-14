app: TelegramDesktop
-
go saved: user.move_click(273, 181)
go settings: user.move_click(44, 91)

# deletes selected messages
message delete:
    key(delete)
    user.move_click(1069, 604, 300)

user change:
    mimic("go settings")
    sleep(250ms)
    mouse_move(122, 263)
    mouse_drag(0)
    user.move_click(158, 227, 100)
    sleep(100ms)
    mouse_click(0)

test: user.mouse_relative(10, 10,"True", 5000)