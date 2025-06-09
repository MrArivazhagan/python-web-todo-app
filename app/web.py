import streamlit as st

st.warning("⚠️ This page has been moved!")
st.info("The Todo App has been restructured. Please use the new main page.")

if st.button("🚀 Go to New Todo App"):
    st.switch_page("app/main.py")

st.write("---")
st.write("### What's New:")
st.write("✅ Improved interface with better layout")
st.write("✅ New dedicated Todos List viewer page")
st.write("✅ Export functionality")
st.write("✅ Multiple viewing options")