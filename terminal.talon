app: Gnome-terminal
app: Code
app: cool-retro-term
-

# terminal shortcuts
term clear: key(ctrl-l)

# movement commands
path change: insert("cd ")
path last: key(c d space - enter)
path list: key(l s space - l a h enter)
path location: key(p w d enter)


# bookmarked locations
mark home: key(c d space ~ enter)
mark my stuff: 
    insert("cd ~/my-stuff/")
    key(enter)

mark web:
    insert("cd ~/my-stuff/web")
    key(enter)


# git commands
git stage: 
    insert("git add .")
    key(enter)

git status: 
    insert("git status")
    key(enter)

git commit:
    insert("git commit -m ")
    user.insert_between('"', '"')

git push:
    insert("git push origin master")
    key(enter)

# misc commands
touch: insert("touch ")
vim: insert("vim ")
nahno: insert("nano ")
which: insert("which ")