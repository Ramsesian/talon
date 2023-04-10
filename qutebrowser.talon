app: qutebrowser
-
# url related
search: key(o)
search new: key(O)
follow: key(f)
follow new: key(F)
follow rapid: key(; r)
follow yank: key(; y)

# address related
address copy: key(y:2)
address bar: key(g o)
address bar new: key(g O)
address paste: key(p p)
address paste new: key(P p)

# tab related
tab next: key(J)
tab last: key(K)
tab move next: key(g J)
tab move last: key(g K)
tab clone: key(g C)
tab detach: key(g D)
tab switch: key(ctrl-tab)
tab restore: key(u)
tab close: key(d)
go tab <user.number_key>: key("alt-{number_key}")

# session related
session save: key(: w space)
session load: insert(":session-load ")

go back: key(H)
[go] forward: key(L)
reload it: key(r)

# YouTube related
YouTube home:
    key(o)
    insert("https://www.youtube.com/")
    key(enter)

YouTube home new:
    key(O)
    insert("https://www.youtube.com/")
    key(enter)

YouTube search:
    mouse_move(884, 123)
    mouse_click(0)
    
YouTube change user:
    mouse_move(1865, 118)
    mouse_click(0)
    sleep(500ms)
    mouse_move(1681, 351)
    mouse_click(0)

YouTube skip:
    mouse_move(1332, 784)
    mouse_click(0)

YouTube max: key(i f escape)
YouTube min: key(escape space)
YouTube like: 
    mouse_move(822, 959)
    mouse_click(0)

YouTube channel:
    mouse_move(132, 958)
    mouse_click(0)

zoom in: key(+)
zoom out: key(-)
zoom reset: key(=)