# DSA210-Project
This project is for DSA210 Introduction to Data Science class. I have analyzed my photo gallery for this project. 
[My website for this project](https://zeynep-0.github.io/DSA210-Project/index.html#)


# Photo Gallery Analysis Project

## About the Project
This project is for the **DSA210 Introduction to Data Science** class. I analyzed my photo gallery from 2016 to 2024 to uncover patterns and trends in my photography habits.

---

## Motivation
I aimed to explore potential relationships between a photo's color and the month it was taken. Specifically, I wanted to identify prominent colors for each month and observe any shifts over the years. Additionally, I analyzed trends in the quantity of photos taken across months and years. My primary motivation stemmed from a fascination with colors, making this project an exciting opportunity to delve into their patterns while learning about my photo gallery and photography habits.

---

## Data Set
I used **my photo gallery** as the dataset, with photos sourced from:
- [Google Photos](https://photos.google.com/)
- My phone's memory.

---

## Data Pre-Processing
1. **Manual Categorization**:
   - Organized photos by year and month.
   - Excluded screenshots due to their predominantly white color skewing the results.

2. **Python Script**:
   - Extracted photo metadata (e.g., taken date) from JSON files provided by Google Takeout.
   - Created a Word document summarizing monthly photo counts for each year.

---

## Data Processing

### Dominant Color Analysis
- **Method**:
  - Used **kMeans clustering** to identify the top 5 dominant colors in each photo.
  - Determined the `k` value by experimenting with different settings and comparing results.
- **Color Merging**:
  - Merged similar colors based on an RGB distance threshold.
  - Fine-tuned the threshold through iterative testing.
- **Optimization**:
  - Processed over 16,000 photos using threads to expedite color extraction.
  - Resized images for faster processing.
- **Output**:
  - Generated CSV files for the top 10 most common colors per month and a combined JSON file for all years.

### Photo Taken Time
- Extracted timestamps from Google metadata.
- Converted Unix time to standard time and included timezone adjustments.
- Stored data in a JSON file to analyze the most common hours for photo-taking.

### Photo Count
- Compiled monthly photo counts for each year into a CSV file using Excel.
- Calculated the average number of photos taken per month manually.

---

## Data Visualization

### Dominant Color Analysis
- Combined monthly data to analyze trends for each year.
- Visualizations created with **Altair**:
  - [Interactive Pie Chart](#pie): Displays color counts and their RGB values.
  - [Bar Charts](#project): Highlights monthly changes in color counts across years.

### Photo Taken Time
- Created a [Scatter Plot](#resume) with Altair to show photo-taking hours by month.
- Added a dropdown menu to view year-specific data.

### Photo Count
- Created a [Scatter Plot](#resume2) with Altair to depict yearly photo counts across months.
- Added a dropdown menu to examine month-specific trends.

---

## Limitations
- Missing photo timestamps for 2022 created a gap in the data.
- Incorporating photo location data could enable map-based visualizations.
- More precise dominant color extraction (e.g., using the elbow method or silhouette analysis) was not feasible with the current dataset size.
- Future improvements include:
  - Enhancing website features.
  - Conducting deeper analysis and visualizations to uncover additional insights.

---

Thank you for exploring this project! 😊








## Motivation
I wanted to see if there was any relation between a photo's color and the month it was taken in my life. I want to figure out if there are any prominent colors related to each month and if there is a shift through the years. I also wanted to see if there were any trends in the amount of photos taken between months and years. Ultimately, my main motivation was that I find colors interesting and this project allows me to explore them while learning more about my gallery and photo taking habits. 

## Data Set
I used **my photo gallery** as my dataset. I got the photos from my [Google Photos](https://photos.google.com/) account. I also got some of them directly from my phone's memory.

## Data Pre-Processing
First I manually categorized the photos by the year and month they were taken. I also disregarded screenshots due to their mostly white color affecting the results. Then I wrote a python script to get when each photo was taken by processing eachh photos json files that Google takeout provides alongside the photos themselves.

## Data Processing
### Dominant Color Analysis
I used kMeans clustering to get each photos 5 most dominant colors. I decided the k value by checking different ones and comparing the results. Then afetr I processed each month I merged similar colors by setting a threshold between the rgb distances of two colors and if they are closer than said threshold I combined them. I also decided on the threshold after running the program with different ones and seeing their accuracy. I used a smallar batch of photos to test my programs accuracy visually also. I had over 16000 photos so I used threads to speed up the process of extracting colors. I also resized images for the same reason. After processing each month I got top 10 most common colors and created a csv file to store the value. I also stored all years combined data in a json file for visualization.

### Photo Taken Time
Since I directly got the photo's times from the google I just collected the data in a json file. I checked for thr most common hour I took by turning unix time to standard time and also adding timezone to be accurate with time.

## Data Visualization

### Dominant Color Analysis
For visualization of each years top 10 most common colors. I got each csv file related to each year and combined every month of that year. Then I used the above mentioned method of merging colors and merged them. Then I used altair to visualize an interactive bar chart to show count of each color and their rbg. I used altair to visualize a bar chart to see how each month changed through the years and the count of each color. I also did the reverse and looked at each years months again using altair to visualize a bar chart.

### Photo Taken Time
I created a scatter plot to show the hours each photo was taken in each month again using altair to plot it. I also looked at each year generally using scatter plot.

## Findings
Unfortunately I coudn't find any overarching trends about dominant colors and their relations with years and differnt months. But finding out there isn't any one big color pallette in a year or in season allowed me to see how different each month can be.
I found out that I like to take my photos at night since most common 5 hour were between 16-21 o'clock. I found out that the number of photos I took significantly decreased around the university exam period and slowly getting back to how it was.

## Limitations
I coudn't get the 2022 photos's taken times so it was quite a gap in understanding the photo taking habits. Also I would've liked to get location of these photos to create a map with it. Also the dominant color extraction can be more precise by using an elbow method or silhoutte to find the optimal k mean but with less photos probably. Doing more analysis and visualization of the data can be done as well. I plan to work on this project to take it to the best state it can get with what I know.
