### user.template Changes
Include shortcuts for keys:
- $c = ctrl
- $a = alt
- $s = shift
- $w = windows key
- $e = escape
- $r = return/enter
- $t = tab
- :u = :up
- :d = :down

Can combine them:
- $cs = ctrl-shift or $c-$s

Can pass through commands with the squares:
- a = auto_insert(“a”)
- [ka]  = keys(“a”)
- [ma]  = mimic(“a”)
- [s1s] = sleep(“1s”)
- [e]   = modifier expansion:
    - $c[eabcd] = $c:d abcd $c:u

Misc Changes
- Shorten template to uni (universal)
- See if you can get rid of the user before user.template

### Misc Changes
- Create new command for bookmarks / paths
- Make some commands available for markdown files