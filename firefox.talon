app: firefox
-

# url related
search: 
    browser.focus_address()
    key(backspace)
search new: app.tab_open()

# address related
address bar new: 
    mimic("address copy") 
    app.tab_open()
    edit.paste()
    
address paste: 
    browser.focus_address()
    edit.paste()
    key(enter)

address paste new:
    app.tab_open()
    edit.paste()
    key(enter)

address paste new:
    edit.copy()
    mimic("address paste")  
    
address from selection new:
    edit.copy()
    mimic("address paste new")

# tap related
tab clone:
    mimic("address copy")
    mimic("address paste new")

tab detach: 
    mimic("address copy")
    user.tab_close_wrapper()
    key(super-w)
    sleep(1s)
    edit.paste()
    key(enter)

select element: key(ctrl-shift-c)

# tube related
tube home: browser.go("https://www.youtube.com")
tube home new: 
    app.tab_open()
    mimic("tube home")

tube search: user.move_click(933, 181)
tube change user: 
    user.move_click(1864, 178)
    user.move_click(1707, 412, 500)

tube max: "f"
tube min: key(escape space)

tube like: user.move_click(1036, 1004) 
tube channel: user.move_click(134, 1004)

# for evernote web clipper
clipper show: "`"
clipper cancel: user.move_click(1863, 190)
clipper save: user.move_click(1739, 237) 
clipper notebook: user.move_click(1742, 545)

# for canvas
school next: 
    edit.file_end()
    user.move_click(1000, 1000, 300)
    
school last:
    edit.file_end()
    user.move_click(364, 1015, 300)

school quiz start:
    user.move_click(723, 670)
    mimic("drowse")

school quiz end: user.move_click(1074, 994)

school expose one:
    mimic("select element")
    mouse_move(727, 713)
    sleep(100ms)
    mouse_click(0)
    user.move_click(1586, 243)
    sleep(100ms)
    edit.page_up()
    
school expose two:
    mimic("duke")
    edit.copy()
    app.tab_open()
    edit.paste()
    key(enter)
    sleep(4s)
    mimic("clipper show")
    sleep(2s)
    mimic("clipper save")

school expose three:
    user.tab_close_wrapper()
    user.move_click(1258, 977, 500)
    edit.file_end()
    user.move_click(1214, 1012, 300)

# yomisan's definition
show definition:
    key(shift:down)
    sleep(100ms)
    key(shift:up)

word lookup:
    user.move_click(922, 267)
    mimic("select all")
    edit.paste()
    key(enter)
    