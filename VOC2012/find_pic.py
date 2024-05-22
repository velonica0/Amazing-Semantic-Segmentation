import os
import shutil


def find_and_copy_common_files(source_dir1, source_dir2, dest_dir):
    # Create destination directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)

    # Get list of files in both source directories
    files_source_dir1 = {os.path.splitext(f)[0] for f in os.listdir(source_dir1) if
                         os.path.isfile(os.path.join(source_dir1, f))}
    files_source_dir2 = {os.path.splitext(f)[0] for f in os.listdir(source_dir2) if
                         os.path.isfile(os.path.join(source_dir2, f))}
    # Find common files
    common_files = files_source_dir1.intersection(files_source_dir2)

    # Copy common files to destination directory
    for file_name in common_files:
        src_file_path1 = os.path.join(source_dir1, file_name + '.jpg')
        src_file_path2 = os.path.join(source_dir2, file_name + '.png')

        # Copy from the first source directory
        shutil.copy(src_file_path1, os.path.join(dest_dir, file_name + '.jpg'))

        # Optionally, copy from the second source directory if needed
        #shutil.copy(src_file_path2, os.path.join(dest_dir, file_name + '.png'))


    print(f"Copied {len(common_files)} files to {dest_dir}")

if __name__ == "__main__":
    source_directory1 = 'C:\\GitHub\\Amazing-Semantic-Segmentation\\VOC2012\\JPEGImages'
    source_directory2 = 'C:\\GitHub\\Amazing-Semantic-Segmentation\\VOC2012\\SegmentationClass'
    destination_directory = 'JPEGSegment'
    find_and_copy_common_files(source_directory1, source_directory2, destination_directory)
