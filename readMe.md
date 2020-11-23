The HackerRank Interview Prep Kit Solution Stash/ Test Environment!
-------------------------------------------------------------------
This repo is both a stash of my solutions to the Hacker Rank Interview 
Prep Kit AND a a testing environment that makes it easy to do the challenges
On your local machine. 

Common problems I encounter in integrated web IDE's like the one featured 
on HackerRank is the lack of good linting and/or not enough feedback on test
failures (especially on the long time complexity tests). Inevitably I found 
myself copy pasting the test data and making my own tests.

Pretty soon I got tired of rewriting unit tests so I wrote code inside of the
test_utilities directory that makes dynamically generated tests given the test data and 
the function you wanna test. I've also added code to process the text files
that Hacker Rank provides which contain the SUPER long test data for time complexity
tests.

The repo is divided up into different topics from data structures & algorithms,i.e., 
sorting, arrays, greedy algorithms, etc. (not including the test_utilities directory)

It is further divided into easy, medium, hard, and advanced problem sets for each topic.

The repo is FURTHER divided into the problems themselves, which are further divided into:
- test_resources
- brute_force.py
- optimal.py
- (sometimes) hacker_rank_submission.py
- readMe.md
- (sometimes) some pngs for the readMe when I need it

I specify the problem in the readMe, store the test data in test_resources, sometimes have 
a final formatted solution for the hacker rank IDE if Hacker Rank is picky with the solution,
and have my regular solutions in the two .py files: 
 
- brute_force.py:
Has the brunt solution that likely doesn't meet the time complexity 
requirements but DOES meet the functionality requirements.

2. optimal.py:
Meets both the time complexity requirements AND the functionality requirements. 


If there's only one or the other, it means I either solved it completely with the
brute force attempt, OR I didn't solve it on my own and got some help. I'll specify
in the respective readMe's of each problem :)

Some problems from the HackerRank Interview Prep Kit are omitted from here since they were either:
1. Too easy to warrant a full test suite + file structure and were solved
within hacker rank's awesome integrated web IDE (which is awesome), or,
2. Not well worded or too tedious to replicate in this environment.

Installation
------------
1. Clone the repo!

2. Navigate to the generated directory and within your terminal, run:

    `python3 -m venv env`
    
    if you haven't installed python virtual environments before, look up just that, then run:
    
    `pip install virtualenv`
    
    If you haven't installed pip, its a package manager for Python, so look it up and install :)
3. run:

    `source env/bin/activate`
    
    to activate your virtual environment. You should see a `(env)` in front of your terminal
    prompt now.
    
4. run:
    
    `pip install -r dependencies.txt`
    
    to install the dependencies for the test environment. 
    
5. You're all set! :)

How to Use
------------
 I've already written test data for the challenges I've done. all the test data is in the 
 respective directories of each challenge, inside the test_resources folder. I've separated
 the functionality tests from the time complexity tests in their respectively named files.
 
 ###Example 0
 
 I have a challenge

Feel free to shoot me any questions regarding this repo! Happy coding! <3

The link to the interview prep kit is: [Here](https://www.hackerrank.com/interview/interview-preparation-kit)

