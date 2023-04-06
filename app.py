from datetime import datetime
import gradio as gr
import pandas as pd
from decouple import config
import requests


def auth(username: str, password: str) -> bool:
    """
    Authenticate a user.

    Parameters
    ----------
    username : str
        The username to authenticate.
    password : str
        The password to authenticate.

    Returns
    -------
    bool
        True if the username and password are correct, False otherwise.
    """
    if username == config("USERNAME") and password == config("PASSWORD"):
        return True
    else:
        return False

def predict(df):
    """
    Performs multilabel prediction on a pandas DataFrame containing text data using a saved PyTorch model.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing the text data to be predicted.

    Returns
    -------
    pandas.DataFrame
        The input DataFrame with two additional columns appended for the predicted label and predicted is_offensive value.

    Examples
    --------
    >>> import pandas as pd
    >>> from predict import predict
    >>> df = pd.DataFrame({"text": ["Naber Canım?", "Naber lan hıyarto?"]})
    >>> predicted_df = predict(df)
    >>> print(predicted_df)
              text                  target                  is_offensive
    0  Naber Canım?                 OTHER                       0
    1  Naber lan hıyarto?           INSULT                      1
    """
    start_date = datetime.now()
    api_url = "http://44.210.240.127/multilabel-prediction"
    items = {"texts": list(df["text"])}
    response = requests.post(api_url, json=items)
    results = response.json()["result"]["model"]
    targets = [result["prediction"] for result in results]
    is_offensive = [result["is_offensive"] for result in results]
    df["target"] = targets
    df["is_offensive"] = is_offensive
    end_date = datetime.now()
    print(f" returned successfully - time : {end_date - start_date}")
    return df

def get_file(file):
    """
    Reads a file and returns a processed CSV file containing predicted labels and is_offensive values for each row of text.

    Parameters
    ----------
    file : file object
        A file object that is uploaded by the user through the interface.

    Returns
    -------
    output_file : str
        The file path of the resulting CSV file.

    Examples
    --------
    >>> file = open("sample_data.txt", "r") - example...
    >>> get_file(file)
    "datasets/Nane&Limon.csv"
    """
    output_file = "datasets/Nane&Limon.csv"

    df = pd.read_csv(file.name, sep="|")

    predicted_df = predict(df.copy())
    predicted_df.to_csv(output_file, index=False, sep="|")
    return output_file


# Launch the interface with user password
iface = gr.Interface(get_file, "file", "file")

if __name__ == "__main__":
    iface.launch(share=True, auth=auth)
