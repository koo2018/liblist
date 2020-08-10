import json
import calendar

# Читаем словарь из файла
with open('data.json', 'r') as f:
   data = json.loads(str(f.read()))

files = ['origins/mediacom_academ.txt','origins/mediacom_creative.txt','origins/jour_academ.txt','origins/jour_creative.txt',
         'origins_new/allbooks.txt','origins_new/mediacom.txt','origins_new/jour.txt']


for file in files:
    file_short = file.split('/')[-1:][0]
    print(file_short)
    fout = open('dates/topdates_' + file_short + ".csv", 'w')
    

    #fout.write(file+'\n\n')

    date_top = {}

    for smf in data[file]:

        dt = data[file][smf]['5']
        if dt:
            if dt not in date_top:
                date_top[dt] = 1
            else:
                date_top[dt] += 1




    #date_top_sorted = sorted(drl_top, key=url_top.get, reverse=True)
    date_top_sorted = sorted(date_top, reverse=True)
    fout.write("Year-month;Works qnty\n")
    for dt in date_top_sorted:
        fout.write(dt+";"+str(date_top[dt])+"\n")



    fout.close()

    fout = open('dates/topmonth_' + file_short + ".csv", 'w')

    dates_m = {}
    dates_m_cnt = {}
    fout.write("Year-month;Works qnty;Avrg each day in month;Avrg daily\n")

    for ddt in date_top:

        if ddt[:7] not in dates_m:
            dates_m[ddt[:7]] = date_top[ddt]
            dates_m_cnt[ddt[:7]] = 1
        else:
            dates_m[ddt[:7]] += date_top[ddt]
            dates_m_cnt[ddt[:7]] += 1

    for srt in sorted(dates_m, reverse=True):



        if 'xist' not in srt or 'nex' not in srt:

            day_in_mon = calendar.monthrange(int(srt[:4]), int(srt[5:7]))[1]
        else:
            day_in_mon = 1

        fout.write(srt+';'+str(dates_m[srt])+';'+str(round(dates_m[srt]/day_in_mon,2))+';'+str(round(dates_m[srt]/dates_m_cnt[srt],2))+'\n')

    fout.close()
