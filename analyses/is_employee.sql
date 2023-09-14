with employee as
(
    select * from {{ ref('employees') }}
),
is_employee as 
(
    select employee_id is not null as is_employee,
    email,
    customer_id from employee
)
select * from is_employee