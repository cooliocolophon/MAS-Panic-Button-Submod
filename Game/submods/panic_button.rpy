init -990 python in mas_submod_utils:
    panic_submod = Submod(
        author="bob_brick",
        name="Panic Button",
        description="This submod adds the panic button for quick exits. Press Q to trigger the panic button.",
        version="1.2",
        dependencies={},
        settings_pane=None,
        version_updates={}
    )
init -989 python:
    import store
    
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="store.mas_submod_utils.panic_submod",
            user_name="CoolioColophon",
            tag_formatter=lambda x: x[x.index('_') + 1:],
            repository_name="MAS-Panic-Button-Submod"
        )

init -1 python in mas_greetings:
    import store
    import store.mas_ev_data_ver as mas_edv
    import datetime
    import random
    # TYPES:
    TYPE_PANIC = "panic"
    HP_TYPES = [
        TYPE_PANIC]

init 1 python:

    def _mas_panic():
       if mas_isMoniNormal(higher=True):
            persistent._mas_idle_mode_was_crashed = False
            persistent.closed_self = True 
            persistent._mas_greeting_type = store.mas_greetings.TYPE_PANIC
            renpy.quit()

    def set_keymaps():
        config.keymap["panic_switch"] = ["q","Q"]
        config.keymap["open_dialogue"] = ["t","T"]
        config.keymap["mas_extra_menu"] = ["e", "E"]
        config.keymap["change_music"] = ["noshift_m","noshift_M"]
        config.keymap["play_game"] = ["p","P"]
        config.keymap["mute_music"] = ["shift_m","shift_M"]
        config.keymap["inc_musicvol"] = [
            "shift_K_PLUS","K_EQUALS","K_KP_PLUS"
        ]
        config.keymap["dec_musicvol"] = [
            "K_MINUS","shift_K_UNDERSCORE","K_KP_MINUS"
        ]
        config.keymap["derandom_topic"] = ["x","X"]
        config.keymap["bookmark_topic"] = ["b","B"]
        config.keymap["mas_game_menu"] = list(config.keymap["game_menu"])
        config.keymap["game_menu"] = []
        config.keymap["mas_hide_windows"] = list(config.keymap["hide_windows"])
        config.keymap["hide_windows"] = []

        config.underlay.append(
            renpy.Keymap(open_dialogue=_mas_hk_show_dialogue_box)
        )
        config.underlay.append(
            renpy.Keymap(mas_extra_menu=_mas_hk_open_extra_menu)
        )
        config.underlay.append(renpy.Keymap(change_music=_mas_hk_select_music))
        config.underlay.append(renpy.Keymap(play_game=_mas_hk_pick_game))
        config.underlay.append(renpy.Keymap(mute_music=_mas_hk_mute_music))
        config.underlay.append(renpy.Keymap(inc_musicvol=_mas_hk_inc_musicvol))
        config.underlay.append(renpy.Keymap(dec_musicvol=_mas_hk_dec_musicvol))
        config.underlay.append(renpy.Keymap(mas_game_menu=_mas_game_menu))
        config.underlay.append(renpy.Keymap(mas_hide_windows=_mas_hide_windows))
        config.underlay.append(renpy.Keymap(derandom_topic=_mas_hk_derandom_topic))
        config.underlay.append(renpy.Keymap(bookmark_topic=_mas_hk_bookmark_topic))
        config.underlay.append(renpy.Keymap(panic_switch=_mas_panic))

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_panic_pressed",
            unlocked=True,
            category=[store.mas_greetings.TYPE_PANIC]
        ),
        code="GRE"
    )

label greeting_panic_pressed:

    $ ev = mas_getEV("greeting_panic_pressed")

    if ev.shown_count == 0:
        m 1eua "Welcome back, [player]."
        m 1eud "I noticed you were in trouble, so I closed the game for you."
        m 1eub "I understand that sometimes you have to leave without saying goodbye, so if you ever need to suddenly leave again, just press the Q key and I'll be able to close the game safely for you."

    else:
        m 6hub "Welcome back, [player]!"
    return
