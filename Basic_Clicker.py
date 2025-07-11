import tkinter as tk


class Clicker:
    def __init__(self,parent):
        self.parent = parent
        self.clicks = 0
        self.increment = 1

        self.parent.geometry("600x400")
        self.parent.title("Basic Clicker Game")

        self.label = tk.Label(parent, text=f"Clicks: {self.clicks}")
        self.label.pack()



        button = tk.Button(self.parent, text="Basic Clicker", command=self.click)
        button.pack()

        upgrades_frame = tk.Frame(self.parent)
        upgrades_frame.pack()
        upgrade_button1 = tk.Button(upgrades_frame, text="Upgrade Clicks +1 Cost: 100 Clicks", command=self.upgrade_clicks1)
        upgrade_button1.pack(side="left")
        upgrade_button2 = tk.Button(upgrades_frame, text="Upgrade Clicks +10 Cost: 1000 Clicks", command=self.upgrade_clicks2)
        upgrade_button2.pack(side="right")

    def upgrade_clicks1(self):
        if self.clicks >= 100:
            self.clicks -= 100
            self.increment += 1
            buttons_bought = 0
            buttons_bought += 1
            self.label.config(text=f"Clicks: {self.clicks}")
            self.upgrade_button1.config(text=f"Upgrade Clicks +1 Cost: {100 * (buttons_bought)} Clicks")
        else:
            self.label.config(text="Not enough clicks to upgrade!")
    
    def upgrade_clicks2(self):
        if self.clicks >= 1000:
            self.clicks -= 1000
            self.increment += 10
            buttons_bought = 0
            buttons_bought += 1
            self.label.config(text=f"Clicks: {self.clicks}")
            self.upgrade_button2.config(text=f"Upgrade Clicks +10 Cost: {1000 * (buttons_bought)} Clicks")
        else:
            self.label.config(text="Not enough clicks to upgrade!")
            

    def click(self):
        self.clicks += self.increment
        
        self.label.config(text=f"Clicks: {self.clicks}")
    
    def start(self):
        self.parent.mainloop()

    
    


def main():
    parent = tk.Tk()
    clicker = Clicker(parent)
    clicker.start()

if __name__ == "__main__":
    main()