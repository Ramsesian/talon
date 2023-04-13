app: Gnome-terminal
app: Code
app: cool-retro-term
-

# terminal shortcuts
term clear: key(ctrl-l)
term last: key(up enter)

# movement commands
path change: "cd "
path last: """cd -\n"""
path list: """ls -lah\n"""
path location: """pwd\n"""

# bookmarked locations
mark home: """cd ~\n"""
mark my stuff: """cd ~/my-stuff\n"""
mark web: """cd ~/my-stuff/web\n"""

# git commands
git status: """git status\n"""
git stage: """git add .\n"""
git add: "git add "
git push: """git push origin master\n"""
git rollback: "git reset --soft HEAD~"
git commit: 
    insert("git commit -m ")
    user.insert_between('"', '"')

# misc commands
touch: "touch "
vim: "vim "
nah no: "nano "
which: "which "

# apack
pack: "apack "

# runners
python run: "python3 "