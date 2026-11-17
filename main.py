import tkinter as tk
from tkinter import ttk



teal="#429494"
darkgrey = "#414444"
lightgrey="#E6E3DD"
white = "#FFFFFF"

window = tk.Tk()
window.configure(bg=lightgrey)
window.title('Demo');
window.geometry('650x400')
notebook = ttk.Notebook(window);
notebook.pack(expand="True", fill='both')

style = ttk.Style()
style.configure("nextButton.TButton", foreground=white,font=("OCR A Extended", 14, "bold"),background=teal,focuscolor="")
style.theme_use('alt')
style.configure("Title.TLabel", foreground=teal, font=("System", 36, "bold"),background=lightgrey)
style.configure("subtitle.TLabel", foreground=darkgrey,background=lightgrey,font = ('OCR A Extended', 16, "bold"))
style.configure("smallText.TLabel", foreground = darkgrey, background = lightgrey, font = ('OCR A Extended', 12))
style.configure("smallBold.TLabel", foreground = teal, background = lightgrey, font = ('OCR A Extended', 11, "bold"))

style.configure("TEntry", foreground = darkgrey, background = white, font = ('OCR A Extended', 12))

style.configure("TFrame",background=lightgrey)

#HOME BELOW----------------------------------------------------------------------------------------|
home_page = ttk.Frame(notebook, style="TFrame")
home_page.rowconfigure(0, weight=1)
home_page.columnconfigure(0, weight=1)

center_frame = ttk.Frame(home_page)
center_frame.grid(row=0, column=0)

title_label = ttk.Label(center_frame, text = 'LakeMUN Parli Pro Wizard', style="Title.TLabel")
subtitle_label = ttk.Label(center_frame, text = 'Happy Chairing!', style="subtitle.TLabel")


title_label.pack(fill='none')
subtitle_label.pack(fill="none")

# input field
input_frame = ttk.Frame(center_frame, style="Custom.TFrame")

input_frame.pack(pady=5)


notebook.add(home_page, text="Home")
#HOME ABOVE_____________________________________________________________________________________________|


#MOTIONS PAGE BELOW ------------------------------------------|


motion_page = ttk.Frame(notebook, style = "TFrame")
motion_page.rowconfigure(0,weight=1)
motion_page.columnconfigure(0,weight=1)
motion_page.columnconfigure(1,weight=1)
motion_page.columnconfigure(2,weight=2)


motion_title = ttk.Label(master = motion_page, text = "Motions", style = "Title.TLabel",justify='center',anchor="n")
motion_title.grid(column=1)
motion_title.pack()

motion_output = ttk.Frame(motion_page, style = "TFrame")
motion_output.pack(side='right')
all_motions = text_box = tk.Text(motion_output, width=35, height=90, wrap="word")
all_motions.pack(side='top',padx=10, pady=10)


motion_input = ttk.Frame(motion_page, style = "TFrame")
motion_input.pack(side='left',padx=10)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MODS
mod_input = ttk.Frame(motion_input, style="TFrame")
mod_input.pack(fill='x', side='top',pady=8)
mod_label = ttk.Label(master=mod_input, text="moderated caucus—", style = "smallText.TLabel", justify='left')
mod_label.pack(side='left')
mod_total_enter = ttk.Entry(master=mod_input, style = "TEntry", width=3)
mod_total_enter.pack(side=tk.LEFT)
semicolon = ttk.Label(master=mod_input, text=":", style = "smallText.TLabel", justify='left')
semicolon.pack(side=tk.LEFT)
mod_speaking_enter = ttk.Entry(master=mod_input, style = "TEntry", width=3)
mod_speaking_enter.pack(side=tk.LEFT)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ EXTENSIONS
ext_input = ttk.Frame(motion_input, style = "TFrame")
ext_input.pack(fill='x',side = 'top', pady=8)
ext_label = ttk.Label(ext_input, text="extension—", style = "smallText.TLabel", justify="left")
ext_label.pack(side='left')
ext_total_enter = ttk.Entry(master=ext_input, style = "TEntry", width=3)
ext_total_enter.pack(side=tk.LEFT)
semicolon2 = ttk.Label(master=ext_input, text=":", style = "smallText.TLabel", justify='left')
semicolon2.pack(side=tk.LEFT)
ext_speaking_enter = ttk.Entry(master=ext_input, style = "TEntry", width=3)
ext_speaking_enter.pack(side=tk.LEFT)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ UNMODS 
unmod_input = ttk.Frame(motion_input, style = "TFrame")
unmod_input.pack(fill='x',side='top',pady=8)
unmod_label = ttk.Label(master = unmod_input, text="unmoderated caucus—", style = "smallText.TLabel", justify='left')
unmod_label.pack(side='left')
unmod_total_enter = ttk.Entry(master=unmod_input, style = "TEntry", width=3)
unmod_total_enter.pack(side=tk.LEFT)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GENTS UNMODS
gents_input = ttk.Frame(motion_input, style = "TFrame")
gents_input.pack(fill='x',side='top',pady=8)
gents_label = ttk.Label(master = gents_input, text="gentleman's unmod—", style = "smallText.TLabel", justify='left')
gents_label.pack(side='left')
gents_total_enter = ttk.Entry(master=gents_input, style = "TEntry", width=3)
gents_total_enter.pack(side=tk.LEFT)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SPEAKERS LIST
speakers_input = ttk.Frame(motion_input, style = "TFrame")
speakers_input.pack(fill='x', side = 'top', pady=8)
speakers_label = ttk.Label(master = speakers_input, text = "speaker's list—", style = "smallText.TLabel", justify = 'left')
speakers_label.pack(side='left')
speakers_st_enter = ttk.Entry(master = speakers_input, style = "TEntry", width = 2)
speakers_st_enter.pack(side='left')
speakers_questions = ttk.Label(master = speakers_input, text="Qs:", style = "smallText.TLabel", justify='left')
speakers_questions.pack(side='left', padx=2)
speakers_q_enter = ttk.Entry(speakers_input, style = "TEntry", width=2)
speakers_q_enter.pack(side='left')
speakers_follows = ttk.Label(speakers_input, text="Fs:", style="smallText.TLabel", justify='left')
speakers_follows.pack(side='left', padx = 2)
speakers_f_enter = ttk.Entry(speakers_input, style = "TEntry", width=2)
speakers_f_enter.pack(side='left')
#-----------------------------------------------------------------------------------------------------------------------------
proposer = ttk.Frame(motion_input, style = 'TFrame')
proposer.pack(fill='x', side = 'top', pady=15)
proposer_label = ttk.Label(proposer, text="proposing delegation:", style="smallBold.TLabel", justify='left')
proposer_label.pack(fill='x',side='top')
proposer_ent = ttk.Entry(proposer, style = "TEntry", width=3)
proposer_ent.pack(fill='x',side='top')

motions = []
# def enter_motion():
#     motion=[]
#     motion.append(proposer_ent.get())
#     if (speakers_st_enter.get()!=""):
#         motion.append(speakers_st_enter.get())
#         motion.append(speakers_q_enter.get())
#         motion.append(speakers_f_enter.get())
#     if (gents_total_enter.get()!=""):
#         motion.append(gents_total_enter.get())
#     print(motion)
#     motions.append(motion)

motion_enter_button = ttk.Button(motion_input, style = 'nextButton.TButton', text="Enter Motion", width = 20
                                 #command = enter_motion()
                                 )
motion_enter_button.pack()



notebook.add(motion_page, text="Motions")

window.mainloop()
