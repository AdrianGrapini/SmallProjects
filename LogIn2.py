import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

student_info = [['James M.', '8'], ['Wiliam G.', '9'], ['Sandra B.', '10'], ['Elena L.', '10']]

frame_styles = {'relief': 'raised',
                'bd': 4, 'bg': '#49A',
                'fg': 'black', 'font': ('Arial', 10, 'bold')}

class LoginPage(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg='white', height=500, width=600)
        main_frame.pack(fill='both', expand='True')

        self.geometry('600x600')
        self.resizable(True, True)
        title_styles = {'font': ("Trebuchet MS Bold", 16), "background": "blue"}
        
        text_styles = {'font': ('Arial', 16), 'background': 'blue', 'foreground': '#E1FFFF'}

        frame_login = tk.Frame(main_frame, bg='white', relief='groove', bd=4)
        frame_login.place(rely=0.30, relx=0.17, height=200, width=500)

        label_title = tk.Label(frame_login, title_styles, text='Login Page')
        label_title.grid(row=0, column=1, columnspan=2)

        label_user = tk.Label(frame_login, text_styles, text='Username:')
        label_user.grid(row=1, column=0)

        label_pw = tk.Label(frame_login, text_styles, text='Password:')
        label_pw.grid(row=2, column=1)

        entry_user = ttk.Entry(frame_login, text_styles, width=50, cursor='dotbox')
        entry_user.grid(row=1, column=1)

        entry_pw = ttk.Entry(frame_login, text_styles, width=50, cursor='dotbox', show='*')
        entry_pw.grid(row=2, column=1)

        button = ttk.Button(frame_login, text='Login', command=lambda: getlogin())
        button.place(rely=0.70, relx=0.75)

        signup_btn = ttk.Button(frame_login, text='Register', command=lambda: get_signup())
        signup_btn.place(rely=0.70, relx=0.75)

        def get_signup():
            SignupPage()

        def getlogin():
            username = entry_user.get()
            password = entry_pw.get()
            validation = validate(username, password)
            if validation:
                tk.messagebox.showinfo('Login Succesful',
                                        'Welcome {}'.format(username) )
                root.deiconify()
                top.destroy()
            else:
                tk.messagebox.showerror('The username or password you entered are incorect')
        
        def validate(username, password):
            try:
                with open("credentials.txt", "r") as credentials:
                    for line in credentials:
                        line = line.split(",")
                        if line[1] == username and line[3] == password:
                            return True
                    return False
            except FileNotFoundError:
                print("You need to Register first or amend Line 71 to     if True:")
                return False

class SignupPage(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self, bg="#3F6BAA", height=150, width=250)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")

        self.geometry("250x150")
        self.resizable(0, 0)

        self.title("Registration")

        text_styles = {"font": ("Verdana", 10),
                       "background": "#3F6BAA",
                       "foreground": "#E1FFFF"}

        label_user = tk.Label(main_frame, text_styles, text="New Username:")
        label_user.grid(row=1, column=0)

        label_pw = tk.Label(main_frame, text_styles, text="New Password:")
        label_pw.grid(row=2, column=0)

        entry_user = ttk.Entry(main_frame, width=20, cursor="xterm")
        entry_user.grid(row=1, column=1)

        entry_pw = ttk.Entry(main_frame, width=20, cursor="xterm", show="*")
        entry_pw.grid(row=2, column=1)

        button = ttk.Button(main_frame, text="Create Account", command=lambda: signup())
        button.grid(row=4, column=1)

        def signup():
            
            user = entry_user.get()
            pw = entry_pw.get()
            validation = validate_user(user)
            if not validation:
                tk.messagebox.showerror("Information", "That Username already exists")
            else:
                if len(pw) > 3:
                    credentials = open("credentials.txt", "a")
                    credentials.write(f"Username,{user},Password,{pw},\n")
                    credentials.close()
                    tk.messagebox.showinfo("Information", "Your account details have been stored.")
                    SignupPage.destroy(self)

                else:
                    tk.messagebox.showerror("Information", "Your password needs to be longer than 3 values.")

        def validate_user(username):
            # Checks the text file for a username/password combination.
            try:
                with open("credentials.txt", "r") as credentials:
                    for line in credentials:
                        line = line.split(",")
                        if line[1] == username:
                            return False
                return True
            except FileNotFoundError:
                return True

