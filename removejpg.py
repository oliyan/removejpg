import os

allraw = ('.NEF', '.CR2', '.CR3', '.ARW')
thispath = input("Enter the location you want to clean: ")

# Ensure the path is valid
if not os.path.isdir(thispath):
    print("The specified path is not a valid directory.")
else:
    n = 0
    # for every file in this directory
    for thisfile in os.listdir(thispath):

        # if the file name ends with a JPG
        if thisfile.lower().endswith(".jpg"):
            # Build the full path of the jpg file
            jpg_path = os.path.join(thispath, thisfile)

            # check whether any raw file is present too
            for thisraw in allraw:
                raw_file_path = os.path.join(thispath, os.path.splitext(thisfile)[0] + thisraw)
                if os.path.exists(raw_file_path):
                    # if yes, then remove the jpg file
                    os.remove(jpg_path)
                    print(f"Removed: {jpg_path}")
                    n += 1
                    break  # Stop checking other raw formats once a match is found

    print(f"Total JPG files removed: {n}")
