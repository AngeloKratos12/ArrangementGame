from time import strftime
from tkinter import *
from tkinter import ttk
import json



root = Tk()

root.title("X-CORPORATE")
# root.geometry("950x500")
root.resizable(width=False, height=False)

font11, font13, font20 = ('Arial', 11, 'bold'), ('Arial', 13, 'bold'), ('Arial', 60, 'bold')

with open('meilleur_score.json', 'r') as myfile:
    register = json.load(myfile)
    meilleur_score = register["meilleur_score"]
    temps = register["temps"]


##TIME FUNCTION (UPDATE TIME!!)
def timeUpdate(i):

    """
        UPDATE TIME!!
    """
    global string

    string = '{:02d}'.format(i)
    time.config(text=string)
    time.after(1000, lambda: timeUpdate(i+1))
    canvas.itemconfigure(time_, text="Time: " + string)
    


##-----------------------------------------##---------------------------------------##
def game_over(score):

    """
        GAME OVER!!!
    """

    for widget in root.winfo_children():
        widget.destroy()

    with open('meilleur_score.json', 'r') as myfile:
        register = json.load(myfile)
        meilleur_score = register["meilleur_score"]

    Label(root, text="GAME OVER!!",  font=font20, foreground="red").pack()
    Label(root, text=f'Votre score:{score}', font=font13, foreground="green").pack()

    if len(all_arrangement) > meilleur_score:

        with open('meilleur_score.json', 'w') as myfile:
            json.dump({"meilleur_score": len(all_arrangement), "temps": int(string)}, myfile)
        
        Label(root, text=f'Nouvel meilleur score: {meilleur_score}', font=font13, foreground="green").pack()
        
    
    else:
        Label(root, text=f'Meilleur score: {meilleur_score}', font=font13, foreground="green").pack()
    
    Button(root, text="Restart", command=main, font=font11).pack()

        


#######################################################################################
all_arrangement = []
one_arrangement = []

def one_color_choice(event):

    global one_arrangement, all_arrangement

    color = event.keysym

    dic_color = {

            "KP_4":"r",
            "KP_5":"b",
            "KP_1":"y",
            "KP_2":"g"

            }
    
    if color in dic_color:

        if len(one_arrangement) != 4:
            if dic_color[color] not in one_arrangement:
                one_arrangement.append(dic_color[color])
                
            else:

                ###GAME OVER###             
                game_over(len(all_arrangement))
                print(int(string))

        else:

            if one_arrangement not in all_arrangement:
                all_arrangement.append(one_arrangement)
                canvas.itemconfigure(score, text="Score: " + str(len(all_arrangement)))
                one_arrangement = []
                one_arrangement.append(dic_color[color])

            else:

                ###GAME OVER###
                game_over(len(all_arrangement))

    else:
        pass
    


    


##---------------------------------------------
def run_game():

    """
        Run the game
    """

    global time, canvas, time_, score


    for widget in root.winfo_children():
        widget.destroy()
    
    
    Label(root, text='H_GAME', font=font13).grid(row=0, column=0, columnspan=2, pady=15)

    Button(root, text="", background="red", width=15, height=10).grid(row=1, column=0)
    Button(root, text="", background="blue", width=15, height=10).grid(row=1, column=1)
    Button(root, text="", background="yellow", width=15, height=10).grid(row=2, column=0)
    Button(root, text="", background="green", width=15, height=10).grid(row=2, column=1)

    canvas = Canvas(root, background='white', height=380, width=250)
    canvas.grid(row=1, column=2, rowspan=2)
    time_ = canvas.create_text(50, 20, text="time: 00", font=("Arial", 18))
    score_ = 0
    score = canvas.create_text(50, 50, text=f"Score: {score_}", font=("Arial", 18))
    ##-------------------------##-----------------------##

    root.bind("<KeyPress>", one_color_choice)
    time = Label(root, font=font13, foreground='green')

    timeUpdate(0)


        

##-----------------------------------##----------------------------------------##
def main():

    """
        main function
    """

    for widget in root.winfo_children():
        widget.destroy()
    
    Label(root, text='WELCOME TO H_GAME', font=font13).grid(row=0, column=1, columnspan=2, pady=15)
    Label(root, text='Number of color:', font=font11).grid(row=1, column=0,pady=10, padx=10)

    nbr_color = ttk.Combobox(root, values=[i for i in range(15)], width=2)
    nbr_color.set(4)
    nbr_color.grid(row=1, column=1)

    Button(root, text="", background="red", width=15, height=10).grid(row=2, column=0, padx=5)
    Button(root, text="", background="blue", width=15, height=10).grid(row=2, column=1, padx=10)
    Button(root, text="", background="yellow", width=15, height=10).grid(row=2, column=2)
    Button(root, text="", background="green", width=15, height=10).grid(row=2, column=3, padx=10)

    Label(root, text=f"Meilleur score: {meilleur_score}   Temps: {temps}s", font=font11, fg="green").grid(row=3, column=0, columnspan=2)
    Button(root, text="start", font=font11, command=run_game).grid(row=3, column=3, pady=10)




if __name__ == '__main__':
    main()
    root.mainloop()