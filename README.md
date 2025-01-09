# DSA210-Project
This project is for DSA210 Introduction to Data Science class. I have analyzed my photo gallery for this project.

## Motivation
I wanted to see if there was any relation between a photo's color and the month it was taken in my life. I want to figure out if there are any prominent colors related to each month and if there is a shift through the years. I also wanted to see if there were any trends in the amount of photos taken between months and years. Ultimately, my main motivation was that I find colors interesting and this project allows me to explore them while learning more about my gallery and photo taking habits. 

## Data Set
I used **my photo gallery** as my dataset. I got the photos from my [Google Photos](https://photos.google.com/) account. I also got some of them directly from my phone's memory.

## Data Pre-Processing
First I manually categorized the photos by the year and month they were taken. I also disregarded screenshots due to their mostly white color affecting the results. Then I wrote a python script to get when each photo was taken by processing eachh photos json files that Google takeout provides alongside the photos themselves.

## Data Processing
# Dominant Color Analysis
I used kMeans clustering to get each photos 5 most dominant colors. I decided the k value by checking different ones and comparing the results. Then afetr I processed each month I merged similar colors by setting a threshold between the rgb distances of two colors and if they are closer than said threshold I combined them. I also decided on the threshold after running the program with different ones and seeing their accuracy. I used a smallar batch of photos to test my programs accuracy visually also. I had over 16000 photos so I used threads to speed up the process of extracting colors. I also resized images for the same reason. After processing each month I got top 10 most common colors and created a csv file to store the value. I also stored all years combined data in a json file for visualization.

# Photo Taken Time
Since I directly got the photo's times from the google I just collected the data in a json file. I checked for thr most common hour I took by turning unix time to standard time and also adding timezone to be accurate with time.

## Data Visualization
[My website for charts also findings but prettier](https://zeynep-0.github.io/DSA210-Project/index.html#)
# Dominant Color Analysis
For visualization of each years top 10 most common colors. I got each csv file related to each year and combined every month of that year. Then I used the above mentioned method of merging colors and merged them. Then I used altair to visualize an interactive bar chart to show count of each color and their rbg. I used altair to visualize a bar chart to see how each month changed through the years and the count of each color. I also did the reverse and looked at each years months again using altair to visualize a bar chart.

# Photo Taken Time
I created a scatter plot to show the hours each photo was taken in each month again using altair to plot it. I also looked at each year generally using scatter plot.

## Findings
Unfortunately I coudn't find any overarching trends about dominant colors and their relations with years and differnt months. But finding out there isn't any one big color pallette in a year or in season allowed me to see how different each month can be.
I found out that I like to take my photos at night since most common 5 hour were between 16-21 o'clock. I found out that the number of photos I took significantly decreased around the university exam period and slowly getting back to how it was.
## Limitations
I coudn't get the 2022 photos's taken times so it was quite a gap in understanding the photo taking habits. Also I would've liked to get location of these photos to create a map with it. Also the dominant color extraction can be more precise by using an elbow method or silhoutte to find the optimal k mean but with less photos probably. Doing more analysis and visualization of the data can be done as well. I plan to work on this project to take it to the best state it can get with what I know.
