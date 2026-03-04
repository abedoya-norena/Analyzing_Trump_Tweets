#!/usr/bin/python3

'''
# Lab: Analyzing Trump Tweets

In this lab, you will analyze all tweets sent by president Trump from 2009-2018.
You will get practice
1. loading datasets stored in JSON files,
2. creating plots in python, and
3. writing "fully open ended" code where I don't give you any starter code/doctests to guide you.

The data we will analyze is used to create the following two websites:
1. [An analysis of which types of tweets Trump is likely to send himself, versus which his staffers send.](http://varianceexplained.org/r/trump-tweets/)
2. [A search engine for all of Trump's tweets.](https://www.thetrumparchive.com/)

> **Note:**
> I am using Markdown formatting within this python docstring.
> This is a *very* common practice.
> Markdown (unlike HTML) is designed to be human readable in it's "uncompiled" form,
> and so programmers write markdown *everywhere*.

## Part 0: Setup Project

You will have to upload files to github to submit this lab.
Complete the following steps to setup your project.

1. Create a new github repo through the github interface.

2. Clone that project onto your computer.

3. Copy this `lab_tweets.py` file into your project folder.

## Part 1: Download the Data

The github repo <https://github.com/bpb27/trump_tweet_data_archive> contains an archive of tweets sent by Donald Trump.

1. Download these files `master_*.json.zip`, where * is a year.
    There should be 10 total files (2009-2018).

    > **Note:**
    > This particular archive stops in 2018 because the maintainer moved their codebase to <https://github.com/bpb27/tta-elastic>.
    > The newer archive has data that goes through the current year (and includes messages sent on Truth Social),
    > but it's a bit more complicated to access the data,
    > so we will use this older archive for this assignment.

2. Unzip these files into the project folder you created in Part 0 above.
    You should get a bunch of files that look like `master_*.json`.

## Part 2: Data Analysis

1. Modify this python file so that it:

    1. Opens each json file and loads the file using the json library.
       Each file contains a list of tweets, and if you concatenate each file's tweets
       together you will get a list of all tweets ever sent by Donald Trump.

    2. Prints the total number of tweets.

    3. Counts the number of tweets that contain the following keywords:
       `Obama`, `Trump`, `Mexico`, `Russia`, and `Fake News`.

       > **NOTE:**
       > It's important to remember that each of these words can appear with many different capitalizations,
       > and your program should count the word no matter how it is capitalized.
       > For example, `OBAMA`, `obama`, and `ObAmA` all need to count as an occurrence of the word `Obama`.
       > Recall that the easiest way to do this is to use the .lower() function and in keyword.

    4. Prints out a count of each of these words.

        > **Hint:**
        > My program gives the following output:
        > ```
        > len(tweets)= 36307
        > counts= {'trump': 13924, 'obama': 2712 ... }
        > ```
        > You'll know your program is correct if you get the same numbers.

2. Select at least 3 more interesting words/phrases to count in trump's tweets,
    and modify your program to display those words.

3. Calculate the percentage of tweets that contain each word.  (Both your new words and Trump's original tweets.)

4. Display the results nicely in a markdown table.

    The display must have all words right justified and the percents printed with two
    significant figures (on both sides of the decimal) as shown in the example output below.

    ```
    | phrase            | percent of tweets |
    | ----------------- | ----------------- |
    |              daca | 00.17             |
    |         fake news | 00.92             |
    |  mainstream media | 00.06             |
    |            mexico | 00.55             |
    |             obama | 07.47             |
    |            russia | 01.13             |
    |             trump | 38.35             |
    |              wall | 00.91             |
    ```

    There are many ways to achieve this effect in python,
    but I recommend using python's f-string syntax.
    Here is a little cheat sheet using doctests:

    >>> name = "Alice"
    >>> f"{name:<10}"
    'Alice     '
    >>> f"{name:>10}"
    '     Alice'
    >>> f"{name:^10}"
    '  Alice   '
    >>> f"{name:*^10}"
    '**Alice***'

    >>> pi = 3.14159265
    >>> f"{pi:.2f}"
    '3.14'
    >>> f"{pi:.4f}"
    '3.1416'
    >>> f"{pi:8.2f}"
    '    3.14'
    >>> f"{pi:08.2f}"
    '00003.14'

5. Plot the results in a bar graph.

    > HINT:
    > The most common way to plot in python is with the matplotlib library.
    > We won't be covering how to use it in class in order to get you practice figuring things out by yourself.
    > You can find a tutorial here: <https://www.w3schools.com/python/matplotlib_bars.asp>.
    > You are also welcome to ask your favorite AI.

## Submission

Create a properly formatted markdown file `README.md` that contains:
1. the markdown table created by your program
2. the image created by your program
3. a short description (1 sentence is fine) for your table/image above

Ensure that you have uploaded to your github repo:
1. your modified python file
2. your python image

You do not need to pass any github actions for this submission.

Upload your github url to canvas.

## Extra Credit

There are two extra credit opportunities for this lab, worth one point each.

1. If you use the latest version of the data (instead of the files in the github repo) you will get +1 point.
    You can find instructions for accessing the data at <https://www.thetrumparchive.com/faq> under the question "Can I have the data?"

2. If you make a plot of other interesting information in this dataset (that doesn't use the 'text' key).
    For example, you could plot: what time of day does Trump tweet most often? or what state does Trump tweet from most often?
    If you add this to your repo you will get +1 point.
'''
#!/usr/bin/python3

import json
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

# Load dataset,extra credit #1 :) 
with open("tweets_01-08-2021.json", "r") as f:
    tweets = json.load(f)

print("len(tweets)=", len(tweets))

# Required keywords + 3 new ones
keywords = [
    "trump",
    "obama",
    "mexico",
    "russia",
    "fake news",
    "wall",
    "daca",
    "media"
]

counts = {word: 0 for word in keywords}

# Count keyword occurrences
for tweet in tweets:
    text = tweet["text"].lower()
    for word in keywords:
        if word in text:
            counts[word] += 1

print("counts=", counts)

# Calculate percentages
total = len(tweets)
percents = {}

for word in keywords:
    percents[word] = (counts[word] / total) * 100


# Markdown table output
print()
print("| phrase            | percent of tweets |")
print("| ----------------- | ----------------- |")

for word in sorted(keywords):
    percent = percents[word]
    print(f"| {word:>17} | {percent:05.2f}             |")


# Bar graph
labels = keywords
values = [percents[word] for word in keywords]

plt.bar(labels, values)
plt.xlabel("Phrase")
plt.ylabel("Percent of Tweets")
plt.title("Frequency of Words in Trump's Tweets")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("tweet_word_frequency.png")
plt.show()

# Extra Credit

hours = []

for tweet in tweets:
    time = tweet["date"]
    dt = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    hours.append(dt.hour)

hour_counts = Counter(hours)

plt.figure()

plt.bar(hour_counts.keys(), hour_counts.values())
plt.xlabel("Hour of Day")
plt.ylabel("Number of Tweets")
plt.title("When Trump Tweets During the Day")

plt.tight_layout()

plt.savefig("tweets_by_hour.png")