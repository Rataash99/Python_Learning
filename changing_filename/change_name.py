import os

# files = os.listdir("python_Learning")

images = os.listdir("changing_filename/Images")

for i, image in enumerate(images, start = 1):
    old_path = os.path.join("changing_filename/Images", image)
    new_path = os.path.join("changing_filename/Images", f"image_{i}")

    os.rename(old_path, new_path)

print(os.listdir("changing_filename/Images"))
