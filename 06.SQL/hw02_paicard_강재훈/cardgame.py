from card import Card
from player import Player
from gamedealer import Gamedealer

def play_game():
    # 두명의 player객체 생성
    player1=Player('흥부')
    player2=Player('놀부')
    dealer=Gamedealer()
    dealer.make_deck()
    print('='*100)
    print(f'카드 나누어 주기: 10장')
    print('-'*100)
    a,b=dealer.distribute_card(10)
    print()
    print('='*100)
    player1.add_card_list(a)
    player2.add_card_list(b)
    player1.check_one_pair_card()
    player1.display_two_card_lists()
    player2.check_one_pair_card()
    player2.display_two_card_lists()
    player1.print_status_card()
    print('='*100)
    player2.print_status_card()


play_game()
