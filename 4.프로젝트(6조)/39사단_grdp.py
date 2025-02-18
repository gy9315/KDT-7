import pandas as pd
import pymysql as pl
from tabulate import tabulate
import matplotlib.pyplot as plt
import koreanize_matplotlib
conn=pl.connect(host='localhost',user='root',password='1234',db='economic_condition')
cur=conn.cursor(pl.cursors.DictCursor)
sql2='''
select * from army_grdp'''
cur.execute(sql2)
row=cur.fetchall()
grdpDF=pd.DataFrame(row)
cur.close()
conn.close()
grdpDF.rename(columns={'경제활동별(1)':'구분'},inplace=True)
# # # 2015년
창원DF=grdpDF[(grdpDF['주소']=='경상남도 창원시')]
함안DF=grdpDF[(grdpDF['주소']=='경상남도 함안군')]
의령DF=grdpDF[(grdpDF['주소']=='경상남도 의령군')]
print(창원DF)
army_27DF=pd.concat([창원DF.iloc[:,:].reset_index(drop=True),함안DF.iloc[:,:].reset_index(drop=True),의령DF.iloc[:,:].reset_index(drop=True)])
army_27DF.dropna(axis=1,inplace=True)
army_27DF.reset_index(drop=True,inplace=True)
print(army_27DF)
fig,axes=plt.subplots(1,3,figsize=(30,5), constrained_layout=True)
plt.suptitle('39사단 이전 전 지역과 이전 후 지역과 주변지역 비교',size=15)
colors=['red','blue','purple']
titles=['지역내총생산','숙박 및 음식집 총생산']
print(army_27DF['주소'])
print(3//2)
for x in range(army_27DF.shape[0]):
    if x%2==0:    
        axes[x//2].bar(army_27DF.columns[3:].astype('int')*2,army_27DF.iloc[x][3:],label=titles[0],color='green')       
        axes[x//2].set_xticks((army_27DF.columns[3:].astype('int')*2)+0.4, army_27DF.columns[3:].str[2:])
        axes[x//2].set_title(army_27DF['주소'][x].split(' ')[1])
        axes[x//2].axvline(x=2008*2+0.4, color='k', linestyle='--', linewidth=2, label='착공연도')
        axes[x//2].axvline(x=2015*2+0.4, color='r', linestyle='--', linewidth=2, label='이전연도')
    else:
        axes1=axes[x//2].twinx()
        axes1.bar((army_27DF.columns[3:].astype('int')*2)+0.8,army_27DF.iloc[x][3:],label=titles[1],color='yellow',edgecolor='k')
        axes1.set_ylabel(titles[1])
        axes1.legend(loc=1)

    axes[x//2].set_xlabel('연도')
    axes[x//2].set_ylabel(titles[0])
    axes[x//2].legend()
plt.show()

