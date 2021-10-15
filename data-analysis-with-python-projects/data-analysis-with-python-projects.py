import pandas as pd

def calculate_demographic_data(print_data=True):
    
    pd.options.display.float_format = '{:.2f}'.format
    print(pd.options.display.float_format)
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.filter(["race"],axis= 1).value_counts()
    print("race_count",race_count)
    # What is the average age of men?
    average_age_men = df.groupby(["sex"])["age"].mean()["Male"]
    average_age_men =round(average_age_men,1)

    print("average_age_men","{:2f}".format(average_age_men))
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors =  (df[df["education"]=="Bachelors"].value_counts().sum() / df["education"].value_counts().sum() )*100
    percentage_bachelors = round(percentage_bachelors,1)
    
    # total = df["education"].value_counts().sum()
    print("percentage_bachelors",percentage_bachelors)
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # higher_education = None
    # lower_education = None
    # # with and without `Bachelors`, `Masters`, or `Doctorate`
    all_edu = df["education"].value_counts().sum()
    high_edu = df[df["education"].isin(["Bachelors","Masters","Doctorate"])].value_counts().sum()
    low_edu = (df["education"].value_counts().sum()  - df[df["education"].isin(["Bachelors","Masters","Doctorate"])].value_counts().sum())


    higher_education = high_edu / df["education"].value_counts().sum()
    lower_education = low_edu / df["education"].value_counts().sum()
    higher_education *= 100
    lower_education *= 100
    higher_education =round(higher_education,1)
    lower_education =round(lower_education,1)


    print("higher or lower_education",higher_education,lower_education)
    # percentage with salary >50K
    higher_education_rich = None
    lower_education_rich = None



    higher_education_rich = df[df["education"].isin(["Bachelors","Masters","Doctorate"])].query("salary=='>50K'").value_counts().sum()/high_edu
    lower_education_rich = df[df["education"].isin(["Bachelors","Masters","Doctorate"])].query("salary=='>50K'").value_counts().sum()/low_edu

    lower_education_rich = df[~df["education"].isin(["Bachelors","Masters","Doctorate"])].query("salary=='>50K'").value_counts().sum()/low_edu



    higher_education_rich *= 100
    lower_education_rich *= 100
    higher_education_rich =round(higher_education_rich,1)
    lower_education_rich =round(lower_education_rich,1)

    print("higher or lower_education_rich",higher_education_rich,lower_education_rich)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = None
    min_work_hours = min(df["hours-per-week"])
    print("min_work_hours",min_work_hours)
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None
    num_min_workers = df.query("salary=='>50K'").value_counts().sum()/all_edu
    print("num_min_workers",num_min_workers)
    num_min_workers *= 100

    num_min_workers =round(num_min_workers,1)


    rich_percentage = df.query("salary=='>50K' & `hours-per-week` == @min_work_hours").value_counts().sum()/df.query("`hours-per-week` == @min_work_hours").value_counts().sum()
    rich_percentage *= 100
    rich_percentage =round(rich_percentage,1)

    
    print("rich_percentage",rich_percentage)
    # What country has the highest percentage of people that earn >50K?
    rich_in_country = df.query("salary=='>50K'")["native-country"].value_counts()
    all_in_country = df["native-country"].value_counts()
    # print("rich and all" , (rich_in_country,all_in_country,rich_in_country / all_in_country) )
    
    highest_earning_country = None
    highest_earning_country = (rich_in_country/all_in_country).idxmax()
    print("highest_earning_country",highest_earning_country)  

    highest_earning_country_percentage = (rich_in_country/all_in_country).max()
    highest_earning_country_percentage *= 100

    highest_earning_country_percentage =round(highest_earning_country_percentage,1)

    print("highest_earning_country_percentage",highest_earning_country_percentage)  

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.query("salary=='>50K' & `native-country` == 'India'")["occupation"].value_counts().idxmax()
    print("top_IN_occupation",top_IN_occupation)  

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
