score = {}
score[('spot', 'pot')] = 3
score[('', 'a')] = 0
score[('maps', 'spam')] = 1

print( score[('', 'a')] in score and 'spot' in score )

print( max(score[('spot', 'pot')], score[('maps', 'spam')]) ) 
