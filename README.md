# Data-Analysis-and-Visualisation :shipit:

Context

The [Dataset](https://www.kaggle.com/olistbr/brazilian-ecommerce) has information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allows viewing an order from multiple dimensions: from order status, price, payment and freight performance to customer location, product attributes and finally reviews written by customers.

This [Dataset](https://www.kaggle.com/olistbr/brazilian-ecommerce) was generously provided by Olist, the largest department store in Brazilian marketplaces. Olist connects small businesses from all over Brazil to channels without hassle and with a single contract. Those merchants are able to sell their products through the Olist Store and ship them directly to the customers using Olist logistics partners. 

After a customer purchases the product from Olist Store a seller gets notified to fulfill that order. Once the customer receives the product, or the estimated delivery date is due, the customer gets a satisfaction survey by email where he can give a note for the purchase experience and write down some comments.

The module [data_analysis.py](https://github.com/icodeitnl/Data-Analysis-and-Visualisation/blob/master/data_analysis.py) contains the scripts that brings the order and structure to the selected data.

The first part provides the general overview of the data, prints samples and Null values.
The second part prepares the data for the following analysis, extracting the relevant information.

Further on, Monthly Revenue and Revenue Growth Rate is calculated and visualised on a graph.

**Monthly Revenue** grew steadily untill *November 2017* when it reached it’s peak of *1.176 million* reais. *December* followed by a drop to the amount of the previous month of *October*. A slight increase in orders by *two hundred thousand* is observed in *January* with a backdrop and raise of about a *hundred thousand in March 2018* and remained relatively the same all the way through *April till May 2015*. Starting from month of *May*, the orders decreased to *1 million* and from *August to September* plummeted to zero in one month.

<img src="https://github.com/icodeitnl/Data-Analysis-and-Visualisation/blob/master/MonthlyRevenue.png"/>

**Revenue Growth Rate**
The maximum Revenue Growth Rate was reached in *January 2017* and is *13033%*. A more thorough look into details is required to investigate the сausal relationship that generated such result.

<img src="https://github.com/icodeitnl/Data-Analysis-and-Visualisation/blob/master/RevenueGrowthRate201609.png"/>

Zoom into random 4 month period from 201709 to 201803 reveals minor fluctuations within *+0,5%* and *-0,3%*.

<img src="https://github.com/icodeitnl/Data-Analysis-and-Visualisation/blob/master/RevenueGrowthRate201710.png"/>

One way to increase the revenue is to understand the client's behavior. Therefore, first we need to keep the track of **Monthly Active Users.** A record quantity of *7342* active users ordered in November 2017. From *May 2017* when the amount of users reached *3588* users the monthly number doubled in *November 2011* and untill *September 2018* was not gowing lower then *5557 users(201712)*. September 2018 shows no active users which explains the abrupt revenue drop.

<img src="https://github.com/icodeitnl/Data-Analysis-and-Visualisation/blob/master/ActiveUsers.png"/>

Next, we are going to look at the **Monthly Sales**. As expected, the record amount of *10.63k* items were sold in *November 2017.*. The plot pattern looks similar in shape to the monthly active users.

<img src="https://github.com/icodeitnl/Data-Analysis-and-Visualisation/blob/master/MonthlySales.png"/>

**Average Revenue Per Order** is an important indicator of the business wellbeing. *December 2016* was marked by the most modest **average revenue** of *10 reais*. The highest average *of 156 reais* was reached in *September 2017* and the average revenue per order is *130 reais*.

<img src="https://github.com/icodeitnl/Data-Analysis-and-Visualisation/blob/master/AverageRevenuePerOrder.png"/>

To explore business growth opportunities, the management needs to know its loyal customers rate. In order to do this, first we should try to plot on the graph new and old customers. The pattern of the plot resembles *monthly revenue* graph. It also reveals that new clients brough almost all of the  business revenue. *June 2018* brought *29.87k reais* in revenue by old customers comparing to *945.20k reais* by the new ones.

<img src="https://github.com/icodeitnl/Data-Analysis-and-Visualisation/blob/master/NewAndOldCustomers.png"/>





















