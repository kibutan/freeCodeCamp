import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    print(df.head(),df.dtypes)
    df = df[["Year","CSIRO Adjusted Sea Level"]]
    start = 1850
    stop = 2076
    step=25
    # Create scatter plot
    plt.scatter(df["Year"],df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    result = linregress(df["Year"],df["CSIRO Adjusted Sea Level"])
    a = result.slope
    b = result.intercept
    print("a,b",a,b)
    print(result)
    # for i in range(2014,2051):
    #     df2 = pd.DataFrame({"Year":i,"CSIRO Adjusted Sea Level":a*i +b})
    df2 = pd.DataFrame({"Year":range(2014,2051),"CSIRO Adjusted Sea Level":[a*t +b for t in range(2014,2051)]})
    print(df2)
    line1 = pd.DataFrame({"Year":range(1880,2051),"CSIRO Adjusted Sea Level":[a*t +b for t in range(1880,2051)]})

    df_con = pd.concat([df, df2], join='inner')
    # print("append",df_con,len(df_con))
    # Create second line of best fi
    # plt.plot(df_con["Year"],df_con["CSIRO Adjusted Sea Level"],".")
    # plt.plot(range(start,stop),[a*t +b for t in range(start,stop)])
    # plt.plot(range(1880,2051),[a*t +b for t in range(1880,2051)])
    # plt.plot(range(1880,2051),df_con["CSIRO Adjusted Sea Level"])
    plt.plot(range(1880,2051),line1["CSIRO Adjusted Sea Level"],color="red")
    
    print("X_1,Y_1",[a*t +b for t in range(1880,2051)],len([a*t +b for t in range(1880,2051)]))
    print("PLT TO LIST",plt.gca().get_lines()[0].get_ydata().tolist(), len(plt.gca().get_lines()[0].get_ydata().tolist()))
    df_second = df.query("Year >= 2000")
    result_second = linregress(df_second["Year"],df_second["CSIRO Adjusted Sea Level"])
    a_second = result_second.slope
    b_second = result_second.intercept
    # print("a_2,b_2",a_second,b_second)
    # print("X_2,Y_2",len([a_second*t +b_second for t in range(2000,2051)]))
    plt.plot(range(2000,2051),[a_second*t +b_second for t in range(2000,2051)],color="blue")
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.xlim((start, stop))
    plt.xticks(range(start, stop, step))

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
