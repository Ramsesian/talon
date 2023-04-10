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

# YouTube related
YouTube home: browser.go("https://www.youtube.com/")
YouTube home new: 
    app.tab_open()
    mimic("YouTube home")

YouTube search:
    mouse_move(933, 181)
    mouse_click(0)

YouTube change user:
    mouse_move(1864, 178)
    mouse_click(0)
    sleep(500ms)
    mouse_move(1707, 412)
    mouse_click(0)

YouTube max: key(f)
YouTube min: key(escape space)

YouTube like: 
    mouse_move(1036, 1004)
    mouse_click(0)

YouTube channel:
    mouse_move(134, 1004)
    mouse_click(0)

# for evernote web clipper
clipper show: insert("`")
clipper cancel:
    mouse_move(1863, 190)
    mouse_click(0)

clipper save: 
    mouse_move(1739, 237)
    mouse_click(0)

clipper notebook:
    mouse_move(1742, 545)
    mouse_click(0)

# for canvas
school next: 
    key(ctrl-end)
    sleep(300ms)
    mouse_move(1390, 1005)
    mouse_click(0)

school last:
    key(ctrl-end)
    sleep(300ms) 
    mouse_move(364, 1015)
    mouse_click(0)


# yomisan's definition
show definition:
    key(shift:down)
    sleep(100ms)
    key(shift:up)

word lookup:
    mouse_move(922, 267)
    mouse_click(0)
    mimic("select all")
    edit.paste()
    key(enter)
    