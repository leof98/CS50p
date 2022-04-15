# implement a program that prompts the user for the name of a file
# and then outputs that file’s media type if the file’s name ends,
# case-insensitively, in any of these suffixes:.gif jpg jpeg png pdf txt .zip
# 14.04

file = str(input("File name: "))
file = file.lower()

if file.endswith(".gif"):
    print("image/gif")

elif file.endswith(".png"):
    print("image/png")

elif file.strip().endswith(".pdf"):
    print("application/pdf")

elif file.endswith(".txt"):
    print("text/plain")

elif file.endswith(".zip"):
    print("application/zip")

elif file.endswith(".bin"):
    print("application/octet-stream")

elif file.endswith(".jpg") or file.endswith("jpeg"):
    print("image/jpeg")
