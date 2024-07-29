import customtkinter as ctk
import main_page
import config

ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('logica')
        self.geometry(f'{700}x{700}')
        main_page.mainpage(self)



if __name__ == '__main__':
    app = App()
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(10, weight=1)


    app.mainloop()


# class App(ctk.CTk):
#     def __init__(self):
#         super().__init__()
        
#         self.screen_width = self.winfo_screenwidth()
#         self.screen_heigth = self.winfo_screenheight()
        
#         self.geometry(f'{self.screen_width}x{self.screen_heigth}')
#         self.resizable(True, True)
#         self.title('logica')
        
#         self.main_frame = ctk.CTkFrame(master=self, fg_color='transparent')
#         self.main_frame.grid(row=0, column=0, padx=int(self.screen_width)//2-70, sticky='nsew')
        
        
        
#         self.logo = ctk.CTkLabel(master=self.main_frame, text='menu', width=200, font=('Arial', 120))
#         self.logo.grid(row=0, column=0)
        
#         self.but_textbook = ctk.CTkButton(master=self.main_frame, text='textbook', command=self.textbook, font=('Arial', 70))
#         self.but_textbook.grid(row=1, column=0, pady=20)
        
#         self.but_test = ctk.CTkButton(master=self.main_frame, text='test', command=self.test, font=('Arial', 70))
#         self.but_test.grid(row=2, column=0, pady=10)
        

#     def textbook(self):
#         pass
    
#     def test(self):
#         print('fkfk')
        
        
# if __name__ == '__main__':
#     app = App()
#     app.mainloop()
