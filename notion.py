import requests
import keys
import json

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


def getData(keyword):
    url = "https://api.notion.com/v1/databases/" + keys.notion_board + "/query"
    payload = {
        "filter": {
            "property": "이름",
            "rich_text": {
                "equals": keyword,
            }
        }
    }
    headers = {
        'Authorization': 'Bearer ' + keys.notion_key,
        "Notion-Version": "2022-06-28"
    }

    response = requests.post(url, json=payload, headers=headers)

    try:
        return json.loads(response.text)['results'][0]['id']
    except:
        return False




def editData(keyword,col,data):
    id = getData(keyword)
    url = "https://api.notion.com/v1/pages/" + id

    headers = {
        'Authorization': 'Bearer ' + keys.notion_key,
        "Notion-Version": "2022-06-28",
    }

    payload = {
        "properties": {
            col: {
                'multi_select': [
                    {
                        'name': data,
                    },
                ],
            },
        }
    }

    response = requests.patch(url, json=payload, headers=headers)

    print(response.text)

#editData()