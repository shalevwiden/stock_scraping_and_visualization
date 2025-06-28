'''
June 26, 2025
Lets make some stock visualizations with matplot lib
'''

from stockscraping import name_mktcap_dict

from matplotlib import pyplot as plt
import os

def makesortedcountrylist():
    countries=[]

    for i in name_mktcap_dict:
        countries.append(name_mktcap_dict[i][1])

    uniquecountries=list(set(countries))

    print('Unique Countries:')
    print(uniquecountries)
    #count function, very interesting. 
    usacount=countries.count('USA')
    # goes in order of the unique value countries

    countrysizes=[countries.count(country) for country in uniquecountries ]


    country_countrycount_list=[]
    for country in uniquecountries:
        if country:
            tup=country, countries.count(country)
            country_countrycount_list.append(tup)

    print(f'\nCountry_countrycount_list {country_countrycount_list}\n')

    # .sort sorts in place, sorted returns a new thing
    # lamda allows you to sort based on elements in a list
    sortedcountry_countrycount_list=sorted(country_countrycount_list, key=lambda x:x[1], reverse=True)
    print(f'sortedcountry_countrycount_list:\n{sortedcountry_countrycount_list}\n')
    return sortedcountry_countrycount_list

sortedcountry_countrycount_list=makesortedcountrylist()

print(f'sortedcountry_countrycount_list:\n{sortedcountry_countrycount_list}')

def getlabelsandsizes(sortedcountry_countrycount_list,rangenum,otherinchart=True):
    '''
    returns labels and sizes lists based on a certain range. Takes in presorted data( a list of tuples)

    Also takes the otherinchart argument to add other to the chart, or just the values in the range given by the rangenum
    '''
    labels=[]
    sizes=[]
    # can use hexcodes or names. alot of stuff
    colors=[
    "#489EC2",  # USA - Red
    '#DE2910',  # China - Red
    "#071945",  # UK - Blue
    '#FFCE00',  # Germany - Gold
    "#6A0F0F"   # Netherlands - Red
]

    for i in range(rangenum):
        label, size=sortedcountry_countrycount_list[i]
        labels.append(f'{label}: {size}')
        sizes.append(size)

    if otherinchart:
        otherval=0
        for i in range(rangenum,len(sortedcountry_countrycount_list)):
            size=sortedcountry_countrycount_list[i][1]
            otherval+=size
    # add other to the label
        labels.append(f'other: {otherval}')
        sizes.append(otherval)


    return labels, sizes, colors

print(f'\nThe output of the getlabelsandsizes function\n')
print(getlabelsandsizes(sortedcountry_countrycount_list=sortedcountry_countrycount_list,rangenum=5))



 

print(f'len of the name_mktcap_dict:')
print(len(name_mktcap_dict))

print(f'Availablestyles=\n{plt.style.available}')


pathtocurrentfile = os.path.dirname(os.path.abspath(__file__))
print(f'pathtocurrentfile:{pathtocurrentfile}')
save_path = os.path.join(pathtocurrentfile, 'graphs/piechart.png')
# set the size of the chart
def makepiechart():
    '''
    Gets labels, sizes, and colors from getlabelsandsizes()
    '''
# can I add seperate data that will be ON the piechart? In each quadrant hmmmmmm

    labels=getlabelsandsizes(sortedcountry_countrycount_list=sortedcountry_countrycount_list,rangenum=5)[0]
    sizes=getlabelsandsizes(sortedcountry_countrycount_list=sortedcountry_countrycount_list,rangenum=5)[1]
    colors=getlabelsandsizes(sortedcountry_countrycount_list=sortedcountry_countrycount_list,rangenum=5)[2]
    styles=['fivethirtyeight','ggplot']
    plt.style.use(styles[1])

    plt.figure(figsize=(10,6))
    plt.pie(sizes,labels=labels, colors=colors,startangle=270)
    plt.title("Country Distribution in top 100 Companies")
    plt.axis('equal')
    plt.legend(loc='lower right',bbox_to_anchor=(1.1, -0.1))   
    # it rewrites it each time
    plt.savefig(save_path)

    plt.show()

makepiechart()

def makebarchart():
    '''
    Make a bar chart with "other" as an option too. Do this in 20 min.
    '''
    pass


# I still have to analyze and visualize the car data though

# incorporate this code

# top_n = 5

# top_entries = sorted_data[:top_n]
# other_entries = sorted_data[top_n:]

# # Combine "Other"
# top_labels = [entry[0] for entry in top_entries] + ['Other']
# top_sizes = [entry[1] for entry in top_entries] + [sum(entry[1] for entry in other_entries)]

# # Plot
# plt.figure(figsize=(6,6))
# plt.pie(top_sizes, labels=top_labels, startangle=90)
# plt.title("Country Distribution (Top 5 + Other)")
# plt.axis('equal')
# plt.show()

