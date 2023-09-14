with payment as 
(
    select * from {{ ref('stg_payments') }}
),

total_revenue as
(select 
sum(amount) as total_revenue_amount
from payment
where status='success')

select * from total_revenue