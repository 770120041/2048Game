import pygame


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
    CELL_COLOR_DICT = {2: "#776e65", 4: "#776e65", 8: "#f9f6f2", 16: "#f9f6f2", \
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

    def __init_backgroud(self):
        pass


    def on_init(self):
        pygame.init()
        pygame.display.set_caption(self._title)
        self._display_surf = pygame.display.set_mode(self._size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.__init_backgroud()
        self.__grid = [[0 for x in range(self.GRID_NUM)] for y in range(self.GRID_NUM)]
        self.init_bg()


    def on_event(self,event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("up")
            elif event.key ==pygame.K_DOWN:
                print("down")
            elif event.key == pygame.K_LEFT:
                print("left")
            elif event.key == pygame.K_RIGHT:
                print("right")

    def on_loop(self):
        pass
    def init_bg(self):
        self._display_surf.fill(self.__rgb_to_hext(self.BACKGROUND_COLOR))
        # creating GRID, initially all pos are 0
        for row in range(self.GRID_NUM):
            for col in range(self.GRID_NUM):
                # draw the background of the cell
                # print(row,col)
                # print("sellf pos=", str([self.GRID_PADDING + row*(self.WINDOW_WIDTH/self.GRID_NUM),
                #                    self.GRID_PADDING + col*(self.WINDOW_HEIGHT/self.GRID_NUM),
                #                    -self.GRID_PADDING + (row+1) * (self.WINDOW_WIDTH/self.GRID_NUM),
                #                    -self.GRID_PADDING + (col+1) * (self.WINDOW_HEIGHT/self.GRID_NUM)
                #                    ]))

                # render rec background
                pygame.draw.rect(self._display_surf,
                                 self.__rgb_to_hext(self.BACKGROUND_COLOR_DICT[self.__grid[row][col]]),
                                  [self.GRID_PADDING + row*(self.WINDOW_WIDTH/self.GRID_NUM),
                                   self.SCORE_WIDTH+self.GRID_PADDING + col*(self.WINDOW_WIDTH/self.GRID_NUM),
                                   (self.WINDOW_WIDTH/self.GRID_NUM)- 2 * self.GRID_PADDING,
                                   (self.WINDOW_WIDTH / self.GRID_NUM) - 2 * self.GRID_PADDING
                                   ])
                # render numbers:


        pygame.display.flip()

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == '__main__':
    game_2048 = game_2048()
    game_2048.on_execute()
