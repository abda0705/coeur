def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.pause(2000)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
basic.forever(on_forever)
