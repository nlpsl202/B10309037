score1 = int(input('第一次考試成績\n'))
score2 = int(input('第二次考試成績\n'))
score3 = int(input('第三次考試成績\n'))
score = [score1 , score2 , score3]
sorted(score)
score.sort()
x=score[0]*0.2+score[1]*0.3+score[2]*0.5
print ('你的期末成績是%s' %x)
