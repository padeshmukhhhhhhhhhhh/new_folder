#pip install MetaTrader5
# import MetaTrader5 as mt
#login=
#password=
#server=
#mt.login(login, password, server)
#mt.account_info()


# symbol='BTCUSD'

# request={
#     "action":mt.TRADE_ACTION_DEAL,
#     "symbol":symbol,
#     "voulume":0.01,
#     "type":mt.ORDER_TYPE_BUY,
#     "price":mt.symbol_info_tick(symbol).ask,
#     "sl":290000.0,
#     "tp":33000.0,
#     "comment":'Python_Script_Buy',
#     "type_time":mt.ORDER_TIME_GTC,
#     "type_filling":mt.ORDER_FILLING_IOC
# }



# result=mt.order_send(request)
# print(result)