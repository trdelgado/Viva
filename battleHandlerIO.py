class BattleHanderIO(object):

    def __init__(self):
        self.window_length = 90
    
    def title_menu(self, string):
        # Begin Game Message
        print("\n")
        print(self.window_length*"=")
        padding_diff = self.window_length-2
        string = string.center(padding_diff, " ")
        string = "|" + string + "|"
        print(string)
        print(self.window_length*"=")
            
    # Prompt user to exit (y/n)
    def ask_yes_no(self, question):
        response = None
        while response not in ("y", "n"):
            response = input(question).lower()
        return response
    
    # Display game status to user
    def battle_stats(self, active_player, heroes, enemies):
        
        # Print enemy stats
        self.title_menu("Enemy Stats")
        enemy_name = "|\tName\t|\t"
        enemy_health = "|\tHealth\t|\t"
        enemy_health_list = []
        enemy_mana = "|\tMana\t|\t"
        enemy_mana_list = []
        
        # For each enemy get the name and health
        for player in enemies.get_teammembers():
                enemy = enemies.get_teammember(player)
                enemy_name += enemy.get_name() + "\t|\t"
                enemy_health += "{:.2f}" + "\t|\t"
                enemy_health_list.append(enemy.get_health())
                enemy_mana += "{:.2f}" + "\t|\t"
                enemy_mana_list.append(enemy.get_mana())
                
        # Display stats
        print(enemy_name)
        print(self.window_length*"=")
        print(enemy_health.format(*enemy_health_list))
        print(self.window_length*"=")
        print(enemy_mana.format(*enemy_mana_list))
        print(self.window_length*"=")

        
        # Print hero stats
        self.title_menu("Hero Stats")
        hero_name = "|\tName\t|\t"
        hero_health = "|\tHealth\t|\t"
        hero_health_list = []
        hero_mana = "|\tMana\t|\t"
        hero_mana_list = []
        
        # For each hero get the name, health, and mana
        for player in heroes.get_teammembers():
                hero = heroes.get_teammember(player)
                hero_name += hero.get_name() + "\t|\t"
                hero_health += "{:.2f}" + "\t|\t"
                hero_health_list.append(hero.get_health())
                hero_mana += "{:.2f}" + "\t|\t"
                hero_mana_list.append(hero.get_mana())
                
        # Display stats
        print(hero_name)
        print(self.window_length*"=")
        print(hero_health.format(*hero_health_list))
        print(self.window_length*"=")
        print(hero_mana.format(*hero_mana_list))


        # Display which player is taking a turn
        active_player_string = "{}'s turn".format(active_player.get_name())
        self.title_menu(active_player_string)