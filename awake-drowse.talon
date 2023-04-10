mode: all
-
# awake and sleep replacements
^drowse [<phrase>]$: speech.disable()
^(awake)+$: speech.enable()