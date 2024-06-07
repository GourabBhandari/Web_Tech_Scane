import streamlit as st
import builtwith


def main():
    st.title("Website Technology Lookup")

    url = st.text_input("Enter Url:")

    if url:
        website = builtwith.parse(url)
        st.write("Technologies used by the website:")
        for key, value in website.items():
            st.write(f"**{key}**: {', '.join(value)}")


if __name__ == "__main__":
    main()
