import robin_stocks.robinhood as rh
import robin_stocks.gemini as gem
import robin_stocks.tda as tda

# Global variables/types
robinhood = "robinhood"
gemini = "gemini"
ameritrade = "ameritrade"

class API:
    """API wrapper class for which ever API you want to use."""
    def __init__(self, type, token, username=""):
        self.type = type
        self.username = username
        self.token = token
        self._setup()
    
    def _setup(self):
        """Setup the API based on the type of API.

        Args:
           type (str): The type of API to be used.

        Returns:
           API object
        """
        match self.type:
            case "robinhood":
                self._setup_rh()
            case "gemini":
                self._setup_gem()
            case "ameritrade":
                self._setup_tda()
            case _:
                raise ValueError("Invalid API type")

    def _setup_rh(self):
        """Setup the robinhood API."""
        login = rh.login(self.username, self.token)

    def _setup_gem(self):
        """Setup the gemini API."""
        pass

    def _setup_tda(self):
        """Setup the ameritrade API."""
        pass

    def get_price(self, ticker):
        """Get the price of a stock.
        
        Args:
           ticker (str): The ticker to get the price for.

        Returns:
            float: The price of the stock. Optional None type return
        """
        match self.type:
            case "robinhood":
                return rh.stocks.get_latest_price(ticker)[0]
            case "gemini":
                pass
            case "ameritrade":
                pass
            case _:
                raise ValueError("Invalid API type")
            
    



        
