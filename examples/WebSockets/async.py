from requests_futures.sessions import FuturesSession

session = FuturesSession(max_workers=10)

# first request is started in background
print("sending ONE ")
# future_one = session.get('https://btc-e.com/api/3/ticker/btc_usd')

print(session.__attrs__)
print(session.params)

# second requests is started immediately
print("sending TWO ")
# future_two = session.get('https://btc-e.com/api/3/depth/btc_usd')

# wait for the first request to complete, if it hasn't already
# response_one = future_one.result()
# print('response one status: {0}'.format(response_one.status_code))
# print(response_one.content)

# wait for the second request to complete, if it hasn't already
# response_two = future_two.result()
# print('response two status: {0}'.format(response_two.status_code))
# print(response_two.content)
