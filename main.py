import modules.api as api

def get_token(filename=''):
    """Helper to get a token from a file 
    (just reads a file and strips whitespace)
    
    Returns:
        str: Contents of the file
    """
    token = ''
    try: 
        with open(filename, 'r') as f:
            token = f.read().strip()
    except Exception as e:
        raise e
    return token


def main():
    try:
        token = get_token("./token")
        username = get_token("./username")
    except Exception as e:
        print(f"Failed to get token: {str(e)}")
        exit()

    api_obj = api.API(api.robinhood, token, username=username)

    # Trivial test to see if you were able to login!
    print(f"AAPL price from robinhood: {str(api_obj.get_price("AAPL"))}")


if __name__ == '__main__':
    main()