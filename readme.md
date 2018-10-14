# using python3

note:　FB graph tool 在2018.4月歷經大改版,為了確保安全性, 很多的功能都被拿掉, 沒拿掉的也很多變成要通過審核才能使用
現在用起來簡直像個shit, 建議使用puppeteer / phantomJS來直接操作網頁

## using graph tool

go to graph tool 
https://developers.facebook.com/tools/explorer/?method=GET&path=me&version=v3.1

find your feeds id and message
`me/?fields=feed{id,message}`

```
{
  "feed": {
    "data": [
      {
        "id": "1902194509828194_1898238116890500",
        "message": "Northern beaches 的第一家飲料店!?
雖然coming soon means nothing here"
      },
      {
        "id": "1902194509828194_1894380180609627",
        "message": "$ rm -rf *"
      },
      {
....          
```

access the feed
`{id}`
ex: `1902194509828194_1898238116890500`

## using python facebookSDK

note: 還是要用FB graph tool 取得token才能使用
https://developers.facebook.com/tools/explorer/?method=GET&path=me&version=v3.1

```
graph = facebook.GraphAPI(access_token='{...}}', version='2.7') 
```
### graph tool的'/' ，在facebook sdk是用get_connections來實現
```
me = graph.get_object(id='me')
feedList = graph.get_connections(id='me', connection_name='feed')

# note: 取得物件中的data，不能像js一樣用.取得
# 印出id和 message小玩一下
for feed in feedList['data']:
    print(feed['id'])
    print('')
    print(feed['message'])

```