class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        menu_file = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu1", menu=menu_file)
        menu_file.add_command(label="All Widgets", command=lambda: parent.show_frame(Some_Widgets))
        menu_file.add_separator()
        menu_file.add_command(label="Exit Application", command=lambda: parent.Quit_application())

        menu_orders = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu2", menu=menu_orders)

        menu_pricing = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu3", menu=menu_pricing)
        menu_pricing.add_command(label="Page One", command=lambda: parent.show_frame(PageOne))

        menu_operations = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu4", menu=menu_operations)
        menu_operations.add_command(label="Page Two", command=lambda: parent.show_frame(PageTwo))
        menu_positions = tk.Menu(menu_operations, tearoff=0)
        menu_operations.add_cascade(label="Menu5", menu=menu_positions)
        menu_positions.add_command(label="Page Three", command=lambda: parent.show_frame(PageThree))
        menu_positions.add_command(label="Page Four", command=lambda: parent.show_frame(PageFour))

        menu_help = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu6", menu=menu_help)
        menu_help.add_command(label="Open New Window", command=lambda: parent.OpenNewWindow())


class MyApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        main_frame = tk.Frame(self, bg="#84CEEB", height=600, width=1024)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        pages = (Some_Widgets, PageOne, PageTwo, PageThree, PageFour)
        for F in pages:
            frame = F(main_frame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Some_Widgets)
        menubar = MenuBar(self)
        tk.Tk.config(self, menu=menubar)

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def OpenNewWindow(self):
        OpenNewWindow()

    def Quit_application(self):
        self.destroy()


class GUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.main_frame = tk.Frame(self, bg="#BEB2A7", height=600, width=1024)
        # self.main_frame.pack_propagate(0)
        self.main_frame.pack(fill="both", expand="true")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)


class Some_Widgets(GUI):  
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        frame1 = tk.Entry(self, frame_styles, text="This is a LabelFrame containing a Treeview")
        frame1.place(rely=0.05, relx=0.02, height=400, width=400)

        frame2 = tk.Entry(self, frame_styles, text="Some widgets")
        frame2.place(rely=0.05, relx=0.45, height=500, width=500)

        button8 = ttk.Button(self, frame_styles, text='Create', command=lambda: new())

        def new():
            frame3 = frame1.get()
            frame4 = frame2.get()

        # This is a treeview.
        tv1 = ttk.Treeview(frame1)
        column_list_account = ["Name", "Type", "Base Stat Total"]
        tv1['columns'] = column_list_account
        tv1["show"] = "headings"  # removes empty column
        for column in column_list_account:
            tv1.heading(column, text=column)
            tv1.column(column, width=50)
        tv1.place(relheight=1, relwidth=0.995)
        treescroll = tk.Scrollbar(frame1)
        treescroll.configure(command=tv1.yview)
        tv1.configure(yscrollcommand=treescroll.set)
        treescroll.pack(side="right", fill="y")

        def Load_data():
            for row in pokemon_info:
                tv1.insert("", "end", values=row)

        def Refresh_data():
            # Deletes the data in the current treeview and reinserts it.
            tv1.delete(*tv1.get_children())  # *=splat operator
            Load_data()

        Load_data()


class PageOne(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page One")
        label1.pack(side="top")


class PageThree(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page Three")
        label1.pack(side="top")


class PageFour(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page Four")
        label1.pack(side="top")


class PageTwo(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Page Two")
        label1.pack(side="top")


class OpenNewWindow(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        main_frame = tk.Frame(self)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        self.title("Here is the Title of the Window")
        self.geometry("500x500")
        self.resizable(0, 0)

        frame1 = ttk.LabelFrame(main_frame, text="This is a ttk LabelFrame")
        frame1.pack(expand=True, fill="both")

        label1 = tk.Label(frame1, font=("Verdana", 20), text="OpenNewWindow Page")
        label1.pack(side="top")


top = LoginPage()
top.title("Tkinter App Template - Login Page")
root = MyApp()
root.withdraw()
root.title("Tkinter App Template")
root.mainloop()