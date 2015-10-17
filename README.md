# Temple Analytics 2015  [Team TOJI]
[Compeition Link][]
v0.01

Team Members: Devin Trejo, James Novino, Tyler Olivieri, Robert Irwin

## Project Files
### Main Program [`run.py`][]
Queries data and plots data.

### Classes
Imported from [/data/qvc/][] .csv files.
- Customer Class: Takes data from `customer_master.csv`
- Order Class: Takes data from `order_master.csv`
- Media Class: Takes data from `product_airtime.csv`

### Obsolete
The following scripts are obsolete. Expect them to be removed in future
releases.
- [`filecleanup.py`][] : removes the headers from all the csv files, to 
processing easier. Will created updated files

## Project Requirements
- Python 2.7 (Recommend: [Anaconda 2.7][])
- [Plotly 1.8.6][]
- [Pandas 0.17.0][]

[Compeition Link]: http://ibit.temple.edu/analytics/
[`run.py`]: /src/run.py
[`filecleanup.py`]: /src/filecleanup.py
[Anaconda 2.7]: https://www.continuum.io/downloads
[Plotly 1.8.6]: https://plot.ly/
[Pandas 0.17.0]: http://pandas.pydata.org/