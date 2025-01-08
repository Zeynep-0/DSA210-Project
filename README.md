# DSA210-Project
## Data Set
I used **my photo gallery** as my dataset. I got the photos from my [Google Photos](https://photos.google.com/) account. I also got some of them directly from my phone's memory.

## Project Idea
I will analyze the **color palette** and **frequency** of the photos taken each month through the years. I'm also planning to include location information if I can get enough photos's location data. 

## Project Plan
First I will get my [Google Photos](https://photos.google.com/) data from the [Google takeout]( https://takeout.google) service. I will analyze and categorize the data by year and month which will give me the number of photos in each respective month and year. Then I will analyze the color distribution by using [K-Means clustering](https://en.wikipedia.org/wiki/K-means_clustering) to get the dominant color of each photo and adding up the found colors to find the most common ones in a month. Lastly I will visualize the data.

## Motivation
I want to see if there is any relation between a photo's color and the month it was taken in my life. I want to figure out if there are any prominent colors related to each month and if there is a shift through the years. I also want to see if there are any trends in the amount of photos taken between months and years. Ultimately, my main motivation is that I find colors interesting and this project allows me to explore them while learning more about my gallery. 

# DSA210-Project
This project is for DSA210 Introduction to Data Science class. I have analyzed my photo gallery for this project.

## Data Processing
I got my [Google Photos](https://photos.google.com/) data from the [Google takeout]( https://takeout.google) service and also directly from my phones memory. Then I manually categorized the photos by the year and month they were taken. I also disregarded screenshots due to their mostly white color affecting the results and I do not think they accurately display the specified time periods color theme.
