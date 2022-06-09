def average_calculate(list):
	n=len(list)
	sum=0
	for i in list:
		sum=sum+i
	average=(sum)/n
	return average

def speed_calculate(distance,time):
	if distance==0 or time==0:
		speed=0
		return speed
	else:
		speed=distance/time
	return speed

def addition(list):
	sum=0
	for i in list:
		sum=sum+i
	return sum

def simple_interest(p,t,r):
	return (p*t*r)/100
