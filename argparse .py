import argparse
import requests

def download_file(url, local_filename): 
    if local_filename is None:
        local_filename = url.split('/')[-1]
    
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename

# Create an ArgumentParser
parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("url", help="URL of the file to download")
parser.add_argument("-o", "--output", type=str, help="Name of the file", default=None)

# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print("URL:", args.url)
print("Output:", args.output)

# Call the download_file function with the provided URL and output file name
downloaded_file = download_file(args.url, args.output)

print(f"File '{downloaded_file}' has been downloaded.")
