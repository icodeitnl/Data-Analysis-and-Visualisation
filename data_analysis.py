from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import matplotlib
import os

print(os.getcwd())

print(os.listdir(os.getcwd()))

# Data Exploration
# Import Data
orders = pd.read_csv("olist_orders_dataset.csv") 
order_items=pd.read_csv("olist_order_items_dataset.csv")
customers=pd.read_csv("olist_customers_dataset.csv")
order_payments=pd.read_csv("olist_order_payments_dataset.csv")
products=pd.read_csv("olist_products_dataset.csv")

# Print Info
print(orders.info())
print(order_items.info())
print(customers.info())
print(order_payments.info())
print(products.info())

# Print Sample
print(orders.sample(5))
print(order_items.sample(5))
print(customers.sample(5))
print(order_payments.sample(5))
print(products.sample(5))


# Describe Data

print(order_items.describe())
print(customers.describe())
print(order_payments.describe())
print(products.describe())


# Show Null Values 
print(pd.isnull(orders))
print(pd.isnull(order_items))
print(pd.isnull(customers))
print(pd.isnull(order_payments))
print(pd.isnull(products))

# Merge Tables

price_products = pd.merge(order_items,orders[['order_id', 'customer_id']], on = 'order_id', how = 'left')
print(price_products.sample(5))
print(price_products.info())

price_customers_products = pd.merge(price_products,customers[['customer_id', 'customer_unique_id']], on = 'customer_id', how = 'left')
print(price_customers_products.sample(5))
print(price_customers_products.info())

price_customers_products_time = pd.merge(price_customers_products,orders[['customer_id','order_purchase_timestamp']], on = 'customer_id', how = 'left')
print(price_customers_products_time.sample(5))
print(price_customers_products_time.info())

# Sort table by time
price_customers_products_time=price_customers_products_time.sort_values(by='order_purchase_timestamp')
price_customers_products_time['order_purchase_timestamp'] = pd.to_datetime(price_customers_products_time['order_purchase_timestamp'])
price_customers_products_time['order_purchase_timeyearmonth'] = price_customers_products_time['order_purchase_timestamp'].map(lambda date: date.month + 100*date.year)

# Monthly revenue
price_customers_products_time['revenue'] = price_customers_products_time['price'] * price_customers_products_time['order_item_id']
revenue = price_customers_products_time.groupby(['order_purchase_timeyearmonth'])['revenue'].sum().reset_index()

revenue['growth_rate'] = revenue['revenue'].pct_change()

print(revenue.sample(10))
print(revenue.info())
print(revenue.describe())



# Revenue Growth Rate Range 201609 - 201704
fig = go.Figure(
    data=go.Scatter(x=revenue.query("201609 < order_purchase_timeyearmonth < 201704")['order_purchase_timeyearmonth'],
        y=revenue.query("201609 < order_purchase_timeyearmonth < 201704")['growth_rate'], marker={"color":"IndianRed"}, line={"width": 4.5}),
    layout= go.Layout(
        xaxis={"type": "category", "title":'Monthly Orders'},
        yaxis={"title":'Revenue Growth Rate'},
        title='Revenue Growth Rate'
        )
    )
fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="IndianRed",
    plot_bgcolor="Gainsboro",
    font=dict(
        family='Courier New, monospace',
        size=14,
        color="Gainsboro"),
    titlefont=dict(
        family='Courier New, monospace',
        size=18,
        color="Gainsboro")
)
fig.show()

# Plot Revenue Growth Rate < 201809
fig = go.Figure(
    data=go.Scatter(x=revenue.query("order_purchase_timeyearmonth < 201809")['order_purchase_timeyearmonth'],
        y=revenue.query("order_purchase_timeyearmonth < 201809")['growth_rate'], marker={"color":"IndianRed"},line={"width": 4.5}),
    layout= go.Layout(
        xaxis={"type": "category", "title":'Monthly Orders'},
        yaxis={"title":'Revenue Growth Rate'},
        title='Revenue Growth Rate', 
        )
    )
fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="IndianRed",
    plot_bgcolor="Gainsboro",
    font=dict(
        family='Courier New, monospace',
        size=14,
        color="Gainsboro"),
    titlefont=dict(
        family='Courier New, monospace',
        size=18,
        color="Gainsboro")
)
fig.show()

# Plot Revenue Growth Rate Range 201709 - 201803
fig = go.Figure(
    data=go.Scatter(x=revenue.query("201709 < order_purchase_timeyearmonth < 201803")['order_purchase_timeyearmonth'],
        y=revenue.query("201709 < order_purchase_timeyearmonth < 201803")['growth_rate'], marker={"color":"IndianRed"},line={"width": 4.5}),
    layout= go.Layout(
        xaxis={"type": "category", "title":'Monthly Orders'},
        yaxis={"title":'Revenue Growth Rate'},
        title='Revenue Growth Rate'
        )
    )
fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="IndianRed",
    plot_bgcolor="Gainsboro",
    font=dict(
        family='Courier New, monospace',
        size=14,
        color="Gainsboro"),
    titlefont=dict(
        family='Courier New, monospace',
        size=18,
        color="Gainsboro")
)
fig.show()

