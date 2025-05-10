import streamlit as st
import requests

st.title("Pdatatrigger - Vulnerability Scanner")

target_url = st.text_input("Enter URL to scan:")

if st.button("Scan"):
    if target_url:
        try:
            response = requests.post(
                "http://localhost:8000/api/v1/scan/",
                json={"target": target_url}
            )
            response.raise_for_status()
            results = response.json()
            st.subheader(f"Scan Results for: {results['target']}")
            if results["vulnerabilities"]:
                st.warning("Vulnerabilities Found:")
                for vuln in results["vulnerabilities"]:
                    st.markdown(f"- {vuln}")
            else:
                st.success("No vulnerabilities found.")
        except requests.exceptions.RequestException as e:
            st.error(f"Error during scan: {e}")
    else:
        st.warning("Please enter a URL.")
