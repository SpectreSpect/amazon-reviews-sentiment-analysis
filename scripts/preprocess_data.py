import pandas as pd


if __name__ == "__main__":
    df = pd.read_csv("../data/raw/train.csv", names=["polarity", "title", "text"])
    df = df.drop("title", axis=1)
    df.to_csv("../data/preprocessed/train.csv")