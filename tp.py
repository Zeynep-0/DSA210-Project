import cv2
import numpy as np
import os
from sklearn.cluster import KMeans
from collections import Counter
import matplotlib.pyplot as plt
import json
from concurrent.futures import ThreadPoolExecutor
import csv

os.environ["LOKY_MAX_CPU_COUNT"] = "4"

def extract_dominant_colors(image, num_colors=7):
    """Extract dominant colors using MiniBatchKMeans for faster processing."""
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.reshape(-1, 3)
    kmeans = KMeans(n_clusters=num_colors, random_state=30, max_iter=500)
    kmeans.fit(image)
    return kmeans.cluster_centers_.astype(int)

def merge_similar_colors_in_counter(color_counter, threshold=30):
    """Merge similar colors based on distance threshold."""
    merged_counter = Counter()
    colors = list(color_counter.keys())
    color_array = np.array(colors)
    for color, count in color_counter.items():
        dist = np.linalg.norm(color_array - np.array(color), axis=1)
        close_colors = np.where(dist < threshold)[0]
        if close_colors.size > 0:
            merged_color = tuple(color_array[close_colors[0]])
            merged_counter[merged_color] += count
        else:
            merged_counter[color] = count
    return merged_counter

def process_image(image_path, num_colors=7):
    """Process a single image to extract dominant colors."""
    try:
        image = cv2.imread(image_path)
        if image is None:
            print(f"Failed to read image: {image_path}")
            return []
        image = cv2.resize(image, (150, 150))  # Resize once per image
        dominant_colors = extract_dominant_colors(image, num_colors)
        return {tuple(color): 1 for color in dominant_colors}
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return []

def process_images_in_folder(folder_path, num_colors=7):
    """Process all images in a folder and cluster dominant colors."""
    color_counter = Counter()
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        for file_name in os.listdir(folder_path):
            if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                image_path = os.path.join(folder_path, file_name)
                futures.append(executor.submit(process_image, image_path, num_colors))
        
        for future in futures:
            image_colors = future.result()
            color_counter.update(image_colors)
    
    merged_counter = merge_similar_colors_in_counter(color_counter, threshold=45)
    return merged_counter

def display_color_summary(colors_with_counts):
    """Display a summary of colors."""
    color_bar = np.zeros((50, 300, 3), dtype='uint8')
    num_colors = len(colors_with_counts)
    block_width = 300 // num_colors

    for i, (color, _) in enumerate(colors_with_counts):
        start_x = i * block_width
        end_x = start_x + block_width
        color = np.array(color, dtype='uint8')
        color_bar[:, start_x:end_x, :] = color

    plt.figure(figsize=(6, 2))
    plt.axis("off")
    plt.imshow(color_bar)
    plt.show()

def save_color_data_to_csv(year_folder, month_folder, colors, counts):
    """Save flattened color data (RGB values and counts) to a CSV file for each month/year."""
    output_file = f"{year_folder}_{month_folder}_color_summary.csv"
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Color (R, G, B)', 'Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header
        writer.writeheader()
        
        # Write color data rows
        for color, count in zip(colors, counts):
            writer.writerow({'Color (R, G, B)': color, 'Count': count})

    print(f"Color data for {year_folder} - {month_folder} saved to {output_file}")

def process_year_and_month(base_path, num_colors=7):
    """Process folders by year and month."""
    results = {}
    for year_folder in os.listdir(base_path):
        year_path = os.path.join(base_path, year_folder)
        if os.path.isdir(year_path) and year_folder.startswith("Photos_20"):
            results[year_folder] = {}
            for month_folder in os.listdir(year_path):
                month_path = os.path.join(year_path, month_folder)
                if os.path.isdir(month_path):
                    print(f"Processing Year: {year_folder}, Month: {month_folder}")
                    month_colors = process_images_in_folder(month_path, num_colors)
                    top_colors = month_colors.most_common(10)
                    results[year_folder][month_folder] = [(tuple(color), count) for color, count in top_colors]
                    
                    # Save the monthly color data to CSV
                    colors = [color for color, _ in top_colors]
                    counts = [count for _, count in top_colors]
                    save_color_data_to_csv(year_folder, month_folder, colors, counts)

                    display_color_summary(top_colors)
    return results

# Base folder containing year and month folders
base_folder = r"C:\Users\Lenovo\Desktop"

# Process and store results
color_data = process_year_and_month(base_folder, num_colors=5)