time_delay = 1  #every 1 seconde
smsUrlSend = 'http://www.behinpayam.com/APISend.aspx?Username=000&Password=000&From=50002060414921&To=000&Text='
sendSmsEnable = False

Data = [
    {'stockName':'vSina',
      'url':'http://www.tsetmc.com/tsev2/data/instinfodata.aspx?i=45050389997905274&c=57+',
      'desire_methods':['final_price_trade_is_less_than'],
      'desires':['1450'],
      'message':[u'سهم بانک سینا صف فروش شد']
    },
    {'stockName':'minoo',
      'url':'http://www.tsetmc.com/tsev2/data/instinfodata.aspx?i=5516102131364383&c=42+',
      'desire_methods':['final_price_trade_is_less_than'],
      'desires':['4100'],
      'message':[u'موقع خرید سهم غمینو است']
    },
    {'stockName':'hKhazar',
      'url':'http://www.tsetmc.com/tsev2/data/instinfodata.aspx?i=28253678449273505&c=61+',
      'desire_methods':['last_price_trade_is_more_than'],
      'desires':['9300'],
      'message':[u'موقع فروش سهم حخزر است']
    },
    {'stockName':'damavand',
      'url':'http://www.tsetmc.com/tsev2/data/instinfodata.aspx?i=66142616039907394&c=40+',
      'desire_methods':['last_price_trade_is_more_than', 'last_price_trade_is_more_than'],
      'desires':['82000', '84000'],
      'message':[u'سهم دماوند به 8200 تومان رسید',
				 u'سهم دماوند به قیمت 8400 تومان رسید']
    },
    {'stockName':'takamba',
      'url':'http://www.tsetmc.com/tsev2/data/instinfofast.aspx?i=30719054967088301&c=29+',
      'desire_methods':['last_price_trade_is_more_than', 'final_price_trade_is_less_than'],
      'desires':['965', '830'],
      'message':[u'موقع فروش سهم تکنبا است',
                 u'سهم تنکبا به حد ضرر رسید',]
    },    
	{'stockName':'bMapna',
      'url':'http://www.tsetmc.com/tsev2/data/instinfodata.aspx?i=39807886630843041&c=40+',
      'desire_methods':['last_price_trade_is_more_than'],
      'desires':['16500'],
      'message':[u'سهم بمپنا به قیمت 1550 تومان رسید. نزدیک به فروش است.']
    },
	{'stockName':'samga',
      'url':'http://www.tsetmc.com/tsev2/data/instinfofast.aspx?i=46741025610365786&c=55+',
      'desire_methods':['final_price_trade_is_more_than'],
      'desires':['4300'],
      'message':[u'سهم در موقعیت خرید قرار دارد']
    },
	{'stockName':'hKeshti',
      'url':'http://www.tsetmc.com/tsev2/data/instinfofast.aspx?i=60610861509165508&c=60+',
      'desire_methods':['last_price_trade_is_less_than', 'last_price_trade_is_more_than'],
      'desires':['5700','6800'],
      'message':[u'حد ضرر سهم حکشتی فعال شده است', 
				 u'سهم حکشتی به هدف اول خود رسید']
    },
    {'stockName':'tapico',
      'url':'http://www.tsetmc.com/tsev2/data/instinfofast.aspx?i=22560050433388046&c=44+',
      'desire_methods':['last_price_trade_is_less_than'],
      'desires':['2250'],
      'message':[u' زمان خرید تاپیکو است']
    },
	{'stockName':'valsapa',
      'url':'http://www.tsetmc.com/tsev2/data/instinfodata.aspx?i=45174198424472334&c=58+',
      'desire_methods':['last_price_trade_is_less_than'],
      'desires':['3000'],
      'message':[u'زمان خرید سهم ولساپا است']
    },
	{'stockName':'rmapna',
      'url':'http://www.tsetmc.com/tsev2/data/instinfofast.aspx?i=67126881188552864&c=74+',
      'desire_methods':['last_price_trade_is_less_than', 'last_price_trade_is_more_than'],
      'desires':['8650', '12000'],
      'message':[u'حد ضرر سهم رمپنا فعال گردید',
				 u'سهم رمپنا به هدف اول خور 1200 تومان رسید']
    },
	{'stockName':'akontor',
      'url':'http://www.tsetmc.com/tsev2/data/instinfodata.aspx?i=44834847569322522&c=33+',
      'desire_methods':['last_price_trade_is_more_than'],
      'desires':['82500'],
      'message':[u'زمان فروش سهم آکنتور است']
    },
]