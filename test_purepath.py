from pathlib import PurePath

# Create a PurePath
path = PurePath('/path/to/some/file.txt')

# Combine paths
new_path = path / 'subdirectory' / 'new_file.txt'

# Access different parts of the path

print("\n ---------------------------------------------------------")
print("path = ", path)
print("new_path = ", new_path)
print("Parent new_path.parent :", new_path.parent)
print("Name: new_path.name ", new_path.name)
print("Stem (filename without extension): new_path.stem ", new_path.stem)
print("Suffix (file extension): new_path.suffix", new_path.suffix)
print("\n ---------------------------------------------------------")

# Convert PurePath to string
path_str = str(new_path)

# Check if the path is absolute
print("Is absolute:", new_path.is_absolute())

# Join paths
combined_path = PurePath('/path', 'to', 'some', 'file.txt')

# Relative paths
relative_path = PurePath('subdirectory', 'file.txt')

# Resolving paths (joining without normalization)
resolved = combined_path
print("Resolved:", resolved)

# Comparing paths
print("Are paths equal?", combined_path == resolved)

##########################OutPut################################################
# path =  \path\to\some\file.txt
# new_path =  \path\to\some\file.txt
# Parent new_path.parent : \path\to\some
# Name: new_path.name  file.txt
# Stem (filename without extension): new_path.stem  file
# Suffix (file extension): new_path.suffix .txt
##########################OutPut################################################



################################################################################
from pathlib import PurePath

# Example file path
file_path = PurePath('/path/to/some/file.txt')

# Extract stem (filename without extension) and suffix (file extension)
stem = file_path.stem
suffix = file_path.suffix

print("File path:", file_path)
print("Stem (filename without extension):", stem)
print("Suffix (file extension):", suffix)

# Modify the filename components
new_stem = stem + "_modified"
new_suffix = ".csv"
new_path = PurePath(file_path.parent, new_stem + new_suffix)

print("New path:", new_path)

##########################OutPut################################################
# File path: /path/to/some/file.txt
# Stem (filename without extension): file
# Suffix (file extension): .txt
# New path: /path/to/some/file_modified.csv
##########################OutPut################################################
