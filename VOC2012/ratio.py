import os
import shutil
import random

def split_dataset(image_source_dir, label_source_dir, dest_dir, train_ratio=0.7, val_ratio=0.2, test_ratio=0.1):
    print(train_ratio + val_ratio + test_ratio)
    #assert train_ratio + val_ratio + test_ratio == 1.0, "The sum of ratios must be 1.0"

    # Create destination directories
    train_image_dir = os.path.join(dest_dir, 'train', 'images')
    val_image_dir = os.path.join(dest_dir, 'val', 'images')
    test_image_dir = os.path.join(dest_dir, 'test', 'images')

    train_label_dir = os.path.join(dest_dir, 'train', 'labels')
    val_label_dir = os.path.join(dest_dir, 'val', 'labels')
    test_label_dir = os.path.join(dest_dir, 'test', 'labels')

    os.makedirs(train_image_dir, exist_ok=True)
    os.makedirs(val_image_dir, exist_ok=True)
    os.makedirs(test_image_dir, exist_ok=True)

    os.makedirs(train_label_dir, exist_ok=True)
    os.makedirs(val_label_dir, exist_ok=True)
    os.makedirs(test_label_dir, exist_ok=True)

    # Get all image files from source directory
    image_files = [f for f in os.listdir(image_source_dir) if os.path.isfile(os.path.join(image_source_dir, f))]
    label_files = [f for f in os.listdir(label_source_dir) if os.path.isfile(os.path.join(label_source_dir, f))]

    # Ensure the image and label files are sorted and matched
    image_files.sort()
    label_files.sort()
    assert len(image_files) == len(label_files), "Number of images and labels must be the same"

    # Shuffle files
    combined = list(zip(image_files, label_files))
    random.shuffle(combined)
    image_files, label_files = zip(*combined)

    # Calculate split indices
    train_end = int(len(image_files) * train_ratio)
    val_end = train_end + int(len(image_files) * val_ratio)

    # Split files
    train_images = image_files[:train_end]
    val_images = image_files[train_end:val_end]
    test_images = image_files[val_end:]

    train_labels = label_files[:train_end]
    val_labels = label_files[train_end:val_end]
    test_labels = label_files[val_end:]

    # Move files to corresponding directories
    for f in train_images:
        shutil.move(os.path.join(image_source_dir, f), os.path.join(train_image_dir, f))
    for f in val_images:
        shutil.move(os.path.join(image_source_dir, f), os.path.join(val_image_dir, f))
    for f in test_images:
        shutil.move(os.path.join(image_source_dir, f), os.path.join(test_image_dir, f))

    for f in train_labels:
        shutil.move(os.path.join(label_source_dir, f), os.path.join(train_label_dir, f))
    for f in val_labels:
        shutil.move(os.path.join(label_source_dir, f), os.path.join(val_label_dir, f))
    for f in test_labels:
        shutil.move(os.path.join(label_source_dir, f), os.path.join(test_label_dir, f))

    print(f"Moved {len(train_images)} image files to {train_image_dir} and {len(train_labels)} label files to {train_label_dir}")
    print(f"Moved {len(val_images)} image files to {val_image_dir} and {len(val_labels)} label files to {val_label_dir}")
    print(f"Moved {len(test_images)} image files to {test_image_dir} and {len(test_labels)} label files to {test_label_dir}")

if __name__ == "__main__":
    image_source_directory = 'C:\\GitHub\\Amazing-Semantic-Segmentation\\VOC2012\\JPEGSegment'
    label_source_directory = 'C:\\GitHub\\Amazing-Semantic-Segmentation\\VOC2012\\SegmentationClass'
    destination_directory = 'VOCSegment'
    split_dataset(image_source_directory, label_source_directory, destination_directory)
