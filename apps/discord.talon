app: discord
-
# SETTINGS RELATED COMMANDS
go settings: user.move_click(297, 1040)
go my account: user.move_click(484, 171)
go profiles: 
    mimic("go my account")
    user.mouse_relative(0, 30)

go about me: user.move_click(747, 711)

# ACCESSED FROM THE MAIN VIEW
go status: user.move_click(103, 1044)
status edit: user.mouse_relative(0, -130)