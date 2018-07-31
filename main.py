import pygame

from Character import Character
from Shared.GameConstants import GameConstants
# from Shared.Animator import Animator


class ARPG:

    def __init__(self):

        pygame.init()
        pygame.mixer.init()

        # pygame.mouse.set_visible(True)

        self.__screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE)
        self.__clock = pygame.time.Clock()
        self.__playtime = 0
        self.__current_scene = 0
        self.__mainloop = True
        self.__background = pygame.Surface(GameConstants.SCREEN_SIZE).convert_alpha()
        self.__background.fill(GameConstants.BLACK)
        self.__allgroup = pygame.sprite.LayeredUpdates()  # ordered sprite group

    def start(self):
        # animator = Animator(GameConstants.SPRITE_SHEET_ADVENTURER,
        #                     sprite_size=GameConstants.SIZE_ADVENTURER)

        sprite_sheet = GameConstants.ADVENTURER_SPRITE_SHEET
        size = GameConstants.ADVENTURER_SIZE
        position = (GameConstants.SCREEN_SIZE[0]/2-size[0]/2, GameConstants.SCREEN_SIZE[1]/2-size[1]/2)

        hero = Character(sprite_sheet, size, position)
        self.__allgroup.add(hero)

        cycletime = 0

        while self.__mainloop:
            milliseconds = self.__clock.tick(GameConstants.FPS)  # ms passed since last tick/frame
            seconds = milliseconds / 1000.0  # seconds since last tick/frame
            self.__playtime += seconds
            cycletime += seconds

            # hero default mode
            new_speed = (0, 0)
            hero.set_action("idle")

            pygame.event.pump()
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                self.__mainloop = False
            if key[pygame.K_a] or key[pygame.K_d] or key[pygame.K_w] or key[pygame.K_s]:
                hero.set_action("run")
            if key[pygame.K_a]:
                new_speed = (-GameConstants.ADVENTURER_SPEED[0], new_speed[1])
            if key[pygame.K_d]:
                new_speed = (GameConstants.ADVENTURER_SPEED[0], new_speed[1])
            if key[pygame.K_w]:
                new_speed = (new_speed[0], -GameConstants.ADVENTURER_SPEED[1])
            if key[pygame.K_s]:
                new_speed = (new_speed[0], GameConstants.ADVENTURER_SPEED[0])
            if key[pygame.K_LSHIFT]:
                hero.set_action("walk")
                new_speed = (new_speed[0]/2, new_speed[1]/2)
            if key[pygame.K_SPACE]:
                # TODO: need to implement jump
                pass
            mouse_keys = pygame.mouse.get_pressed()

            if mouse_keys[0]:
                new_speed = (0, 0)
                hero.set_action("bow")
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] > hero.get_position()[0] + hero.get_size()[0]:
                    hero.turn_right()
                else:
                    hero.turn_left()


            hero.set_speed(new_speed)

            if cycletime > GameConstants.INTERVAL:
                cycletime = 0
                self.__allgroup.clear(self.__screen, self.__background)
                self.__allgroup.update(seconds)
                self.__allgroup.draw(self.__screen)

            pygame.display.set_caption("[FPS]: %.2f action: %s" % (self.__clock.get_fps(), hero.get_action()))
            # pygame.display.set_caption("[FPS]: %.2f action: %s picture: %i" % (self.__clock.get_fps(),
            #                                                                    action,
            #                                                                    hero.get_sprite_index()))

            pygame.display.update()
            # pygame.display.flip()

    def change_scene(self, scene):
        self.__current_scene = scene


ARPG().start()
