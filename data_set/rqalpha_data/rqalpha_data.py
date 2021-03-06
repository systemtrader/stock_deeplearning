# coding: utf8
import os
import sys
import pandas as pd
from datetime import datetime
sys.path.append('C:/Users/ll/Desktop/rqalpha')
sys.path.append('../stock_get_finance_data')
import rqalpha as rqa
from stock_codes_utility import stock_codes_utility as SCU
from rqalpha.data.base_data_source import BaseDataSource
from rqalpha.data.instrument_mixin import InstrumentMixin
#from rqalpha.data.instrument_store import instrument_store

path = '../../../data/'
path_market = os.path.join(path,'trade_market')
if not os.path.exists(path_market):
      os.makedirs(path_market)
      
scu = SCU(path=path)
stocks = scu.stock_codes_remove_no_stock_basic()
stocks = scu.add_allstock_xshg_xshe(stocks)

#rqa.update_bundle()
rqalpha_path = "~/.rqalpha"
data_bundle_path = os.path.join(os.path.expanduser(rqalpha_path), "bundle")
data = BaseDataSource(data_bundle_path)

Instru = InstrumentMixin(data._instruments._instruments)
for stock_code in stocks:
  print('procesing...',stock_code)
  stock_data = pd.DataFrame(data._all_day_bars_of(Instru.instruments(stock_code)))
  stock_data.datetime = stock_data.datetime.apply(lambda x: datetime.strptime(str(x)[:-6],'%Y%m%d'))
  stock_data.to_csv(os.path.join(path_market,stock_code[:-5]+'.csv'),index=False)
  
sec_name = []
sec_index = []

for k,v in Instru._sym_id_map.items():
  sec_name.append(k)
  sec_index.append(v)
Instru.all_instruments('CS')
Instru.instruments('603032.XSHG')
Instru.instruments('德新交运')