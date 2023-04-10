app: TelegramDesktop
-
go saved:
    mouse_move(273, 181)
    mouse_click(0)

go settings:
    mouse_move(44, 91)
    mouse_click(0)

user change:
    mimic("go settings")
    sleep(250ms)
    mouse_move(122, 263)
    mouse_drag(0)
    mouse_move(158, 227)
    sleep(100ms)
    mouse_click(0)
    sleep(100ms)
    mouse_click(0)
