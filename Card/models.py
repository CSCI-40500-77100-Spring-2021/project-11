from django.db import models

class Card(models.Model):

    card_id = models.IntegerField(
    primary_key=True,
    )

    card_in_deck = models.BooleanField(
    default=True,
    )

    card_in_discard = models.BooleanField(
    default=False,
    )

    card_on_top = models.BooleanField(
    default=False,
    )

    card_in_hand = models.IntegerField(
    default=0,
    )

    card_is_playable = models.BooleanField(
    default=False,
    )

    CARD_COLOR = (
    ("BLACK", "BLACK"),
    ("RED", "RED"),
    ("YELLOW", "YELLOW"),
    ("GREEN", "GREEN"),
    ("BLUE", "BLUE"),
	)

    card_color = models.CharField(
    max_length=10,
    choices=CARD_COLOR,
    null=False,
    default="BLACK",
    )

    CARD_VALUE = (
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("SKIP", "SKIP"),
    ("REVERSE", "REVERSE"),
    ("PLUS TWO", "PLUS TWO"),
    ("CHANGE COLOR", "CHANGE COLOR"),
    ("PLUS FOUR AND CHANGE COLOR", "PLUS FOUR AND CHANGE COLOR"),
    )

    card_value =  models.CharField(
    max_length=30,
    choices=CARD_VALUE,
    null=False,
    default=0,
    )

        #def SET CARD ON/OFF DECK
        #def SET CARD ON/OFF DISCARD
        #def SET CARD ON/OFF TOP

        #def SET RANDOM CARD FROM DECK TO HAND
        #def SET CARD ON/OFF PLAYABLE



    def __str__(self):
        return str(self.card_id)

###################################################

    # CLASS PLAYER
    #
    #     NUM OF PLAYERS?
    #
    #     #def DRAW CARD TO HAND

    #CLASS GAME

        ### NUMBER OF PLAYERS

        ### WHOSE TURN
        ### DIRECTION OF PLAY
        ### GAME WON?

        #def ASSIGN INTIAL HANDS TO PLAYERS
        #def LOAD TOP
        #def CURRENT PLAYER PLAYS CARD
        #def NEXT PLAYER IS NOW CURRENT PLAYER
        #def CURRENT PLAYER DRAWS 2
        #def CURRENT PLAYER DRAWS 4
        #def CHANGES DIRECTION OF PLAY
        #def SKIPS NEXT PLAYER
        #def COUNT CARDS IN EACH HAND
        #def PLAYER ANNOUNCES UNO
        #def PLAYER X WINS
