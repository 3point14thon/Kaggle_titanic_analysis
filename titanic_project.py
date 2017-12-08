#A challenge taken from Kaggle.com as one of thier starter projects

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def main():
    dfrealdat = pd.read_csv('test.csv')
    dftraintest = pd.read_csv('train.csv')
    #filling in the only missing value in the real data manually
    dfrealdat.at[152, 'Fare'] = dfrealdat[dfrealdat.Pclass == 3].Fare.mean()

    dftraintest = clean(dftraintest)
    train_test(dftraintest)

def clean(df):
    #I have elected to use front fill for replacing nan values for Age.
    #Using front fill has the benefit of filling in missing data in a way
    #that should increase any age group in a proportional way given that
    #there arn't too many consecutive blanks. Looking through the training
    #data the most I could find were four blanks.

    #There are only two missing values in Embarked and they are not next to
    #eachother. Using ffill seems like it would introduce a negligable bias
    df.Age = df.Age.ffill()
    df.Embarked = df.Embarked.ffill()
    #Droping Name, although Name could be usfull in telling relations between
    #people it would require a large amount of work to parse that data and
    #should be done only if the results require more pressision
    
    #Droping Ticket and PassengerId, these features could be more usefull with
    #research into how they are determined but in thier raw state add  little
    
    #Droping Cabin, there are too many cabin numbers missing for this to be
    #a reliable feature.

    df = df.drop(['Name', 'Ticket', 'Cabin', 'PassengerId'],axis=1)
    #encodeing Sex and Embarked
    df.Sex = df.Sex.replace('female', 0)
    df.Sex = df.Sex.replace('male', 1)
    #For EDA...df.Embarked = df.Embarked.astype('category').cat.codes
    df = pd.get_dummies(df,columns=['Embarked'])
    #Pclass and Fare and SibSp and Parch have abs(r~0.5) possably dependent
    #corr = df.corr()
    #print corr
    return df

def train_test(x):
    y = x.iloc[:,0]
    x = x.drop('Survived',axis=1)
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.03,random_state=26)
    
    min_max = MinMaxScaler()
    x_test = min_max.fit_transform(x_test) 
    x_train = min_max.fit_transform(x_train)

    model = KNeighborsClassifier(n_neighbors=4)
    model.fit(x_train, y_train)
    print accuracy_score(y_test,model.predict(x_test))


def EDA(df,column):
    plt.figure()
    prep = df[df.Survived== 1]
    plt.hist(df[column].dropna(),alpha=0.5)
    plt.hist([prep[column].dropna()],alpha=0.5)
    plt.title(column)
#    print(len(df[column]) - len(df[column].dropna()))
#    print(df[column].dropna().mean())  

def cohend(mean1,mean2,pooledstd):
    return (mean1 - mean2)/pooledstd

main()
