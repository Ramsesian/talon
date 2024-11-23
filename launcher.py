from .dwell_clicker import DwellClick
from talon import ctrl, ui




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
    box.add_rect({"answer_hidden"}, "back", [750, -100], [420, 100], [" ", {"answer_shown"}], {})

    colors = ("red", "yellow", "green", "blue")

    for i in range(1, 5):
        #box.add_rect({"answer_shown"}, f"button_{i}", [739 + 76 * i, -10 - 52], [62, 42], [f"{i}", {"answer_hidden"}], {"hover_duration": "500ms"}) 
        box.add_rect({"answer_shown"}, f"button_{i}", [300, 150 * i - 50], [100, 100], [f"{i}", {"answer_hidden"}], {"hover_duration": "500ms", "text": f"{i}", "rect": [{"color": colors[i - 1]}]})
    box.show()
     
def dpad():
    box = DwellClick({"combat"})
    rect = ui.active_window().rect

    size = 100
    center_x = (rect.width / 2) - (size / 2)
    center_y = rect.top + (rect.height / 2) - size

    offset = 150
    inset = 15
    reset = "up:up right:up down:up left:up"

    hover_duration = {"hover_duration": "0ms"}

    

    print(center_x)
    #for i in ()
    #box.add_rect({"combat"}, "disable"    , [center_x                 , center_y                 ], [size], [   reset                        ], {"text": "Reset"    , **hover_duration})
    box.add_rect({"combat"}, "disable"    , [0, 0                 ], ["auto"], [   reset                        ], {**hover_duration, "continual_clicking": True})
    box.add_rect({"combat"}, "north"      , [center_x                 , center_y - offset        ], [size], [f"{reset}    up:down"           ], {"text": "North"    , **hover_duration})
    box.add_rect({"combat"}, "northeast"  , [center_x + offset - inset, center_y - offset + inset], [size], [f"{reset}    up:down right:down"], {"text": "Northeast", **hover_duration})
    box.add_rect({"combat"}, "east"       , [center_x + offset        , center_y                 ], [size], [f"{reset} right:down"           ], {"text": "East"     , **hover_duration})
    box.add_rect({"combat"}, "southeast"  , [center_x + offset - inset, center_y + offset - inset], [size], [f"{reset}  down:down right:down"], {"text": "Southeast", **hover_duration})
    box.add_rect({"combat"}, "south"      , [center_x                 , center_y + offset        ], [size], [f"{reset}  down:down"           ], {"text": "South"    , **hover_duration})
    box.add_rect({"combat"}, "southwest"  , [center_x - offset + inset, center_y + offset - inset], [size], [f"{reset}  down:down  left:down"], {"text": "Southwest", **hover_duration})
    box.add_rect({"combat"}, "west"       , [center_x - offset        , center_y                 ], [size], [f"{reset}  left:down"           ], {"text": "West"     , **hover_duration})
    box.add_rect({"combat"}, "northwest"  , [center_x - offset + inset, center_y - offset + inset], [size], [f"{reset}    up:down  left:down"], {"text": "Northwest", **hover_duration})


    box.show()

def inverted_fate():
    box = DwellClick({"comic"})
    text_size = {"text_textsize": 30}
    settings = {"hover_duration": "500ms", **text_size}
    
    size = [620, "auto"]

    box.add_rect({"comic"}, "back"       , (0  ,  0), size      , ["left" ], {**settings , "text": "Left" })
    box.add_rect({"comic"}, "next_right ", [-1 ,  0], size      , ["right"], {**settings , "text": "Right"})
    box.add_rect({"comic"}, "next_bottom", [620, -1], (680, 200), ["right"], {**text_size, "text": "Auto Right", "hover_duration": "2000ms", "continual_clicking": True})
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



def website_scroll(scroll_distance):
    box = DwellClick({"scroll"})
    settings = {"continual_clicking":True, "rect":[{"color": None}]}
    box.add_rect({"scroll"}, "scroll_up"  , [0,  0], ["auto", 200], [(0, -scroll_distance)], settings)
    box.add_rect({"scroll"}, "scroll_down", [0, -1], ["auto", 350], [(0,  scroll_distance)], settings)
    box.show()
    ctrl.cursor_visible(False)


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
    
    reward_hover = {"hover_duration": "500ms"}
    box.add_rect({"done"    }, "done" , (820, 830), (280, 80 ), [0, {"combat"}], reward_hover)
    box.add_rect({"level_up"}, "items", (660, 268), (600, 690), [0, {"combat"}], reward_hover)

    box.show()




### GAMES
anki()
#website_scroll(100) #ao3
#dpad()
#inverted_fate()
#mangadex()
#website_scroll(300) #pinterest
#simple_move()
#slay_the_spire()
#vampire_survivors()


mouse_pos = ctrl.mouse_pos()
print(f"Mouse position on monitor one: x: {mouse_pos[0]       }, y: {mouse_pos[1]}")
print(f"Mouse position on monitor two: x: {mouse_pos[0] - 1920}, y: {mouse_pos[1]}")

