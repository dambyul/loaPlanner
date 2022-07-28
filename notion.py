import requests
import keys

headers = {
    'Authorization': 'Bearer ' + keys.notion_key,
    'Notion-Version': '2022-06-28'
}

def createData(name, num, type, comp):
    json_data = {
        'parent': {
            'database_id': keys.notion_board,
        },
        'properties': {
            '이름': {
                'title': [
                    {
                        'text': {
                            'content': name,
                        },
                    },
                ],
            },
            '번호': {
                'number':int(num),
            },
            '태그': {
                'multi_select': [
                    {
                        'name': type,
                    },
                ],
            },
            '완료': {
                'multi_select': [
                    {
                        'name': comp,
                    },
                ],
            },
        },
    }

    response = requests.post('https://api.notion.com/v1/pages', headers=headers, json=json_data)
    print(response.text)
