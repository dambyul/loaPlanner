import requests
import keys
import json

headers = {
    'Authorization': 'Bearer ' + keys.notion_key,
    'Notion-Version': '2022-06-28'
}

def setDatabase():
    url = "https://api.notion.com/v1/databases/" + keys.notion_board

    payload = {
        "properties": {
            "번호": {
                "type": "number",
                "number": {
                    "format": "number",
                }
            },
            "구분": {
                "type": "select",
                "select": {
                    "options": [
                        {
                            "name": "섬의 마음",
                            "color": "pink",
                        },
                        {
                            "name": "거인의 심장",
                            "color": "brown",
                        },
                        {
                            "name": "향해 모험물",
                            "color": "blue",
                        },
                        {
                            "name": "위대한 미술품",
                            "color": "red",
                        },
                        {
                            "name": "세계수의 잎",
                            "color": "green",
                        },
                        {
                            "name": "이그네아의 징표",
                            "color": "orange",
                        },
                        {
                            "name": "오르페우스의 별",
                            "color": "yellow",
                        },
                    ]
                }
            },
        }
    }

    response = requests.patch(url, json=payload, headers=headers)

    print(response.text)


def createData(name, num, type, comp, charName):
    url = "https://api.notion.com/v1/databases/" + keys.notion_board

    payload = {
        "properties": {
            charName: {
                "type": "select",
                "select": {
                    "options": [
                        {
                            "name": "완료",
                            "color": "green",
                        },
                        {
                            "name": "진행중",
                            "color": "red",
                        },
                        {
                            "name": "유기",
                            "color": "gray",
                        },
                        {
                            "name": "미완료",
                            "color": "blue",
                        },
                    ]
                }
            },
        }
    }

    response = requests.patch(url, json=payload, headers=headers)
    print(response.text)


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
            '구분': {
                "select": {
                    "name": type
                }
            },
            charName: {
                "select": {
                    "name": comp
                }
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

    response = requests.post(url, json=payload, headers=headers)

    try:
        return json.loads(response.text)['results'][0]['id']
    except:
        return False

def addCol(charName):
    url = "https://api.notion.com/v1/databases/" + keys.notion_board

    payload = {
        "properties": {
            charName: {
                "type": "select",
                "select": {
                    "options": [
                        {
                            "name": "완료",
                            "color": "green",
                        },
                        {
                            "name": "진행중",
                            "color": "red",
                        },
                        {
                            "name": "유기",
                            "color": "gray",
                        },
                        {
                            "name": "미완료",
                            "color": "blue",
                        },
                    ]
                }
            },
        }
    }

    response = requests.patch(url, json=payload, headers=headers)
    print(response.text)


def editData(keyword,charName,data):
    id = getData(keyword)
    url = "https://api.notion.com/v1/pages/" + id

    payload = {
        "properties": {
            charName: {
                "select": {
                    "name": data
                }
            },
        }
    }

    response = requests.patch(url, json=payload, headers=headers)
    print(response.text)
