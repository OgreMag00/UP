import customtkinter as ctk
import main_page
import json
import config
import random


with open('test.json', 'r', encoding='utf-8') as fh:
        data = json.load(fh)   



def check_result(pos, ans, i):
    if pos ==ans:
        data[i]['result'] += 1

    
def final_page(frame, i, master):
    a = len(data[i]['questions'])
    b = data[i]['result']
    frame.destroy()
    fram = ctk.CTkFrame(master=master, fg_color='transparent')
    fram.grid(row=0, column=0)
    logo = ctk.CTkLabel(master=fram, text=f'result: {b}/{a}', font=('Arial', 70))
    logo.grid()
    back_but = ctk.CTkButton(master=fram, text='back', command= lambda: back(fram, master, i), font=('Arial', 70), fg_color=config.button_color)
    back_but.grid(row=10, column=0, sticky="s")
    
def next_page(frame, master, i , page):
    frame.destroy()
    if page == len(data[i]['questions']):
        final_page(frame=frame, master=master, i=i)

    else:    
        test(master=master,fram=frame, i=i, page=page)

def test(fram, master, i, page) -> None:
    
    variables = list(data[i]['questions'][page])
    variables.remove('description')
    random.shuffle(variables)
    ans = variables.index("answer")
    
    frame = ctk.CTkFrame(master=master, fg_color='transparent', width=700, height=700)
    frame.grid(row=0, column=0)
    logo = ctk.CTkLabel(master=frame, text=f'#{page+1}', font=('Arial', 40))
    logo.grid(row=0, column=0, sticky="sw")
    
    back_but = ctk.CTkButton(master=frame, text='back', command= lambda: back(frame, master, i), font=('Arial', 40), fg_color=config.button_color)
    back_but.grid(row=10, column=0,pady=10, stick="esw")
    
    quest = ctk.CTkLabel(master=frame, text=data[i]['questions'][page]['description'], font=('Arial', 55))
    quest.grid(row=1, column=0, sticky="ew")
    
    ch_boxes = [
        ctk.CTkCheckBox(master=frame,fg_color=config.button_color_up, text=data[i]['questions'][page][variables[0]], command=lambda: check_result(pos=0, ans=ans, i=i), font=('Arial', 55)).grid(row=3, column=0, pady=10, sticky="w"),
        ctk.CTkCheckBox(master=frame,fg_color=config.button_color_up, text=data[i]['questions'][page][variables[1]], command=lambda: check_result(pos=1, ans=ans, i=i), font=('Arial', 55)).grid(row=4, column=0, pady=10, sticky="w"),
        ctk.CTkCheckBox(master=frame,fg_color=config.button_color_up, text=data[i]['questions'][page][variables[2]], command=lambda: check_result(pos=2, ans=ans, i=i), font=('Arial', 55)).grid(row=5, column=0, pady=10, sticky="w"),
        ctk.CTkCheckBox(master=frame,fg_color=config.button_color_up, text=data[i]['questions'][page][variables[3]], command=lambda: check_result(pos=3, ans=ans, i=i), font=('Arial', 55)).grid(row=6, column=0, pady=10, sticky="w")      
    ]
    
    

    
    # ch1 = ctk.CTkCheckBox(master=frame, text=data[i]['questions'][page][variables[0]])
    # ch1.grid(row=3, column=0)
    
    # ch2 = ctk.CTkCheckBox(master=frame, text=data[i]['questions'][page][variables[1]])
    # ch2.grid(row=3, column=1)
    
    # ch3 = ctk.CTkCheckBox(master=frame, text=data[i]['questions'][page][variables[2]])
    # ch3.grid(row=3, column=2)
    
    # ch4 = ctk.CTkCheckBox(master=frame, text=data[i]['questions'][page][variables[3]])
    # ch4.grid(row=3, column=3)
    
   
    
    # ans = ctk.CTkEntry(master=frame, placeholder_text='your answer', font=('Arial', 70))
    # ans.grid(row=3, column=0, pady=10)
    
    # ans_but = ctk.CTkButton(master=frame, text='send', command= lambda: check_result(ans.get(), data[i]['questions'][page]['answer'], i), font=('Arial', 70))
    
    # ans_but.grid(row=3, column=2, pady=10)
    
    next_but = ctk.CTkButton(master=frame, text='next', command= lambda: next_page(frame, master,i , page+1), font=('Arial', 40), fg_color=config.button_color)
    next_but.grid(row=7, column=0, pady=10, sticky="ew")
    

def back(frame, master, i) -> None:
    frame.destroy()
    main_page.mainpage(master=master)
    data[i]['result'] = 0

    

def testpage(master):
    frame = ctk.CTkFrame(master=master, fg_color='transparent')
    frame.grid(row=0, column=0)
        
    back_but = ctk.CTkButton(master=frame, text='back', command= lambda: back(frame, master, i='test1'), font=('Arial', 70), fg_color=config.button_color)
    back_but.grid(row=10, column=0, sticky="s")

    logo = ctk.CTkLabel(master=frame, text='tests:', font=('Arial', 70))
    logo.grid(row=1, column=0, pady=10)
    
    test_but = ctk.CTkButton(master=frame, text=data['test1']['title'], command= lambda: next_page(frame, master, i='test1', page=0), font=('Arial', 70), fg_color=config.button_color)
    test_but.grid(row=2, column=0, pady=20)
    
    
    
        