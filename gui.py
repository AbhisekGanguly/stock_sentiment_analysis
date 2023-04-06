import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import sentiment_analysis as sa
import matplotlib.pyplot as plt

class GUI:

    def __init__(self, master):

        # Making the app screen and the table size a little larger
        master.geometry("800x600")

        self.master = master
        master.title("Sentiment Analysis GUI")

        self.label = ttk.Label(master, text="Enter a stock symbol (e.g., AAPL)")
        self.label.pack()

        self.entry = ttk.Entry(master)
        self.entry.pack()

        self.button = ttk.Button(master, text="Analyze", command=self.analyze)
        self.button.pack()

        # tables to properly display the result in the analyze() function
        self.table = ttk.Treeview(master, columns=("text", "sentiment"), show="headings", height=30)
        self.table.column("text", width=600)
        self.table.column("sentiment", width=200)
        self.table.heading("text", text="Tweet")
        self.table.heading("sentiment", text="Sentiment")
        self.table.pack()

        # Adding a pie chart of the sentiment analysis of neutral, positive, mixed and negative tweets
        self.pie_chart = ttk.Label(master, text="Pie Chart")
        self.pie_chart.pack()

    global tweets_with_sentiment_df

    # Function to analyze the sentiment of tweets containing a specific stock symbol
    def analyze(self):
        stock_symbol = self.entry.get().upper()
        if not stock_symbol:
            messagebox.showerror("Error", "Please enter a stock symbol")
            return
        try:
            tweets_with_sentiment_df = sa.get_tweets_with_sentiment(stock_symbol)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        
        # Out put the returned dataframe to the GUI with proper formatting as an interactive table
        for index, row in tweets_with_sentiment_df.iterrows():
            self.table.insert("", "end", values=(row["text"], row["sentiment"]))
        self.table.pack()


def main():
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()