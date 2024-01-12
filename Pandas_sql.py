# Pandas_sql
# Реализация операторов языка sql в библиотеке pandas
# Примеры
# pip install nycflights13 - полеты в США 2013 год
# pip install pandas
import pandas as pd
import numpy as np
import nycflights13 as nyc
import time

start_t = time.perf_counter()
flights = nyc.flights
airlines = nyc.airlines

pd.set_option('display.max_columns', None) # Вывод всех полей
pd.options.display.expand_frame_repr = False # Вывод полей в одну строку без переносов

print(f'exp_time: {time.perf_counter() - start_t:0.4f} секунд')

start_t = time.perf_counter()
print(flights)

# Where .query , Top 10 - .head(10)
print(
    flights
    .filter(['year', 'month', 'day', 'dep_time', 'flight', 'tailnum',
             'origin', 'dest'])
)

print(flights.filter(['year', 'month', 'day', 'dep_time',
                      'flight', 'tailnum', 'origin', 'dest'])
      .query("origin=='JFK'").head(10))

print(f'exp_time: {time.perf_counter() - start_t:0.4f} секунд')


print((flights.filter(['year', 'month', 'day', 'dep_time', 'flight',
                       'tailnum', 'origin', 'dest']).query("origin in ['JFK', 'EWR', 'LGA']"
                                                           "and (dest != 'MIA')").head(10)))

# Добавление вычисляемых полей .assign , like %% - .str.find , isnull
print('Добавление вычисляемых полей .assign , like %% - .str.find')
print(flights.filter(['year', 'month', 'day', 'dep_time', 'flight', 'tailnum',
                      'origin', 'dest', 'distance', 'time_hour'])
      .assign(delay_total=flights.dep_delay + flights.arr_delay)
      .query("origin in ['JFK', 'EWR', 'LGA']"
             "and (dest != 'MIA')"
             "and (distance <= 1000)"
             "and ('2013–09–01' <= time_hour  <= '2014–09–30')"
             "and (tailnum > '')" # is not null
             "and (tailnum.str.find('N')>=0)"  # like %B%
             "and dep_time.isnull()" # isnull
             )
      # .sort_index(axis=0)
      .sort_values(['origin', 'dest'], ascending=[True, False])
      .drop_duplicates()
      .head(100)
      )

print(flights.groupby(['year', 'month'], as_index=False)['dep_delay'].agg([('Min', 'min'), ('Max', 'max'),
                                                                           ('Avg', 'mean')]))


# Group By - .groupby
result = ( flights   .groupby(['year','month'],as_index=False)   .agg({'dep_delay':['max','min','mean','count'],
                                                                       'arr_delay':['max','min','sum']
                                                                       })

           .sort_index(axis=0)
           # .query('(dep_delay.max()<1000)')
           )
result.columns = result.columns.map('_'.join)
result = result.query('(dep_delay_max>1000)')
print(result)

# Union
Flights_NYC = (
 flights
 .filter(['year', 'month', 'day', 'dep_time', 'flight',
         'tailnum', 'origin', 'dest', 'time_hour',
         'dep_delay', 'arr_delay'])
 .assign(delay_total = flights.dep_delay + flights.arr_delay )
 .query(
         " (origin in ['JFK', 'EWR', 'LGA'])"
         " and ('2013–09–01' <= time_hour )"
 )
 .assign(group ='NYC')
 .sort_values('delay_total',ascending=False)
 .head(3)
)

Flights_MIAMI = (
 flights
 .filter(['year', 'month', 'day', 'dep_time', 'flight',
         'tailnum', 'origin', 'dest', 'time_hour',
         'dep_delay', 'arr_delay'])
 .assign(delay_total = flights.dep_delay + flights.arr_delay )
 .query(
     " (dest in ['MIA', 'OPF', 'FLL'])"
     " and ('2013–07–01' <= time_hour )"
 )
 .assign(group ='MIA')
 .sort_values('delay_total',ascending=False)
 .head(2)
)

# union all
result = pd.concat([ Flights_NYC,Flights_MIAMI],axis=0)
print(result)

# CASE WHEN - np.where
print(
    flights
    .filter(['year', 'month', 'day', 'dep_time', 'flight', 'tailnum',
             'origin', 'dest', 'time_hour', 'dep_delay', 'arr_delay'])
    .assign(status=np.where((flights['dep_delay'] + flights['arr_delay']) > 0,
                            'Delayed',
                            'On Time')
            )
    .head(5)
)


# case else - np.select default

a = ['ATL', 'PDK', 'FTY']
b = ['MIA', 'OPF', 'FLL']
print(
    flights
    .filter(['year', 'month', 'day', 'dep_time', 'flight', 'tailnum',
             'origin', 'dest', 'time_hour', 'dep_delay', 'arr_delay'])
    .assign(city=np.select([
        flights['dest'].isin(a),
        flights['dest'].isin(b),
    ],
        ['ATL', 'MIA'],
        default='Other')
    )
    .head(10)


)

print(
 flights
 .filter(['year', 'month', 'day', 'dep_time', 'flight', 'tailnum',
              'origin', 'dest', 'time_hour', 'dep_delay', 'arr_delay',
              'carrier'])
 .merge(airlines, how = 'left', on ='carrier')
 .rename(columns= {'name':'airline_name','origin':'airport_origen'})
 .head(5)
)