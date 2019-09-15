import os
import webview


"""
An example of serverless app architecture
"""


class Api():
    def changeMessage(self, param):
        return {'text': 'abc'} 


if __name__ == '__main__':
    api = Api()
    webview.create_window('Todos magnificos', 'assets/index.html', js_api=api, min_size=(600, 450))
    webview.start()
