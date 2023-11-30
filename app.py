import streamlit as st

def main():
    st.title('Streamlit App with Embedded My Google Map')
    st.write('Here is an example of embedded LDS Londonderry Map:')

    # Embedding Google Map using HTML iframe
    st.markdown("""
    <iframe src="https://www.google.com/maps/d/embed?mid=19HDePXZ3Lry3h7pQaelMXKL5QYGpgJg&ehbc=2E312F" width="640" height="480"></iframe>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

