import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == "__main__":
    st.title("Streamlit Demo")

    df = pd.DataFrame(np.random.randn(20, 20), columns=[f"col_{i}" for i in range(20)])
    st.dataframe(df)

    fig = plt.figure()
    plt.plot(df["col_0"], df["col_1"])
    st.pyplot(fig)

    image = np.random.randint(low=0, high=256, size=(512, 512, 3))
    # image = np.arange(512) // 2
    # image = image * image.reshape(1, -1)
    # image = image / image.max()
    # print(image.shape)
    st.image(image)