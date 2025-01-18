from .dwell_clicker import DwellClick
from talon import ctrl, ui, actions
import os
import subprocess



#
#          _____              _____             _____           _              _____          
#         /\    \            /\    \           /\    \         /\    \        /\    \         
#        /::\    \          /::\    \         /::\____\       /::\    \      /::\    \        
#       /::::\    \        /::::\    \       /::::|   |      /::::\    \    /::::\    \       
#      /::::::\    \      /::::::\    \     /:::::|   |     /::::::\    \  /::::::\    \      
#     /:::/\:::\    \    /:::/\:::\    \   /::::::|   |    /:::/\:::\    \/:::/\:::\    \     
#    /:::/  \:::\    \  /:::/__\:::\    \ /:::/|::|   |   /:::/__\:::\    \::/__\:::\    \    
#   /:::/    \:::\    \/::::\   \:::\    \:::/ |::|   |  /::::\   \:::\    \:\   \:::\    \   
#  /:::/    / \:::\    \:::::\   \:::\    \:/  |::|___|_/::::::\   \:::\    \:\   \:::\    \  
# /:::/    /   \:::\ ___\/\:::\   \:::\    \   |::::::::\    \::\   \:::\    \:\   \:::\    \ 
#/:::/____/  ___\:::|    | \:::\   \:::\____\  |:::::::::\____\::\   \:::\____\:\   \:::\____\
#\:::\    \ /\  /:::|____|  \:::\  /:::/    / / ~~~~~/:::/    /:::\   \::/    /::\   \::/    /
# \:::\    /::\ \::/    /__/ \:::\/:::/    /_/      /:::/    / \:::\   \/____/\:::\   \/____/ 
#  \:::\   \:::\ \/____/      \::::::/    /        /:::/    /   \:::\    \:\   \:::\    \     
#   \:::\   \:::\____\         \::::/    /        /:::/    /:\   \:::\____\:\   \:::\____\    
#    \:::\  /:::/    /         /:::/    /        /:::/    /:::\   \::/    /::\  /:::/    /    
#     \:::\/:::/    /         /:::/    /        /:::/    / \:::\   \/____/\:::\/:::/    /     
#      \::::::/    /         /:::/    /        /:::/    /   \:::\    \     \::::::/    /      
#       \::::/    /         /:::/    /        /:::/    /     \:::\____\     \::::/    /       
#        \::/____/          \::/    /         \::/    /       \::/    /      \::/    /        
#                            \/____/           \/____/         \/____/        \/____/         
#                                                                                                                             

def anki():
    box = DwellClick({"answer_hidden"})


    start_x = [787]
    length = [72, 60, 82, 68]

    # Generate X value based on the length i.e. the next x is the last one + how long it is
    for i, e in enumerate(length):
        start_x.append(start_x[i] + e)

    # Add gaps between the boxes
    for i, e in enumerate(length):
        if i == 0 or i == len(length): continue
        start_x[i] += 10
        length[i] -= 10

    button_y = 53
    button_height = 25

    box.add_rect(None, "deck"  , [start_x[0], button_y], [length[0], button_height], ["d", {"answer_hidden"}])
    box.add_rect(None, "add"   , [start_x[1], button_y], [length[1], button_height], ["a", {"answer_hidden"}])
    box.add_rect(None, "browse", [start_x[2], button_y], [length[2], button_height], ["b", {"answer_hidden"}])
    box.add_rect(None, "stats" , [start_x[3], button_y], [length[3], button_height], ["t", {"answer_hidden"}])
    box.add_rect(None, "edit"  , [6, -10]              , [83, 43]                  , ["e", {"answer_hidden"}])

    box.add_rect({"answer_hidden"}, "show_card", [750, -100], [420, 100], [" ", {"answer_shown" }], {"text": "Show Card"})
    box.add_rect({"answer_shown" }, "back"     , [20 ,  102], [ 83, 43 ], [     {"answer_hidden"}], {"text": "Back"     })

    colors = ("red", "yellow", "green", "blue", "gray")
    for i in range(1, 5):
        #box.add_rect({"answer_shown"}, f"button_{i}", [739 + 76 * i, -10 - 52], [62, 42], [f"{i}", {"answer_hidden"}], {"hover_duration": "500ms"}) 
        box.add_rect({"answer_shown"}, f"button_{i}", [300, 150 * i - 50], [100, 100], [f"{i}", {"answer_hidden"}], {"hover_duration": "500ms", "text": f"{i}", "rect": [{"color": colors[i - 1]}]})
    
    
    
    box.show()
     
