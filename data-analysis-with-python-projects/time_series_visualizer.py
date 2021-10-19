import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
#https://it-ojisan.tokyo/pandas-read_csv-datetime/
#https://www.yutaka-note.com/entry/pandas_read_csv
#https://pythondatascience.plavox.info/seaborn/%E6%A3%92%E3%82%B0%E3%83%A9%E3%83%95
df = pd.read_csv("fcc-forum-pageviews.csv",
                  names=("date","value"),
                  index_col="date",
                  parse_dates=True,
                  header=0,
)
print(df.dtypes)
print()
print(df)
print()

# Clean data

bottom = df["value"].quantile(0.025)
top = df["value"].quantile(0.975)
df = df.query("@bottom <= value <= @top")
print("df_clear",df)


def draw_line_plot():
    # Draw line plot
    #https://pythondatascience.plavox.info/matplotlib/%E6%8A%98%E3%82%8C%E7%B7%9A%E3%82%B0%E3%83%A9%E3%83%95
    #https://biotech-lab.org/articles/1638
    #https://pythondatascience.plavox.info/pandas/%E3%83%87%E3%83%BC%E3%82%BF%E3%83%95%E3%83%AC%E3%83%BC%E3%83%A0%E3%82%92%E7%A2%BA%E8%AA%8D
    fig= plt.figure()
    plt.plot(df)
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
# Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    #https://note.nkmk.me/python-pandas-time-series-multiindex/
    #https://note.nkmk.me/python-pandas-multiindex-set-reset-sort-swap/
    #https://note.nkmk.me/python-pandas-time-series-resample-asfreq/
    #https://stackoverflow.com/questions/19555525/saving-plots-axessubplot-generated-from-python-pandas-with-matplotlibs-savefi#:~:text=plot%20%3D%20dtf.plot()%0Afig%20%3D%20plot.get_figure()%0Afig.savefig(%22output.png%22)
    #https://qiita.com/takuto512/items/66e1257a471a07e841c4
    #https://samurait.hatenablog.com/entry/2014/01/16/matplotlib%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9%281%29#:~:text=plt.subplots()%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89%E3%81%AFFigure%2CAxesSubplot%E3%82%AA%E3%83%96%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%82%92%E3%82%BF%E3%83%97%E3%83%AB%E3%81%A7%E8%BF%94%E3%81%99%E3%81%AE%E3%81%A7%EF%BC%8C%20%E3%81%BE%E3%81%9AFigure%2CAxesSubplot%E3%82%AA%E3%83%96%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%82%92%E7%94%9F%E6%88%90%E3%81%97%E3%81%BE%E3%81%99%EF%BC%8E
    #https://forum.freecodecamp.org/t/page-view-time-series-visualizer-bar-chart/452072
    #https://pythondatascience.plavox.info/matplotlib/%e6%a3%92%e3%82%b0%e3%83%a9%e3%83%95


    # df_bar = df.copy()
    # print("Graph",df_bar.index.size)
    # print("Value",df_bar["value"].size)
    
    df_bar = df.set_index([df.index.year,df.index.month, df.index])
    df_bar.index.names=["year","month","date"]
    
    # print("df_bar",df_bar,df_bar.index)
    df_bar.reset_index(inplace=True)
    df_bar.set_index("date",inplace=True)
    df_bar_mean = df_bar.resample("M").mean()
    print("DF_bar",df_bar)
    print("DF_bar_resample",df_bar_mean)

    # df_test["year"] =df_test["year"].astype(str)
    # df_test["month"] =df_test["month"].astype(str)

    # date = pd.to_datetime(df_test["year"].str.cat(df_test["month"],sep="-"))

    # print("df_test",df_test)
    # print("date",date)
    # print("df_bar_mean",df_bar.mean(level=["year","month"]))

    # Draw bar plot
    fig,ax = plt.subplots(1, figsize=(20,10))
    bar = sns.barplot(data=df_bar, x="year", y="value", hue="month")
    bar.set(xlabel = 'Years', ylabel = 'Average Page Views')
    handler, label = ax.get_legend_handles_labels()
    ax.legend(handler, ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    # plt.bar(df)
    # plt.plot(date,df_bar.mean(level=["year","month"]))
    # Save image and return fig (don't change this part)
    fig=bar.get_figure()
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    #https://stats.biopapyrus.jp/python/boxplot.html
    #https://stats.biopapyrus.jp/python/subplot.html
    #https://qiita.com/hik0107/items/7233ca334b2a5e1ca924
    #http://ailaby.com/subplots_adjust/#:~:text=pyplot%20as%20plt-,plt.subplots_adjust(wspace%3D0.4%2C%20hspace%3D0.6),-2%E8%A1%8C2
    
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    print("df_box",df_box)
    print(df_box.dtypes)
    # Draw box plots (using Seaborn)

    fig= plt.figure(figsize=(10,5))
    ax1 = fig.add_subplot(1,2,1)
    
    plt.title("Year-wise Box Plot (Trend)")
    plt.subplots_adjust(wspace=0.4, hspace=0.6)
    sns.boxplot(x = "year",y = "value",data = df_box,ax=ax1)
    plt.xlabel("Year")
    plt.ylabel("Page Views")
    
    ax2 = fig.add_subplot(1,2,2)
    plt.title("Month-wise Box Plot (Seasonality)")
    sns.boxplot(x = "month",order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],y = "value",data = df_box,ax=ax2)
    plt.xlabel("Month")
    plt.ylabel("Page Views")    


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
