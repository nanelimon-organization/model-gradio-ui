import gradio as gr
import pandas as pd
from decouple import config

def auth(username, password):
    if username == config("USERNAME") and password == config("PASSWORD"):
        return True
    else:
        return False


def predict(df):
    # TODO:
    df["offansive"] = 1
    df["target"] = None

    # ***************************
    # WRITE YOUR INFERENCE STEPS BELOW
    #
    # HERE
    #
    # *********** END ***********
    return df


def get_file(file):
    output_file = "output_Nane&Limon.csv"

    # For windows users, replace path seperator
    file_name = file.name.replace("\\", "/")

    df = pd.read_csv(file_name, sep="|")

    predict(df)
    df.to_csv(output_file, index=False, sep="|")
    return (output_file)


# Launch the interface with user password
iface = gr.Interface(get_file, "file", "file")

if __name__ == "__main__":
    iface.launch(share=True, auth=auth)