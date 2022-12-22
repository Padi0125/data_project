import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('20221216파이썬job_list.csv', encoding='utf-8')

def app1():
    cont = len(df.loc[df['경력'] == '경력무관'])
    not_cont = len(df.loc[df['경력'] != '경력무관'])
    tit = ["경력무관","경력자"]
    values = [cont,not_cont]

    print(tit,values)
    
    plt.rc('font', family='Malgun Gothic')

    plt.rcParams['axes.unicode_minus'] = False

    plt.title('경력자 비율')
    plt.pie(values, labels=tit, autopct='%.1f%%')
    
    plt.legend(tit)

    plt.show()

app1()

def app2():
    cont = len(df.loc[(df['학력'] == '학력무관') | (df['학력']=='고졸↑')])
    not_cont = len(df.loc[(df['학력'] != '학력무관') & (df['학력']!='고졸↑') & (df['학력']!='null')])
    tit = ["초대졸↑","학력무관 & 고졸↑"]
    values = [not_cont,cont]

    print(tit,values)
    
    plt.rc('font', family='Malgun Gothic')

    plt.rcParams['axes.unicode_minus'] = False

    plt.title('학력 비율')
    plt.pie(values, labels=tit, autopct='%.1f%%')
    
    plt.legend(tit)

    plt.show()

app2()

def app3():
    cont = len(df.loc[((df['학력'] == '학력무관') | (df['학력']=='고졸↑')) & (df['경력']=='경력무관')])
    not_cont = len(df.loc[(df['학력'] != '학력무관') & (df['학력']!='고졸↑') & (df['학력']!='null') & (df['경력']!='경력무관')])
    tit = ["지원 불가","지원 가능"]
    values = [not_cont,cont]

    print(tit,values)
    
    plt.rc('font', family='Malgun Gothic')

    plt.rcParams['axes.unicode_minus'] = False

    plt.title('학력&경력 비율')
    plt.pie(values, labels=tit, autopct='%.1f%%')
    
    plt.legend(tit)

    plt.show()

app3()