import random, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')
#logging.disable(logging.CRITICAL)
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug('guess is: (%s)' %(guess))
tos1 = random.randint(0,1) # 0 is tails, 1 is heads

if tos1 == 0:
    toss='tails'
else:
    toss='heads'
logging.debug('toss is: %s'%(toss))
if toss == guess:
    logging.debug('toss is: (%s)'%(toss))
    logging.debug('guess is: (%s)'%(guess))
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')