from hooman import Hooman   # import hooman


# create the hooman api (hapi)
# set the window size to 500 pixels wide and 500 pixels tall
hapi = Hooman(500, 500)


# loop while the window is open
while hapi.is_running:

    # this is the game loop
    # everything in here occurs once every frame

    #set the background to white, this should always be the first thing you draw to the screen
    hapi.background(hapi.color['white'])


    # get any new events like a mouse click or a key press, this handles the events
    # and should only be called once every frame
    hapi.event_loop()

    # update the screen with everything you have drawn
    # this should only be called once every frame
    hapi.flip_display()
