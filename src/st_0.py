import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


if __name__ == "__main__":
    st.title("Experiments")

    df = pd.DataFrame(np.random.randn(50, 20), columns=(f"col {i}" for i in range(20)))
    st.dataframe(df)

    fig = plt.figure()
    plt.plot(df["col 0"], df["col 1"])
    st.pyplot(fig)

    image = np.random.randint(low=0, high=255, size=(512, 512, 3))
    st.image(image)
