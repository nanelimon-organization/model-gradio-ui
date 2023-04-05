from datetime import datetime
import gradio as gr
import pandas as pd
from decouple import config
import requests


def auth(username, password):
    if username == config("USERNAME") and password == config("PASSWORD"):
        return True
    else:
        return False


def predict(df):

    start_date = datetime.now()
    api_url = "http://127.0.0.1:5000/prediction"
    items = {"texts": list(df["text"])}
    response = requests.post(api_url, json=items)
    print(response.json())
    results = response.json()["result"]["model"]
    labels = [result["prediction"] for result in results]
    is_offensive = [result["is_offensive"] for result in results]
    df["predicted_label"] = labels
    df["predicted_is_offensive"] = is_offensive
    end_date = datetime.now()
    print(f" returned successfully - time : {end_date - start_date}")
    return df


def get_file(file):
    output_file = "datasets/Nane&Limon.csv"

    df = pd.read_csv(file.name, sep="|")

    predicted_df = predict(df.copy())
    predicted_df.to_csv(output_file, index=False, sep="|")
    return output_file


# Launch the interface with user password
iface = gr.Interface(get_file, "file", "file")

if __name__ == "__main__":
    iface.launch(share=True, auth=auth)
