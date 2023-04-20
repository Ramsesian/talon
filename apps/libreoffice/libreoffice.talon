app: Soffice
app: libreoffice-startcenter
app: libreoffice-writer
-
##############################
#### NOT INSIDE A SECTION ####
##############################
go font[s]: user.move_click(425, 158)
go font size: 
    user.move_click(473, 158)
    key(ctrl-a)
go document: user.move_click(908, 636)


insert squared: key(shift-ctrl-p 2 shift-ctrl-p)
#################################
#### INSIDE THE FILE SECTION ####
#################################
go file: user.go_file()
go file new:
    user.go_file()
    user.tool_into()

file new text document: key(ctrl-n)
go export as:
    user.go_file()
    user.tool_into(15)

export as pdf:
    mimic("go export as")
    key(enter)
    mouse_move(1294, 838)

###################################
#### INSIDE THE INSERT SECTION ####
###################################
go insert:
    user.go_file()
    key(right:3)

insert page break: key(ctrl-enter)
go object:
    mimic("go insert")
    user.tool_into(6)

insert formula: key(alt-ctrl-=)

insert special character:
    mimic("go insert")
    user.tool_select(17)

####################################
#### INSIDE THE FORMAT SECTION ####
####################################
go format: user.go_format()
go text:
    user.go_format()
    user.tool_into()

text bold: key(ctrl-b)
text italic: key(ctrl-i)
text super: key(shift-ctrl-p)
text sub: key(shift-ctrl-b)

go spacing: user.go_spacing()
    
spacing one:
    user.go_spacing()
    key(enter)

spacing one point five:
    user.go_spacing()
    user.tool_select(2)
    
spacing two:
    user.go_spacing()
    user.tool_select(3)

go align:
    user.go_format()
    user.tool_into(3)

align left: key(ctrl-l)
align center: key(ctrl-e)

go paragraph:
    user.go_format()
    user.tool_select(7)

go list[s]:
    user.go_format()
    user.tool_into(8)

unordered switch: key(shift-f12)
ordered switch: key(f12)

go page style:
    user.go_format()
    user.tool_select(10)

#################################
#### INSIDE THE HELP SECTION ####
#################################
go help:
    user.go_file()
    key(right:10)

help search: key(shift-escape)