
# Photo Gallery Analysis Project

## About the Project
This project is for the **DSA210 Introduction to Data Science** class. I analyzed my photo gallery from 2016 to 2024 to uncover patterns and trends in my photography habits.[My website for this project](https://zeynep-0.github.io/DSA210-Project/index.html#)

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
- [Limitations](#limitations)

## Motivation
I wanted to see if there was any relation between a photo's color and the month it was taken in my life. I want to figure out if there are any prominent colors related to each month and if there is a shift through the years. I also wanted to see if there were any trends in the amount of photos taken between months and years. Ultimately, my main motivation was that I find colors interesting and this project allows me to explore them while learning more about my gallery and photo taking habits.



## Data Set
I used **my photo gallery** as the dataset, with photos sourced from:
- [Google Photos](https://photos.google.com/)
- My phone's memory.


## Data Pre-Processing
1. **Manual Categorization**:
   - Organized photos by year and month.
   - Excluded screenshots due to their predominantly white color skewing the results.
   - Created a Word document summarizing monthly photo counts for each year.
2. **Python Script**:
   - Extracted photo metadata (e.g., photo taken time) from JSON files provided by Google Takeout.
  

## Data Processing

### Dominant Color Analysis
- **Method**:
  - Used **kMeans clustering** to identify the top 5 dominant colors in each photo.
  - Determined the `k` value by experimenting with different settings and comparing results.
- **Color Merging**:
  - Merged similar colors based on an RGB distance threshold.
  - Determined the threshold through iterative testing.
- **Optimization**:
  - Processed over 16,000 photos using threads to speed up the color extraction.
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

## Data Visualization

### Dominant Color Analysis
For visualizing the top 10 most common colors for each year, I processed the CSV files containing monthly color data and combined them into yearly datasets. After merging similar colors using an RGB distance threshold, I created visualizations using **Altair**:

- **Interactive Pie Chart**: Displays the count of each color along with their RGB values.
- **Bar Chart**: Shows how the top colors for each month evolved over the years.
- **Bar Chart**: Analyzes the distribution of yearly color data across all months.

I initially considered using Plotly for these visualizations but faced issues embedding Plotly graphs as HTML files into the website. 


### Photo Taken Time
- Created a [Scatter Plot] with Altair to show photo-taking hours by month.
- Added a dropdown menu to view year-specific data.

### Photo Count
- Created a [Scatter Plot] with Altair to depict yearly photo counts across months.
- Added a dropdown menu to examine month-specific trends.


## Limitations
I couldn't get the 2022 photos' taken times so it was quite a gap in understanding the photo-taking habits. Also, I would've liked to get the location of these photos to create a map with it. Also, the dominant color extraction can be more precise by using an elbow method or silhouette to find the optimal k value but with fewer photos probably. Doing more analysis and visualization of the data to find more observations can be done as well. I plan to work on this project to improve the website and do more analysis of the results.
