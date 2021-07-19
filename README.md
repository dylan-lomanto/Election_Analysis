# Election_Analysis

### Project Overview
The election audit was conducted to return the following information: total votes cast, total and percentage of votes by county, largest county turnout, total and percentage of votes by candidate, election winner, winning vote count, and winning vote percentage.  

### Election-Audit Results

##### Total votes cast: 
369,711

##### County Vote Counts and Percentages:
Jefferson: 10.5% (38,885)

Denver: 82.8% (306,055)

Arapahoe: 6.7% (24,801)

##### Largest County Turnout:
Denver

##### Candidate Vote Counts and Percentages:
Charles Casper Stockham: 23.0% (85,213)

Diane DeGette: 73.8% (272,892)

Raymon Anthony Doane: 3.1% (11,606)

##### Winner:
Diane Degetter

##### Winning Vote Count and Percentage:
73.8% (272,892)

![Election_Analysis_TXT_screen](https://user-images.githubusercontent.com/86164867/126208949-9d171e94-c3ea-4e5e-9346-790260bca5c9.PNG)

### Summary
The scritpt found in PyPoll_Challenge.py can be used to audit any election in which the results are delivered in the same format as election_results.csv, with minor adjustments to labeling.  The for loops and conditional statements will remain intact, but the names will be adjusted based upon the type of election.

##### Adjustment for Ballot Measure Election
The scrpit can be tweaked to audit a single ballot measure election. The candidate_options list and candidate_votes dictionary need to be renamed to measure_options and measure_votes, repectively.  The candidate_name variable will also need to be changed to measure_result.

##### Adjustment for Federal Election
The script can also be tweaked to measure votes for individual states in a federal election, instead of counties in a state election.  All variables, lists, and dictionaries that use the word 'county' will need to have the word replaced with 'state'.  

