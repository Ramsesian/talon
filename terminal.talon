app: Gnome-terminal
app: Code
app: cool-retro-term
-

# terminal shortcuts
term clear: key(ctrl-l)
term last: key(up enter)

# movement commands
path change: "cd "
path last: user.template("cd -[enter]")
path list: user.template("ls -lah[enter]")
path location: user.template("pwd[enter]")

# bookmarked locations
mark home: user.template("cd ~[enter]")
mark my stuff: user.template("cd ~/my-stuff[enter]")
mark web: user.template("cd ~/my-stuff/web[enter]")

# git commands
git status: user.template("git status[enter]")
git stage: user.template("git add .[enter]")
git push: user.template("git push origin master[enter]")
git rollback: "git reset --soft HEAD~"
git commit: 
    insert("git commit -m ")
    user.insert_between('"', '"')

# misc commands
touch: "touch "
vim: "vim "
nah no: "nano "
which: "which "

# runners
python run: "python3 "