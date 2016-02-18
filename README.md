This is a [Python 2.7] [1] and [Scrapy] [2]–based web scraper that collects the
historical opinion polls (1970 to the present day) from the archive at
[UK Polling Report] [3], converts them into a long-form table, and uploads the
data to CartoDB.

The latest data is always available from `http://data.flother.is/ukpolls` and
is updated weekly. You can query the data using SQL, for example:

    $ curl -Ls "http://data.flother.is/ukpolls?q=SELECT+party,AVG(share)+FROM+ukpolls+GROUP+BY+party+ORDER+BY+AVG(share)+DESC"
    party,avg
    Labour,38.8456553448635
    Conservative,35.6344238382997
    SDP-Liberal Alliance,23.1614379084967
    Liberal Democrats,12.9686744013824
    Liberal,12.4162629757785
    UKIP,12.3052407932011
    SDP,3.83776595744681
    Green,3.69500372856078


[1]: https://www.python.org/
[2]: http://scrapy.org/
[3]: http://ukpollingreport.co.uk/
