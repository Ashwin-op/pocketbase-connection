# Streamlit Pocketbase Connector

This repository contains a [Streamlit](https://streamlit.io) app that connects to a [Pocketbase](https://pocketbase.io) database.

The goal of this app is to provide a simple example of how to connect to a Pocketbase database using the [Pocketbase Python Client](https://github.com/vaphes/pocketbase) and Streamlit's new [Experimental Connection API](https://docs.streamlit.io/library/api-reference/connections/st.experimental_connection).

## How to run this app

> **Note:** You need poetry installed to run this app. If you don't have it, you can follow the instructions [here](https://python-poetry.org/docs/#installation).

1. Clone this repo.
2. Create `.streamlit/secrets.toml` and add your Pocketbase Endpoint to it. It should look like this:

```toml
pb_url = "http://127.0.0.1:8090"
```

3. Run `poetry install` in the root directory of this repo.
4. Download the Pocketbase Executable from [here](https://github.com/pocketbase/pocketbase/releases) and run it.
5. Run `poetry run streamlit run app.py` in the root directory of this repo.
6. Enjoy!
