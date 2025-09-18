#name: Jude Martin
#class: 5th hour
#assighnment: playground
import random





players=["bryson" , "eli" , "aiden" , "alden" , "julian" , "ivan" , "huntar" , "statham" , "gabe"]
bullets=[0,0,0,0,0,0,0,0,1]
print(players)
next_player=(random.choice(players))
print(next_player)
players.remove(next_player)
print(players)
print(bullets)
next_bullet=(random.choice(bullets))
print(next_bullet)
bullets.remove(next_bullet)
print(bullets)


import random
magic_8_ball=["yes","no","maybe","perchance","nuh uh monkey","hell no never in a million years","fine I guess"]
random.shuffle(magic_8_ball)
print(magic_8_ball)
print(random.choice(magic_8_ball))






