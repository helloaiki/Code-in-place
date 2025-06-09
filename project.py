import tkinter as tk

BOARD_WIDTH=700
BOARD_HEIGHT=700
game_mode_on=False
during_game_identifier=False
symbol_detector="X"
place_holder=1
place_taken_1=[
              [0,0,0],
              [0,0,0],
              [0,0,0]
               ]
place_taken_2=[
              [0,0,0],
              [0,0,0],
              [0,0,0]
               ]
place_taken_combo=[]
game_ended=False

def banner_after_session(canvas,str):
    canvas.create_rectangle(150,150,150+400,150+400,fill="blue", stipple="gray25",outline="light blue")
    if str=="DRAW":
        canvas.create_text(340,350-50,text="DRAW",font=("Comic Sans Ms",40,"bold"),fill="light blue")
    elif str=="X":
        canvas.create_text(340,350-50,text="X WON",font=("Comic Sans Ms",40,"bold"),fill="light blue")
    else:
        canvas.create_text(340,350-50,text="Y WON",font=("Comic Sans Ms",40,"bold"),fill="light blue")
    
    canvas.create_rectangle(195,450,350,500,fill="dark blue",outline="dark blue")
    canvas.create_text(235,475,text="     PLAY",font=("Comic Sans Ms",20,"bold"),fill="light blue")
    canvas.create_rectangle(355,450,510,500,fill="dark blue",outline="dark blue")
    canvas.create_text(405,475,text="   EXIT",font=("Comic Sans Ms",20,"bold"),fill="light blue")


def someone_won(canvas):
    #checks for draw
    
    global place_taken_combo,game_ended
    all_places_taken=True
    for i in range(9):
        if place_taken_combo[i]==0:
            all_places_taken=False
            break
    if all_places_taken:
        #draw logic
        game_ended=True
        canvas.after(500,lambda:banner_after_session(canvas,"DRAW"))
    else:
        #checks for either X or Y winning
        won=False
        if symbol_detector=="X":
            count=0
            for i in range(3):
                for j in range(3):
                    if place_taken_1[i][j]==1:
                        count=count+1
                if count==3:
                    won=True
                    break
                else:
                    count=0
            
            count=0

            for i in range(3):
                for j in range(3):
                    if place_taken_1[j][i]==1:
                        count=count+1
                if count==3:
                    won=True
                    break
                else:
                    count=0
            
            count=0
            for i in range(3):
                if place_taken_1[i][i]==1:
                    count=count+1

            if count==3:
                won=True

            if place_taken_1[0][2]==1 and place_taken_1[1][1]==1 and place_taken_1[2][0]==1:
                won=True
            
            if won:
                game_ended=True
                canvas.after(500,lambda:banner_after_session(canvas,"X"))
        else:
            count=0
            for i in range(3):
                for j in range(3):
                    if place_taken_2[i][j]==1:
                        count=count+1
                if count==3:
                    won=True
                    break
                else:
                    count=0
            
            count=0

            for i in range(3):
                for j in range(3):
                    if place_taken_2[j][i]==1:
                        count=count+1
                if count==3:
                    won=True
                    break
                else:
                    count=0
            
            count=0
            for i in range(3):
                if place_taken_2[i][i]==1:
                    count=count+1

            if count==3:
                won=True

            if place_taken_2[0][2]==1 and place_taken_2[1][1]==1 and place_taken_2[2][0]==1:
                won=True
            
            if won:
                game_ended=True
                canvas.after(500,lambda:banner_after_session(canvas,"Y"))   