# Plot Monthly Revenue
fig = go.Figure(
    data=go.Scatter(x=revenue['order_purchase_timeyearmonth'],y=revenue['revenue'],marker={"color":"IndianRed"},line={"width": 4.5}),
    layout= go.Layout(
        xaxis={"type": "category", "title":'Monthly Orders'},
        yaxis={"title":'Revenue'},
        title='Montly Revenue'
        )
    )
fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="IndianRed",
    plot_bgcolor="Gainsboro",
    font=dict(
        family='Courier New, monospace',
        size=14,
        color="Gainsboro"),
    titlefont=dict(
        family='Courier New, monospace',
        size=18,
        color="Gainsboro")
)
fig.show()

active_users = price_customers_products_time.groupby('order_purchase_timeyearmonth')['customer_unique_id'].nunique().reset_index()

print(active_users.sample(10))

# Plot Active Users
fig = go.Figure(
    data=go.Bar(x=active_users['order_purchase_timeyearmonth'],y=active_users['customer_unique_id'], 
        marker={"color":"IndianRed"}),
    layout= go.Layout(
        xaxis={"type": "category", "title":'Monthly Orders'},
        yaxis={"title":'Users'},
        title='Active Users'
        )
    )
fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="IndianRed",
    plot_bgcolor="Gainsboro",
    font=dict(
        family='Courier New, monospace',
        size=14,
        color="Gainsboro"),
    titlefont=dict(
        family='Courier New, monospace',
        size=18,
        color="Gainsboro")
)
fig.show()

# Monthly Item Sales
sales = price_customers_products_time.groupby(['order_purchase_timeyearmonth'])['order_item_id'].sum().reset_index()
print(sales.sample(10))


# Plot Sales
fig = go.Figure(
    data=go.Bar(x=sales['order_purchase_timeyearmonth'],y= sales['order_item_id'], 
        marker={"color":"IndianRed"}),
    layout= go.Layout(
        xaxis={"type": "category", "title":'Sales'},
        yaxis={"title":'Orders'},
        title='Montly Sales'
        )
    )
fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="IndianRed",
    plot_bgcolor="Gainsboro",
    font=dict(
        family='Courier New, monospace',
        size=14,
        color="Gainsboro"),
    titlefont=dict(
        family='Courier New, monospace',
        size=18,
        color="Gainsboro")
)
fig.show()

# Average Revenue per Order
average_revenue= price_customers_products_time.groupby(['order_purchase_timeyearmonth'])['revenue'].mean().reset_index()
print(average_revenue.sample(10))

# Plot Average Revenue per Order
fig = go.Figure(
    data=go.Bar(x=average_revenue['order_purchase_timeyearmonth'],y= average_revenue['revenue'], 
        marker={"color":"IndianRed"}),
    layout= go.Layout(
        xaxis={"type": "category", "title":'Revenue Per Order'},
        yaxis={"title":'Orders'},
        title='Average Revenue per Order'
        )
    )
fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="IndianRed",
    plot_bgcolor="Gainsboro",
    font=dict(
        family='Courier New, monospace',
        size=14,
        color="Gainsboro"),
    titlefont=dict(
        family='Courier New, monospace',
        size=18,
        color="Gainsboro")
)
fig.show()

# New Customer Ratio
# Create dataframe, group unique IDs to order time
customer_order=price_customers_products_time.groupby('customer_unique_id').order_purchase_timestamp.min().reset_index()
print(customer_order.info())

# Create new label
customer_order.columns = ['customer_unique_id','first_order']

# Convert to year-month format
customer_order['first_order_ym'] = customer_order['first_order'].map(lambda date: 100*date.year + date.month)
print(customer_order.info())

# Merge dataframe to main table
price_customers_products_time= pd.merge(price_customers_products_time, customer_order, on='customer_unique_id')
print(price_customers_products_time.sample(10))
print(price_customers_products_time.info())

# Create new column and  lable "new"
price_customers_products_time['customers'] = 'new'

# Select cells if customers first invoice was earlier then current
price_customers_products_time.loc[price_customers_products_time['order_purchase_timeyearmonth']>price_customers_products_time['first_order_ym'],'customers'] = 'old'

# Revenue per month for every user 
customers_revenue = price_customers_products_time.groupby(['order_purchase_timeyearmonth','customers'])['revenue'].sum().reset_index()

# Filtering the dates and plot the result
customers_revenue = customers_revenue.query("order_purchase_timeyearmonth != 201609 and order_purchase_timeyearmonth != 201809")

# Plot New Customer Ratio
print(customers_revenue.sample(10))

fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(x=customers_revenue.query("customers == 'new'")['order_purchase_timeyearmonth'],
        y= customers_revenue.query("customers == 'new'")['revenue'],
        marker={"color":"Coral"},name='New')
    )
fig.add_trace(go.Scatter(x=customers_revenue.query("customers == 'old'")['order_purchase_timeyearmonth'],
        y=customers_revenue.query("customers == 'old'")['revenue'],
        marker={"color":"Olive"},name='Old')
    )
fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    title='New Customer Ratio',
    xaxis={"type": "category"},
    paper_bgcolor="IndianRed",
    plot_bgcolor="Gainsboro",
    font=dict(
        family='Courier New, monospace',
        size=14,
        color="Gainsboro"),
    titlefont=dict(
        family='Courier New, monospace',
        size=18,
        color="Gainsboro")
    )
fig.show()

# New Customer Ratio
customers_ratio = price_customers_products_time.query("customers == 'new'").groupby(['order_purchase_timeyearmonth'])['customer_unique_id'].nunique()/price_customers_products_time.query("customers == 'old'").groupby(['order_purchase_timeyearmonth'])['customer_unique_id'].nunique() 
customers_ratio = customers_ratio.reset_index()
customers_ratio = customers_ratio.dropna()

# Plot New Customer Ratio in 2018
fig = go.Figure(
    data=go.Bar(x=customers_ratio.query("order_purchase_timeyearmonth>201801 and order_purchase_timeyearmonth<201809")['order_purchase_timeyearmonth'],
        y= customers_ratio.query("order_purchase_timeyearmonth>201801 and order_purchase_timeyearmonth<201809")['customer_unique_id'], 
        marker={"color":"Olive"}),
    layout= go.Layout(
        xaxis={"type": "category", "title":'Months'},
        yaxis={"title":'Loyal Customers'},
        title='Customers Ratio'
        )
    )
fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="IndianRed",
    plot_bgcolor="Gainsboro",
    font=dict(
        family='Courier New, monospace',
        size=14,
        color="Gainsboro"),
    titlefont=dict(
        family='Courier New, monospace',
        size=18,
        color="Gainsboro")
)
fig.show()

# Monthly Loyalty Rate
customers_purchase =price_customers_products_time.groupby(['customer_unique_id','order_purchase_timeyearmonth'])['revenue'].sum().reset_index()

# Create retention matrix with crosstab
customers_loyalty = pd.crosstab(customers_purchase['customer_unique_id'], customers_purchase['order_purchase_timeyearmonth']).reset_index()
print(customers_loyalty.head())
print(customers_loyalty.sample(5))

# Create an array of dictionary which keeps Loyal & Total User count for each month
months = customers_loyalty.columns[2:]
loyalty_library = []
for xxx in range(len(months)-1):
    loyalty_data = {}
    month_filter = months[xxx+1]
    prev_month = months[xxx]
    loyalty_data['order_purchase_timeyearmonth'] = int(month_filter)
    loyalty_data['total_customers'] = customers_loyalty[month_filter].sum()
    loyalty_data['loyal_customers'] = customers_loyalty[(customers_loyalty[month_filter]>0) & (customers_loyalty[prev_month]>0)][month_filter].sum()
    loyalty_library.append(loyalty_data)
    
# Convert the array to dataframe and calculate Loyalty Rate
customers_loyalty = pd.DataFrame(loyalty_library)
customers_loyalty['loyalty_rate'] = customers_loyalty['loyal_customers']/customers_loyalty['total_customers']
print(customers_loyalty.sample(5))

# Plot the retention rate graph
fig = go.Figure(
    data=go.Bar(x=customers_loyalty['order_purchase_timeyearmonth'],y= customers_loyalty['loyalty_rate'], 
        marker={"color":"Olive"}),
    layout= go.Layout(
        xaxis={"type": "category", "title":'Months'},
        yaxis={"title":'Loyalty Rate'},
        title='Loyalty Rate'
        )
    )
fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="IndianRed",
    plot_bgcolor="Gainsboro",
    font=dict(
        family='Courier New, monospace',
        size=14,
        color="Gainsboro"),
    titlefont=dict(
        family='Courier New, monospace',
        size=18,
        color="Gainsboro")
)
fig.show()

# Cohort Loyalty Rate
customers_loyalty = pd.crosstab(customers_purchase['customer_unique_id'], customers_purchase['order_purchase_timeyearmonth']).reset_index()
new_columns = [ 'new_' + str(column) for column in customers_loyalty.columns]
customers_loyalty.columns = new_columns

# Create the array of Retained users for each cohort monthly
loyalty_library = []
for xxx in range(len(months)):
    loyalty_data = {}
    month_filter = months[xxx]
    prev_months = months[:xxx]
    next_months = months[xxx+1:]
    for prev_month in prev_months:
        loyalty_data[prev_month] = np.nan
        
    totalcustomers =  loyalty_data['total_customers'] = customers_loyalty['new_' + str(month_filter)].sum()
    loyalty_data[month_filter] = 1 
    
    query = "{} > 0".format('new_' + str(month_filter))
    
    for next_month in next_months:
        query = query + " and {} > 0".format(str('new_' + str(next_month)))
        loyalty_data[next_month] = np.round(customers_loyalty.query(query)['new_' + str(next_month)].sum()/totalcustomers,2)
    loyalty_library.append(loyalty_data)
    
customers_loyalty = pd.DataFrame(loyalty_library)
customers_loyalty.index = months

# Prints out new cohort based retention table
print(customers_loyalty.sample(22))


