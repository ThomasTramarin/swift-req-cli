import requests
import argparse
from api_request import make_request
import json
import os

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(prog="swift-req", description="A simple CLI API client for making fast and efficient HTTP requests with minimal setup.")
    parser.add_argument("-m", "--method", help="The HTTP method to use for the request.", choices=["GET", "POST", "PUT", "DELETE", "PATCH"], default="GET")
    parser.add_argument("-u", "--url", help="The URL to make the request to.", required=True, type=str)
    parser.add_argument("-v", "--verbose", help="Show detailed response information", action="store_true")
    parser.add_argument("-o", "--output", help="File to save the response to (.txt)", type=str)
    parser.add_argument("-d", "--data", help="Data to send with the request", type=str)
    parser.add_argument("-H", "--headers", help="Headers to send with the request (as JSON)", action="append", default=[])

    args = parser.parse_args()

    # Convert the JSON string in the -d argument to a Python dictionary
    data = None
    if args.data:
        try:
            data = json.loads(args.data)  # Convert the string to a dictionary
        except json.JSONDecodeError:
            print("Invalid JSON data provided.")
            return
    
     # Convert the JSON string in the -H argument to a Python dictionary for headers
    headers = {}
    for header in args.headers:
        try:
            key, value = header.split(":", 1)
            headers[key.strip()] = value.strip()
        except ValueError:
            print(f"Invalid header format: {header}. Headers should be in 'Key: Value' format.")
            return


    response = make_request(method=args.method, url=args.url, data=args.data, headers=headers)

    if response:
        
        if args.output: # Save the response to a file

            output_dir = os.path.dirname(args.output)  # Get the directory of the output file
            
            if output_dir and not os.path.exists(output_dir): # If the directory doesn't exist, create it
                os.makedirs(output_dir)  # Create the directory
            
            # Check if the file is a txt file
            if not args.output.endswith(".txt"):
                print("Output file must be a .txt file.")
                return

            # Confirm before overwriting the file
            if os.path.exists(args.output):
                overwrite = input(f"File {args.output} already exists. Do you want to overwrite it? (y/n): ")
                if overwrite.lower() != "y" or overwrite.lower() == "yes":
                    print("File not overwritten.")
                    return
                
            # Open the file in write mode    
            with open(args.output, "w") as file:
                # Write the response to the file
                if args.verbose:
                    file.write(f"Status Code: {response.status_code}\n\n")
                    file.write(f"Headers:\n{json.dumps(dict(response.headers), indent=4)}\n\n")

                file.write(f"Response Body:\n{response.text}")

            print(f"Response saved to {args.output}")
            return
        
        # If verbose mode, print status, headers and body
        if args.verbose:
            print(f"Status Code: {response.status_code}\n")
            print(f"Headers:\n{json.dumps(dict(response.headers), indent=4)}\n")

        print(f"Response Body:\n{response.text}")

    else:
        print(f"Error: No response received")

    

if __name__ == '__main__':
    main()