#def dpad():
#    box = DwellClick({"combat"})
#    rect = ui.active_window().rect
#
#    size = 100
#    center_x = (rect.width / 2) - (size / 2) 
#    center_y = rect.top + (rect.height / 2) - size
#
#    offset = 150
#    inset = 15
#    reset = "up:up right:up down:up left:up"
#
#    hover_duration = {"hover_duration": "0ms"}
#
#    
#
#    print(center_x)
#    #for i in ()
#    #box.add_rect({"combat"}, "disable"    , [center_x                 , center_y                 ], [size], [   reset                        ], {"text": "Reset"    , **hover_duration})
#    box.add_rect({"combat"}, "disable"    , [0, 0                 ], ["auto"], [   reset                        ], {**hover_duration, "continual_clicking": True})
#    box.add_rect({"combat"}, "north"      , [center_x                 , center_y - offset        ], [size], [f"{reset}    up:down"           ], {"text": "North"    , **hover_duration})
#    box.add_rect({"combat"}, "northeast"  , [center_x + offset - inset, center_y - offset + inset], [size], [f"{reset}    up:down right:down"], {"text": "Northeast", **hover_duration})
#    box.add_rect({"combat"}, "east"       , [center_x + offset        , center_y                 ], [size], [f"{reset} right:down"           ], {"text": "East"     , **hover_duration})
#    box.add_rect({"combat"}, "southeast"  , [center_x + offset - inset, center_y + offset - inset], [size], [f"{reset}  down:down right:down"], {"text": "Southeast", **hover_duration})
#    box.add_rect({"combat"}, "south"      , [center_x                 , center_y + offset        ], [size], [f"{reset}  down:down"           ], {"text": "South"    , **hover_duration})
#    box.add_rect({"combat"}, "southwest"  , [center_x - offset + inset, center_y + offset - inset], [size], [f"{reset}  down:down  left:down"], {"text": "Southwest", **hover_duration})
#    box.add_rect({"combat"}, "west"       , [center_x - offset        , center_y                 ], [size], [f"{reset}  left:down"           ], {"text": "West"     , **hover_duration})
#    box.add_rect({"combat"}, "northwest"  , [center_x - offset + inset, center_y - offset + inset], [size], [f"{reset}    up:down  left:down"], {"text": "Northwest", **hover_duration})
#
#
#    box.show()

def inverted_fate():
    box = DwellClick({"comic"})
    text_size = {"text_textsize": 30}
    settings = {"hover_duration": "500ms", **text_size}
    
    size = [620, "auto"]

    box.add_rect({"comic"}, "back"       , (0  ,  0), size      , ["left" ], {**settings , "text": "Left" })
    box.add_rect({"comic"}, "next_right ", [-1 ,  0], size      , ["right"], {**settings , "text": "Right"})
    box.add_rect({"comic"}, "auto_right_slow" , [620, -1], (340, 200), ["right"], {**text_size, "text": "Auto Right (Slow)", "hover_duration": "3000ms", "continual_clicking": True})
    box.add_rect({"comic"}, "auto_right_quick", [960, -1], (340, 200), ["right"], {**text_size, "text": "Auto Right (Fast)", "hover_duration": "2000ms", "continual_clicking": True})
    box.show()

def mangadex():
    box = DwellClick({"comic"})
    settings = {"hover_duration": "500ms", "text_textsize": 30}

    size = [520, "auto"]
    
    box.add_rect({"comic"}, "back", (0 , 0), size, ["left" ], {**settings, "text": "left" })
    box.add_rect({"comic"}, "next", [-1, 0], size, ["right"], {**settings, "text": "right"})
    box.show()

