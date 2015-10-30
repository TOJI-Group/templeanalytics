# Temple Analytics 2015  [Team TONI]
[Compeition Link][]
v0.03  
Group Compeition Webiste: www.tonianalytics.me

Team Members: Devin Trejo, James Novino, Tyler Olivieri, Robert Irwin


### Release Additions:
- Team name change from TOJI -> TONI for conistent relationship to last name
of team members
- Added plotMap
- Added plotRevTime which plots top three categories best revenue
- Added plotSentiment. Overall comment histogram (barplot)
- Data Statistics on best selling item and host
- load data in now handled by rawFileOp class.
- loadMaster now combines orderList, customerList, and product category lists.
- Added more functionality in rawFileOp class. (Ex. now save a local copy of
masterList to master.csv in data folder. 

## Project Files
### Main Program [`run.py`][]
Queries data and plots data.

### Classes [`classes`][]
The class [`rawFileOp.py`][] read and loads the raw data from the compeition.

### Plotting Functions
All plotting functions reside in a package [`myPlot`][].

## Project Requirements
- Python 2.7 (Recommend: [Anaconda 2.7][])
- [Plotly 1.8.6][]
- [Pandas 0.17.0][]

[Compeition Link]: http://ibit.temple.edu/analytics/
[`run.py`]: /src/run.py
[`classes`]: /src/classes/
[`rawFileOp.py`]: /src/classes/rawFileOp.py
[`myPlot`]: /src/myPlot/
[`filecleanup.py`]: /src/filecleanup.py
[Anaconda 2.7]: https://www.continuum.io/downloads
[Plotly 1.8.6]: https://plot.ly/
[Pandas 0.17.0]: http://pandas.pydata.org/
