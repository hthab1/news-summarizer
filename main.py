import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def summarize():
    url = utext.get("1.0", "end").strip()

    article = Article(url)

    article.download()
    article.parse()
    article.nlp()

    title.config(state="normal")
    publication.config(state="normal")
    summary.config(state="normal")
    sentiment.config(state="normal")
    author.config(state="normal")

    title.delete("1.0", "end")
    publication.delete("1.0", "end")
    author.delete("1.0", "end")
    summary.delete("1.0", "end")
    sentiment.delete("1.0", "end")

    title.insert("1.0", article.title)
    publication.insert("1.0", str(article.publish_date))
    author.insert("1.0", ', '.join(article.authors))
    summary.insert("1.0", article.summary)

    analysis = TextBlob(article.text)
    sentiment.insert("1.0", f'Polarity: {analysis.polarity}, Sentiment: {"Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"}')

    title.config(state="disabled")
    publication.config(state="disabled")
    summary.config(state="disabled")
    sentiment.config(state="disabled")
    author.config(state="disabled")


root = tk.Tk()
root.title("News Summarizer")
root.geometry("1200x600")

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state="disabled", background="#000000")
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state="disabled", background="#000000")
author.pack()

plabel = tk.Label(root, text="Publication date")
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state="disabled", background="#000000")
publication.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state="disabled", background="#000000")
summary.pack()

selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state="disabled", background="#000000")
sentiment.pack()

ulable = tk.Label(root, text="URL")
ulable.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()