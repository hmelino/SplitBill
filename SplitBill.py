class Brunch:
	activities=[]
	mainDic={}
	db={}
	
	def processIt(self):
		db=Brunch.db
		for user in db.keys():
			credit=sum([v for v in db[user].values() if isinstance(v,int)])
			for activ in db[user].keys():
				q=db[user][activ]
				if q!=None:
					fee=Brunch.mainDic[activ][2]
					credit-=fee
			print(f"Result for {user} is {round(credit,2)}")
					
	def __init__(self,*args):
		Brunch.activities=list(args)
		Brunch.mainDic={a:[0,0,0] for a in list(args)}
	
	def addPerson(self,name,*activity):
		activList=list(activity)
		Brunch.db[name]={Brunch.activities[v]:activList[v] for v in range(len(activList))}
		for a in range(len(activity)):
			if isinstance(activity[a],int):
					
				#create dictionary of activities with amount of people and total price
				Brunch.mainDic[Brunch.activities[a]][0]+=1
				Brunch.mainDic[Brunch.activities[a]][1]+=list(activity)[a]
				people,price,p=Brunch.mainDic[Brunch.activities[a]]
					
				#count price of activity per person
				Brunch.mainDic[Brunch.activities[a]][2]=price/people
		
o=Brunch("prosseco","karaoke1","karaoke2")
o.addPerson("Matus",33,0,0)
o.addPerson("Mimi",0,0,None)
o.addPerson("Surag",0,180,80)
o.addPerson("Izzi",0,0,0)
o.processIt()
