#!/usr/bin/env python
# coding: utf-8

# In[7]:
from csv import writer

import pandas as pd
import numpy as np
from pandas import DataFrame
import random

l = 0

Num_of_Hands = int(input("Input Number of Hands to be generated"))
while l < Num_of_Hands:
    cards_value = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

    card_val = []
    cards_suit = ['h', 'd', 'c', 's']
    card_list = []
    cards = []

    suit = 0
    hero_SO = []
    hero_hand = []
    hero_hand_val = []
    hero_card1 = []
    hero_card2 = []
    list_of_rankings = []
    card_num = 1
    rank_str = 1
    ranks = []
    sorted_hands = []
    rank_list = []
    card_vals = []
    i = 0

    for i in range(0, 13):

        for suit in range(0, 4):
            cards.append(cards_value[i] + cards_suit[suit])
            card_vals.append(cards_value[i])

    random.shuffle(cards)

    # for i in range(0,1):
    small_blind_card1 = cards[0]
    small_blind_card2 = cards[1]
    big_blind_card1 = cards[2]
    big_blind_card2 = cards[3]
    UTG_card1 = cards[4]
    UTG_card2 = cards[5]
    UTG2_card1 = cards[6]
    UTG2_card1 = cards[7]
    MP_card1 = cards[8]
    MP_card2 = cards[9]
    MP2_card1 = cards[10]
    MP2_card2 = cards[11]
    MP3_card1 = cards[12]
    MP3_card2 = cards[13]
    HJ_card1 = cards[14]
    HJ_card2 = cards[15]
    Button_card1 = cards[16]
    Button_card2 = cards[17]
    Burn_card1 = cards[18]
    Flop_card1 = cards[19]
    Flop_card2 = cards[20]
    Flop_card3 = cards[21]
    Burn_card2 = cards[22]
    Turn = cards[23]
    Burn_card3 = cards[24]
    River = cards[25]
    cards_value_df = []
    cards_suit_df = []

    # Button_card1 = "3d"
    # Button_card2 = "Ad"
    # Flop_card1 = "4d"
    # Flop_card2 = "7h"
    # Flop_card3 = "5d"
    # Turn = "2d"
    # River = "2c"

    x = 0
    y = 0
    index = []
    suit_index = []
    index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    x = 0
    while x < 4:
        suit_index.append(x)
        x += 1
    x = 0
    Hero_Card_Suits = []
    Hero_Hand_Rank = []
    Card_Suits_ = []
    Button_card1_str = str(Button_card1)
    Button_card2_str = str(Button_card2)
    cards_value_df = pd.DataFrame(cards_value, columns=["card_values"], index=index)
    cards_suit_df = pd.DataFrame(cards_suit, columns=["Card_Suits"], index=suit_index)
    Hero_Card_Ranks = []

    Button_Hand_Rank = []
    Button_Hand_Suits = []
    while y < 4:

        if cards_suit_df.at[y, "Card_Suits"] == Button_card1[1]:
            Button_Hand_Suits.append(Button_card1[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Button_card2[1]:
            Button_Hand_Suits.append(Button_card2_str[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card1[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card2[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card3[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Turn[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == River[1]:
            Card_Suits_.append(y)

        y += 1

    y = 0

    while y < 13:

        if cards_value_df.at[y, "card_values"] == Button_card1[0]:
            Button_Hand_Rank.append(Button_card1[0])
            Hero_Card_Ranks.append(y)
            Hero_Card_Suits.append(Button_card1[1])

        if cards_value_df.at[y, "card_values"] == Button_card2[0]:
            Button_Hand_Rank.append(Button_card2[0])
            Hero_Card_Ranks.append(y)
            Hero_Card_Suits.append(Button_card2[1])

        if cards_value_df.at[y, "card_values"] == Flop_card1[0]:
            Hero_Card_Suits.append(Flop_card1[1])
            Hero_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card2[0]:
            Hero_Card_Suits.append(Flop_card2[1])
            Hero_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card3[0]:
            Hero_Card_Suits.append(Flop_card3[1])
            Hero_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Turn[0]:
            Hero_Card_Suits.append(Turn[1])
            Hero_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == River[0]:
            Hero_Card_Suits.append(River[1])
            Hero_Card_Ranks.append(y)

        y += 1

    Heros_Hand_df = pd.DataFrame(list(zip(Hero_Card_Ranks, Hero_Card_Suits, [1, 1, 1, 1, 1, 1, 1])),
                                 columns=["Card_Rank", "Card_Suit", "Suit_Value"])
    Heros_Hand_rank_suit_df = Heros_Hand_df.sort_values(by=["Card_Rank"], ascending=True)

    Heros_Hand_df_sum = Heros_Hand_df.groupby(['Card_Suit'], as_index=False)['Suit_Value'].sum()
    Heros_Hand_sorted_df_sum = Heros_Hand_df_sum.sort_values(by=["Suit_Value"], ascending=False)

    Hero_Suit_Sum_index = []
    n = 0
    while n < len(Heros_Hand_sorted_df_sum["Suit_Value"]):
        Hero_Suit_Sum_index.append(n)
        n += 1
    Heros_Hand_sorted_df_sum["index"] = Hero_Suit_Sum_index
    Heros_Hand_sorted_df_sum.set_index("index", inplace=True)
    Hero_Hand_Rank_Flush = []
    if Heros_Hand_sorted_df_sum.at[0, "Suit_Value"] >= 5:
        Hero_Hand_Rank_Flush.clear()
        Hero_Hand_Rank_Flush.append(5)
        Hero_Hand_Rank_Flush.append(Heros_Hand_df.at[0, "Card_Rank"])
        Hero_Hand_Rank_Flush.append(Heros_Hand_df.at[1, "Card_Rank"])
        Hero_Hand_Rank_Flush.append(Heros_Hand_df.at[2, "Card_Rank"])
        Hero_Hand_Rank_Flush.append(Heros_Hand_df.at[3, "Card_Rank"])
        Hero_Hand_Rank_Flush.append(Heros_Hand_df.at[4, "Card_Rank"])

    Hero_Suit_for_straight = str(Heros_Hand_sorted_df_sum.at[0, "Card_Suit"])

    Button_Hand_Rank_sort = sorted(Button_Hand_Rank)
    Heros_Hand = sorted(Hero_Card_Ranks)
    # Heros_Hand = [2 ,6 , 8, 9, 10, 11, 12]

    p = 0
    s = 0
    Hero_seen = set()
    uniq = []
    Hero_seen = {}
    Pairs = []
    Fourofakind_val = []
    Threeofakind_val = []
    Hand_Rank = []
    Pair_Rank = []
    Card_Rank = []
    Hero_Hand_index = []
    for p in Heros_Hand:
        if p not in Hero_seen:
            Hero_seen[p] = 1

        else:

            Hero_seen[p] += 1
    while s < len(Hero_seen):
        Hero_Hand_index.append(s)
        s += 1

    Card_Rank_Hand = []
    # printing iniial_dictionary

    # split dictionary into keys and values
    Hero_Card_Rank_Hand = []
    Num_of_Cards = []
    Num_of_Cards.clear()

    Num_of_Cards1 = [0, 1, 2, 3, 4, 5, 6]
    items = Hero_seen.items()
    for item in items:
        Hero_Card_Rank_Hand.append(item[0]), Num_of_Cards.append(item[1])

    Hero_Hand_dict = []
    Hero_Hand_dict_sortforpair = []
    Hero_Hand_dict_sortforstraight = []

    Hero_Hand_dict = pd.DataFrame(list(zip(Hero_Card_Rank_Hand, Num_of_Cards, Hero_Card_Suits)),
                                  columns=['a', 'b', 'c'])
    Hero_Hand_dict_straight = pd.DataFrame(list(zip(Hero_Card_Rank_Hand, Num_of_Cards, Hero_Card_Suits)),
                                           columns=['a', 'b', 'c'])
    Hero_Hand_dict_sortforpair = Hero_Hand_dict.sort_values(by=['b'], ascending=False)
    Hero_Hand_dict_sortforstraight = Hero_Hand_dict_straight.sort_values(by=['a'])

    v = 0
    f = 0

    q = 0
    Hero_Hand_Rank_straight = []
    Hero_Hand_Rank_straight.clear()
    Hero_Hand_Rank_straight_wheel = []
    Hero_Hand_Rank_straight_wheel.clear()
    Hero_Hand_Rank_straight_wheel_flush = []
    Hero_Hand_Rank_straight_wheel_flush.clear()
    Hero_Hand_Rank_Royal_Flush = []
    Hero_Hand_Rank_Royal_Flush.clear

    q = 0
    v = 0
    Hero_Hand_Rank_straight_flush = []
    Hero_Hand_Rank_straight_flush.clear()

    while q < 9:


        if len(Hero_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if Hero_Hand_dict_sortforstraight.at[v, "a"] == 0:

                    if Hero_Hand_dict_sortforstraight.at[(v + 6), "a"] == 12:
                        if Hero_Hand_dict_sortforstraight.at[(v + 5), "a"] == 11:
                            if Hero_Hand_dict_sortforstraight.at[(v + 4), "a"] == 10:
                                if Hero_Hand_dict_sortforstraight.at[(v + 3), "a"] == 9:

                                    f = 0
                                    Hero_Hand_Rank_straight_wheel.clear()

                                    Hero_Hand_Rank_straight_wheel.append(12)
                                    Hero_Hand_Rank_straight_wheel.append(11)
                                    Hero_Hand_Rank_straight_wheel.append(10)
                                    Hero_Hand_Rank_straight_wheel.append(9)
                                    Hero_Hand_Rank_straight_wheel.append(Hero_Hand_dict_sortforstraight.at[0, "a"])

                                    if len(Hero_Hand_Rank_Flush) >= 1:
                                        if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                (v + 6), 'c']:
                                                if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                    (v + 5), 'c']:
                                                    if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                        (v + 4), 'c']:
                                                        if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            Hero_Hand_Rank_straight_wheel_flush.clear()

                                                            Hero_Hand_Rank_straight_wheel_flush.append(12)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(11)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(10)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(9)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(
                                                                Hero_Hand_dict_sortforstraight.at[v, "a"])
                v += 1

        elif len(Hero_Hand_dict_sortforstraight) == 6:
            v = 0
            while v < 2:

                if Hero_Hand_dict_sortforstraight.at[v, "a"] == 0:

                    if Hero_Hand_dict_sortforstraight.at[(v + 5), "a"] == 12:
                        if Hero_Hand_dict_sortforstraight.at[(v + 4), "a"] == 11:
                            if Hero_Hand_dict_sortforstraight.at[(v + 3), "a"] == 10:
                                if Hero_Hand_dict_sortforstraight.at[(v + 2), "a"] == 9:

                                    f = 0
                                    Hero_Hand_Rank_straight_wheel.clear()

                                    Hero_Hand_Rank_straight_wheel.append(12)
                                    Hero_Hand_Rank_straight_wheel.append(11)
                                    Hero_Hand_Rank_straight_wheel.append(10)
                                    Hero_Hand_Rank_straight_wheel.append(9)
                                    Hero_Hand_Rank_straight_wheel.append(Hero_Hand_dict_sortforstraight.at[0, "a"])

                                    if len(Hero_Hand_Rank_Flush) >= 1:
                                        if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                (v + 5), 'c']:
                                                if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                    (v + 4), 'c']:
                                                    if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Hero_Suit_for_straight == \
                                                                Hero_Hand_dict_sortforstraight.at[(v + 2), 'c']:
                                                            Hero_Hand_Rank_straight_wheel_flush.clear()

                                                            Hero_Hand_Rank_straight_wheel_flush.append(12)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(11)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(10)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(9)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(
                                                                Hero_Hand_dict_sortforstraight.at[v, "a"])

                                                            break

                v += 1

        elif len(Hero_Hand_dict_sortforstraight) == 5:

            v = 0
            while v < 1:


                if Hero_Hand_dict_sortforstraight.at[v, "a"] == 0:

                    if Hero_Hand_dict_sortforstraight.at[(v + 4), "a"] == 12:
                        if Hero_Hand_dict_sortforstraight.at[(v + 3), "a"] == 11:
                            if Hero_Hand_dict_sortforstraight.at[(v + 2), "a"] == 10:
                                if Hero_Hand_dict_sortforstraight.at[(v + 1), "a"] == 9:

                                    f = 0
                                    Hero_Hand_Rank_straight_wheel.clear()

                                    Hero_Hand_Rank_straight_wheel.append(12)
                                    Hero_Hand_Rank_straight_wheel.append(11)
                                    Hero_Hand_Rank_straight_wheel.append(10)
                                    Hero_Hand_Rank_straight_wheel.append(9)
                                    Hero_Hand_Rank_straight_wheel.append(
                                        Hero_Hand_dict_sortforstraight.at[0, "a"])

                                    if len(Hero_Hand_Rank_Flush) >= 1:
                                        if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                (v + 3), 'c']:
                                                if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                    (v + 3), 'c']:
                                                    if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                        (v + 2), 'c']:
                                                        if Hero_Suit_for_straight == \
                                                                Hero_Hand_dict_sortforstraight.at[
                                                                    (v + 1), 'c']:
                                                            Hero_Hand_Rank_straight_wheel_flush.clear()

                                                            Hero_Hand_Rank_straight_wheel_flush.append(12)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(11)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(10)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(9)
                                                            Hero_Hand_Rank_straight_wheel_flush.append(
                                                                Hero_Hand_dict_sortforstraight.at[v, "a"])

                                                            break



                v += 1
        if len(Hero_Hand_dict_sortforstraight) == 4:
            break
        if len(Hero_Hand_dict_sortforstraight) == 3:
            break
        q += 1



    f=0

    q = 0
    v = 0

    while q < 9:

        if len(Hero_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if Hero_Hand_dict_sortforstraight.at[v, "a"] == q:

                    if Hero_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                        if Hero_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                            if Hero_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                if Hero_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                    f = 0
                                    Hero_Hand_Rank_straight.clear()

                                    Hero_Hand_Rank_straight.append(q)
                                    Hero_Hand_Rank_straight.append(q + 1)
                                    Hero_Hand_Rank_straight.append(q + 2)
                                    Hero_Hand_Rank_straight.append(q + 3)
                                    Hero_Hand_Rank_straight.append(q + 4)

                                    if len(Hero_Hand_Rank_Flush) >= 1:
                                        if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                (v + 1), 'c']:
                                                if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                    (v + 2), 'c']:
                                                    if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Hero_Suit_for_straight == \
                                                                Hero_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                            Hero_Hand_Rank_straight_flush.clear()

                                                            Hero_Hand_Rank_straight_flush.append(q)
                                                            Hero_Hand_Rank_straight_flush.append(q + 1)
                                                            Hero_Hand_Rank_straight_flush.append(q + 2)
                                                            Hero_Hand_Rank_straight_flush.append(q + 3)
                                                            Hero_Hand_Rank_straight_flush.append(q + 4)

                                                            if q == 0:
                                                                Hero_Hand_Rank_Royal_Flush.clear()
                                                                Hero_Hand_Rank_Royal_Flush.append(0)
                                                                Hero_Hand_Rank_Royal_Flush.append(1)
                                                                Hero_Hand_Rank_Royal_Flush.append(2)
                                                                Hero_Hand_Rank_Royal_Flush.append(3)
                                                                Hero_Hand_Rank_Royal_Flush.append(4)
                                                                break
                                                            break

                v += 1

        if len(Hero_Hand_dict_sortforstraight) == 6:
            v = 0
            while v < 2:

                if Hero_Hand_dict_sortforstraight.at[v, "a"] == q:

                    if Hero_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                        if Hero_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                            if Hero_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                if Hero_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                    f = 0
                                    Hero_Hand_Rank_straight.clear()

                                    Hero_Hand_Rank_straight.append(q)
                                    Hero_Hand_Rank_straight.append(q + 1)
                                    Hero_Hand_Rank_straight.append(q + 2)
                                    Hero_Hand_Rank_straight.append(q + 3)
                                    Hero_Hand_Rank_straight.append(q + 4)

                                    if len(Hero_Hand_Rank_Flush) >= 1:
                                        if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                (v + 1), 'c']:
                                                if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                    (v + 2), 'c']:
                                                    if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Hero_Suit_for_straight == \
                                                                Hero_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                            Hero_Hand_Rank_straight_flush.clear()

                                                            Hero_Hand_Rank_straight_flush.append(q)
                                                            Hero_Hand_Rank_straight_flush.append(q + 1)
                                                            Hero_Hand_Rank_straight_flush.append(q + 2)
                                                            Hero_Hand_Rank_straight_flush.append(q + 3)
                                                            Hero_Hand_Rank_straight_flush.append(q + 4)

                                                            if q == 0:
                                                                Hero_Hand_Rank_Royal_Flush.clear()
                                                                Hero_Hand_Rank_Royal_Flush.append(0)
                                                                Hero_Hand_Rank_Royal_Flush.append(1)
                                                                Hero_Hand_Rank_Royal_Flush.append(2)
                                                                Hero_Hand_Rank_Royal_Flush.append(3)
                                                                Hero_Hand_Rank_Royal_Flush.append(4)

                                                            break

                v += 1

        if len(Hero_Hand_dict_sortforstraight) == 5:
            v = 0
            while v < 1:

                if Hero_Hand_dict_sortforstraight.at[v, "a"] == q:

                    if Hero_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                        if Hero_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                            if Hero_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                if Hero_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                    f = 0
                                    Hero_Hand_Rank_straight.clear()

                                    Hero_Hand_Rank_straight.append(q)
                                    Hero_Hand_Rank_straight.append(q + 1)
                                    Hero_Hand_Rank_straight.append(q + 2)
                                    Hero_Hand_Rank_straight.append(q + 3)
                                    Hero_Hand_Rank_straight.append(q + 4)

                                    if len(Hero_Hand_Rank_Flush) >= 1:
                                        if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                (v + 1), 'c']:
                                                if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                    (v + 2), 'c']:
                                                    if Hero_Suit_for_straight == Hero_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Hero_Suit_for_straight == \
                                                                Hero_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                            Hero_Hand_Rank_straight_flush.clear()

                                                            Hero_Hand_Rank_straight_flush.append(q)
                                                            Hero_Hand_Rank_straight_flush.append(q + 1)
                                                            Hero_Hand_Rank_straight_flush.append(q + 2)
                                                            Hero_Hand_Rank_straight_flush.append(q + 3)
                                                            Hero_Hand_Rank_straight_flush.append(q + 4)

                                                            if q == 0:
                                                                Hero_Hand_Rank_Royal_Flush.clear()
                                                                Hero_Hand_Rank_Royal_Flush.append(0)
                                                                Hero_Hand_Rank_Royal_Flush.append(1)
                                                                Hero_Hand_Rank_Royal_Flush.append(2)
                                                                Hero_Hand_Rank_Royal_Flush.append(3)
                                                                Hero_Hand_Rank_Royal_Flush.append(4)

                                                            break



                v += 1
        if len(Hero_Hand_dict_sortforstraight) == 4:
            break
        if len(Hero_Hand_dict_sortforstraight) == 3:
            break


        q += 1
    q = 0



    q=0


    Hero_Hand_dict_sortforpair["index"] = Hero_Hand_index
    Hero_Hand_dict_sortforpair.set_index("index", inplace=True)

    c = 0

    c = 0
    if Hero_Hand_dict_sortforpair.at[0, "b"] == 1:
        Hero_Hand_Rank.clear()
        Hero_Hand_Rank.append(10)
        Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[6, "a"])
        Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[5, "a"])
        Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[4, "a"])
        Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[3, "a"])
        Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[2, "a"])

    if Hero_Hand_dict_sortforpair.at[0, "b"] == 2:
        if Hero_Hand_dict_sortforpair.at[1, "b"] == 1:
            Hero_Hand_Rank.clear()
            Hero_Hand_Rank.append(9)
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[0, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[5, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[4, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[3, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[2, "a"])

    if Hero_Hand_dict_sortforpair.at[0, "b"] == 2:
        if Hero_Hand_dict_sortforpair.at[1, "b"] == 2:
            if Hero_Hand_dict_sortforpair.at[2, "b"] == 1:
                Hero_Hand_Rank.clear()
                Hero_Hand_Rank.append(8)
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[1, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[0, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[4, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[3, "a"])



    if Hero_Hand_dict_sortforpair.at[0, "b"] == 2:
        if Hero_Hand_dict_sortforpair.at[1, "b"] == 2:
            if Hero_Hand_dict_sortforpair.at[2, "b"] == 2:
                Hero_Hand_Rank.clear()
                Hero_Hand_Rank.append(8)
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[2, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[1, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[0, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[3, "a"])

    if Hero_Hand_dict_sortforpair.at[0, "b"] == 3:
        if Hero_Hand_dict_sortforpair.at[1, "b"] == 1:
            Hero_Hand_Rank.clear()
            Hero_Hand_Rank.append(7)
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[0, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[4, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[3, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[2, "a"])



    if len(Hero_Hand_Rank_straight) >= 1:
        Hero_Hand_Rank.clear()
        Hero_Hand_Rank.append(6)
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight[0])
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight[1])
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight[2])
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight[3])
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight[4])

    if len(Hero_Hand_Rank_Flush) >= 1:
        Hero_Hand_Rank.clear()
        Hero_Hand_Rank.append(5)
        Hero_Hand_Rank.append(Hero_Hand_Rank_Flush[0])
        Hero_Hand_Rank.append(Hero_Hand_Rank_Flush[1])
        Hero_Hand_Rank.append(Hero_Hand_Rank_Flush[2])
        Hero_Hand_Rank.append(Hero_Hand_Rank_Flush[3])
        Hero_Hand_Rank.append(Hero_Hand_Rank_Flush[4])

    if Hero_Hand_dict_sortforpair.at[0, "b"] == 3:
        if Hero_Hand_dict_sortforpair.at[1, "b"] == 2:
            if Hero_Hand_dict_sortforpair.at[2, "b"] == 1:
                Hero_Hand_Rank.clear()
                Hero_Hand_Rank.append(4)
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[0, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[1, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[3, "a"])


    if Hero_Hand_dict_sortforpair.at[0, "b"] == 3:
        if Hero_Hand_dict_sortforpair.at[1, "b"] == 2:
            if Hero_Hand_dict_sortforpair.at[2, "b"] == 2:
                Hero_Hand_Rank.clear()
                Hero_Hand_Rank.append(4)
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[0, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[2, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[1, "a"])

    if Hero_Hand_dict_sortforpair.at[0, "b"] == 3:
        if Hero_Hand_dict_sortforpair.at[1, "b"] == 3:
            if Hero_Hand_dict_sortforpair.at[2, "b"] == 1:
                Hero_Hand_Rank.clear()
                Hero_Hand_Rank.append(4)
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[1, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[0, "a"])
                Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[2, "a"])


    if Hero_Hand_dict_sortforpair.at[0, "b"] == 4:
        if Hero_Hand_dict_sortforpair.at[1, "b"] == 1:
            Hero_Hand_Rank.clear()
            Hero_Hand_Rank.append(3)
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[0, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[3, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[2, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[1, "a"])

    if Hero_Hand_dict_sortforpair.at[0, "b"] == 4:
        if Hero_Hand_dict_sortforpair.at[1, "b"] == 2:
            Hero_Hand_Rank.clear()
            Hero_Hand_Rank.append(3)
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[0, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[2, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[1, "a"])

    if Hero_Hand_dict_sortforpair.at[0, "b"] == 4:
        if Hero_Hand_dict_sortforpair.at[1, "b"] == 3:
            Hero_Hand_Rank.clear()
            Hero_Hand_Rank.append(3)
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[0, "a"])
            Hero_Hand_Rank.append(Hero_Hand_dict_sortforpair.at[1, "a"])


    if len(Hero_Hand_Rank_straight_wheel_flush) >=1:
        Hero_Hand_Rank.clear()
        Hero_Hand_Rank.append(2)
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight_wheel_flush[0])
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight_wheel_flush[1])
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight_wheel_flush[2])
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight_wheel_flush[3])
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight_wheel_flush[4])








    if len(Hero_Hand_Rank_straight_flush) >=1:
        Hero_Hand_Rank.clear()
        Hero_Hand_Rank.append(2)
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight_flush[0])
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight_flush[1])
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight_flush[2])
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight_flush[3])
        Hero_Hand_Rank.append(Hero_Hand_Rank_straight_flush[4])

    if len(Hero_Hand_Rank_Royal_Flush) >= 1 :
        Hero_Hand_Rank.clear()
        Hero_Hand_Rank.append(1)
        Hero_Hand_Rank.append(Hero_Hand_Rank_Royal_Flush[0])
        Hero_Hand_Rank.append(Hero_Hand_Rank_Royal_Flush[1])
        Hero_Hand_Rank.append(Hero_Hand_Rank_Royal_Flush[2])
        Hero_Hand_Rank.append(Hero_Hand_Rank_Royal_Flush[3])
        Hero_Hand_Rank.append(Hero_Hand_Rank_Royal_Flush[4])

    hero_hand.append(Button_card1)
    hero_hand.append(Button_card2)


    Hero_Rank = Hero_Hand_Rank
    x = 0
    y = 0
    index = []
    suit_index = []
    index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    x = 0
    while x < 4:
        suit_index.append(x)
        x += 1
    x = 0
    Villain_Card_Suits = []

    Villain_Hand_Rank = []
    Card_Suits_ = []
    Button_card1_str = str(Button_card1)
    Button_card2_str = str(Button_card2)
    cards_value_df = pd.DataFrame(cards_value, columns=["card_values"], index=index)
    cards_suit_df = pd.DataFrame(cards_suit, columns=["Card_Suits"], index=suit_index)
    Villain_Card_Ranks = []

    Button_Hand_Rank = []
    Button_Hand_Suits = []
    while y < 4:

        if cards_suit_df.at[y, "Card_Suits"] == small_blind_card1[1]:
            Button_Hand_Suits.append(small_blind_card1[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == small_blind_card2[1]:
            Button_Hand_Suits.append(small_blind_card2[1])
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card1[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card2[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Flop_card3[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == Turn[1]:
            Card_Suits_.append(y)

        if cards_suit_df.at[y, "Card_Suits"] == River[1]:
            Card_Suits_.append(y)

        y += 1

    y = 0

    while y < 13:

        if cards_value_df.at[y, "card_values"] == small_blind_card1[0]:
            Button_Hand_Rank.append(small_blind_card1[0])
            Villain_Card_Ranks.append(y)
            Villain_Card_Suits.append(small_blind_card1[1])

        if cards_value_df.at[y, "card_values"] == small_blind_card2[0]:
            Button_Hand_Rank.append(small_blind_card2[0])
            Villain_Card_Ranks.append(y)
            Villain_Card_Suits.append(small_blind_card2[1])

        if cards_value_df.at[y, "card_values"] == Flop_card1[0]:
            Villain_Card_Suits.append(Flop_card1[1])
            Villain_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card2[0]:
            Villain_Card_Suits.append(Flop_card2[1])
            Villain_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Flop_card3[0]:
            Villain_Card_Suits.append(Flop_card3[1])
            Villain_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == Turn[0]:
            Villain_Card_Suits.append(Turn[1])
            Villain_Card_Ranks.append(y)

        if cards_value_df.at[y, "card_values"] == River[0]:
            Villain_Card_Suits.append(River[1])
            Villain_Card_Ranks.append(y)

        y += 1

    Villain_Hand_df = pd.DataFrame(list(zip(Villain_Card_Ranks, Villain_Card_Suits, [1, 1, 1, 1, 1, 1, 1])),
                                   columns=["Card_Rank", "Card_Suit", "Suit_Value"])
    Villain_Hand_rank_suit_df = Villain_Hand_df.sort_values(by=["Card_Rank"], ascending=True)

    Villain_Hand_df_sum = Villain_Hand_df.groupby(['Card_Suit'], as_index=False)['Suit_Value'].sum()
    Villain_Hand_sorted_df_sum = Villain_Hand_df_sum.sort_values(by=["Suit_Value"], ascending=False)

    Villain_Suit_Sum_index = []
    Villain_Suit_Sum_index.clear()
    n = 0
    while n < len(Villain_Hand_sorted_df_sum["Suit_Value"]):
        Villain_Suit_Sum_index.append(n)
        n += 1
    Villain_Hand_sorted_df_sum["index"] = Villain_Suit_Sum_index
    Villain_Hand_sorted_df_sum.set_index("index", inplace=True)
    Villain_Hand_Rank_Flush = []

    if Villain_Hand_sorted_df_sum.at[0, "Suit_Value"] >= 5:
        Villain_Hand_Rank_Flush.clear()
        Villain_Hand_Rank_Flush.append(5)
        Villain_Hand_Rank_Flush.append(Heros_Hand_df.at[0, "Card_Rank"])
        Villain_Hand_Rank_Flush.append(Heros_Hand_df.at[1, "Card_Rank"])
        Villain_Hand_Rank_Flush.append(Heros_Hand_df.at[2, "Card_Rank"])
        Villain_Hand_Rank_Flush.append(Heros_Hand_df.at[3, "Card_Rank"])
        Villain_Hand_Rank_Flush.append(Heros_Hand_df.at[4, "Card_Rank"])

    Suit_for_straight = str(Villain_Hand_sorted_df_sum.at[0, "Card_Suit"])

    Button_Hand_Rank_sort = sorted(Button_Hand_Rank)
    Villain_Hand = sorted(Villain_Card_Ranks)

    # Heros_Hand = [2 ,6 , 8, 9, 10, 11, 12]

    p = 0
    s = 0
    Villain_seen = set()
    uniq = []
    Villain_seen = {}
    Pairs = []
    Fourofakind_val = []
    Threeofakind_val = []
    Villain_Hand_Rank = []
    Pair_Rank = []
    Card_Rank = []
    Villain_Hand_index = []
    for p in Villain_Hand:
        if p not in Villain_seen:
            Villain_seen[p] = 1

        else:

            Villain_seen[p] += 1

    while s < len(Villain_seen):
        Villain_Hand_index.append(s)
        s += 1
    s = 0
    # printing iniial_dictionary

    # split dictionary into keys and values
    Villain_Card_Rank_Hand = []
    Num_of_Cards = []
    Num_of_Cards.clear()

    Num_of_Cards1 = [0, 1, 2, 3, 4, 5, 6]
    items = Villain_seen.items()
    for item in items:
        Villain_Card_Rank_Hand.append(item[0]), Num_of_Cards.append(item[1])

    Villain_Hand_dict = []
    Villain_Hand_dict_sortforpair = []
    Villain_Hand_dict_sortforstraight = []
    Villain_Hand_dict = pd.DataFrame(list(zip(Villain_Card_Rank_Hand, Num_of_Cards, Villain_Card_Suits)),
                                     columns=['a', 'b', 'c'])
    Villain_Hand_dict_straight = pd.DataFrame(list(zip(Villain_Card_Rank_Hand, Num_of_Cards, Villain_Card_Suits)),
                                              columns=['a', 'b', 'c'])
    Villain_Hand_dict_sortforpair = Villain_Hand_dict.sort_values(by=['b'], ascending=False)
    Villain_Hand_dict_sortforstraight = Villain_Hand_dict_straight.sort_values(by=['a'])
    Villain_Hand_Rank = []
    v = 0
    f = 0

    q = 0
    Villain_Hand_Rank_straight = []
    Villain_Hand_Rank_straight.clear()
    Villain_Hand_Rank_straight_wheel = []
    Villain_Hand_Rank_straight_wheel.clear()
    Villain_Hand_Rank_straight_wheel_flush = []
    Villain_Hand_Rank_straight_wheel_flush.clear()
    VillainHand_Rank_Royal_Flush = []
    VillainHand_Rank_Royal_Flush.clear

    q = 0
    v = 0
    Villain_Hand_Rank_straight_flush = []
    Villain_Hand_Rank_straight_flush.clear()


    while q < 9:

        if len(Villain_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if Villain_Hand_dict_sortforstraight.at[v, "a"] == 0:

                    if Villain_Hand_dict_sortforstraight.at[(v + 6), "a"] == 12:
                        if Villain_Hand_dict_sortforstraight.at[(v + 5), "a"] == 11:
                            if Villain_Hand_dict_sortforstraight.at[(v + 4), "a"] == 10:
                                if Villain_Hand_dict_sortforstraight.at[(v + 3), "a"] == 9:

                                    f = 0
                                    Villain_Hand_Rank_straight_wheel.clear()

                                    Villain_Hand_Rank_straight_wheel.append(12)
                                    Villain_Hand_Rank_straight_wheel.append(11)
                                    Villain_Hand_Rank_straight_wheel.append(10)
                                    Villain_Hand_Rank_straight_wheel.append(9)
                                    Villain_Hand_Rank_straight_wheel.append(0)

                                    if len(Villain_Hand_Rank_Flush) >= 1:
                                        if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[(v + 6), 'c']:
                                                if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                    (v + 5), 'c']:
                                                    if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                        (v + 4), 'c']:
                                                        if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            Villain_Hand_Rank_straight_wheel_flush.clear()

                                                            Villain_Hand_Rank_straight_wheel_flush.append(12)
                                                            Villain_Hand_Rank_straight_wheel_flush.append(11)
                                                            Villain_Hand_Rank_straight_wheel_flush.append(10)
                                                            Villain_Hand_Rank_straight_wheel_flush.append(9)
                                                            Villain_Hand_Rank_straight_wheel_flush.append(0)
                                                            break
                                    break



                v += 1

            if len(Villain_Hand_dict_sortforstraight) == 6:
                v = 0
                while v < 2:

                    if Villain_Hand_dict_sortforstraight.at[v, "a"] == 0:

                        if Villain_Hand_dict_sortforstraight.at[(v + 5), "a"] == 12:
                            if Villain_Hand_dict_sortforstraight.at[(v + 4), "a"] == 11:
                                if Villain_Hand_dict_sortforstraight.at[(v + 3), "a"] == 10:
                                    if Villain_Hand_dict_sortforstraight.at[(v + 2), "a"] == 9:

                                        f = 0
                                        Villain_Hand_Rank_straight_wheel.clear()

                                        Villain_Hand_Rank_straight_wheel.append(12)
                                        Villain_Hand_Rank_straight_wheel.append(11)
                                        Villain_Hand_Rank_straight_wheel.append(10)
                                        Villain_Hand_Rank_straight_wheel.append(9)
                                        Villain_Hand_Rank_straight_wheel.append(0)

                                        if len(Villain_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                    (v + 5), 'c']:
                                                    if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                        (v + 4), 'c']:
                                                        if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == \
                                                                    Villain_Hand_dict_sortforstraight.at[
                                                                        (v + 2), 'c']:
                                                                Villain_Hand_Rank_straight_wheel_flush.clear()

                                                                Villain_Hand_Rank_straight_wheel_flush.append(12)
                                                                Villain_Hand_Rank_straight_wheel_flush.append(11)
                                                                Villain_Hand_Rank_straight_wheel_flush.append(10)
                                                                Villain_Hand_Rank_straight_wheel_flush.append(9)
                                                                Villain_Hand_Rank_straight_wheel_flush.append(0)

                                                                break

                                        break

                v += 1
            if len(Villain_Hand_dict_sortforstraight) == 5:
                v = 0
                while v < 1:

                    if Villain_Hand_dict_sortforstraight.at[v, "a"] == 0:

                        if Villain_Hand_dict_sortforstraight.at[(v + 4), "a"] == 12:
                            if Villain_Hand_dict_sortforstraight.at[(v + 3), "a"] == 11:
                                if Villain_Hand_dict_sortforstraight.at[(v + 2), "a"] == 10:
                                    if Villain_Hand_dict_sortforstraight.at[(v + 1), "a"] == 9:

                                        f = 0
                                        Villain_Hand_Rank_straight_wheel.clear()

                                        Villain_Hand_Rank_straight_wheel.append(12)
                                        Villain_Hand_Rank_straight_wheel.append(11)
                                        Villain_Hand_Rank_straight_wheel.append(10)
                                        Villain_Hand_Rank_straight_wheel.append(9)
                                        Villain_Hand_Rank_straight_wheel.append(0)

                                        if len(Villain_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                    (v + 3), 'c']:
                                                    if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                            (v + 2), 'c']:
                                                            if Suit_for_straight == \
                                                                    Villain_Hand_dict_sortforstraight.at[
                                                                        (v + 1), 'c']:
                                                                Villain_Hand_Rank_straight_wheel_flush.clear()

                                                                Villain_Hand_Rank_straight_wheel_flush.append(12)
                                                                Villain_Hand_Rank_straight_wheel_flush.append(11)
                                                                Villain_Hand_Rank_straight_wheel_flush.append(10)
                                                                Villain_Hand_Rank_straight_wheel_flush.append(9)
                                                                Villain_Hand_Rank_straight_wheel_flush.append(0)

                                                                break

                                        break
                v += 1
            if len(Villain_Hand_dict_sortforstraight) == 4:
                break
            if len(Villain_Hand_dict_sortforstraight) == 3:
                break


        q += 1
    q = 0



    f=0
    q = 0
    v = 0

    while q < 9:

        if len(Villain_Hand_dict_sortforstraight) == 7:
            v = 0
            while v < 3:

                if Villain_Hand_dict_sortforstraight.at[v, "a"] == q:

                    if Villain_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                        if Villain_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                            if Villain_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                if Villain_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                    f = 0
                                    Villain_Hand_Rank_straight.clear()

                                    Villain_Hand_Rank_straight.append(q)
                                    Villain_Hand_Rank_straight.append(q + 1)
                                    Villain_Hand_Rank_straight.append(q + 2)
                                    Villain_Hand_Rank_straight.append(q + 3)
                                    Villain_Hand_Rank_straight.append(q + 4)

                                    if len(Villain_Hand_Rank_Flush) >= 1:
                                        if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[v, 'c']:
                                            if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                (v + 1), 'c']:
                                                if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                    (v + 2), 'c']:
                                                    if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                        (v + 3), 'c']:
                                                        if Suit_for_straight == \
                                                                Villain_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                            Villain_Hand_Rank_straight_flush.clear()

                                                            Villain_Hand_Rank_straight_flush.append(q)
                                                            Villain_Hand_Rank_straight_flush.append(q + 1)
                                                            Villain_Hand_Rank_straight_flush.append(q + 2)
                                                            Villain_Hand_Rank_straight_flush.append(q + 3)
                                                            Villain_Hand_Rank_straight_flush.append(q + 4)

                                                            if q == 0:
                                                                VillainHand_Rank_Royal_Flush.clear()
                                                                VillainHand_Rank_Royal_Flush.append(0)
                                                                VillainHand_Rank_Royal_Flush.append(1)
                                                                VillainHand_Rank_Royal_Flush.append(2)
                                                                VillainHand_Rank_Royal_Flush.append(3)
                                                                VillainHand_Rank_Royal_Flush.append(4)
                                                                break
                                                            break
                                    break


                v += 1
            q+=1

            if len(Villain_Hand_dict_sortforstraight) == 6:
                v=0
                while v < 2:

                    if Villain_Hand_dict_sortforstraight.at[v, "a"] == q:

                        if Villain_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                            if Villain_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                                if Villain_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                    if Villain_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                        f = 0
                                        Villain_Hand_Rank_straight.clear()

                                        Villain_Hand_Rank_straight.append(q)
                                        Villain_Hand_Rank_straight.append(q + 1)
                                        Villain_Hand_Rank_straight.append(q + 2)
                                        Villain_Hand_Rank_straight.append(q + 3)
                                        Villain_Hand_Rank_straight.append(q + 4)

                                        if len(Villain_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[(v + 1), 'c']:
                                                    if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                        (v + 2), 'c']:
                                                        if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                                (v + 4), 'c']:

                                                                Villain_Hand_Rank_straight_flush.clear()

                                                                Villain_Hand_Rank_straight_flush.append(q)
                                                                Villain_Hand_Rank_straight_flush.append(q + 1)
                                                                Villain_Hand_Rank_straight_flush.append(q + 2)
                                                                Villain_Hand_Rank_straight_flush.append(q + 3)
                                                                Villain_Hand_Rank_straight_flush.append(q + 4)

                                                                if q == 0:
                                                                    VillainHand_Rank_Royal_Flush.clear()
                                                                    VillainHand_Rank_Royal_Flush.append(0)
                                                                    VillainHand_Rank_Royal_Flush.append(1)
                                                                    VillainHand_Rank_Royal_Flush.append(2)
                                                                    VillainHand_Rank_Royal_Flush.append(3)
                                                                    VillainHand_Rank_Royal_Flush.append(4)

                                                            break

                                        break


                    v+=1

            if len(Villain_Hand_dict_sortforstraight) == 5:
                v=0
                while v < 1:


                    if Villain_Hand_dict_sortforstraight.at[v, "a"] == q:

                        if Villain_Hand_dict_sortforstraight.at[(v + 1), "a"] == q + 1:
                            if Villain_Hand_dict_sortforstraight.at[(v + 2), "a"] == q + 2:
                                if Villain_Hand_dict_sortforstraight.at[(v + 3), "a"] == q + 3:
                                    if Villain_Hand_dict_sortforstraight.at[(v + 4), "a"] == q + 4:

                                        f = 0
                                        Villain_Hand_Rank_straight.clear()

                                        Villain_Hand_Rank_straight.append(q)
                                        Villain_Hand_Rank_straight.append(q + 1)
                                        Villain_Hand_Rank_straight.append(q + 2)
                                        Villain_Hand_Rank_straight.append(q + 3)
                                        Villain_Hand_Rank_straight.append(q + 4)

                                        if len(Villain_Hand_Rank_Flush) >= 1:
                                            if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[v, 'c']:
                                                if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                    (v + 1), 'c']:
                                                    if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                        (v + 2), 'c']:
                                                        if Suit_for_straight == Villain_Hand_dict_sortforstraight.at[
                                                            (v + 3), 'c']:
                                                            if Suit_for_straight == \
                                                                    Villain_Hand_dict_sortforstraight.at[(v + 4), 'c']:

                                                                Villain_Hand_Rank_straight_flush.clear()

                                                                Villain_Hand_Rank_straight_flush.append(q)
                                                                Villain_Hand_Rank_straight_flush.append(q + 1)
                                                                Villain_Hand_Rank_straight_flush.append(q + 2)
                                                                Villain_Hand_Rank_straight_flush.append(q + 3)
                                                                Villain_Hand_Rank_straight_flush.append(q + 4)

                                                                if q == 0:
                                                                    VillainHand_Rank_Royal_Flush.clear()
                                                                    VillainHand_Rank_Royal_Flush.append(0)
                                                                    VillainHand_Rank_Royal_Flush.append(1)
                                                                    VillainHand_Rank_Royal_Flush.append(2)
                                                                    VillainHand_Rank_Royal_Flush.append(3)
                                                                    VillainHand_Rank_Royal_Flush.append(4)

                                                                break

                                        break
            if len(Villain_Hand_dict_sortforstraight) == 4:
                break
            if len(Villain_Hand_dict_sortforstraight) == 3:
                break


        q += 1




    Villain_Hand_dict_sortforpair["index"] = Villain_Hand_index
    Villain_Hand_dict_sortforpair.set_index("index", inplace=True)

    c = 0

    if Villain_Hand_dict_sortforpair.at[0, "b"] == 1:
        Villain_Hand_Rank.clear()
        Villain_Hand_Rank.append(10)
        Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[6, "a"])
        Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[5, "a"])
        Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[4, "a"])
        Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[3, "a"])
        Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[2, "a"])

    if Villain_Hand_dict_sortforpair.at[0, "b"] == 2:
        if Villain_Hand_dict_sortforpair.at[1, "b"] == 1:
            Villain_Hand_Rank.clear()
            Villain_Hand_Rank.append(9)
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[0, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[5, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[4, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[3, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[2, "a"])

    if Villain_Hand_dict_sortforpair.at[0, "b"] == 2:
        if Villain_Hand_dict_sortforpair.at[1, "b"] == 2:
            if Villain_Hand_dict_sortforpair.at[2, "b"] == 2:

                Villain_Hand_Rank.clear()
                Villain_Hand_Rank.append(8)
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[2, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[1, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[0, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[3, "a"])


    if Villain_Hand_dict_sortforpair.at[0, "b"] == 2:
        if Villain_Hand_dict_sortforpair.at[1, "b"] == 2:
            if Villain_Hand_dict_sortforpair.at[2, "b"] == 1:

                Villain_Hand_Rank.clear()
                Villain_Hand_Rank.append(8)
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[1, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[0, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[4, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[3, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[2, "a"])

    if Villain_Hand_dict_sortforpair.at[0, "b"] == 3:
        if Villain_Hand_dict_sortforpair.at[1, "b"] == 1:
            Villain_Hand_Rank.clear()
            Villain_Hand_Rank.append(7)
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[0, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[4, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[3, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[2, "a"])



    if len(Villain_Hand_Rank_straight) >=1:
        Villain_Hand_Rank.clear()
        Villain_Hand_Rank.append(6)
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight[0])
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight[1])
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight[2])
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight[3])
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight[4])

    if len(Villain_Hand_Rank_Flush) >= 1:
        Villain_Hand_Rank.clear()
        Villain_Hand_Rank.append(5)
        Villain_Hand_Rank.append(Villain_Hand_Rank_Flush[0])
        Villain_Hand_Rank.append(Villain_Hand_Rank_Flush[1])
        Villain_Hand_Rank.append(Villain_Hand_Rank_Flush[2])
        Villain_Hand_Rank.append(Villain_Hand_Rank_Flush[3])
        Villain_Hand_Rank.append(Villain_Hand_Rank_Flush[4])

    if Villain_Hand_dict_sortforpair.at[0, "b"] == 3:
        if Villain_Hand_dict_sortforpair.at[1, "b"] == 2:
            if Villain_Hand_dict_sortforpair.at[2, "b"] == 1:
                Villain_Hand_Rank.clear()
                Villain_Hand_Rank.append(4)
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[0, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[1, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[3, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[2, "a"])

    if Villain_Hand_dict_sortforpair.at[0, "b"] == 3:
        if Villain_Hand_dict_sortforpair.at[1, "b"] == 2:
            if Villain_Hand_dict_sortforpair.at[2, "b"] == 2:
                Villain_Hand_Rank.clear()
                Villain_Hand_Rank.append(4)
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[0, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[2, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[1, "a"])


    if Villain_Hand_dict_sortforpair.at[0, "b"] == 3:
        if Villain_Hand_dict_sortforpair.at[1, "b"] == 3:
            if Villain_Hand_dict_sortforpair.at[2, "b"] == 1:
                Villain_Hand_Rank.clear()
                Villain_Hand_Rank.append(4)
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[1, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[0, "a"])
                Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[2, "a"])





    if Villain_Hand_dict_sortforpair.at[0, "b"] == 4:
        if Villain_Hand_dict_sortforpair.at[1, "b"] == 1:
            Villain_Hand_Rank.clear()
            Villain_Hand_Rank.append(3)
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[0, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[3, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[2, "a"])

    if Villain_Hand_dict_sortforpair.at[0, "b"] == 4:
        if Villain_Hand_dict_sortforpair.at[1, "b"] == 2:
            Villain_Hand_Rank.clear()
            Villain_Hand_Rank.append(3)
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[0, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[2, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[1, "a"])

    if Villain_Hand_dict_sortforpair.at[0, "b"] == 4:
        if Villain_Hand_dict_sortforpair.at[1, "b"] == 3:
            Villain_Hand_Rank.clear()
            Villain_Hand_Rank.append(3)
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[0, "a"])
            Villain_Hand_Rank.append(Villain_Hand_dict_sortforpair.at[1, "a"])



    if len(Villain_Hand_Rank_straight_wheel_flush) >= 1:
        Villain_Hand_Rank.clear()
        Villain_Hand_Rank.append(2)
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight_wheel_flush[0])
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight_wheel_flush[1])
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight_wheel_flush[2])
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight_wheel_flush[3])
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight_wheel_flush[4])








    if len(Villain_Hand_Rank_straight_flush) >= 1:
        Villain_Hand_Rank.clear()
        Villain_Hand_Rank.append(2)
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight_flush[0])
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight_flush[1])
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight_flush[2])
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight_flush[3])
        Villain_Hand_Rank.append(Villain_Hand_Rank_straight_flush[4])

    if len(VillainHand_Rank_Royal_Flush) >= 1:
        Villain_Hand_Rank.clear()
        Villain_Hand_Rank.append(1)
        Villain_Hand_Rank.append(VillainHand_Rank_Royal_Flush[0])
        Villain_Hand_Rank.append(VillainHand_Rank_Royal_Flush[1])
        Villain_Hand_Rank.append(VillainHand_Rank_Royal_Flush[2])
        Villain_Hand_Rank.append(VillainHand_Rank_Royal_Flush[3])
        Villain_Hand_Rank.append(VillainHand_Rank_Royal_Flush[4])

    if small_blind_card1[1] == small_blind_card2[1]:
        villain_SO = 's'
    elif small_blind_card1[0] == small_blind_card2[0]:
        villain_SO = ''
    else:
        villain_SO = 'o'

    if Button_card1[1] == Button_card2[1]:
        hero_SO = 's'
    elif Button_card1[0] == Button_card2[0]:
        hero_SO = ''
    else:
        hero_SO = 'o'
    y=0

    villain_hand_val = []
    while y < 13:

        if cards_value_df.at[y, "card_values"] == small_blind_card1[0]:

            villain_hand_val.append(cards_value_df.at[y, "card_values"])


        if cards_value_df.at[y, "card_values"] == small_blind_card2[0]:

            villain_hand_val.append(cards_value_df.at[y, "card_values"])
        y+=1
    y = 0
    while y < 13:

        if cards_value_df.at[y, "card_values"] == Button_card1[0]:

            hero_hand_val.append(cards_value_df.at[y, "card_values"])

        if cards_value_df.at[y, "card_values"] == Button_card2[0]:

            hero_hand_val.append(cards_value_df.at[y, "card_values"])
        y += 1
    y=0


    hero_hand_val.append(hero_SO)



    villain_hand_val.append(villain_SO)


    rel_hero_hand = ''.join([str(elem) for elem in hero_hand_val])
    rel_villain_hand = ''.join([str(elem) for elem in villain_hand_val])

    print("hero:", rel_hero_hand)
    print("villain: ", rel_villain_hand)


    Hero_Rank = Hero_Hand_Rank
    Villain_Rank = Villain_Hand_Rank

    Villain_Rank_card = []
    Hero_Rank_card = []

    if Hero_Rank[0] == 10:
        Hero_Rank_card.append("High Card")
    if Hero_Rank[0] == 9:
        Hero_Rank_card.append("Pair")
    if Hero_Rank[0] == 8:
        Hero_Rank_card.append("Two Pair")
    if Hero_Rank[0] == 7:
        Hero_Rank_card.append("Three of a Kind")
    if Hero_Rank[0] == 6:
        Hero_Rank_card.append("Straight")
    if Hero_Rank[0] == 5:
        Hero_Rank_card.append("Flush")
    if Hero_Rank[0] == 4:
        Hero_Rank_card.append("Full House")
    if Hero_Rank[0] == 3:
        Hero_Rank_card.append("Four of a Kind")
    if Hero_Rank[0] == 2:
        Hero_Rank_card.append("Straight Flush")
    if Hero_Rank[0] == 1:
        Hero_Rank_card.append("Royal Flush")

    if Villain_Rank[0] == 10:
        Villain_Rank_card.append("High Card")
    if Villain_Rank[0] == 9:
        Villain_Rank_card.append("Pair")
    if Villain_Rank[0] == 8:
        Villain_Rank_card.append("Two Pair")
    if Villain_Rank[0] == 7:
        Villain_Rank_card.append("Three of a Kind")
    if Villain_Rank[0] == 6:
        Villain_Rank_card.append("Straight")
    if Villain_Rank[0] == 5:
        Villain_Rank_card.append("Flush")
    if Villain_Rank[0] == 4:
        Villain_Rank_card.append("Full House")
    if Villain_Rank[0] == 3:
        Villain_Rank_card.append("Four of a Kind")
    if Villain_Rank[0] == 2:
        Villain_Rank_card.append("Straight Flush")
    if Villain_Rank[0] == 1:
        Villain_Rank_card.append("Royal Flush")

    x=0

    y=0
    if len(Hero_Rank) < len(Villain_Rank):
        x=0
        while x < len(Hero_Rank):
            if Hero_Rank[x] < Villain_Rank[x]:
                Win_Lose_Tie = 1
                break
            elif Hero_Rank[x] > Villain_Rank[x]:
                Win_Lose_Tie = -1
                break
            else:
                Win_Lose_Tie = 0
                x+=1

    if len(Hero_Rank) > len(Villain_Rank):
        x=0
        while x < len(Villain_Rank):
            if Hero_Rank[x] < Villain_Rank[x]:
                Win_Lose_Tie = 1
                break
            elif Hero_Rank[x] > Villain_Rank[x]:
                Win_Lose_Tie = -1
                break
            else:
                Win_Lose_Tie = 0
                x+=1


    if len(Hero_Rank) == len(Villain_Rank):
        x=0
        while x < len(Hero_Rank):
            if Hero_Rank[x] < Villain_Rank[x]:
                Win_Lose_Tie = 1
                break
            elif Hero_Rank[x] > Villain_Rank[x]:
                Win_Lose_Tie = -1
                break
            else:
                Win_Lose_Tie = 0
                x+=1





    print("WLT", Win_Lose_Tie)

    def append_list_as_row(file_name, list_of_elem):
        # Open file in append mode
        with open("PokerHandData1.csv", 'a+', newline='') as write_obj:
            # Create a writer object from csv module
            csv_writer = writer(write_obj)
            # Add contents of list as last row in the csv file
            csv_writer.writerow(list_of_elem)



    New_Row = [l, (Button_card1,Button_card2), (small_blind_card1,small_blind_card2), (rel_hero_hand), (rel_villain_hand), Flop_card1, Flop_card2, Flop_card3, Turn, River, Hero_Rank_card,
               Villain_Rank_card, Win_Lose_Tie]
    append_list_as_row("PokerHandData1.csv", New_Row)

    # In[ ]:

    Hero_Rank_card.clear()
    Villain_Rank_card.clear()
    print(l)

    l+=1


# In[ ]:
