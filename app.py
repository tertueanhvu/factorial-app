import streamlit as st
from factorial import fact 

def main():
  #Tạo tiêu đề cho ứng dụng
  st.title('Factorial Calculator')

 #Tạo ô nhập số cần tính
  number = st.number_input('Enter a number:',
                           min_value=0,
                           max_value=900,
                           step=1) #python không tính được >1000!
  if st.button('Calculate'): #tạo nút tính toán
    result = fact(number)
    st.write(f'The factorial of {number} is {result}') #In ra kết quả
    st.balloons() #Bóng bóng kết quả thành công
    
if __name__ == '__main__':
     main()