def simple_move():
        box = DwellClick({"combat"})
        box.add_rect({"combat"}, "move_up"   ,      [0 , -1], ["auto", 100   ], [   "up:up",  "down:down"], {"text": "Down" })
        box.add_rect({"combat"}, "move_down" ,      [0 ,  0], ["auto", 100   ], [ "down:up",    "up:down"], {"text": "Up"   })
        box.add_rect({"combat"}, "move_right",      [-1,  0], [100   , "auto"], [ "left:up", "right:down"], {"text": "Right"})
        box.add_rect({"combat"}, "move_left" ,      [0 ,  0], [100   , "auto"], ["right:up",  "left:down"], {"text": "Left" })
        box.show()


def slay_the_spire():
        
        box = DwellClick({"combat"})

        slow = {"hover_duration": "500ms"}
        click = {"continual_clicking": True}
        slow_click = {**slow, **click}
        
        long_button = (250, 70)

        box.add_rect({"combat"                  }, "end_turn"       , [-200, -170], (170, 80  ), ["e"                            ], {"hover_duration":"750ms"})
        box.add_rect({"combat"                  }, "draw_pile"      , [ 30 , -20 ], [100      ], ["a"     , {"return"           }])
        box.add_rect({"combat"                  }, "discard_pile"   , [-30 , -20 ], [100      ], ["s"     , {"return"           }])
        box.add_rect({"combat"                  }, "map"            , [-160,  5  ], (60 , 55  ), ["m"     , {"return"           }])
        box.add_rect({"return"                  }, "return"         , [ 0  , -150], long_button, [0       , {"combat"           }])
        box.add_rect({"combat"                  }, "deck"           , [-85 ,  10 ], (60 , 50  ), ["d"     , {"return"           }])
        box.add_rect({"combat"                  }, "settings"       , [-15 ,  10 ], (55 , 50  ), ["escape", {"return", "restart"}])
        box.add_rect({"restart"                 }, "restart"        , ( 0  ,  733), long_button, [0       , {"combat"           }], {**slow                  })
        box.add_rect({"combat"                  }, "potions"        , ( 580,  10 ), (160, 50  ), [0       , {"potion_select"    }], {**slow_click            })
        box.add_rect({"potion_select"           }, "potion_select"  , ( 450,  140), (310, 110 ), [0       , {"combat"           }], {**slow_click            })
        box.add_rect({"enemies", "potion_select"}, "enemies"        , [-180,  400], (790, 350 ), [0       , {"combat"           }], {**slow                  })
        box.add_rect({"combat"                  }, "exhausted_cards", [-40 , -155], [60       ],        ["x"     , {"return"           }])
        #box.add_rect(None, "back", (800, 800), (100, 100), [box.history_back], {"text": "Back"})
        
        #box.add_rect({"proceed"}, "proceed"        , 1600, 730, 140, 70 , 0   , None, None, 1000)

        for i, card in enumerate([*range(1, 10), 0]):
            # slay the spire goes from 1-9, 0 so I need to reflect that
            box.add_rect({"combat", "enemies"}, f"card_{card}", (1200 - i*120, 150), [100], [f"{card}", {"enemies"}], {"text": f"{card}"})

        box.show()

def undertale():
    box = DwellClick({"main"})
    #settings =  {"rect": [
    #     {"color": "blue"},
    #     {"color": "red", "display": {"clicked"}}
    #]}

    def click():
        subprocess.Popen(
        'xdotool windowactivate --sync "$(xdotool search --name Undertale | tail -n1)" && xdotool key z',
        shell=True
    )
        
    def back():
        subprocess.Popen(
        'xdotool windowactivate --sync "$(xdotool search --name Undertale | tail -n1)" && xdotool key x',
        shell=True
    )
        
    def mouse():
        actions.tracking.control_toggle(False)
        subprocess.Popen(
            "sh ~/.talon/user/Ramsesian/antimicrox-switcher.sh 'mouse'",
            shell=True
        )
        
    def arrows():
        actions.tracking.control_toggle(True)

        subprocess.Popen(
            "sh ~/.talon/user/Ramsesian/antimicrox-switcher.sh 'arrow'",
            shell=True
        )

    box.add_rect({"main"}, "click1", [-300, -170], (70, 80), [click], {"text": "Interact"})
    box.add_rect({"main"}, "click2", [-200, -170], (70, 80), [click], {"text": "Interact", "continual_clicking": True})
    box.add_rect({"main"}, "back1", [-300, -70], (70, 80), [back], {"text": "Back"})
    box.add_rect({"main"}, "back2", [-200, -70], (70, 80), [back], {"text": "Back", "continual_clicking": True})
    box.add_rect({"main"}, "mouse", [-300, -270], (70, 80), [mouse], {"text": "Mouse"})
    box.add_rect({"main"}, "arrows", [-200, -270], (70, 80), [arrows], {"text": "Arrows"})



    box.show()


