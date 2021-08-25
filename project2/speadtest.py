from speedtest import Speedtest
st = Speedtest()
print("Your connection's Download Speed is: ", st.download())
print("Your connection's upload is : ", st.upload())
