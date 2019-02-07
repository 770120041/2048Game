import pygame
import game_logic

class game_2048:

    #grid defination
    SCORE_WIDTH = 50
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500 + SCORE_WIDTH
    GRID_NUM = 4
    GRID_PADDING = 8

    BACKGROUND_COLOR = "#92877d"
    BACKGROUND_COLOR_DICT = {0:"#9e948a", 2: "#eee4da", 4: "#ede0c8", 8: "#f2b179", 16: "#f59563", \
                             32: "#f67c5f", 64: "#f65e3b", 128: "#edcf72", 256: "#edcc61", \
                             512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"}
    CELL_COLOR_DICT = {0:"#9e948a",2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2", \
                       32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2", 256: "#f9f6f2", \
                       512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2"}
    FONT = ("Verdana", 40, "bold")

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._title = "2048"
        self._size = self.weight, self.height = self.WINDOW_WIDTH, self.WINDOW_HEIGHT

    def __rgb_to_hext(self, hex_color):
        return tuple(int(hex_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))


    def on_init(self):
        pygame.init()
        pygame.display.set_caption(self._title)
        self._display_surf = pygame.display.set_mode(self._size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        # self.__grid = [[16 for x in range(self.GRID_NUM)] for y in range(self.GRID_NUM)]
        self.score = 0
        self.is_new_game = True

    # init the grid at first running
    def __init_grid(self):
        self.is_new_game = False
        self.grid = game_logic.new_game(self.GRID_NUM)

    def on_event(self, event):
        key_pressed = ""
        if event.type == pygame.QUIT:
            self._running = False
            return
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                key_pressed = "up"
            elif event.key ==pygame.K_DOWN:
                key_pressed = "down"
            elif event.key == pygame.K_LEFT:
                key_pressed = "left"
            elif event.key == pygame.K_RIGHT:
                key_pressed = "right"
            elif event.key == pygame.K_ESCAPE:
                self._running = False
                return
        # TODO: update score content
        if key_pressed != "":
            self.grid,score_got = game_logic.update_grid(self.grid, key_pressed)
            self.score += score_got


    #TODO  show result text of the whole game
    def show_result_text(self,text):
        pass

    def on_loop(self):
        # render background
        self._display_surf.fill(self.__rgb_to_hext(self.BACKGROUND_COLOR))

        # rendering score
        font = pygame.font.Font(None, 30)
        scoretext = font.render("Score:" + str(self.score), 1, (255, 255, 255))
        self._display_surf.blit(scoretext, (10, 20))

        # rendering grid
        for row in range(self.GRID_NUM):
            for col in range(self.GRID_NUM):
                # render grid background
                grid_value = self.grid[col][row]
                grid_row_pos = self.GRID_PADDING + row*(self.WINDOW_WIDTH/self.GRID_NUM)
                grid_col_pos =  self.SCORE_WIDTH+self.GRID_PADDING + col*(self.WINDOW_WIDTH/self.GRID_NUM)
                grid_rect_width = (self.WINDOW_WIDTH/self.GRID_NUM)- 2 * self.GRID_PADDING
                pygame.draw.rect(self._display_surf,
                                 self.__rgb_to_hext(self.BACKGROUND_COLOR_DICT[grid_value]),
                                  [grid_row_pos,grid_col_pos,grid_rect_width,grid_rect_width])
                # render numbers:
                font = pygame.font.Font(None, 60)
                grid_text = font.render(str(grid_value), 1, self.__rgb_to_hext(self.CELL_COLOR_DICT[grid_value]))
                text_rect = grid_text.get_rect(center=(grid_row_pos+ grid_rect_width/2, grid_col_pos+ grid_rect_width/1.9))

                self._display_surf.blit(grid_text,text_rect )


        if game_logic.game_state(self.grid) == 'win':
           pass
        if game_logic.game_state(self.grid) == 'lose':
           pass
        pygame.display.update()

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            if self.is_new_game:
                self.__init_grid()
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == '__main__':
    game_2048 = game_2048()
    game_2048.on_execute()
