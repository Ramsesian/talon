app: obsidian
-

# go related commands
go settings: key(ctrl-,)
go back: key(ctrl-alt-left)
go forward: key(ctrl-alt-right)

# text manipulation
text bold: key(ctrl-b)
insert comment: user.insert_between('%% ', ' %%')
heading <number>: key("#:{number}")
    

# templates
template note top:
    user.template("---[enter]")
    user.template("description: [enter]")
    user.template("---[enter:2]")
    user.template("Tags: [enter]")
    user.template("Links: \[\[Index\]\][enter]")    
    user.template("___[enter]")

# tags
tag primary: "#meta/primary "
tag code: "#code "

# window manipulation
tab last: key(ctrl-shift-tab)
tab next: key(ctrl-tab)
tab close: key(ctrl-w)
tab new: key(ctrl-t)


# fold plug in commands
fold all: key(alt-f )
insert fold: "%% fold %%"
