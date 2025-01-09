import os
import shutil
from sklearn.model_selection import train_test_split

dataset_dir = r"C:\Users\Vansh Payala\Downloads\archive (13)\raw-img"
train_dir = r"C:\Users\Vansh Payala\Downloads\train"
val_dir = r"C:\Users\Vansh Payala\Downloads\val"
test_dir = r"C:\Users\Vansh Payala\Downloads\test"

# List of animal classes
animal_classes = [
    "pecora", "mucca", "gatto", "gallina", "farfalla", "elefante",
    "cavallo", "cane", "scoiattolo", "ragno"
]

# Creating the directories for train, validation, and test splits
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Creating class-specific directories within train, validation, and test folders
for class_name in animal_classes:
    os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(val_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(test_dir, class_name), exist_ok=True)

# Function to split images into train, validation, and test directories
def split_data(src_dir, train_dir, val_dir, test_dir, test_size=0.2, val_size=0.2):
    for class_name in animal_classes:
        class_src_dir = os.path.join(src_dir, class_name)
        if not os.path.isdir(class_src_dir):
            continue
        
        # Getting all image file paths for the current class
        image_paths = [os.path.join(class_src_dir, img) for img in os.listdir(class_src_dir) if img.endswith(('.jpeg', '.jpg', '.png'))]
        
        # Splitting images into train, validation, and test
        train_images, temp_images = train_test_split(image_paths, test_size=test_size, random_state=42)
        val_images, test_images = train_test_split(temp_images, test_size=val_size/(val_size + test_size), random_state=42)
        
        # Moving the images to the appropriate directories
        for img in train_images:
            shutil.copy(img, os.path.join(train_dir, class_name))
        for img in val_images:
            shutil.copy(img, os.path.join(val_dir, class_name))
        for img in test_images:
            shutil.copy(img, os.path.join(test_dir, class_name))

# Splitting the data into train, validation, and test sets
split_data(dataset_dir, train_dir, val_dir, test_dir)

print("Data split completed successfully into train, validation, and test sets!")