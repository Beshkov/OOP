from project.player.player import Player


class BattleField:

    def fight(self, attacker: Player, enemy: Player):
        if self.is_death(attacker, enemy):
            raise ValueError("Player is dead!")

        if attacker.__class__.__name__ == "Beginner":
            attacker.health += 40
            for card in attacker.card_repository.cards:
                card.damage_points += 30

        if enemy.__class__.__name__ == "Beginner":
            enemy.health += 40
            for card in enemy.card_repository.cards:
                card.damage_points += 30

        self.start_of_fight_healt_boost(attacker)
        self.start_of_fight_healt_boost(enemy)


        attacker_damage = [card.damage_points for card in attacker.card_repository.cards]
        enemy_damage = [card.damage_points for card in enemy.card_repository.cards]


        for attacker_card in attacker_damage:
            if enemy.is_dead:
                return
            enemy.take_damage(attacker_card)

        for enemy_card in enemy_damage:
            if attacker.is_dead:
                return
            attacker.take_damage(enemy_card)

    def start_of_fight_healt_boost(self, player):
        for card in player.card_repository.cards:
            player.health += card.health_points

    def is_death(self, attacker, enemy):
        return attacker.is_dead or enemy.is_dead