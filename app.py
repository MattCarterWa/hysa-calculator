import streamlit as st

st.title("HYSA vs T-Bill Calculator")

p = st.number_input("Principal ($)", value=10000)
hysa_apy = st.number_input("HYSA APY (%)", value=4.5) / 100
tbill_yield = st.number_input("T-Bill Yield (%)", value=5.2) / 100
fed_tax = st.number_input("Federal Tax Rate (%)", value=22.0) / 100
state_tax = st.number_input("State Tax Rate (%)", value=0.0) / 100

hysa_net = p * hysa_apy * (1 - fed_tax - state_tax)
tbill_net = p * tbill_yield * (1 - fed_tax)

st.subheader(f"HYSA Annual Net: ${hysa_net:,.2f}")
st.subheader(f"T-Bill Annual Net: ${tbill_net:,.2f}")

if tbill_net > hysa_net:
    st.success(f"T-Bills win by ${tbill_net - hysa_net:,.2f}")
else:
    st.success(f"HYSA wins by ${hysa_net - tbill_net:,.2f}")
  
