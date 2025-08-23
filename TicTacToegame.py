import tkinter as tk
from tkinter import messagebox

def checker_winner(buttons):
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
                  [0, 3, 6], [1, 4, 7], [2, 5, 8], 
                  [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Winner", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()
                
def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        checker_winner(buttons)  
        toggle_player()  
        
def toggle_player():
    global current_player
    current_player = "X" if current_player == "0" else "0"
    label.config(text=f"Current Player: {current_player}")   
    
root = tk.Tk()
root.title("Tic Tac Toe")

buttons = [tk.Button(root, text="", font=('Arial', 24), width=5, height=2, command=lambda index=i: button_click(index)) for i in range(9)]     

for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3)
    
current_player = "X"
winner = False
label = tk.Label(root, text=f"Current Player: {current_player}", font=('Arial', 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()