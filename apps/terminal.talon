app: Gnome-terminal
app: Code
app: cool-retro-term
app: Kgx
-

# terminal shortcuts
term clear: key(ctrl-l)
term last: key(up enter)
term yank: key(ctrl-shift-c)

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
mark downloads:  """cd ~/Downloads\n"""
mark speed read:  """cd ~/Downloads/speedread\n"""
mark my stuff:   """cd ~/my-stuff\n"""
mark web:        """cd ~/my-stuff/web\n"""

# common commands
touch: "touch "
edit: "vim "
cat: "cat "
nah no: "nano "
which: "which "
ch mod: "chmod "
ncdu: """ncdu\n"""

# git commands
git init: "git init"
git status: """git status\n"""
git stage: """git add .\n"""
git add: "git add "
git push: """git push origin master\n"""
git push force: "git push -f origin master"
git rollback: "git reset --soft HEAD~"
git commit: user.insert_between('git commit -m "', '"') 
git fetch: """git fetch\n"""

# package manager commands
package upgrade: """sudo nala upgrade\n"""

# apack
a pack: "apack "
a unpack: "aunpack "

# flatpak commands
flatpak list: """flatpak list\n"""

# npm commands
nodemon: "nodemon "

# runners
shell run: "sh "
python run: "python3 "

# misc commands
g orse: """gource\n"""