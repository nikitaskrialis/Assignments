
# arxikh othonh wste na katalabainoun oi paixtes pws na paizoun
def drawDirections():
    print('Movements you can choose: 1, 2, 3, 4, 5, 6, 7, 8, 9')
    print('        |        |')
    print('   ' + '1' + '    |   ' + '2' + '    |   ' + '3')
    print('        |        |')
    print('--------------------------')
    print('        |        |')
    print('   ' + '4' + '    |   ' + '5' + '    |   ' + '6')
    print('        |        |')
    print('--------------------------')
    print('        |        |')
    print('   ' + '7' + '    |   ' + '8' + '    |   ' + '9')
    print('        |        |')
    print('Every player has 6 pieces of size:2x1, 2x2, 2x3')

# typwnei kathe fora pou kaleitai ton pinaka tou paixnidiou me tis kinhseis twn paixtwn
def drawBoard(Board):
    print('\n')
    print('        |        |')
    print(' ' + Board[0][len(Board[0])-1] + '   | ' + Board[1][len(Board[1])-1] + '   | ' + Board[2][len(Board[2])-1])
    print('        |        |')
    print('--------------------------')
    print('        |        |')
    print(' ' + Board[3][len(Board[3])-1] + '   | ' + Board[4][len(Board[4])-1] + '   | ' + Board[5][len(Board[5])-1])
    print('        |        |')
    print('--------------------------')
    print('        |        |')
    print(' ' + Board[6][len(Board[6])-1] + '   | ' + Board[7][len(Board[7])-1] + '   | ' + Board[8][len(Board[8])-1])
    print('        |        |')
    print('\n')



    
# h lista Board exei 9 ypo listes kai kathe mia apo aytes to poly 4 stoixeia
# sthn arxikopoihsh kathe ypolista exei mono to '    '
# player1 kai 2 einai ta pieces tou kathe paikth arxika me megethos analogo ths
# thesis sthn lista: 2x1, 2x2, 2x3
def init(Board):
    for i in range(9):
        Board.append(['    '])
    player1 = [2,2,2]
    player2 = [2,2,2]
    return Board, player1, player2

# kaleitai kathe fora gia na kanei enas paixths mia kinhsh
def askformove(turn, p1, p2, Board):
    turn %= 2
    print '------------------------------'
    if turn == 1:
        print '\nPlayer1:'
        plist = p1
        player = 1
    else:
        print '\nPlayer2:'
        plist = p2
        player = 2
    ch1 = int(input('Place or Replace a piece (choose 1 or 2):'))
    while(ch1 < 1 or ch1 > 2):
        ch1 = int(input('Wrong choise! Place or Replace a piece (choose 1 or 2):'))
    if ch1 == 1:
        flag = pieceplace(plist,Board,player)
    else:
        flag = piecereplace(plist, Board, player)
    return flag


        
# metakinei ena piece apo mia yparxousa thesi se mia allh
def piecereplace(plist, Board, player):
    if plist[0]==plist[1]==plist[2]==2:
        print 'You have no piece to replace on Board!!'
        return False;
    # h thesi apo opou tha metakinhthei to piece
    frompos = int(input('You want to replace a piece from position(1-9): '))
    while illegalfrompos(player, Board, frompos):
        yes = int(input('Illegal position! Would you like to choose another one?(Yes = 1, No = 2):'))
        if yes == 2:
            return False
        frompos = int(input('You want to replace a piece from position(1-9): '))
    # to piece pou tha metakinhthei se morfh int
    piece = int(Board[frompos-1][len(Board[frompos-1])-1][0])
    # h thesi sthn opoia tha paei to piece
    topos = int(input('You want to put a piece to position(1-9): '))
    while illegalmovement(topos,piece,Board):
        yes = int(input('Illegal position! Would you like to choose another one?(Yes = 1, No = 2):'))
        if yes == 2:
            return False
        topos = int(input('You want to put a piece to position(1-9): '))
    # ola kala topothetoume to piece sthn nea thesi kai to bgazoume apo thn palia
    s = str(piece)+':p'+str(player)
    Board[topos-1].append(s)
    Board[frompos-1].pop()
    return True


# elegxei gia mh epitreptes metakinhseis
def illegalfrompos(player, Board, frompos):
    if frompos < 1 or frompos > 9:
        return True
    # an o paixths den exei kapoio piece diko tou se ayth th thesh
    if Board[frompos-1][len(Board[frompos-1])-1][3] != str(player):
        return True


    
# topothetei ena neo piece sto Board kai to afairei apo ta diathesima tou paixth
def pieceplace(plist, Board, player):
    if plist[0]==plist[1]==plist[2]==0:
        print 'You have no piece to place!!'
        return false;
    print 'You have: '+str(plist[0])+'x1 '+str(plist[1])+'x2 '+str(plist[2])+'x3'
    piece = int(input('Choose a piece (1-3):'))
    while piece < 1 or piece > 3 or plist[piece-1] == 0:
        piece = int(input('You not have this piece! Choose a piece (1-3):'))
    pos = int(input('Choose a place on the Board(1-9):'))
    while illegalmovement(pos,piece,Board):
        pos = int(input('Illegal movement! Choose another place on the Board(1-9):'))
    # ola kala mporoume na kanoume thn topothethsh kai na bgaloume to piece apo ta diathesima
    s = str(piece)+':p'+str(player)
    Board[pos-1].append(s)
    plist[piece-1]-=1
    return True
    


# elegxei an einai kanonikh h topothethsh tou piece apo ton player
def illegalmovement(pos, piece, Board):
    if pos < 1 or pos > 9:
        return True
    # an yparxei hdh piece megalytero h iso apo ayto pou thelw na balw
    if Board[pos-1][len(Board[pos-1])-1][0] >= str(piece):
        return True
    return False

# elegxei tis theseis tou Board gia na dei an yparxei nikhths
def checkforwinner(Board, pl):
    list = []
    pl = str(pl)
    # bazoume oles tis emfaniseis twn dyo paixtwn se mia lista kai kanoume ton elegxo
    # an brethei nikhths epistrefei True alliws False
    for i in range(9):
        list.append(Board[i][len(Board[i])-1][3])
    return ((list[0]==pl and list[1]==pl and list[2]==pl)or
            (list[3]==pl and list[4]==pl and list[5]==pl)or
            (list[6]==pl and list[7]==pl and list[8]==pl)or
            (list[0]==pl and list[3]==pl and list[6]==pl)or
            (list[1]==pl and list[4]==pl and list[7]==pl)or
            (list[2]==pl and list[5]==pl and list[8]==pl)or
            (list[0]==pl and list[4]==pl and list[8]==pl)or
            (list[2]==pl and list[4]==pl and list[6]==pl))
    

    

def main():
    Board = []
    Board, p1, p2 = init(Board)
    count = 1
    drawDirections()
    while count != -1:
        drawBoard(Board)
        #ex = raw_input('For exit press e: ')
        #if ex == 'e':
            #break
        proceed = askformove(count,p1,p2,Board)
        # an proceed True tote synexizei o epomenos paixths
        if proceed:
            player = count%2
            if player == 0:
                player = 2
            count += 1
            winner = checkforwinner(Board, player)
        if winner:
            drawBoard(Board)
            print 'And the winner is: PLAYER'+ str(player)
            break

    

    


main()
