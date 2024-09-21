from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from datetime import datetime, timedelta
import requests

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text="请选择预约天数")
        layout.add_widget(self.label)

        # 创建 Spinner，用于选择天数 (明天、后天、大后天)
        self.spinner = Spinner(
            text='1',  # 默认选择1天（明天）
            values=('1', '2', '3')  # 1: 明天, 2: 后天, 3: 大后天
        )
        layout.add_widget(self.spinner)

        # 创建按钮，用于触发预约
        self.btn = Button(text="预约")
        self.btn.bind(on_press=self.schedule_appointment)
        layout.add_widget(self.btn)

        return layout

    def get_future_date(self, days_ahead):
        # 计算未来日期并格式化
        start_time = (datetime.now() + timedelta(days=int(days_ahead))).replace(hour=18, minute=30, second=0, microsecond=0)
        end_time = start_time + timedelta(hours=2)
        return start_time.strftime("%Y-%m-%d %H:%M:%S"), end_time.strftime("%Y-%m-%d %H:%M:%S")

    def schedule_appointment(self, instance):
        # 获取选择的天数并计算日期
        days_ahead = self.spinner.text
        occupy_time_start_str, occupy_time_end_str = self.get_future_date(days_ahead)

        # 显示预约时间
        self.label.text = f"预约开始时间: {occupy_time_start_str}\n预约结束时间: {occupy_time_end_str}"

        # 预约请求数据
        xuehao = "2022400328"
        phone = "18098994389"
        cookies = {
            'ltToken': '10b33ef71ccd41acaabf272b16f19d78',
            'sdp_app_session-legacy-443': 'c9750d978c9238a029e3fb2c1eccb2eee314cef7440276a64033fd5013d6973867c47e90c25b959a9d983a050842c71f7aa086e525c66cb2b5807d5c5c4a95391f4e012f62430a2d7aa01f6d4d51825271bdfd309ba6c377b28355a109538dd5b5c541655afa19e97590ca44daa199a09619e6032494b66fb5e7a358b0387cb898acfc9aa176e5b1e2a2444706ba17c41bbf6531cba384a29a66520883a7b458',
            'sdp_app_session-443': 'c9750d978c9238a029e3fb2c1eccb2eee314cef7440276a64033fd5013d6973867c47e90c25b959a9d983a050842c71f7aa086e525c66cb2b5807d5c5c4a95391f4e012f62430a2d7aa01f6d4d51825271bdfd309ba6c377b28355a109538dd5b5c541655afa19e97590ca44daa199a09619e6032494b66fb5e7a358b0387cb898acfc9aa176e5b1e2a2444706ba17c41bbf6531cba384a29a66520883a7b458',
        }
        data = {
            "users": [
                {
                    "jobNum": xuehao,
                    "userId": xuehao,
                    "contact": phone,
                    "checked": False
                }
            ],
            "jobNum": xuehao,
            "userId": xuehao,
            "applyRemark": "",
            "infoId": "ff8081818a601d39018aa718771005ef",
            "occupyId": "",
            "occupyTimeEnd": occupy_time_end_str,
            "occupyTimeStart": occupy_time_start_str,
            "occupyType": "1",
            "resUseType": "0",
            "timeChooseType": "2",
            "isInvite": "0",
            "location": "深圳市南山区",
            "msgLeadTime": [],
            "leaveUsers": [],
            "auditUserIds": [],
            "formManagePropertyValueList": []
        }
        

        headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,zh-Hans;q=0.8',
    'content-type': 'application/json;charset=UTF-8',
    # 'cookie': 'ltToken=10b33ef71ccd41acaabf272b16f19d78; sdp_app_session-legacy-443=c9750d978c9238a029e3fb2c1eccb2eee314cef7440276a64033fd5013d6973867c47e90c25b959a9d983a050842c71f7aa086e525c66cb2b5807d5c5c4a95391f4e012f62430a2d7aa01f6d4d51825271bdfd309ba6c377b28355a109538dd5b5c541655afa19e97590ca44daa199a09619e6032494b66fb5e7a358b0387cb898acfc9aa176e5b1e2a2444706ba17c41bbf6531cba384a29a66520883a7b458; sdp_app_session-443=c9750d978c9238a029e3fb2c1eccb2eee314cef7440276a64033fd5013d6973867c47e90c25b959a9d983a050842c71f7aa086e525c66cb2b5807d5c5c4a95391f4e012f62430a2d7aa01f6d4d51825271bdfd309ba6c377b28355a109538dd5b5c541655afa19e97590ca44daa199a09619e6032494b66fb5e7a358b0387cb898acfc9aa176e5b1e2a2444706ba17c41bbf6531cba384a29a66520883a7b458',
    'origin': 'https://cgyy.ssti.net.cn',
    'priority': 'u=1, i',
    'referer': 'https://cgyy.ssti.net.cn/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MjY3NjIzNjgsInVzZXJuYW1lIjoiMjAyMjQwMDMyOCJ9.6uGmrLoat7SPwns9EOFWtp8SHlU4KyiQZIz4fk444kc',
}

        response = requests.post(
            'https://cgyy.ssti.net.cn/hzsun-resm/sub/occupy/doOccupy',
            json=data,
            headers=headers,
            cookies=cookies
        )
        
        if response.status_code == 200:
            self.label.text += "\n预约成功!"
        else:
            self.label.text += f"\n预约失败: {response.text}"

if __name__ == '__main__':
    MyApp().run()
