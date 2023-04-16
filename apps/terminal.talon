app: Gnome-terminal
app: Code
app: cool-retro-term
app: Kgx
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
mark home:       """cd ~\n"""
mark talon home: """cd ~/.talon/user\n"""
mark talon user: """cd ~/.talon/user/my_custom\n"""
mark documents:  """cd ~/Documents\n"""
mark obsidian:   """cd ~/Documents/obsidian/General\n"""
mark my stuff:   """cd ~/my-stuff\n"""
mark web:        """cd ~/my-stuff/web\n"""

# git commands
git status: """git status\n"""
git stage: """git add .\n"""
git add: "git add "
git push: """git push origin master\n"""
git push force: "git push -f origin master"
git rollback: "git reset --soft HEAD~"
git commit: user.template('git commit -m ""[left]') 

# package manager commands
package upgrade: """sudo nala upgrade\n"""

# common commands
touch: "touch "
vim: "vim "
nah no: "nano "
which: "which "
ch mod: "chmod "

# misc commands
g orse: """gource\n"""

# apack
a pack: "apack "

# runners
shell run: "sh "
python run: "python3 "