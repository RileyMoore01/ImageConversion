TimeDelaySubImage = PhotoImage(file='GUI/subtract.gif')
TimeDelaySubImage = TimeDelaySubImage.subsample(2, 2)

timeDelayLabel = Label(image=TimeDelaySubImage)
timeDelayLabel.config(font=('Helvatical bold', 5), bg='white')

button5 = Button(win, image=TimeDelaySubImage,command= TimeDelaySub, borderwidth=0
    , height=BUTTON_HEIGHT, width=BUTTON_WIDTH, bg='white')
button5.place(x=400, y=200)