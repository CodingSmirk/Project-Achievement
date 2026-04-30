import folium
import pandas
import haversine

file_name = 'long'

# GPS data & Latency data
original_data = pandas.read_csv(file_name+'.csv')
GPS_log = original_data[['ulPayloadLength','ulPayloadCrc32']].div(1000000).values
latency_log = original_data[['Latency']].values

# Make variable
middle_point = GPS_log.shape[0]//2
max_latency = original_data['Latency'].max()
before_long = 0
before_lat = 0

# Make Color Table
color_table = [0] * GPS_log.shape[0]
for x in range(0,latency_log.shape[0]):
    if latency_log[x] >=0  and (max_latency*1)/30 > latency_log[x]:
        color_table[x] = "#00FF00"
    elif latency_log[x] >= (max_latency*1)/30  and (max_latency*2)/30 > latency_log[x]:
        color_table[x] = "#12FF00"
    elif latency_log[x] >= (max_latency*2)/30  and (max_latency*3)/30 > latency_log[x]:
        color_table[x] = "#24FF00"
    elif latency_log[x] >= (max_latency*3)/30  and (max_latency*4)/30 > latency_log[x]:
        color_table[x] = "#35FF00"
    elif latency_log[x] >= (max_latency*4)/30  and (max_latency*5)/30 > latency_log[x]:
        color_table[x] = "#47FF00"
    elif latency_log[x] >= (max_latency*5)/30  and (max_latency*6)/30 > latency_log[x]:
        color_table[x] = "#58FF00"
    elif latency_log[x] >= (max_latency*6)/30  and (max_latency*7)/30 > latency_log[x]:
        color_table[x] = "#6AFF00"
    elif latency_log[x] >= (max_latency*7)/30  and (max_latency*8)/30 > latency_log[x]:
        color_table[x] = "#7CFF00"
    elif latency_log[x] >= (max_latency*8)/30  and (max_latency*9)/30 > latency_log[x]:
        color_table[x] = "#8DFF00"
    elif latency_log[x] >= (max_latency*9)/30  and (max_latency*10)/30 > latency_log[x]:
        color_table[x] = "#9FFF00"
    elif latency_log[x] >= (max_latency*10)/30  and (max_latency*11)/30 > latency_log[x]:
        color_table[x] = "#B0FF00"
    elif latency_log[x] >= (max_latency*11)/30  and (max_latency*12)/30 > latency_log[x]:
        color_table[x] = "#C2FF00"
    elif latency_log[x] >= (max_latency*12)/30  and (max_latency*13)/30 > latency_log[x]:
        color_table[x] = "#D4FF00"
    elif latency_log[x] >= (max_latency*13)/30  and (max_latency*14)/30 > latency_log[x]:
        color_table[x] = "#E5FF00"
    elif latency_log[x] >= (max_latency*14)/30  and (max_latency*15)/30 > latency_log[x]:
        color_table[x] = "#F7FF00"
    elif latency_log[x] >= (max_latency*15)/30  and (max_latency*16)/30 > latency_log[x]:
        color_table[x] = "#FFF600"
    elif latency_log[x] >= (max_latency*16)/30  and (max_latency*17)/30 > latency_log[x]:
        color_table[x] = "#FFE400"
    elif latency_log[x] >= (max_latency*17)/30  and (max_latency*18)/30 > latency_log[x]:
        color_table[x] = "#FFD300"
    elif latency_log[x] >= (max_latency*18)/30  and (max_latency*19)/30 > latency_log[x]:
        color_table[x] = "#FFC100"
    elif latency_log[x] >= (max_latency*19)/30  and (max_latency*20)/30 > latency_log[x]:
        color_table[x] = "#FFAF00"
    elif latency_log[x] >= (max_latency*20)/30  and (max_latency*21)/30 > latency_log[x]:
        color_table[x] = "#FF9E00"
    elif latency_log[x] >= (max_latency*21)/30  and (max_latency*22)/30 > latency_log[x]:
        color_table[x] = "#FF8C00"
    elif latency_log[x] >= (max_latency*22)/30  and (max_latency*23)/30 > latency_log[x]:
        color_table[x] = "#FF7B00"
    elif latency_log[x] >= (max_latency*23)/30  and (max_latency*24)/30 > latency_log[x]:
        color_table[x] = "#FF6900"
    elif latency_log[x] >= (max_latency*24)/30  and (max_latency*25)/30 > latency_log[x]:
        color_table[x] = "#FF5700"
    elif latency_log[x] >= (max_latency*25)/30  and (max_latency*26)/30 > latency_log[x]:
        color_table[x] = "#FF4600"
    elif latency_log[x] >= (max_latency*26)/30  and (max_latency*27)/30 > latency_log[x]:
        color_table[x] = "#FF3400"
    elif latency_log[x] >= (max_latency*27)/30  and (max_latency*28)/30 > latency_log[x]:
        color_table[x] = "#FF2300"
    elif latency_log[x] >= (max_latency*28)/30  and (max_latency*29)/30 > latency_log[x]:
        color_table[x] = "#FF1100"
    elif latency_log[x] >= (max_latency*29)/30  and (max_latency) >= latency_log[x]:
        color_table[x] = "#FF0000"

# Make Folium map
mymap = folium.Map(location=GPS_log[middle_point], zoom_start=17)

# Add line to the map
before_lat = GPS_log[1][0]
before_long = GPS_log[1][1]
for x in range(1,GPS_log.shape[0]):
    if before_lat != GPS_log[x][0] and before_long != GPS_log[x][1] and abs(before_lat)<=90 and abs(GPS_log[x][0])<=90 and haversine.haversine((before_lat,before_long), (GPS_log[x][0],GPS_log[x][1]), unit = 'm')<50:
        folium.PolyLine(locations=[(before_lat, before_long),GPS_log[x]], color=color_table[x]).add_to(mymap)
        before_lat = GPS_log[x][0]
        before_long = GPS_log[x][1]

# Save map(html)
mymap.save(file_name+'.html')