def website_scroll(scroll_distance):
    box = DwellClick({"scroll"})
    settings = {"continual_clicking":True, "rect":[{"color": None}]}
    box.add_rect({"scroll"}, "scroll_up"  , [0,  0], ["auto", 200], [(0, -scroll_distance)], settings)
    box.add_rect({"scroll"}, "scroll_down", [0, -1], ["auto", 350], [(0,  scroll_distance)], settings)
    box.show()
    ctrl.cursor_visible(False)

def website_auto_scroll(scroll_distance):
    box = DwellClick({"scroll"})
    settings = {"continual_clicking":True, "hover_duration": "0ms"}#, "rect":[{"color": None}]}
    #box.add_rect({"scroll"}, "scroll_up"  , [0,  0], ["auto", 200], [(0, -scroll_distance)], settings)
    height = 150
    offset = 300
    accel = 25
    box.add_rect({"scroll"}, "scroll_down"      , [680, offset+height]  , [560, height], [(0,  scroll_distance)], settings)
    box.add_rect({"scroll"}, "scroll_down_two"  , [680, offset+height*2], [560, height], [(0,  scroll_distance+accel)], settings)
    box.add_rect({"scroll"}, "scroll_down_three", [680, offset+height*3], [560, height], [(0,  scroll_distance+accel*2)], settings)
    box.add_rect({"scroll"}, "scroll_down_four" , [680, offset+height*4], [560, height], [(0,  scroll_distance+accel*3)], settings)
    box.show()
    #ctrl.cursor_visible(False)


def vampire_survivors():
    box = DwellClick({"combat"})
    rect = ui.active_window().rect
    center = (1920 + (rect.width / 2), rect.top + (rect.height / 2) - 30)

    def move_center():
        #print(1920 + (rect.width / 2), rect.top + (rect.height / 2) - 30)
        ctrl.mouse_move(*center)
        ctrl.mouse_click(button=0, down=True)
    

    height = 100
    spacing = height * -1.5

    offset = 50



    box.add_rect({"combat"}, "reset_cursor" , [-30,              - offset], [height], [move_center ], {"text": "Go Center"    })
    box.add_rect({"combat"}, "stop_drag"    , [-30,  spacing     - offset], [height], [0           ], {"text": "Stop Dragging"})
    box.add_rect({"combat"}, "level_up"     , [-30,  spacing * 2 - offset], [height], [{"level_up"}], {"text": "Level Up"     })
    box.add_rect({"combat"}, "reward_accept", [-30,  spacing * 3 - offset], [height], [{"done"}    ], {"text": "Accept Reward"})
    actions.tracking.control_toggle(False)
    reward_hover = {"hover_duration": "500ms"}
    box.add_rect({"done"    }, "done" , (820, 830), (280, 80 ), [0, {"combat"}], reward_hover)
    box.add_rect({"level_up"}, "items", (660, 268), (600, 690), [0, {"combat"}], reward_hover)

    box.show()




### GAMES
#anki() 
#website_scroll(100) #ao3
#dpad()
inverted_fate()
#mangadex()
#undertale()
#website_scroll(300) #pinterest
#website_auto_scroll(50)
#simple_move()
#slay_the_spire()
#vampire_survivors()


mouse_pos = ctrl.mouse_pos()
print(f"Mouse position on monitor one: x:  {mouse_pos[0]}, y: {mouse_pos[1]}")
print(f"Mouse position on monitor two: x: ({mouse_pos[0] - 1920}, {mouse_pos[0] - 1920*2}), y: ({mouse_pos[1]}, {mouse_pos[1] - 1920})")



#Don't kill Papyrus at the end of his fight, and go on that "date" with him.
#Flee from Undyne in her battle, everytime, and give her water from the cooler once you reach Hotland. Go to the cooking date with her.
#And you have to befriend Alphys: Run after her all the way once she says goodbye to you at the elevator in the Core, until Undyne calls you about a letter. 
#
#
#
#
#