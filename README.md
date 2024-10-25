# python-challenge
Week three graded assignment

In this challenge I analysed data from two different files using Python. In PyBank I used Python to analyse a financial dataset. I used csv.DictReader as opposed to csv.reader so that the Header row could automatically be detected (line 28) without having to skip it explicitly (which I got from researching through ChatGPT).

In the PyPoll election dataset, I change the names of some of the list's & Dictionary's. I also had to name the row ("Candidate") explicitly as opposed to using the row[2] (line 28) because I chose to use the DictReader here as well.
