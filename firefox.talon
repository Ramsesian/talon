app: firefox
-

# url related
search: key(ctrl-l backspace)
search new: app.tab_open()

# URL related
location yank: mimic("address copy")
location bar: browser.focus_address()
location bar new: 
    mimic("address copy") 
    key(ctrl-t ctrl-v)
    
location paste: 
    browser.focus_address()
    key(ctrl-v enter)

location paste new: key(ctrl-l ctrl-v enter)
location from selection: key(ctrl-c ctrl-l ctrl-v enter)
location from selection new: key(ctrl-c ctrl-t ctrl-v enter)

# tap related
tab clone:
    mimic("address copy")
    mimic("location paste new")

tab detach: 
    mimic("address copy")
    key(ctrl-w super-w)
    sleep(1s)
    key(ctrl-v enter)

select element: key(ctrl-shift-c)

# tube related
tube home: browser.go("https://youtube.com")
tube home new: user.template("[ctrl-t]https://youtube.com[enter]")
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
    mimic("talon sleep")

school quiz end: user.move_click(1074, 994)

school expose one:
    mimic("select element")
    user.move_click(727, 713, 100)
    user.move_click(1586, 243)
    sleep(100ms)
    edit.page_up()
    
school expose two:
    mimic("duke")
    mimic("location from selection new")
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
show definition: user.hold_key("shift", 100)

word lookup:
    user.move_click(922, 267)
    key(ctrl-a ctrl-v enter)
    