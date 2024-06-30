import pygame, sys
from pawn import Pawn

class Game:
    def __init__(self, screen_size):
        #General
        self.pieces = {
        "B_Pawn"    :1,
        "B_knight"  :2,
        "B_bishop"  :3,
        "B_tower"   :4,
        "B_queen"   :5,
        "B_king"    :6
        }
        self.tile_size = screen_size/8

        self.board_background = pygame.sprite.Group()
        self.board_figures    = pygame.sprite.Group()
        self.setup()
        self.board_background.draw(screen)

    def setup(self):
        #board_setup
        tile_size = self.tile_size
        path  = ''
        color = ''
        for column_index in range(8):
            x = (column_index + 1/2) * tile_size
            for row_index in range(8):
                y = (row_index + 1/2) * tile_size
        
                if (column_index + row_index) % 2 == 0:
                    color = 'b'
                else:
                    color = 'w'
                path =  'Graphics/sqr_brwn_' + color + '.png'
                tile = Pawn(path, (x,y), tile_size)
                self.board_background.add(tile)
        #pawn setup

            ywhite = tile_size * 3/2
            yblack = tile_size * 13/2 
        for column_index in range(8):
            x = (column_index + 1/2) * tile_size
            pawn_w = Pawn('Graphics/w_pawn.png', (x,ywhite), tile_size*2/3)
            pawn_b = Pawn('Graphics/b_pawn.png', (x,yblack), tile_size*2/3)
            self.board_figures.add(pawn_w)
            self.board_figures.add(pawn_b)

    def run(self):
        '''GameLoop here:'''
        self.board_background.draw(screen)
        self.board_figures.draw(screen)

if __name__ == '__main__':
    # Window initialize:
    pygame.init()
    screen_size = 800
    screen = pygame.display.set_mode((screen_size, screen_size))

    # Window Details
    pygame.display.set_caption("Chess")
    icon = pygame.image.load('Graphics/w_knight.png') 
    pygame.display.set_icon(icon)

    # Logic and time
    game = Game(screen_size)
    clock = pygame.time.Clock()
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        game.run()
        pygame.display.flip()
        clock.tick(60)
