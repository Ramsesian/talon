app: Code
-
file run: key(ctrl-alt-n)
file stop: key(ctrl-alt-m)
runner:
    mimic("file save")
    mimic("file stop")
    sleep(300ms)
    mimic("file run")
    