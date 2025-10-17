import pandas as pd
data={'rollno':[1,2,3,4,5,6,7,8,9,10],
		'name':['teja','sree','sidhu','laxmi','amar','sai','hemanth','siva','kumar','hyma'],
		'age':[18,19,16,22,21,20,19,18,18,20],
		'branch':['CSE','ECE','AIDS','EEE','MECH','CIVIL','AIML','CSE','ECE','EEE'],
		'Marks':[94,90,98,75,67,54,87,92,57,88]	
		}
df=pd.DataFrame(data)
print(df)
print("using head function:\n",df.head())
print("using tail function:\n",df.tail())
print("Details in branch column:\n",df["branch"])
print("Details in name,branch,age column:\n",df[["name", "age", "branch"]])
print("Details in single row:\n",df.iloc[4])
print("Details in multiple rows:\n",df[4:9])