def draw_symbol(canvas):
    global symbol_detector
    global place_taken_combo
    global place_taken_1
    global place_taken_2
    coords = {
        1: (200, 350-155),
        2: (350, 350-155),
        3: (500, 350-155),
        4: (200, 505-155),
        5: (350, 505-155),
        6: (500, 505-155),
        7: (200, 650-155),
        8: (350, 650-155),
        9: (500, 650-155),
    }

    x,y=coords[place_holder]
    if place_taken_combo[place_holder-1]==0:
        place_taken_combo[place_holder-1]=1
        if symbol_detector=="X":
            canvas.create_line(x-40,y-40,x+40,y+40,width=10,fill="dark blue")
            canvas.create_line(x-40,y+40,x+40,y-40,width=10,fill="dark blue")
            place_taken_1[(place_holder-1)//3][(place_holder-1)%3]=1
            someone_won(canvas)
            #check for win
        else:
            canvas.create_oval(x-40,y-40,x+40,y+40,width=10,outline="dark blue")
            place_taken_2[(place_holder-1)//3][(place_holder-1)%3]=1
            someone_won(canvas)
            #check for win
        if symbol_detector=="X":
            symbol_detector="O"
        else:
            symbol_detector="X"
        #will finish later

        

    

    
    
    

def during_game(canvas,str):
    global symbol_detector
    global during_game_identifier
    during_game_identifier=True
    
    if str=="X":
        symbol_detector="X"
    else:
        symbol_detector="O"
    
        




def choose_symbol(canvas):
    global game_mode_on
    game_mode_on=True
    canvas.create_rectangle(0,0,BOARD_WIDTH,BOARD_HEIGHT,fill="light blue")
    canvas.create_rectangle(200,250,500,300,fill="dark blue",outline="dark blue")
    canvas.create_text(345,275,text="CHOOSE SYMBOL",font=("Comic Sans Ms",20,"bold"),fill="light blue")
    canvas.create_rectangle(200,320,347,370,fill="dark blue",outline="dark blue")
    canvas.create_text(250,345,text="   X",font=("Comic Sans Ms",20,"bold"),fill="light blue")
    canvas.create_rectangle(353,320,500,370,fill="dark blue",outline="dark blue")
    canvas.create_text(403,345,text="   O",font=("Comic Sans Ms",20,"bold"),fill="light blue")



def draw_board(canvas,str):
    canvas.create_rectangle(0,0,BOARD_WIDTH,BOARD_HEIGHT,fill="light blue")
    canvas.create_text(320,80,text="   ||LET THE FUN BEGIN||",font=("Comic Sans Ms",20,"bold"),fill="dark blue")
    canvas.create_rectangle(125,280,575,290,fill="grey",outline="grey")
    canvas.create_rectangle(125,430,575,440,fill="grey",outline="grey")
    canvas.create_rectangle(265,130,275,589,fill="grey",outline="grey")
    canvas.create_rectangle(415,130,425,589,fill="grey",outline="grey")
    during_game(canvas,str)

def click(buttonPlay,canvas):
    global place_holder,game_mode_on,during_game_identifier,place_taken_1,place_taken_2,place_taken_combo,game_ended
    if 200<=buttonPlay.x<=500 and 200<=buttonPlay.y<=250 and not game_mode_on and not during_game_identifier and not game_ended:
        canvas.delete("all")
        choose_symbol(canvas)
    elif 200<=buttonPlay.x<=500 and 300<=buttonPlay.y<350 and not game_mode_on and not during_game_identifier and not game_ended:
        root.destroy()
    elif 200<=buttonPlay.x<=347 and 320<=buttonPlay.y<=370 and game_mode_on and not during_game_identifier and not game_ended:
        draw_board(canvas,"X")
    elif 353<=buttonPlay.x<=500 and 320<=buttonPlay.y<=370 and game_mode_on and not during_game_identifier and not game_ended:
        draw_board(canvas,"O")
    elif during_game_identifier and not game_ended:
        if 125<=buttonPlay.x<=274 and 280-150<=buttonPlay.y<=429-150:
            place_holder=1
            draw_symbol(canvas)
        elif 275<=buttonPlay.x<=424 and 280-150<=buttonPlay.y<=429-150:
            place_holder=2
            draw_symbol(canvas)
        elif 425<=buttonPlay.x<=575 and 280-150<=buttonPlay.y<=429-150:
            place_holder=3
            draw_symbol(canvas)
        elif 125<=buttonPlay.x<=274 and 430-150<=buttonPlay.y<=579-150:
            place_holder=4
            draw_symbol(canvas)
        elif 275<=buttonPlay.x<=424 and 430-150<=buttonPlay.y<=579-150:
            place_holder=5
            draw_symbol(canvas)
        elif 425<=buttonPlay.x<=575 and 430-150<=buttonPlay.y<=579-150:
            place_holder=6
            draw_symbol(canvas)
        elif 125<=buttonPlay.x<=274 and 580-150<=buttonPlay.y<=700-150:
            place_holder=7
            draw_symbol(canvas)
        elif 275<=buttonPlay.x<=424 and 580-150<=buttonPlay.y<=700-150:
            place_holder=8
            draw_symbol(canvas)
        elif 425<=buttonPlay.x<=575 and 580-150<=buttonPlay.y<=700-150:
            place_holder=9
            draw_symbol(canvas)
    elif game_ended:
        game_ended=False
        if 195<=buttonPlay.x<=350 and 450<=buttonPlay.y<=500:
            canvas.delete("all")
            game_mode_on=False
            during_game_identifier=False
            symbol_detector="X"
            place_holder=1
            place_taken_1=[
                        [0,0,0],
                        [0,0,0],
                        [0,0,0]
                        ]
            place_taken_2=[
                        [0,0,0],
                        [0,0,0],
                        [0,0,0]
                        ]
            place_taken_combo=[0,0,0,0,0,0,0,0,0]
            start_screen(canvas)
        elif 355<=buttonPlay.x<=510 and 450<=buttonPlay.y<=500:
            root.destroy()

            
        
def start_screen(canvas):
    canvas.create_rectangle(0,0,BOARD_WIDTH,BOARD_HEIGHT,fill="light blue")
    canvas.create_text(350,75,text="WELCOME TO TICTACTOE",font=("Comic Sans Ms",30,"bold"),fill="dark blue")
    canvas.create_rectangle(200,200,500,250,fill="dark blue",outline="dark blue")
    canvas.create_text(345,225,text="PLAY",font=("Comic Sans Ms",20,"bold"),fill="light blue")
    canvas.create_rectangle(200,300,500,350,fill="dark blue",outline="dark blue")
    canvas.create_text(345,325,text="EXIT",font=("Comic Sans Ms",20,"bold"),fill="light blue")


def main():
    global root
    global place_taken_combo
    for i in range(9):
        place_taken_combo.append(0)
    root=tk.Tk()
    root.title("Tic Tac Toe")
    canvas=tk.Canvas(root,width=BOARD_WIDTH,height=BOARD_HEIGHT,bg="white")
    canvas.pack()
    start_screen(canvas)
    canvas.bind("<Button-1>",lambda event: click(event,canvas))
    root.mainloop()
    


if __name__=="__main__":
    main()