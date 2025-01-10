
# Photo Gallery Analysis Project

## About the Project
This project is for the **DSA210 Introduction to Data Science** class. I analyzed my photo gallery from 2016 to 2024 to uncover patterns and trends in my photography habits. [My website for this project is here](https://zeynep-0.github.io/DSA210-Project/index.html#)

## Table of Contents

- [Motivation](#motivation)
- [Data Set](#data-set)
- [Data Pre-Processing](#data-pre-processing)
- [Data Processing](#data-processing)
  - [Dominant Color Analysis](#dominant-color-analysis)
  - [Photo Taken Time](#photo-taken-time)
  - [Photo Count](#photo-count)
- [Data Visualization](#data-visualization)
  - [Dominant Color Analysis](#dominant-color-analysis-1)
  - [Photo Taken Time](#photo-taken-time-1)
  - [Photo Count](#photo-count-1)
- [Findings](#findings)
- [Limitations](#limitations)
- [Future Plans](#future-plans)

## Motivation
I wanted to explore potential relationships between a photo's dominant colors and the month it was taken. Specifically, I wanted to identify any prominent colors associated with each month and observe if there are any trends over the years. Additionally, I tried to uncover trends in the number of photos taken across different months and years. Ultimately, my primary motivation rooted from the fact that I find colors interesting. This project allowed me to explore this interest while gaining insights into my photo gallery and photography habits.



## Data Set
I used **my photo gallery** as the dataset, with photos sourced from:
- [Google Photos](https://photos.google.com/)
- My phone's memory.


## Data Pre-Processing
1. **Manual Categorization**:
   - Organized photos by year and month.
   - Excluded screenshots due to their mostly white color effecting the results.
   - Created a Word document summarizing monthly photo counts for each year.
2. **Python Script**:
   - Extracted photo metadata (photo taken time) from JSON files provided by Google Takeout.
  

## Data Processing

### Dominant Color Analysis
- **Method**:
  - Used **kMeans clustering** to identify the top 5 dominant colors in each photo.
  - Determined the `k` value by experimenting with different values and comparing results.
- **Color Merging**:
  - Merged similar colors based on an RGB distance threshold.
  - Determined the threshold through iteratively testing.
- **Optimization**:
  - Processed over 16,000 photos using threads to speed up the color extraction.
  - Resized images for faster processing.
- **Output**:
  - Generated CSV files for the top 10 most common colors per month and a combined JSON file for all years.

### Photo Taken Time
- Extracted timestamps from Google metadata.
- Converted Unix time to standard time and included the timezone difference.
- Stored data in a JSON file to analyze the most common hours for photo-taking.

### Photo Count
- Compiled monthly photo counts for each year into a CSV file using Excel.
- Manually calculated the average number of photos taken per month.

## Data Visualization

### Dominant Color Analysis
For visualizing the top 10 most common colors for each year, I processed the CSV files containing monthly color data and combined them into yearly datasets. After merging similar colors using an RGB distance threshold, I created visualizations using **Altair**:

- **Interactive Pie Chart**: Displays the count of each color along with their RGB values.
- **Bar Chart**: Shows how the top colors for each month chanaged over the years.
- **Bar Chart**: Analyzes the distribution of every years color data across all months.

I initially considered using Plotly for these visualizations but coudn't able to embed Plotly graphs as HTML files into the website. 

### Photo Taken Time
- Created a [Scatter Plot] with Altair to show which hours photos were taken each month.
- Added a dropdown menu to view the year specific data.

### Photo Count
- Created a [Scatter Plot] with Altair to show yearly photo counts across months.
- Added a dropdown menu to examine month specific trends.

## Findings
### Dominant Color Analysis

The most common color in all of my 16000 photos is brown which is understandable since almost every month had some shade of brown in it. I didn't anticipate every year having its own color pallete, it was suprising. There were couple unique colors in most years, some examples:
                  
- 2016: Pink
- 2019: Blue
- 2022: Green
  
2020 had a quite different color pallette. It's colors were mostly due to the month of March which is the month I had a trip to Europe and I took a lot of photos.
As for any trend regarding season I couldn't observe any except the month of May having 3 years with very green color pallettes: 2017, 2018 and 2022. There was also some greens in 2021 as well. 2021's January was an outlier compared to other months in 2021 which is the result of taking over 20 photos for my birthday celebration.

There were a lot of greens and blues all through the months and years which was kind of expected with the amount of nature and sky photos I like to take. Comparing the bar charts with the photos themselves led me to realize the sheer amount of repetitive photos I take of things and how they effect the color results.
                  

### Photo Taken Time

I discovered that I prefer taking photos at night, as the five most common hours for photo-taking were:
- 21:00 with 1415 occurrences.
- 18:00 with 1213 occurrences.
- 20:00 with 1141 occurrences.
- 17:00 with 1130 occurrences.
- 16:00 with 1098 occurrences.

In 2020 and 2024, there was an increase in photos taken late at night (between 12 AM and 4 AM) from April to July. Looking at my photos in 2020, this was likely due to COVID affecting my sleep schedule, while in 2024, it was probably because of midterm exam preparation, as I tend to study late into the night.


### Photo Count
I also found out that the number of photos I took significantly decreased around the start of COVID (end of 2020) and continued to be low during the university exam period (2022-2023). They slowly got back to how they were especially with starting the university (September 2023). The outlier month regarding the photo count was March 2020 since I took a trip to Europe that month and took in total 1006 photos in a month.


## Limitations 
I couldn't get the 2022 photos' taken times so there is a gap in understanding the photo-taking habits. I would've liked to get the location of these photos to create a map with it but I couldn't get this data. Also, the dominant color extraction can be more precise by using an elbow method or silhouette to find the optimal k value but with fewer photos probably. Doing more analysis and visualization of the data to find more observations can be done as well.

## Future Plans
I plan to work on this project to improve the website and do more analysis of the results.
