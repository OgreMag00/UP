import customtkinter as ctk
import main_page


def back(frame, master) -> None:
    frame.destroy()
    main_page.mainpage(master=master)
    
def textbookpage(master):
    frame = ctk.CTkFrame(master=master, fg_color='transparent')
    frame.grid(row=0, column=0)
        
    back_but = ctk.CTkButton(master=frame, text='back', command= lambda: back(frame, master), font=('Arial', 10))
    back_but.grid(row=0, column=0)
    
    