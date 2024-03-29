from random import choice
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root=customtkinter.CTk()
root.geometry("600x400")

def roll_dice():

    choose=[1,2,3,4,5,6]
    dice=choice(choose)
    dice2=choice(choose)
    dice_cpu=choice(choose)
    dice_cpu1=choice(choose)
    total_player=dice+dice2
    total_cpu=dice_cpu+dice_cpu1
    label2.configure(text=f"First dice rolls: {dice}\nSecond dice rolls: {dice2}\nTotal: {total_player}")
    label3.configure(text=f"First CPU dice rolls: {dice_cpu1}\nSecond CPU dice rolls: {dice_cpu1}\n Total: {total_cpu}")

    if total_cpu==total_player:
        label4.configure(text=f"Tie!")
    elif total_cpu>total_player:
        label4.configure(text=f"Winner: CPU!")
    else:
        label4.configure(text=f"Winner: Player!")
frame= customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both",expand=True)
label= customtkinter.CTkLabel(master=frame,text="Dice roll system")
label.pack(pady=12,padx=10)
button= customtkinter.CTkButton(master=frame,text="Roll",command=roll_dice,)
button.pack(pady=10,padx=10)
label2=customtkinter.CTkLabel(master=frame,text="")
label2.pack(pady=12,padx=10)
label3=customtkinter.CTkLabel(master=frame,text="")
label3.pack(pady=12,padx=10)
label4=customtkinter.CTkLabel(master=frame,text="Please PRESS ROLL")
label4.pack(pady=12,padx=10)

root.mainloop()
