app: Gnome-terminal
app: Code
-

# terminal shortcuts
term clear: key(ctrl-l)

# movement commands
path change: insert("cd ")
path home: key(c d space ~ enter)
path last: key(c d space - enter)
path list: key(l s space - l a h enter)


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