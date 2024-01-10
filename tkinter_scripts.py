from tkinter import Tk, ttk, Listbox
class App():
    def __init__(self):
        self.window = Tk()
        self.window.geometry("500x500")
        self.keysym_ = ''
        self.keysym_counter = 0
        self.widget_name = ''
        self.listbox_label = ttk.Label(self.window, text='Listbox Label')
        self.listbox_label.grid(row=0, column=0, padx=10, pady=10)
        self.data_list = Listbox(self.window, height=1, exportselection=0, font=('Times', 12))
        self.data_list.grid(row=0, column=1, padx=10, pady=10)
        self.data_list.bind('<KeyPress>', self.select_keysym_value)
        self.data_list.insert(0, 'Islamabad')
        self.data_list.insert(1, 'New York')
        self.data_list.insert(2, 'Paris')
        self.data_list.insert(3, 'Beijing')
        self.data_list.insert(4, 'Moscow')
        self.data_list.insert(5, 'London')
        self.data_list.insert(6, 'Madrid')
        self.data_list.insert(7, 'Riadh')
        self.data_list.insert(8, 'New Dehli')
        self.data_list.insert(9, 'Moroni')
        self.data_list.insert(10, 'Brussels')



    def select_keysym_value(self, event):
        start = None
        if self.widget_name == event.widget and self.keysym_ == event.keysym:
            self.keysym_counter += 1
            loop_counter = 0
            for itm in range(event.widget.size()):
                if event.keysym.upper() == event.widget.get(itm)[:1]: 
                    loop_counter += 1
                    if self.keysym_counter == loop_counter:
                        start= itm
            if start == None:
                self.keysym_counter = 1
                start = 0
        else:
            start = 0
            
        self.widget_name = event.widget
        self.keysym_ = event.keysym
        for itm in range(start,event.widget.size()):
            if event.keysym.upper() == event.widget.get(itm)[:1]:
                event.widget.selection_clear(0, 'end')
                event.widget.select_set(itm)
                event.widget.see(itm)
                event.widget.activate(itm)
                break
if __name__ == '__main__':
    app_obj = App()
    app_obj.window.mainloop()