app: firefox
-

# URL related
location yank: mimic("address copy")
location bar: browser.focus_address()
location bar new: key(ctrl-l ctrl-c ctrl-t ctrl-v)
location paste: key(ctrl-l ctrl-v enter) 
location paste new: key(ctrl-t ctrl-v enter)
location from selection: key(ctrl-c ctrl-l ctrl-v enter)
location from selection new: key(ctrl-c ctrl-t ctrl-v enter)


select element: key(ctrl-shift-c)

# bookmarks
mark tube: browser.go("https://youtube.com")
mark tube new: user.template("[ctrl-t]https://youtube.com\n")
mark tube history: user.template("https://www.youtube.com/feed/history\n")
mark tube history new: user.template("[ctrl-t]https://www.youtube.com/feed/history\n")

# youtube related
tube search: user.move_click(933, 181)
tube change user: 
    user.move_click(1864, 178)
    user.mouse_relative(0, 230, 500)

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
    user.move_click(1264, 1008, 500)
    sleep(100ms)
    edit.file_end()
    user.mouse_relative(-30, 0)

# yomisan's definition
show definition: user.hold_key("shift", 100)

word lookup:
    user.move_click(922, 267)
    key(ctrl-a ctrl-v enter)
    