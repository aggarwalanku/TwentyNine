from server import server
from score import score

if __name__ == "__main__":
	s, c = server(), score()
	d = s.CreatePile()
	for x in d:
		print [ str(t) for t in x ]
		print c.PileScore( x )
	bet=16
	p1=1
	p2=2
	option_player2 = ''
	while (bet<=29 and p2<5):
			print "Bet=",bet
			print "Player",p1
			print option_player2
			if (option_player2 != '3'):
				if (bet!=16):
					option=raw_input("Enter your options :1.Bet 2.Stay 3.Pass")
				else:
					option=raw_input("Enter your options :1.Bet 2.pass")	
				print option
				if (option=='1' and option_player2 != '3'):
					bet1 = int(raw_input("Enter your bet : "))
					if (bet1<=bet):
						print "Invalid Input"
						continue
					else:
						bet=bet1	
				elif ((option == '3' and bet != 16 ) or (option == '2' and bet == 16)):
					p1,p2 = p2,p2+1	

					
			print "Player",p2
			option_player2=raw_input("Enter your options :1.Bet 3.Pass")
			if (option_player2 == '1'):
				bet_player2 = int(raw_input("Enter your bet player2:"))
				if(bet_player2<=bet):
					print "Invalid Input"
				else:
					bet = bet_player2	
			else:
				p2=p2+1
	print bet,p1






