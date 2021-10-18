import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")
print(df.dtypes)
print("DF AT FIRST!")
print(df.query("weight / ((height/100) **2) > 25 " ))

print()
# Add 'overweight' column
df['overweight'] = 1
# df.query("weight / ((height/100) **2) > 25 ")["overweight"] = 1
df["overweight"].where((df["weight"]/((df["height"]/100)**2)) > 25 , 0,inplace = True)
print("df DEBU ",df["cholesterol"])

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"].where( df["cholesterol"]> 1, 0,inplace = True)
df["cholesterol"].where( df["cholesterol"] == 0 , 1,inplace = True)
df["gluc"].where( df["gluc"]> 1, 0,inplace = True)
df["gluc"].where( df["gluc"]== 0, 1,inplace = True)


print("df CHOLESTEROL")
print(df[["cholesterol","gluc"]])
# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df,
            id_vars=["cardio"], 
            value_vars=[ 'active','alco', "cholesterol","gluc",'overweight', 'smoke'], 
            var_name=None, 
            value_name='value', 
            col_level=None)
    print("DF_CAT",df_cat)
    print(df_cat[["value","cardio"]])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    # df_cat = df.groupby("cardio")
    # titanic = sns.load_dataset("titanic")
    

    # Draw the catplot with 'sns.catplot()'
    # fig = sns.catplot(x = "variable" , y = "value",hue = 'value',col = "cardio",data = df_cat,kind="bar")
    fig = plt.figure()
    
    fig = sns.catplot(x = "variable", hue = 'value',col = "cardio",data = df_cat,kind="count")
    # ax = sns.catplot(x = "variable", hue = 'value',col = "cardio",data = df_cat,kind="count").axes
    fig.set_axis_labels('variable', 'total')
    fig=fig.fig
    # ax.set(ylabel = "total")
    # fig = sns.catplot(x = "valiable",col = "cardio",data = df_cat,kind="count")
    # print("catplotfigprint",ax[0])
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
#https://cocoinit23.com/pandas-query-multi/
#https://happy-analysis.com/wp2/python/python-topic-var-in-query.html
#https://qiita.com/hiroyuki_kageyama/items/00d0f52724f16ad7cf77#%E3%82%AB%E3%83%A9%E3%83%BC%E3%83%90%E3%83%BC%E3%81%AE%E7%AF%84%E5%9B%B2%E6%8C%87%E5%AE%9A--vminvmax
#https://qiita.com/waytodatascientist/items/5075e263179d9937f435
#https://note.nkmk.me/python-seaborn-heatmap/
#https://note.nkmk.me/python-pandas-corr/
#https://note.nkmk.me/python-pandas-quantile/


def draw_heat_map():
    # Clean the data
    # df_heat = df

    height_min = df["height"].quantile(0.025)
    height_max = df["height"].quantile(0.975)
    weight_min = df["weight"].quantile(0.025)
    weight_max = df["weight"].quantile(0.975)
    df_heat = df.query("@height_min <= height <= @height_max & @weight_min <= weight <= @weight_max  & ap_lo <= ap_hi")
    print("quantile",df_heat)

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))




    # Set up the matplotlib figure
    fig = plt.figure()
    ax2 = fig.add_subplot(1, 1, 1) # 明示的にAxesを作成する
    
    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr,mask = mask,annot=True,fmt="1.1f",center=0,
                linewidths=.5,ax=ax2)

    print("heatmapfigprint",fig)
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
