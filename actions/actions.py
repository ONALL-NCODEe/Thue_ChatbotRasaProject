from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import csv
import pandas as pd

class ActionAnswerMST(Action):

    def name(self) -> Text:
        return "action_get_tax_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        tax_id = tracker.get_slot('taxid')
        
        df = pd.read_csv("./data_chatbot/Data_MST_Chatbot.csv", encoding='utf-8')

        col = df.iloc[:, 0] # lấy cột MST
        total_row = col.size  # lấy tổng số hàng
        
        info = None
        i = 0
        while i < total_row:
            # print(col.iloc[i])
            if col.iloc[i] == int(tax_id):
                info = df.iloc[i]

                keys = ['MST', 'Họ và tên', 'Địa chỉ KD', 'Thuế GTGT', 'Thuế TNCN', 'Thuế Tài Nguyên', 'Tổng số']
                reply = f"Thông tin mã số thuế {tax_id}: \n"
                for key in keys:
                    reply += f"- {key}: {str(info[key])}\n"

                dispatcher.utter_message(text=reply)
                break
            
            i = i + 1

        if info is None:
            dispatcher.utter_message(text=f"Không tìm thấy dữ liệu của mã số thuế {tax_id}. Bạn vui lòng kiểm tra lại.")
           
        return []


class AnswerTaxQuestion(Action):
    def name(self) -> Text:
        return "action_reply_tax_question"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tax_intent = tracker.latest_message['intent'].get('name') # Lấy intent
        tax_content = tracker.get_slot("contentoftax") # Lấy content của tax
        print("Intent extracted: ", tax_intent)
        print("Entity extracted: ", str(tax_content[0]))

        df = pd.read_csv("./data_chatbot/Data_Answers.csv", encoding='utf-8')

        col = df.iloc[:, 0] # lấy cột Tag
        # print(col.iloc[1])
        total_row = col.size  # lấy tổng số hàng
        # print(total_row)

        # col = df.iloc[:, 2]
        row = df.iloc[0]
        print(row)
        print(str(row['Tag']))

        tax_answer = None
        i = 0
        while i < total_row:
            if col.iloc[i] == str(tax_content[0]):
                tax_answer = df.iloc[i]
                print(tax_answer['Trả lời'])
                dispatcher.utter_message(text=tax_answer['Trả lời'])
                break

            i = i + 1

        return []

