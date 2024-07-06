AssReqManagement_image = PhotoImage(
    file=relative_to_assets("AssReqManagement.png"))
AssReqManagement = Button(
    image=AssReqManagement_image,
    borderwidth=0,
    highlightthickness=0,
    cursor= "hand2",
    command=lambda: print("AssReqManagement clicked"),
    relief="flat"
)
AssReqManagement.place(
    x=389.0,
    y=400.0,
    width=275.0,
    height=253.0
)