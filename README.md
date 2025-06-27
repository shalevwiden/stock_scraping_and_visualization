## Scraping Stock Data from companiesmarketcap.com

First I used beautiful soup and requests to scrape the data and put it in a dictionary in stockscraping.py.
Then in stockvisualizations.py I used .count and sorted (descending, based on the 2nd element in the tuple with lambda `key=lambda x:x[1]`) to make a list of tuples with the country name and the amount of timese the country appears in the top 100 list.

Then I used

```python

getsizesandlabels(sortedcountry_countrycount_list,rangenum,otherinchart=True)
    ...
    return labels, sizes

```

to get sizes and labels data, with only the top (rangenum) amount.

Then finnaly I used `makepiechart()` to make and save a piechart based on the labels and sizes.
