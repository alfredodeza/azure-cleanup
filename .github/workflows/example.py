import os

def required_variables():
    print("Finding environment vars")
    token = os.environ.get("SECRET_AZURE_TOKEN")
    if token:
        print("Found $SECRET_AZURE_TOKEN environment variable!")
        if len(token) == 0:
            raise RuntimeError("SECRET_AZURE_TOKEN environment variable exists, but is empty")
    else:
        print("No dice! will not be able to work without setting $SECRET_AZURE_TOKEN")
        raise RuntimeError("set env SECRET_AZURE_TOKEN")

def main():
    """
    Simple function that will poke around at environment variables and report back
    on GitHub secrets available for this Action
    """
    required_variables()
    
if __name__ == '__main__':
    main()
