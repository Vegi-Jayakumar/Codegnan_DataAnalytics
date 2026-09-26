use jeevan_raksha_pharmacy;

-- city and name of all customers
select name, city from customers;

-- find the names of medicines that are syrup and injection
select name, category from medicines where category in ('syrup', 'injection');

-- list all orders where the total amount is greater than 500 rupees
select name from customers where customer_id in (select customer_id from orders where total_amount > 500);

-- mumbai city, name, phone
select name, phone from customers where city = 'mumbai';

-- count orders where paid using upi
select count(*) as upi_users from orders where payment_mode = 'upi';

-- count medicines suplied by apollo distributors
select count(*) as apollo_medicines from medicines m join suppliers s on m.supplier_id = s.supplier_id where s.supplier_name = 'apollo distributors';

-- list the customer name, orderdate and total amount for every order
select c.name, o.order_date, o.total_amount from customers c join orders o on c.customer_id = o.customer_id;

-- revenue by payment mode
select payment_mode, sum(total_amount) as revenue from orders group by payment_mode;

-- best selling medicine
select m.name, sum(o.quantity) as total_sales from medicines m join order_items o on m.medicine_id = o.medicine_id group by m.name order by total_sales desc limit 1;

-- customers  who spent 1000 in total
select c.name, sum(o.total_amount) as spent from customers c join orders o on c.customer_id = o.customer_id group by c.name having spent > 1000; 

-- medicinename and stock quantity and supplier name for medicines less than or equal to 50 units left in the stock
select m.name, m.stock_quantity, s.supplier_name from medicines m join suppliers s on m.supplier_id = s.supplier_id where m.stock_quantity <= 50;