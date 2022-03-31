#! /user/bin/python3
# -*- coding:utf-8 -*-
# @Author  : Paul C G LUO
# @Email   : 673951437@qq.com
# @DateTime: 2022/3/31 17:02
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    # beer_card = Card('7', 'diamonds')
    # print(beer_card)

    deck = FrenchDeck()
    # print(len(deck))
    #
    # print(deck[-1])
    from random import choice

    # for i in range(5):
    #     print(choice(deck))

    # print(deck[:3])

    # 反向迭代
    # for card in reversed(deck):
        # print(card)

    # print(Card("2", "hearts") in deck)

    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    print(len(suit_values))

    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        print("rank_value:", rank_value)
        print("rank_value * len(suit_values) + suit_values[card.suit]:", rank_value * len(suit_values) + suit_values[card.suit])
        return rank_value * len(suit_values) + suit_values[card.suit]


    for card in sorted(deck, key=spades_high):
        print(card)


