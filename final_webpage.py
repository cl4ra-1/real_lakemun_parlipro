







###command functions


###ALL PAGES
#motionpage = ttk.Frame(master = window, style = "Custom.TFrame")




# style.configure("nextButton.TButton", foreground=darkgrey,font=("OCR A Extended", 14, "bold"),background=lightgrey,focuscolor="")
# style.configure("Title.TLabel", foreground=teal, font=("System", 36, "bold"),background=lightgrey)
# style.configure("subtitle.TLabel", foreground=darkgrey,background=lightgrey,font = ('OCR A Extended', 16, "bold"))
# style.configure("Custom.TFrame",background=lightgrey)

###HOMEPAGE---------------------------------------------------------------------------------------------
#title
# title_label = ttk.Label(master = homepage, text = 'LakeMUN Parli Pro Wizard', style="Title.TLabel")
# subtitle_label = ttk.Label(master = homepage, text = 'Happy Chairing!', style="subtitle.TLabel")


# title_label.pack(fill='none')
# subtitle_label.pack(fill="none")


# # input field
# input_frame = ttk.Frame(master = homepage)
# ###entry = ttk.Entry(master = input_frame, justify='center', font = ('OCR A Extended', 12))



# continuebutton = ttk.Button(master = input_frame,
#                     text = 'Open Session ->', 
#                     style = "nextButton.TButton",
#                     width = 15,
#                     command=nextButtonPress(homepage,motionpage))
# ###entry.pack(side = 'left', padx=10)
# continuebutton.pack(side = 'top')
# input_frame.pack(pady=5)
import tkinter as tk
from tkinter import ttk

teal="#429494"
darkgrey = "#414444"
lightgrey="#E6E3DD"
white = "#FFFFFF"


class Page(ttk.Frame):
    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()
    def switchPage(nextPage):
        nextPage.lift()

class homePage(Page):
    def __init__(self, parent, motion_page, *args, **kwargs):
        Page.__init__(self, parent, *args, **kwargs)

        style = ttk.Style(self)
        style.configure("TFrame",background=lightgrey)
        style.configure("nextButton.TButton", foreground=darkgrey,font=("OCR A Extended", 14, "bold"),background=lightgrey,focuscolor="")
        style.configure("Title.TLabel", foreground=teal, font=("System", 36, "bold"),background=lightgrey)
        style.configure("subtitle.TLabel", foreground=darkgrey,background=lightgrey,font = ('OCR A Extended', 16, "bold"))
        


        title_label = ttk.Label(master = self, text = 'LakeMUN Parli Pro Wizard', style="Title.TLabel")
        subtitle_label = ttk.Label(master = self, text = 'Happy Chairing!', style="subtitle.TLabel")


        title_label.pack(fill='none')
        subtitle_label.pack(fill="none")

        # input field
        input_frame = ttk.Frame(master=self, style="Custom.TFrame")
        continuebutton = ttk.Button(master = input_frame,
                            text = 'Open Session ->', 
                            style = "nextButton.TButton",
                            width = 15,
                            command=motion_page.show)
        
        continuebutton.pack(side = 'top')
        input_frame.pack(pady=5)

class motionPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        style = ttk.Style(self)
        style.configure("TFrame",background=lightgrey)
        style.configure("nextButton.TButton", foreground=darkgrey,font=("OCR A Extended", 14, "bold"),background=lightgrey,focuscolor="")
        style.configure("Title.TLabel", foreground=teal, font=("System", 36, "bold"),background=lightgrey)
        style.configure("subtitle.TLabel", foreground=darkgrey,background=lightgrey,font = ('OCR A Extended', 16, "bold"))

        motion_title = ttk.Label(master = self, text = "hi lol (will it work)", style = "Title.TLabel")
        motion_title.pack(fill="none")

class mainView(ttk.Frame):
    def __init__(self, *args, **kwargs):
        ttk.Frame.__init__(self, *args, **kwargs)

        motion = motionPage(self)
        home = homePage(self, motion)

        for page in (motion, home):
            page.place(x=0, y=150, relwidth=1, relheight=1)

        home.show()

#window
if __name__ == "__main__":
    window = tk.Tk()
    window.configure(bg=lightgrey)
    #window.title('Demo');
    window.geometry('650x450')  
    main = mainView(window)
    main.pack(expand=True, fill="both")
    window.mainloop()
#MOTIONPAGE------------------------------------------------------------------------------------------------------


    
# run
