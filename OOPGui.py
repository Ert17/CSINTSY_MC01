import pygame

#container for user input
user_text = ''

# model for each "Scene"
class SceneBase:
    def __init__(self):
        self.next = self

    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self): #game logic
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)

# The rest is code where you implement your game using the Scenes model

class MenuScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        global user_text
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    # Move to the next scene when the user pressed Enter
                    self.SwitchToScene(SimScene())
                else:
                    user_text += event.unicode

    def Update(self):
        global input_rect, base_font

        input_rect = pygame.Rect(200,200,140,32)

        base_font = pygame.font.Font(None,32)

    def Render(self, screen):
        global input_rect, base_font

        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((255, 0, 0))

        pygame.draw.rect (screen,(255,255,255),input_rect,2)
        text_surface =  base_font.render(user_text, True, (255,255,255))
        screen.blit(text_surface,(input_rect.x + 5, input_rect.y + 5))

        input_rect.w = max(100, text_surface.get_width() + 10)

        pygame.display.flip()


class SimScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self):
        pass

    def Render(self, screen):
        # The game scene is just a blank blue screen
        screen.fill((0, 0, 255))
        update_grid(screen)

''' ----------- user input -------------'''
# def textbox(screen):
#     global text_surface
#
#     pygame.draw.rect (screen,input_rect,2)
#
#     text_surface = base_front.render(user_text, True, (255,255,255))
#     screen.blit(text_surface, (input_rect.x, input_rect.y))
#     input_rect.w = text_surface.get_width
#     clock.tick(60)

''' -------------------- GRID -------------------- '''
def grid(screen, gridsize, scr_height):

    distBtRows = scr_height // gridsize
    x = 0
    y = 0
    for l in range(gridsize):
        x += distBtRows
        y += distBtRows
        pygame.draw.line(screen, (0,0,0), (x, 0), (x, scr_height)) # horizontal line
        pygame.draw.line(screen, (0,0,0), (0, y), (scr_height, y)) # vertical line

def update_grid(screen):
    global gridsize, scr_height
    gridsize = 32

    screen.fill((255,255,255))      # Color (RGB)
    grid(screen, gridsize, scr_height)
    # update screen
    pygame.display.update()
''' ---------------------------------------------- '''


''' -------------------- Starting Program -------------------- '''
def main():
    global scr_width, scr_height

    scr_width, scr_height = 1500, 1000
    run_program(scr_width, scr_height, 60, MenuScene())

# Program Loop
def run_program(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()

        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                ctrl_held = pressed_keys[pygame.K_LCTRL] or \
                              pressed_keys[pygame.K_RCTRL]
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_w and ctrl_held:
                    return
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)

        active_scene.ProcessInput(filtered_events, pressed_keys)
        active_scene.Update()
        active_scene.Render(screen)

        active_scene = active_scene.next

        pygame.display.flip()
        clock.tick(fps)

if __name__ == "__main__":
    main()
