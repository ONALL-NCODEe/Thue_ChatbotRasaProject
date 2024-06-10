# import csv
# import pandas as pd

# df = pd.read_csv("./Data_Chatbot/Data_MST_Chatbot.csv", encoding='utf-8')

# tax_id = 2100793084

# mst = df[df['MST'] == tax_id]
# print(mst.values)

# keys = ['Họ và tên', 'Địa chỉ KD', 'Tổng số', 'Thuế GTGT', 'Thuế TNCN', 'Thuế Tài Nguyên']
# print(keys[0])

# # print(int(mst['MST'].values))
# # print(int(df[df['MST'].values]))
# print(mst['MST'].values)

# reply = f"Mã số thuế {tax_id}: \n"
# reply += f"- {'MST'}: ['{int(mst['MST'].values)}']\n"
# for key in keys:
#     reply += f"- {key}: {mst[key].values}\n"

# print(reply)






# import csv
# import pandas as pd

# df = pd.read_csv("./Data_Chatbot/Data_Answers.csv", encoding='utf-8')
# print(df)

# col = df.iloc[:, 2]
# print(col)

# print(df.iloc[1])




# def contains_phone_number(text):
#     # Chuyển đổi chuỗi về chữ thường để so sánh dễ dàng hơn
#     text = text.lower()
#     # Tách chuỗi thành các từ
#     words = text.split()
#     # Kiểm tra xem từ "số" và "điện thoại" có đồng thời xuất hiện trong chuỗi hay không
#     return 'số' in words and 'điện thoại' in words

# # Chuỗi cần kiểm tra
# chuoi = "Số điện thoại của Trung tâm Hỗ trợ triển khai Hóa đơn điện tử của Tổng cục Thuế là như thế nào"

# # Kiểm tra xem chuỗi có chứa cụm từ "số điện thoại" hay không
# if contains_phone_number(chuoi):
#     print("Chuỗi chứa cụm từ 'số điện thoại'")
# else:
#     print("Chuỗi không chứa cụm từ 'số điện thoại'")
