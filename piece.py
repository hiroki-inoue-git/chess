# coding:utf-8

# 定義
BOARD_SIZE = 8
B_PAWN = 0
B_ROOK = 1
B_KNIGHT = 2
B_BISHOP = 3
B_QUEEN = 4
B_KING = 5
W_PAWN = 6
W_ROOK = 7
W_KNIGHT = 8
W_BISHOP = 9
W_QUEEN = 10
W_KING = 11
BLACK = 1
WHITE = -1
NONE = 20

class Chess_Piece:
    """駒の種類を保存するクラス。駒の種類、生きた駒かは変更可能。"""
    def __init__(self, piece, activate=True):
        self.piece = piece
        self.color = self._getcolor(piece)
        self.moved = False
        self.active = activate

    def _getcolor(self, piece):
        if piece == NONE:
            return NONE
        elif piece > B_KING:
            return WHITE
        else:
            return BLACK
    
    def setPiece(self, piece):
        self.piece = piece
    
    def move(self):
        self.moved = True
    
    def ismove(self):
        return self.moved

    def isActivate(self):
        return self.active
    
    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True
    
    def getPiece(self):
        return self.piece

    def getColor(self):
        return self.color

    def movingPosition(self):
        # それぞれの方向に対して1マスのみ効く駒ならsingleはTrue。どの方向に効くのかをリストにする。
        # ただし、ポーンとキングに関しては返却しない
        piece = self.piece % 6
        single = False
        dif = []
        if piece == B_ROOK:
            dif = [[1,0],[-1,0],[0,1],[0,-1]]
        elif piece == B_KNIGHT:
            single = True
            dif = [[2,1],[2,-1],[1,2],[1,-2],[-1,2],[-1,-2],[-2,1],[-2,-1]]
        elif piece == B_BISHOP:
            dif = [[1,1],[1,-1],[-1,1],[-1,-1]]
        elif piece == B_QUEEN:
            dif = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        return single, dif
