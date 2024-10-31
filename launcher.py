from .dwell_clicker import DwellClick
from talon import ctrl, ui


# Should reset my cursor each time I save so I don't have to restart talon




def inverted_fate():
    box = DwellClick({"comic"})
    settings = {"hover_duration": "500ms", "text_textsize": 30}
    
    box.add_rect({"comic"}, "back", (0, 0), (520, 1080), ["left"], {**settings, "text": "left"})
    box.add_rect({"comic"}, "next_right ", (1400, 0), (520, 1080), ["right"], {**settings, "text": "right"})
    box.add_rect({"comic"}, "next_bottom", (620, 810), (680, 260), ["right"], {**settings, "text": "right"})
    box.show()

def mangadex():
    box = DwellClick({"comic"})
    settings = {"hover_duration": "500ms", "text_textsize": 30}
    
    box.add_rect({"comic"}, "back", (0, 0), (520, 1080), ["left"], {**settings, "text": "left"})
    box.add_rect({"comic"}, "next_right ", (1400, 0), (520, 1080), ["right"], {**settings, "text": "right"})
    box.show()

def website_scroll(scroll_distance):
    box = DwellClick({"scroll"})
    settings = {"continual_clicking":True, "rect":[{"color": None}]}
    box.add_rect({"scroll"}, "scroll_up"  , (0, 0         ), (1920, 200), [(0, -scroll_distance)], settings)
    box.add_rect({"scroll"}, "scroll_down", (0, 1080 - 350), (1920, 350), [(0,  scroll_distance)], settings)
    box.show()
    ctrl.cursor_visible(False)

def slay_the_spire():
        
        box = DwellClick({"combat"})

        slow = {"hover_duration": "500ms"}
        click = {"continual_clicking": True}
        slow_click = {**slow, **click}
        
        box.add_rect({"combat"                  }, "end_turn"       , (1550, 830), (170, 80 ), ["e"                            ], {"hover_duration":"750ms"})
        box.add_rect({"combat"                  }, "draw_pile"      , (30  , 960), (100, 100), ["a"     , {"return"           }])
        box.add_rect({"combat"                  }, "discard_pile"   , (1790, 960), (100, 100), ["s"     , {"return"           }])
        box.add_rect({"combat"                  }, "map"            , (1700, 5  ), (60 , 55 ), ["m"     , {"return"           }])
        box.add_rect({"combat"                  }, "deck"           , (1775, 10 ), (60 , 50 ), ["d"     , {"return"           }])
        box.add_rect({"combat"                  }, "settings"       , (1850, 10 ), (55 , 50 ), ["escape", {"return", "restart"}])
        box.add_rect({"return"                  }, "return"         , (0   , 860), (250, 70 ), [0       , {"combat"           }])
        box.add_rect({"restart"                 }, "restart"        , (0   , 733), (250, 70 ), [0       , {"combat"           }], {**slow                  })
        box.add_rect({"combat"                  }, "potions"        , (580 , 10 ), (160, 50 ), [0       , {"potion_select"    }], {**slow_click            })
        box.add_rect({"potion_select"           }, "potion_select"  , (450 , 140), (310, 110), [0       , {"combat"           }], {**slow_click            })
        box.add_rect({"enemies", "potion_select"}, "enemies"        , (950 , 400), (790, 350), [0       , {"combat"           }], {**slow                  })
        box.add_rect({"combat"                  }, "exhausted_cards", (1820, 865), (60 , 60 ), ["x"     , {"return"           }])
        #box.add_rect(None, "back", (800, 800), (100, 100), [box.history_back], {"text": "Back"})
        
        #box.add_rect({"proceed"}, "proceed"        , 1600, 730, 140, 70 , 0   , None, None, 1000)

        for i, card in enumerate([*range(1, 10), 0]):
            # slay the spire goes from 1-9, 0 so I need to reflect that
            box.add_rect({"combat", "enemies"}, f"card_{card}", (1200 - i*120, 150), (100, 100), [f"{card}", {"enemies"}], {"text": f"{card}"})

        box.show()

def vampire_survivors():
    box = DwellClick({"combat"})

    def move_center():
        rect = ui.active_window().rect
        ctrl.mouse_move(1920 + (rect.width / 2), rect.top + (rect.height / 2) - 30)
        ctrl.mouse_click(button=0, down=True)

    height = 100
    spacing = height * 1.5
    size = (height, height)


    box.add_rect({"combat"}, "reset_cursor ", (1790, 960              ), size, [move_center ], {"text": "Go Center"    })
    box.add_rect({"combat"}, "stop_drag    ", (1790, 960 - spacing    ), size, [0           ], {"text": "Stop Dragging"})
    box.add_rect({"combat"}, "level_up     ", (1790, 960 - spacing * 2), size, [{"level_up"}], {"text": "Level Up"},)
    box.add_rect({"combat"}, "reward_accept", (1790, 960 - spacing * 3), size, [{"done"}    ], {"text": "Accept Reward"})
    
    reward_hover = {"hover_duration": "500ms"}
    box.add_rect({"done"    }, "done ", (820, 830), (280, 80 ), [0, {"combat"}], reward_hover)
    box.add_rect({"level_up"}, "items", (660, 268), (600, 690), [0, {"combat"}], reward_hover)

    box.show()




### GAMES
#website_scroll(50) #ao3
#inverted_fate()
#mangadex()
#website_scroll(300) #pinterest
#slay_the_spire()
vampire_survivors()


mouse_pos = ctrl.mouse_pos()
print(f"Mouse position on monitor one: x: {mouse_pos[0]       }, y: {mouse_pos[1]}")
print(f"Mouse position on monitor two: x: {mouse_pos[0] - 1920}, y: {mouse_pos[1]}")

