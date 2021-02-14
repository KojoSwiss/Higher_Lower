from art import logo, vs
from game_data import data
import random
from replit import clear

print(logo)
q2 = random.choice(data)
game_over = False
score = 0

while game_over == False:
  q1 = q2
  q2 =random.choice(data)
  if q1['name'] == q2['name']:
    q2 = random.choice(data)

  def format_account(account):
    """Takes a account and returns a format"""
    return(f'{account["name"]} from {account["country"]} is a {account["description"]}')
  def check_guess(first,second):
    if first['follower_count'] > second['follower_count']:
      guess = 'A'
      return guess
    else:
      guess = 'B'
      return guess

  print(f'Compare {format_account(q1)}')
  print(vs)
  print(f'Compare {format_account(q2)}')

  guess = (input('Who has more followers? A or B\n')).lower()

  q1_followers = q1['follower_count']
  q2_followers = q2['follower_count']
  correct_ans = (check_guess(q1,q2)).lower()
  clear()
  print(logo)
  if guess == correct_ans.lower():
    score += 1
    print(f'Correct!! your score is {score}')
  else:
    print(f'Wrong your score is {score}')
    try_again = input('yes or no')
    if try_again == 'no':
      game_over = True
    else:
      game_over = False
