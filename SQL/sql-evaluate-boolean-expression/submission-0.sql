-- Write your query below

select e.left_operand, e.operator, e.right_operand, 
case 
when e.operator = '>' and v1.value > v2.value then 'true' 
when e.operator = '<' and v1.value < v2.value then 'true' 
when e.operator = '=' and v1.value = v2.value then 'true' 
else 'false' 
end
as value
from variables v1 inner join expressions e on e.left_operand = v1.name inner join  variables v2 on e.right_operand = v2.name;
