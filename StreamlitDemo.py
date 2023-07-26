{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPrrTdyEiD0timZb7cdChZX",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/CVVilla/StreamlitDemo/blob/main/StreamlitDemo.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#IMPORT Streamlit\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "\n"
      ],
      "metadata": {
        "id": "04-it1cjQb_k"
      },
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "#import our csv file\n",
        "df = pd.read_csv(\"cereal.csv\")\n",
        "\n",
        "#Create a page title for the page\n",
        "#Emojis can be used as icons from https://www.webfx.com/tools/emoji-cheat-sheet/\n",
        "st.set_page_config(page_title=\"Cereals!\", page_icon=\":bowl_with_spoon:\", layout='wide')\n",
        "\n",
        "with st.container():\n",
        "    st.title(\"A Streamlit analysis demonstration using the Cereals Dataset!\")\n",
        "    st.subheader(\"Below is the full dataset we will be using for our demonstration.\")\n",
        "    st.write(df)\n",
        "\n",
        "\n",
        "\n",
        "#A selection option for choosing desired cereal brand\n",
        "#after selecting a cereal brand, information regarding brand is displayed onto the user\n",
        "with st.container():\n",
        "    st.subheader(\"Select a cereal brand below from the dataset\")\n",
        "    cereals_name = st.selectbox(\"Choose a Cereal Brand\", df['name'].unique())\n",
        "    cereal_info = df[df['name'] == cereals_name]\n",
        "    st.header(f\"Selected: {cereals_name}\")\n",
        "    st.write(cereal_info)\n"
      ],
      "metadata": {
        "id": "GX3mLjDbQgWW"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "ichpMkIIQwQe"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}