import streamlit as st
from generate_password import generate_password


def main():
    st.title("Password generator")

    st.info("Choose your password length")
    length = st.slider("Password Length", min_value=6, max_value=30, value=12)

    st.info("Select the character types to include")
    use_lowercase = st.checkbox("Use Lowercase Letters")
    use_uppercase = st.checkbox("Use Uppercase Letters")
    use_digits = st.checkbox("Use Digits")
    use_special_chars = st.checkbox("Use Special Characters")

    if st.button("Generate Password"):
        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
        if password:
            st.success("Generated Password: {}".format(password))
            st.text_input("Copy the password from here", value=password)


if __name__ == "__main__":
    main()
