import os

def required_variables():
    print("Finding environment vars")
    if os.environ.get("SECRET_AZURE_TOKEN"):
        print("Found $SECRET_AZURE_TOKEN environment variable!")
    else:
        print("No dice! will not be able to work without setting $SECRET_AZURE_TOKEN")
        raise RuntimeError("set env SECRET_AZURE_TOKEN")

def main():
    """
    Simple function that will poke around at environment variables and report back
    on GitHub secrets available for this Action
    """
    required_variables()
    
