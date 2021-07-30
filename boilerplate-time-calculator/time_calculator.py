def add_time(start, duration,day = False):
    start_time, start_ampm = start.split()
    start_hh,start_mm = map(int,start_time.split(":"))
    duration_hh,duration_mm = map(int,duration.split(":"))
    if start_ampm == "PM":
      start_ampm = "AM"
      start_hh = start_hh + 12
    # print(start_hh,start_mm,start_ampm)
    # print(duration_hh,duration_mm)
    days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"] 
    start_day = ""
    if day : start_day = day.lower()
    newtime_mm = start_mm + duration_mm - (start_mm + duration_mm >= 60)*60
    
    newtime_hh = start_hh + duration_hh + (start_mm + duration_mm >= 60)
    #newtime_hhは24時間以上もアリ得るので、後に加工する
    newtime_dd = newtime_hh//24

    newtime_hh_24 = (newtime_hh % 24)
    print("hh_24",newtime_hh_24,start_ampm)
    if newtime_hh_24 >= 12 :newtime_ampm = "PM" 
    else:newtime_ampm = "AM"
    # if newtime_hh_24 == 12 and  newtime_ampm == "PM" : newtime_hh_12 = 12
    # elif newtime_hh_24 == 12 and  newtime_ampm == "AM" : newtime_hh_12 = 12
    # else:newtime_hh_12 = newtime_hh_24 % 12
    newtime_hh_12 = newtime_hh_24 % 12
    if newtime_hh_12 == 0:newtime_hh_12 = 12
    print("hh_12",newtime_hh_12,newtime_ampm)
    newtime_day = ""
    if start_day != "": newtime_day = days[(days.index(start_day) + newtime_dd)%7].capitalize()
    


    if newtime_dd == 0:newtime_dd_body = ""
    elif newtime_dd == 1:newtime_dd_body = "(next day)"
    else:newtime_dd_body = "("+str(newtime_dd)+" days later)"
    
    
    new_time = str(newtime_hh_12)+":"+str(newtime_mm).zfill(2)+" "+newtime_ampm

    if start_day != "": new_time = new_time + ", " +newtime_day
    if newtime_dd_body != "":new_time = new_time +" "+ newtime_dd_body 
    
    print("result = ",start,"+",duration,"=",new_time)
    return new_time
    # 12:03 AM, Thursday (2 days later)
