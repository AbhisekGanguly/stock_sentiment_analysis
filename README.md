# Sentiment Analysis of Stocks

This project is a Python application that performs sentiment analysis on Twitter data related to a specific stock. The application uses the Twitter API to gather tweets containing the stock symbol, and then uses Azure Cognitive Services for Language to perform sentiment analysis on the tweet data. The sentiment analysis results are then displayed in a graphical user interface.

## Getting Started

To use this application, you will need to have the following:

* Python 3.6 or later installed on your computer
* An Azure Cognitive Services for Language account and API key
* A Twitter Developer account and API credentials

You will also need to install the python libraries listed in the requirements.txt file.
To install them you can run the following command in your terminal:

`pip install -r requirements.txt`

I would suggest making a seperate environment to do so. It can be done by running the following command in your terminal:

`python -m venv env`

Then, activate the environment by running the following command:

`env\Scripts\activate`

Alternatively, you can use the Anaconda distribution to create a virtual environment.

`conda create -n env python=3.10`

Then, activate the environment by running the following command:

`conda activate env`

## Usage

To use the application, follow these steps:

1. Clone the repository to your local machine.
2. Open the config.py file and enter your Azure Cognitive Services for Language API key and endpoint, as well as your Twitter API credentials.
3. Open the sentiment_analysis.py file and modify the STOCK_SYMBOL variable to the stock symbol you want to analyze.
4. Run the application by executing the run.py file.

The application will display a graphical user interface with a sentiment analysis chart and a table of the most positive and negative tweets related to the stock symbol.

## Project Structure
* `config.py`: Configuration file for API keys and endpoints.
* `sentiment_analysis.py`: Python script that performs sentiment analysis on tweet data.
* `twitter_api.py`: Python script that uses the Tweepy library to gather tweet data.
* `gui.py`: Python script that creates the graphical user interface.
* `run.py`: Python script that runs the application.
* `README.md`: This file.

## Contributing
This project is open to contributions. If you would like to contribute, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
* Tweepy library
* TKinter library
* Azure Cognitive Services for Language